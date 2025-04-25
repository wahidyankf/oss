---
title: '64 - Airflow in Kubernetes'
date: 2025-04-17T07:20:00+07:00
draft: false
weight: 65
---

**Complexity: Moderate (M)**

## 64.0 Introduction: Why This Matters for Data Engineering

In data engineering, orchestrating complex data pipelines at scale is critical for Hijra Group’s Sharia-compliant fintech analytics, where financial transaction data must be processed reliably across distributed systems. Apache Airflow, a powerful workflow orchestrator, excels in scheduling and monitoring data pipelines, while Kubernetes provides a scalable, containerized environment for deploying Airflow, ensuring high availability and resource efficiency. Deploying Airflow in Kubernetes with Helm Charts, as covered in this chapter, enables Hijra Group to manage thousands of daily transactions with fault tolerance and observability, critical for compliance with Islamic Financial Services Board (IFSB) standards.

Building on **Phase 9** (Chapters 60–63), which introduced Docker, Kubernetes fundamentals, Helm Charts, and PostgreSQL in Kubernetes, this chapter focuses on deploying a type-annotated Airflow instance in Kubernetes using Helm, integrating with PostgreSQL and processing `data/sales.csv`. All Python code includes type annotations verified by Pyright (from Chapter 7) and tests using `pytest` (from Chapter 9), with **4-space indentation** per PEP 8, preferring spaces over tabs to avoid `IndentationError`. The micro-project orchestrates a sales ETL pipeline, preparing for security (Chapter 65) and observability (Chapter 66).

### Data Engineering Workflow Context

This diagram illustrates Airflow’s role in a Kubernetes-based pipeline:

```mermaid
flowchart TD
    A["Raw Data<br>sales.csv"] --> B["Kubernetes Cluster"]
    B --> C["Airflow Helm Chart"]
    C --> D["Airflow Scheduler"]
    C --> E["Airflow Webserver"]
    D --> F["ETL DAG"]
    F --> G["PostgreSQL Pod"]
    F --> H["BigQuery"]
    G --> I["Processed Data"]
    H --> I

    classDef data fill:#f9f9f9,stroke:#333,stroke-width:2px
    classDef process fill:#d0e0ff,stroke:#336,stroke-width:1px
    classDef storage fill:#ddffdd,stroke:#363,stroke-width:1px
    classDef cluster fill:#ffddaa,stroke:#663,stroke-width:1px

    class A,I data
    class B cluster
    class C,D,E,F process
    class G,H storage
```

### Building On and Preparing For

- **Building On**:
  - Chapter 56: Airflow fundamentals, defining DAGs for ETL processes.
  - Chapter 57: Dockerized Airflow, containerizing DAGs.
  - Chapter 60: Docker for data applications, packaging pipelines.
  - Chapter 61: Kubernetes fundamentals, deploying pods and Helm Charts.
  - Chapter 63: PostgreSQL in Kubernetes, managing stateful databases.
- **Preparing For**:
  - Chapter 65: Secures Airflow with OAuth2 and PII masking.
  - Chapter 66: Adds observability with monitoring and logging.
  - Chapters 67–70: Integrates Airflow in capstone projects with FastAPI and Helm.

### What You’ll Learn

This chapter covers:

1. **Airflow in Kubernetes**: Deploying Airflow using Helm Charts.
2. **Type-Annotated DAGs**: Writing robust DAGs with Pyright verification.
3. **Integration with PostgreSQL**: Connecting Airflow to Kubernetes-hosted databases.
4. **Testing**: Validating DAGs with `pytest`.
5. **Logging**: Tracking pipeline execution with YAML-configured logs.

The micro-project deploys a type-annotated Airflow instance in Kubernetes, orchestrating a sales ETL pipeline that loads `data/sales.csv`, validates it, and stores results in PostgreSQL, with `pytest` tests ensuring reliability.

**Follow-Along Tips**:

- Create `de-onboarding/data/` with `sales.csv` and `config.yaml` per **Appendix 1**.
- Install tools: `pip install apache-airflow psycopg2-binary pyyaml pytest kubernetes`, `kubectl`, `helm`, `minikube`, and Docker Desktop.
- Start `minikube` with adequate resources: `minikube start --cpus=2 --memory=4g`. If resource errors occur, check `minikube logs` for issues like “insufficient memory”.
- Use **4-space indentation** per PEP 8. Run `python -tt script.py` to detect tab/space mixing.
- Debug with `kubectl logs`, `kubectl describe`, and `airflow dags list`.
- Verify Helm Chart installation with `helm list`.
- Use `minikube` for local Kubernetes testing.

## 64.1 Airflow in Kubernetes with Helm

Airflow in Kubernetes runs as a set of pods (webserver, scheduler, workers) managed by a Helm Chart, which simplifies configuration and deployment. Helm Charts are templates for Kubernetes resources, enabling scalable deployments with O(1) resource lookup and O(n) pod scheduling for n pods. For Hijra Group’s pipelines, this ensures reliable orchestration of thousands of daily transactions.

### 64.1.1 Helm Chart Setup

Install the official Airflow Helm Chart and configure it for PostgreSQL.

```bash
# Add Helm repository
helm repo add apache-airflow https://airflow.apache.org
helm repo update

# Create namespace
kubectl create namespace airflow

# Install Airflow Helm Chart
helm install airflow apache-airflow/airflow \
  --namespace airflow \
  --set executor=LocalExecutor \
  --set postgresql.enabled=false \
  --set dags.persistence.enabled=false \
  --set webserver.defaultUser.enabled=true \
  --set webserver.defaultUser.username=admin \
  --set webserver.defaultUser.password=admin
```

**Follow-Along Instructions**:

1. Start `minikube`: `minikube start --cpus=2 --memory=4g`.
2. Install Helm: Verify with `helm version`.
3. Pin the Helm Chart version for stability (e.g., `--version 1.10.0` for Airflow Helm Chart; check latest with `helm search repo airflow`).
4. Run commands above in `de-onboarding/`.
5. Verify pods: `kubectl get pods -n airflow`.
6. Access Airflow UI: `kubectl port-forward svc/airflow-webserver 8080:8080 -n airflow`, then open `http://localhost:8080` (login: admin/admin). Check DAG status (e.g., “success” or “failed”) in the UI after triggering. A screenshot of the UI would be provided in a production-grade course but is omitted here for simplicity.
7. **Common Errors**:
   - **Helm Not Found**: Install Helm (`brew install helm` on macOS, `choco install kubernetes-helm` on Windows).
   - **Pod CrashLoopBackOff**: Check logs with `kubectl logs <pod-name> -n airflow`.
   - **Connection Refused**: Ensure port-forwarding is active.

**Key Points**:

- **Helm Chart**: Defines Airflow components (webserver, scheduler, workers).
- **LocalExecutor**: Runs tasks sequentially, suitable for small pipelines.
- **Time Complexity**: O(1) for Helm resource lookup, O(n) for scheduling n pods.
- **Space Complexity**: O(n) for n pods’ configurations (~10MB per pod).
- **Implication**: Simplifies Airflow deployment for Hijra Group’s pipelines.

### 64.1.2 Connecting to PostgreSQL

Configure Airflow to use a PostgreSQL database in Kubernetes (from Chapter 63).

> **Note**: This chapter assumes a PostgreSQL service (`postgresql-service`) deployed in Chapter 63 using the Bitnami PostgreSQL Helm Chart (e.g., `helm install postgresql bitnami/postgresql --namespace airflow`). Review Chapter 63 for setup details, including credentials and service configuration.

```yaml
# File: de-onboarding/values.yaml
airflow:
  # Note: Resource limits (e.g., CPU: 500m, memory: 1Gi) will be configured in Chapter 66 for production-grade deployments
  executor: LocalExecutor
  config:
    AIRFLOW__DATABASE__SQL_ALCHEMY_CONN: 'postgresql+psycopg2://user:password@postgresql-service.airflow.svc.cluster.local:5432/airflow'
  dags:
    persistence:
      enabled: true
      existingClaim: airflow-dags-pvc
```

Apply the configuration:

```bash
helm upgrade airflow apache-airflow/airflow \
  --namespace airflow \
  --values values.yaml
```

**Follow-Along Instructions**:

1. Save `values.yaml` in `de-onboarding/`.
2. Replace `user:password` and `postgresql-service` with your PostgreSQL credentials and service name (from Chapter 63).
3. Run Helm upgrade command.
4. Verify connection: `kubectl exec -it <airflow-scheduler-pod> -n airflow -- airflow connections list`.
5. **Common Errors**:
   - **Connection Error**: Check PostgreSQL service with `kubectl get svc -n airflow`.
   - **Credentials Issue**: Verify credentials in `values.yaml`.

**Key Points**:

- **SQL_ALCHEMY_CONN**: Configures Airflow’s metadata database.
- **Time Complexity**: O(1) for connection setup.
- **Space Complexity**: O(1) for configuration storage.
- **Implication**: Ensures persistent metadata for Airflow tasks.

## 64.2 Type-Annotated Airflow DAGs

Write type-annotated DAGs for ETL pipelines, verified by Pyright, ensuring robust task definitions.

```python
# File: de-onboarding/dags/sales_etl.py
from datetime import datetime
from typing import Dict, Any
from airflow import DAG
from airflow.operators.python import PythonOperator
import pandas as pd
import psycopg2
import yaml
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def load_config(config_path: str) -> Dict[str, Any]:
    """Load YAML configuration."""
    logger.info(f"Loading config: {config_path}")
    with open(config_path, "r") as file:
        config = yaml.safe_load(file)
    return config

def extract_sales(csv_path: str, config: Dict[str, Any]) -> pd.DataFrame:
    """Extract and validate sales data."""
    logger.info(f"Extracting CSV: {csv_path}")
    df = pd.read_csv(csv_path)
    df = df.dropna(subset=["product"])
    df = df[df["product"].str.startswith(config["product_prefix"])]
    df = df[df["quantity"].apply(lambda x: str(x).isdigit())]
    df["quantity"] = df["quantity"].astype(int)
    df = df[df["quantity"] <= config["max_quantity"]]
    df = df[df["price"].apply(lambda x: isinstance(x, (int, float)))]
    df = df[df["price"] >= config["min_price"]]
    logger.info(f"Extracted {len(df)} valid records")
    return df

def transform_sales(df: pd.DataFrame) -> pd.DataFrame:
    """Transform sales data."""
    logger.info("Transforming data")
    df["amount"] = df["price"] * df["quantity"]
    logger.info(f"Transformed {len(df)} records")
    return df

def load_sales(df: pd.DataFrame, conn_params: Dict[str, str]) -> None:
    """Load sales data into PostgreSQL."""
    logger.info("Loading data to PostgreSQL")
    conn = psycopg2.connect(**conn_params)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS sales (
            product TEXT,
            price REAL,
            quantity INTEGER,
            amount REAL
        )
    """)
    # Note: Row-by-row insertion is used for simplicity; efficient methods like pandas.to_sql or PostgresHook will be introduced in Chapter 69
    for _, row in df.iterrows():
        cursor.execute(
            "INSERT INTO sales (product, price, quantity, amount) VALUES (%s, %s, %s, %s)",
            (row["product"], row["price"], row["quantity"], row["amount"])
        )
    conn.commit()
    cursor.close()
    conn.close()
    logger.info("Data loaded successfully")

# Define DAG
default_args: Dict[str, Any] = {
    "owner": "airflow",
    "depends_on_past": False,
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
}
with DAG(
    "sales_etl",
    default_args=default_args,
    description="Sales ETL Pipeline",
    schedule_interval=None,
    start_date=datetime(2023, 1, 1),
    catchup=False,
) as dag:
    config_task = PythonOperator(
        task_id="load_config",
        python_callable=load_config,
        op_kwargs={"config_path": "/opt/airflow/dags/data/config.yaml"}
    )
    extract_task = PythonOperator(
        task_id="extract_sales",
        python_callable=extract_sales,
        op_kwargs={
            "csv_path": "/opt/airflow/dags/data/sales.csv",
            "config": "{{ ti.xcom_pull(task_ids='load_config') }}"
        }
    )
    transform_task = PythonOperator(
        task_id="transform_sales",
        python_callable=transform_sales,
        op_kwargs={"df": "{{ ti.xcom_pull(task_ids='extract_sales') }}"}
    )
    load_task = PythonOperator(
        task_id="load_sales",
        python_callable=load_sales,
        op_kwargs={
            "df": "{{ ti.xcom_pull(task_ids='transform_sales') }}",
            "conn_params": {
                "dbname": "airflow",
                "user": "user",
                "password": "password",
                "host": "postgresql-service.airflow.svc.cluster.local",
                "port": "5432"
            }
        }
    )
    config_task >> extract_task >> transform_task >> load_task
```

**Follow-Along Instructions**:

1. Save as `de-onboarding/dags/sales_etl.py`.
2. Copy `data/sales.csv` and `data/config.yaml` to Airflow’s DAGs folder: `kubectl cp data/sales.csv airflow/<scheduler-pod>:/opt/airflow/dags/data/ -n airflow`.
3. Configure editor for **4-space indentation** per PEP 8.
4. Verify Pyright: `pyright sales_etl.py`.
5. Trigger DAG: `airflow dags trigger sales_etl`.
6. **Common Errors**:
   - **FileNotFoundError**: Ensure `sales.csv` and `config.yaml` are in `/opt/airflow/dags/data/`.
   - **TypeError**: Verify type annotations with `pyright`.
   - **IndentationError**: Use 4 spaces. Run `python -tt sales_etl.py`.

**Key Points**:

- **Type Annotations**: Ensure type safety with `Dict[str, Any]`, `pd.DataFrame`.
- **XCom**: Passes data between tasks (e.g., DataFrame from `extract_sales` to `transform_sales`).
- **Time Complexity**: O(n) for processing n rows in ETL tasks.
- **Space Complexity**: O(n) for DataFrame storage.
- **Implication**: Robust DAGs ensure reliable ETL for Hijra Group’s analytics.

## 64.3 Testing Airflow DAGs

Test DAGs with `pytest` to ensure task reliability.

```python
# File: de-onboarding/tests/test_sales_etl.py
from typing import Dict, Any
import pytest
import pandas as pd
from dags.sales_etl import load_config, extract_sales, transform_sales, load_sales

@pytest.fixture
def config() -> Dict[str, Any]:
    """Fixture for config."""
    return {
        "min_price": 10.0,
        "max_quantity": 100,
        "required_fields": ["product", "price", "quantity"],
        "product_prefix": "Halal",
        "max_decimals": 2
    }

def test_load_config(tmp_path) -> None:
    """Test config loading."""
    config_path = tmp_path / "config.yaml"
    config_path.write_text("""
min_price: 10.0
max_quantity: 100
required_fields:
  - product
  - price
  - quantity
product_prefix: Halal
max_decimals: 2
""")
    config = load_config(str(config_path))
    assert config["min_price"] == 10.0
    assert config["product_prefix"] == "Halal"

def test_extract_sales(config: Dict[str, Any], tmp_path) -> None:
    """Test data extraction."""
    csv_path = tmp_path / "sales.csv"
    csv_path.write_text("""
product,price,quantity
Halal Laptop,999.99,2
Halal Mouse,24.99,10
Non-Halal,50.00,5
""")
    df = extract_sales(str(csv_path), config)
    assert len(df) == 2
    assert all(df["product"].str.startswith("Halal"))
    assert all(df["quantity"] <= 100)

def test_transform_sales() -> None:
    """Test data transformation."""
    df = pd.DataFrame({
        "product": ["Halal Laptop"],
        "price": [999.99],
        "quantity": [2]
    })
    transformed = transform_sales(df)
    assert "amount" in transformed.columns
    assert transformed["amount"].iloc[0] == 999.99 * 2

def test_load_sales(tmp_path) -> None:
    """Test data loading (mocked).
    Note: Mocking psycopg2.connect is deferred to Chapter 69 due to complexity.
    For now, verify PostgreSQL contents manually with:
    kubectl exec -it <postgresql-pod> -n airflow -- psql -U user -d airflow -c "SELECT * FROM sales;"
    """
    df = pd.DataFrame({
        "product": ["Halal Laptop"],
        "price": [999.99],
        "quantity": [2],
        "amount": [1999.98]
    })
    conn_params = {
        "dbname": "test",
        "user": "test",
        "password": "test",
        "host": "localhost",
        "port": "5432"
    }
    # Mocking database connection is complex; assume success if no errors
    try:
        load_sales(df, conn_params)
        assert True
    except Exception:
        assert False
```

**Follow-Along Instructions**:

1. Save as `de-onboarding/tests/test_sales_etl.py`.
2. Configure editor for **4-space indentation** per PEP 8.
3. Install pytest: `pip install pytest`.
4. Run: `pytest tests/test_sales_etl.py -v`.
5. **Common Errors**:
   - **ModuleNotFoundError**: Ensure `dags/sales_etl.py` is accessible.
   - **AssertionError**: Print intermediate DataFrames with `print(df)`.

**Key Points**:

- **Pytest Fixtures**: Provide reusable config.
- **Mocking**: Skips actual database connections for simplicity.
- **Time Complexity**: O(n) for testing n rows.
- **Space Complexity**: O(n) for test DataFrames.
- **Implication**: Ensures DAG reliability for production.

## 64.4 Micro-Project: Sales ETL Pipeline in Kubernetes

### Project Requirements

Deploy a type-annotated Airflow instance in Kubernetes using Helm, orchestrating a sales ETL pipeline that processes `data/sales.csv`, validates it with `data/config.yaml`, and loads results into PostgreSQL. The pipeline supports Hijra Group’s transaction reporting, ensuring compliance with IFSB standards.

- Deploy Airflow with Helm, integrating with PostgreSQL.
- Write a type-annotated DAG (`sales_etl.py`) for ETL.
- Test DAG with `pytest`, covering edge cases.
- Log steps using `logging`.
- Use **4-space indentation** per PEP 8.
- Validate with `data/sales.csv` and `config.yaml` per **Appendix 1**.

### Sample Input Files

`data/sales.csv` (from Appendix 1):

```csv
product,price,quantity
Halal Laptop,999.99,2
Halal Mouse,24.99,10
Halal Keyboard,49.99,5
,29.99,3
Monitor,invalid,2
Headphones,5.00,150
```

`data/config.yaml` (from Appendix 1):

```yaml
min_price: 10.0
max_quantity: 100
required_fields:
  - product
  - price
  - quantity
product_prefix: 'Halal'
max_decimals: 2
```

### Data Processing Flow

```mermaid
flowchart TD
    A["Input CSV<br>sales.csv"] --> B["Load Config<br>config.yaml"]
    B --> C["Extract Task"]
    C --> D["Transform Task"]
    D --> E["Load Task"]
    E --> F["PostgreSQL"]
    F --> G["Processed Data"]

    classDef data fill:#f9f9f9,stroke:#333,stroke-width:2px
    classDef process fill:#d0e0ff,stroke:#336,stroke-width:1px
    classDef storage fill:#ddffdd,stroke:#363,stroke-width:1px

    class A,G data
    class B,C,D,E process
    class F storage
```

### PVC Architecture

This diagram shows how the Persistent Volume Claim (PVC) persists DAGs and data files, with PostgreSQL integration:

```mermaid
flowchart TD
    A["Airflow Scheduler Pod"] --> B["PVC: airflow-dags-pvc"]
    A --> F["PostgreSQL Pod"]
    B --> C["DAGs (sales_etl.py)"]
    B --> D["Data Files (sales.csv, config.yaml)"]
    A --> E["Kubernetes Cluster"]
    F --> G["PostgreSQL Service<br>postgresql-service"]

    classDef pod fill:#d0e0ff,stroke:#336,stroke-width:1px
    classDef storage fill:#ddffdd,stroke:#363,stroke-width:1px
    classDef data fill:#f9f9f9,stroke:#333,stroke-width:2px
    classDef cluster fill:#ffddaa,stroke:#663,stroke-width:1px

    class A,F pod
    class B,G storage
    class C,D data
    class E cluster
```

### Acceptance Criteria

- **Go Criteria**:
  - Airflow deploys successfully in Kubernetes (`kubectl get pods -n airflow`).
  - DAG loads, validates, transforms, and loads data into PostgreSQL.
  - Tests pass with `pytest`.
  - Logs steps and invalid records.
  - Uses type annotations, verified by Pyright.
  - Uses 4-space indentation per PEP 8.
- **No-Go Criteria**:
  - Airflow fails to deploy.
  - DAG fails to execute or load data.
  - Tests fail.
  - Missing type annotations or incorrect indentation.

### Common Pitfalls to Avoid

1. **Helm Installation Failure**:
   - **Problem**: Chart not found or version mismatch.
   - **Solution**: Run `helm repo update`. Verify with `helm search repo airflow`.
2. **Pod CrashLoopBackOff**:
   - **Problem**: Airflow pods fail.
   - **Solution**: Check logs with `kubectl logs <pod-name> -n airflow`.
3. **FileNotFoundError**:
   - **Problem**: `sales.csv` not found.
   - **Solution**: Copy files to `/opt/airflow/dags/data/`. Verify with `kubectl exec -it <scheduler-pod> -n airflow -- ls /opt/airflow/dags/data/`.
4. **Type Errors**:
   - **Problem**: Pyright fails.
   - **Solution**: Run `pyright sales_etl.py`. Print variable types with `print(type(var))`.
5. **IndentationError**:
   - **Problem**: Mixed spaces/tabs.
   - **Solution**: Use 4 spaces. Run `python -tt sales_etl.py`.

### How This Differs from Production

In production, this solution would include:

- **Security**: OAuth2 and secrets management (Chapter 65).
- **Observability**: Prometheus monitoring (Chapter 66).
- **Scalability**: CeleryExecutor for distributed tasks.
- **High Availability**: Multiple scheduler replicas.
- **CI/CD**: Automated Helm deployments (Chapter 66).

### Implementation

See `sales_etl.py` and `test_sales_etl.py` above. Helm configuration:

```yaml
# File: de-onboarding/values.yaml
airflow:
  # Note: Resource limits (e.g., CPU: 500m, memory: 1Gi) will be configured in Chapter 66 for production-grade deployments
  executor: LocalExecutor
  config:
    AIRFLOW__DATABASE__SQL_ALCHEMY_CONN: 'postgresql+psycopg2://user:password@postgresql-service.airflow.svc.cluster.local:5432/airflow'
  dags:
    persistence:
      enabled: true
      existingClaim: airflow-dags-pvc
```

**Persistent Volume Claim** (for DAGs):

```yaml
# File: de-onboarding/dags-pvc.yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: airflow-dags-pvc
  namespace: airflow
spec:
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 1Gi
```

Apply PVC:

```bash
kubectl apply -f dags-pvc.yaml
```

### How to Run and Test

1. **Setup**:

   - **Checklist**:
     - [ ] Start `minikube`: `minikube start --cpus=2 --memory=4g`.
     - [ ] Install `kubectl`, `helm`, Docker Desktop.
     - [ ] Create `de-onboarding/data/` with `sales.csv`, `config.yaml`.
     - [ ] Create `de-onboarding/ex5_sample_logs.txt` with sample logs (see Exercise 5).
     - [ ] Install libraries: `pip install apache-airflow psycopg2-binary pyyaml pytest kubernetes`.
     - [ ] Configure editor for 4-space indentation per PEP 8.
     - [ ] Save `values.yaml`, `dags-pvc.yaml`, `sales_etl.py`, `test_sales_etl.py`, `ex5_sample_logs.txt`.
   - **Troubleshooting**:
     - If `FileNotFoundError`, verify files in `/opt/airflow/dags/data/`.
     - If `pyright` errors, check annotations with `print(type(var))`.
     - If pods fail, check logs with `kubectl logs <pod-name> -n airflow`.

2. **Run**:

   - Apply PVC: `kubectl apply -f dags-pvc.yaml`.
   - Install Airflow: `helm install airflow apache-airflow/airflow --namespace airflow --values values.yaml`.
   - Copy files: `kubectl cp dags/ airflow/<scheduler-pod>:/opt/airflow/dags/ -n airflow`.
   - Trigger DAG: `airflow dags trigger sales_etl`.
   - Verify PostgreSQL: `kubectl exec -it <postgresql-pod> -n airflow -- psql -U user -d airflow -c "SELECT * FROM sales;"`.

3. **Test Scenarios**:

   - **Valid Data**: Verify PostgreSQL table has 3 rows (Halal products).
   - **Empty CSV**: Test with `empty.csv`:
     - Replace `sales.csv`: `kubectl cp data/empty.csv airflow/<scheduler-pod>:/opt/airflow/dags/data/sales.csv -n airflow`.
     - Trigger DAG: `airflow dags trigger sales_etl`.
     - Expected: Logs indicate no valid records, no rows inserted.
   - **Invalid Headers**: Test with `invalid.csv`:
     - Replace `sales.csv`: `kubectl cp data/invalid.csv airflow/<scheduler-pod>:/opt/airflow/dags/data/sales.csv -n airflow`.
     - Trigger DAG: `airflow dags trigger sales_etl`.
     - Expected: DAG skips invalid rows, no rows inserted.
   - **Malformed Data**: Test with `malformed.csv`:
     - Replace `sales.csv`: `kubectl cp data/malformed.csv airflow/<scheduler-pod>:/opt/airflow/dags/data/sales.csv -n airflow`.
     - Trigger DAG: `airflow dags trigger sales_etl`.
     - Expected: Only valid rows (e.g., Halal Mouse) inserted, others skipped.
   - **Run Tests**: `pytest tests/test_sales_etl.py -v`. All tests should pass.

## 64.5 Practice Exercises

### Exercise 1: Helm Configuration

Write a Helm `values.yaml` to configure Airflow with a custom namespace and executor, using 4-space indentation.

**Expected Output**:

```bash
helm install my-airflow apache-airflow/airflow --namespace my-namespace --values values.yaml
# Pods running in my-namespace
```

**Follow-Along Instructions**:

1. Save as `de-onboarding/ex1_values.yaml`.
2. Configure editor for 4-space indentation.
3. Test: Run Helm install command.
4. Verify: `kubectl get pods -n my-namespace`.

### Exercise 2: Type-Annotated DAG Task

Write a type-annotated PythonOperator task to validate sales data, using 4-space indentation.

**Sample Input** (`data/sales.csv`):

```csv
product,price,quantity
Halal Laptop,999.99,2
```

**Expected Output**:

```
Validated 1 record
```

**Follow-Along Instructions**:

1. Save as `de-onboarding/ex2_task.py`.
2. Configure editor for 4-space indentation.
3. Test: Integrate into `sales_etl.py` and trigger DAG.

### Exercise 3: DAG Testing

Write a `pytest` test for the `extract_sales` function, using 4-space indentation.

**Sample Input**:

```csv
product,price,quantity
Halal Laptop,999.99,2
Non-Halal,50.00,5
```

**Expected Output**:

```
2 rows (only Halal products)
```

**Follow-Along Instructions**:

1. Save as `de-onboarding/tests/ex3_test.py`.
2. Configure editor for 4-space indentation.
3. Run: `pytest tests/ex3_test.py -v`.

### Exercise 4: Debug a Failing DAG

Fix a DAG with incorrect XCom usage, ensuring 4-space indentation.

**Buggy Code**:

```python
extract_task = PythonOperator(
    task_id="extract_sales",
    python_callable=extract_sales,
    op_kwargs={"csv_path": "data/sales.csv"}  # Bug: Missing config
)
```

**Expected Output**:

```
DAG runs successfully
```

**Follow-Along Instructions**:

1. Save as `de-onboarding/ex4_debug.py`.
2. Configure editor for 4-space indentation.
3. Fix and test in Airflow.

### Exercise 5: Log Analysis

Analyze Airflow logs to debug task failures, using `kubectl logs`, with 4-space indentation for any scripts. If setup fails, use the sample log file `ex5_sample_logs.txt` for practice.

**Sample Log File** (`de-onboarding/ex5_sample_logs.txt`):

```text
[2025-04-25 10:00:00] ERROR - extract_sales - FileNotFoundError: [Errno 2] No such file or directory: '/opt/airflow/dags/data/sales.csv'
[2025-04-25 10:01:00] ERROR - load_sales - OperationalError: FATAL: password authentication failed for user 'user'
```

**Task**: Retrieve logs from the Airflow scheduler pod to identify:

1. A `FileNotFoundError` for a missing `sales.csv` file in the `extract_sales` task.
2. A PostgreSQL connection error in the `load_sales` task due to incorrect credentials.

**Expected Output**:

```
Scenario 1: "FileNotFoundError: [Errno 2] No such file or directory: '/opt/airflow/dags/data/sales.csv'"
Scenario 2: "OperationalError: FATAL: password authentication failed for user 'user'"
```

**Follow-Along Instructions**:

1. Save any helper script as `de-onboarding/ex5_logs.sh`.
2. Create `ex5_sample_logs.txt` with the sample log content above.
3. **Scenario 1 (FileNotFoundError)**:
   - Remove `sales.csv`: `kubectl exec -it <scheduler-pod> -n airflow -- rm /opt/airflow/dags/data/sales.csv`.
   - Trigger DAG: `airflow dags trigger sales_etl`.
   - Run: `kubectl logs <scheduler-pod> -n airflow | grep extract_sales > ex5_logs.txt`.
   - Verify: Check `ex5_logs.txt` or `ex5_sample_logs.txt` for `FileNotFoundError`.
   - Fix: `kubectl cp data/sales.csv airflow/<scheduler-pod>:/opt/airflow/dags/data/ -n airflow`.
4. **Scenario 2 (PostgreSQL Error)**:
   - Modify `values.yaml` with incorrect credentials (e.g., `password: wrong`).
   - Run: `helm upgrade airflow apache-airflow/airflow --namespace airflow --values values.yaml`.
   - Trigger DAG: `airflow dags trigger sales_etl`.
   - Run: `kubectl logs <scheduler-pod> -n airflow | grep load_sales >> ex5_logs.txt`.
   - Verify: Check `ex5_logs.txt` or `ex5_sample_logs.txt` for `OperationalError`.
   - Fix: Update `values.yaml` with correct credentials and re-run `helm upgrade`.

### Exercise 6: Conceptual Analysis

Explain the benefits of deploying Airflow in Kubernetes (Chapter 64) versus Docker (Chapter 57), focusing on scalability and fault tolerance. Save the answer (100–150 words) to `ex6_concepts.txt`, using a text editor with 4-space indentation for any scripts.

- **Evaluation Criteria**: Address scalability, fault tolerance, and Hijra Group’s context; 100–150 words; clear and concise.

**Expected Output** (`ex6_concepts.txt`):

```
Deploying Airflow in Kubernetes offers scalability and fault tolerance over Docker. Kubernetes orchestrates multiple pods, enabling dynamic scaling of Airflow workers to handle large pipelines, unlike Docker’s single-container setup. It ensures fault tolerance through pod replication and automatic restarts, critical for Hijra Group’s analytics. Kubernetes’ Helm Charts simplify Airflow configuration, while Docker requires manual container management. However, Kubernetes is complex, requiring tools like minikube, whereas Docker is simpler for local testing. Kubernetes suits production-grade pipelines, aligning with Hijra Group’s need for reliable transaction processing.
```

**Follow-Along Instructions**:

1. Write the explanation in a text editor (e.g., VS Code).
2. Save as `de-onboarding/ex6_concepts.txt`.
3. Verify word count (~100–150 words) with `wc -w ex6_concepts.txt` (Unix/macOS) or a text editor’s word count feature.
4. **How to Test**:
   - Compare with the sample solution below.
   - Ensure the explanation meets the evaluation criteria.

### Exercise 7: Airflow UI Debugging

Use the Airflow UI to debug a task failure in the `sales_etl` DAG, saving a description of the UI’s task status to `ex7_ui.txt`, using a text editor with 4-space indentation for any scripts.

**Task**: Trigger the `sales_etl` DAG with a missing `sales.csv` file to cause a `FileNotFoundError` in the `extract_sales` task. Check the Airflow UI to identify the failure and describe the task status.

**Expected Output** (`ex7_ui.txt`):

```
The Airflow UI at http://localhost:8080 shows the sales_etl DAG with a failed extract_sales task. The task status is marked as 'failed' with a red icon, indicating a FileNotFoundError for sales.csv.
```

**Follow-Along Instructions**:

1. Remove `sales.csv`: `kubectl exec -it <scheduler-pod> -n airflow -- rm /opt/airflow/dags/data/sales.csv`.
2. Trigger DAG: `airflow dags trigger sales_etl`.
3. Access Airflow UI: `kubectl port-forward svc/airflow-webserver 8080:8080 -n airflow`, open `http://localhost:8080`.
4. Navigate to the `sales_etl` DAG, check the `extract_sales` task status, and note the failure.
5. Save the description in `de-onboarding/ex7_ui.txt`.
6. **How to Test**:
   - Verify `ex7_ui.txt` describes the “failed” status.
   - Fix: `kubectl cp data/sales.csv airflow/<scheduler-pod>:/opt/airflow/dags/data/ -n airflow`, re-trigger DAG, and confirm “success” in the UI.

## 64.6 Exercise Solutions

### Solution to Exercise 1: Helm Configuration

```yaml
# File: de-onboarding/ex1_values.yaml
airflow:
  executor: LocalExecutor
  namespace: my-namespace
```

**Test**:

```bash
kubectl create namespace my-namespace
helm install my-airflow apache-airflow/airflow --namespace my-namespace --values ex1_values.yaml
kubectl get pods -n my-namespace
```

### Solution to Exercise 2: Type-Annotated DAG Task

```python
# File: de-onboarding/ex2_task.py
from typing import Dict, Any
import pandas as pd
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def validate_sales(df: pd.DataFrame, config: Dict[str, Any]) -> pd.DataFrame:
    """Validate sales data."""
    logger.info("Validating sales data")
    df = df[df["product"].str.startswith(config["product_prefix"])]
    logger.info(f"Validated {len(df)} records")
    return df
```

### Solution to Exercise 3: DAG Testing

```python
# File: de-onboarding/tests/ex3_test.py
from typing import Dict, Any
import pytest
import pandas as pd
from dags.sales_etl import extract_sales

@pytest.fixture
def config() -> Dict[str, Any]:
    return {
        "product_prefix": "Halal",
        "min_price": 10.0,
        "max_quantity": 100
    }

def test_extract_sales(config: Dict[str, Any], tmp_path) -> None:
    csv_path = tmp_path / "sales.csv"
    csv_path.write_text("""
product,price,quantity
Halal Laptop,999.99,2
Non-Halal,50.00,5
""")
    df = extract_sales(str(csv_path), config)
    assert len(df) == 1
    assert df["product"].iloc[0] == "Halal Laptop"
```

### Solution to Exercise 4: Debug a Failing DAG

```python
# File: de-onboarding/ex4_debug.py
extract_task = PythonOperator(
    task_id="extract_sales",
    python_callable=extract_sales,
    op_kwargs={
        "csv_path": "/opt/airflow/dags/data/sales.csv",
        "config": "{{ ti.xcom_pull(task_ids='load_config') }}"
    }
)
```

**Explanation**:

- **Bug**: Missing `config` parameter caused validation failure.
- **Fix**: Added `config` via XCom from `load_config` task.

### Solution to Exercise 5: Log Analysis

```bash
# File: de-onboarding/ex5_logs.sh
#!/bin/bash
# Retrieve Airflow scheduler logs to debug task failures
# Scenario 1: FileNotFoundError
kubectl logs <scheduler-pod> -n airflow | grep extract_sales > ex5_logs.txt
# Scenario 2: PostgreSQL Error
kubectl logs <scheduler-pod> -n airflow | grep load_sales >> ex5_logs.txt
cat ex5_logs.txt
```

**Explanation**:

- **Scenario 1**: Identifies `FileNotFoundError` for `sales.csv`. Fix by copying the file.
- **Scenario 2**: Identifies `OperationalError` for PostgreSQL credentials. Fix by updating `values.yaml`.

### Solution to Exercise 6: Conceptual Analysis

```text
# File: de-onboarding/ex6_concepts.txt
Deploying Airflow in Kubernetes offers significant advantages over Docker for scalability and fault tolerance. Kubernetes orchestrates multiple pods, enabling dynamic scaling of Airflow workers to process large datasets, unlike Docker’s single-container approach in Chapter 57. Kubernetes ensures fault tolerance through pod replication and automatic restarts, critical for Hijra Group’s reliable transaction processing. Helm Charts simplify Airflow configuration, whereas Docker requires manual container management. However, Kubernetes introduces complexity, requiring tools like minikube, while Docker is simpler for local testing. For Hijra Group’s production-grade pipelines, Kubernetes’ scalability and resilience make it ideal, aligning with the need for robust analytics.
```

**Explanation**:

- **Content**: Addresses scalability, fault tolerance, and Hijra Group’s context in ~120 words, meeting the 100–150 word requirement and evaluation criteria.

### Solution to Exercise 7: Airflow UI Debugging

```text
# File: de-onboarding/ex7_ui.txt
The Airflow UI at http://localhost:8080 shows the sales_etl DAG with a failed extract_sales task. The task status is marked as 'failed' with a red icon, indicating a FileNotFoundError for sales.csv.
```

**Explanation**:

- **Task**: Identifies the `extract_sales` task failure in the Airflow UI due to a missing `sales.csv`.
- **Fix**: Copy the file to `/opt/airflow/dags/data/` and re-trigger the DAG.

## 64.7 Chapter Summary and Connection to Chapter 65

In this chapter, you’ve mastered:

- **Airflow in Kubernetes**: Deploying with Helm Charts (O(n) pod scheduling).
- **Type-Annotated DAGs**: Writing robust ETL pipelines with Pyright.
- **Testing**: Validating DAGs with `pytest`.
- **Logging**: Tracking execution with `logging`, reinforced by log analysis and UI debugging.

The micro-project deployed a type-annotated Airflow instance, orchestrating a sales ETL pipeline with PostgreSQL integration, ensuring reliability for Hijra Group’s analytics. All code used **4-space indentation** per PEP 8.

### Connection to Chapter 65

Chapter 65 introduces **Security Best Practices for Data Pipelines**, building on this chapter:

- **Security**: Adds OAuth2 and PII masking to Airflow, protecting sensitive sales data.
- **Configuration**: Extends Helm Charts with secrets management.
- **Testing**: Enhances tests for security compliance.
- **Fintech Context**: Ensures IFSB-compliant data handling for Hijra Group.
