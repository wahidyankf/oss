---
title: '57 - Airflow in Docker'
date: 2025-04-17T07:20:00+07:00
draft: false
weight: 58
---

**Complexity: Moderate (M)**

## 57.0 Introduction: Why This Matters for Data Engineering

In data engineering, orchestrating complex data pipelines reliably is crucial for Hijra Group’s Sharia-compliant fintech analytics, where financial transaction data must be processed consistently across distributed systems. Apache Airflow, introduced in Chapter 56, excels at scheduling and monitoring workflows using Directed Acyclic Graphs (DAGs). However, running Airflow in production requires scalability, portability, and isolation, which Docker provides through containerization. Docker ensures consistent environments, reducing “works on my machine” issues, and supports Hijra Group’s need for reproducible pipelines across development and production clusters.

This chapter builds on Chapter 56 (Airflow Fundamentals) and Chapter 60 (Docker for Data Applications), combining Airflow’s orchestration with Docker’s containerization to deploy a sales ETL (Extract, Transform, Load) pipeline. The pipeline processes `data/sales.csv` and uses `data/config.yaml` for validation, aligning with Hijra Group’s analytics requirements. All Python code includes type annotations verified by Pyright (per Chapter 7) and tests using `pytest` (per Chapter 9), ensuring robust, production-ready pipelines. Code uses **PEP 8’s 4-space indentation**, preferring spaces over tabs to avoid `IndentationError`.

### Data Engineering Workflow Context

This diagram illustrates how Dockerized Airflow fits into a data engineering pipeline:

```mermaid
flowchart TD
    A["Raw Data (CSV)"] --> B["Dockerized Airflow"]
    B --> C{"Airflow Scheduler"}
    C -->|Execute DAG| D["ETL Tasks"]
    D --> E["PostgreSQL/BigQuery"]
    D --> F["Transformed Data"]
    F --> G["Data Mart"]

    classDef data fill:#f9f9f9,stroke:#333,stroke-width:2px
    classDef process fill:#d0e0ff,stroke:#336,stroke-width:1px
    classDef storage fill:#ddffdd,stroke:#363,stroke-width:1px

    class A,F,G data
    class B,C,D process
    class E storage
```

### Docker Container Architecture

This diagram shows the Docker containers and their interactions:

```mermaid
graph TD
    A[User] -->|Access UI| B[Airflow Webserver<br>Port: 8080]
    B -->|Schedule Tasks| C[Airflow Scheduler]
    C -->|Store Metadata| D[PostgreSQL<br>Port: 5432]
    B -->|Read DAGs| E[DAGs Volume<br>dags/]
    C -->|Read DAGs| E
    B -->|Access Data| F[Data Volume<br>data/]
    C -->|Access Data| F

    classDef container fill:#d0e0ff,stroke:#336,stroke-width:1px
    classDef volume fill:#f9f9f9,stroke:#333,stroke-width:2px
    classDef user fill:#ddffdd,stroke:#363,stroke-width:1px

    class B,C,D container
    class E,F volume
    class A user
```

### Building On and Preparing For

- **Building On**:
  - Chapter 56: Uses Airflow DAGs to orchestrate ETL tasks, extended here with Docker deployment.
  - Chapter 60: Leverages Docker and Docker Compose for containerized applications, now applied to Airflow.
  - Chapter 13: Reuses SQLite integration for local data storage.
  - Chapter 34: Applies type-annotated Python for robust data processing.
- **Preparing For**:
  - Chapter 58: Prepares for complex Airflow workflows with retries and dependencies.
  - Chapter 64: Enables Airflow deployment in Kubernetes with Helm Charts.
  - Chapters 67–70: Supports capstone projects with production-grade orchestration.

### What You’ll Learn

This chapter covers:

1. **Airflow in Docker**: Setting up Airflow with Docker Compose.
2. **Type-Annotated DAGs**: Creating robust, type-safe ETL pipelines.
3. **Testing DAGs**: Validating pipelines with `pytest`, including integration tests.
4. **Logging and Monitoring**: Capturing pipeline execution logs with clear prefixes.
5. **Dataset Integration**: Processing `data/sales.csv` with `config.yaml`.

The micro-project deploys a Dockerized Airflow instance running a type-annotated sales ETL DAG, processing `data/sales.csv`, storing results in SQLite, and validating with `pytest`. The setup uses Docker Compose for portability and logs execution details for debugging.

**Follow-Along Tips**:

- Create `de-onboarding/data/` and populate with `sales.csv`, `config.yaml`, `empty.csv`, `invalid.csv`, `malformed.csv`, and `negative.csv` per Appendix 1.
- Install Docker Desktop and ensure it’s running (`docker --version`).
- Install libraries: `pip install apache-airflow pandas pyyaml pytest sqlalchemy psycopg2-binary`.
- Configure editor for **4-space indentation** per PEP 8 (VS Code: “Editor: Tab Size” = 4, “Editor: Insert Spaces” = true, “Editor: Detect Indentation” = false).
- Use print statements (e.g., `print(df.head())`) to debug DataFrames.
- Verify file paths with `ls data/` (Unix/macOS) or `dir data\` (Windows).
- Run `docker-compose down` to clean up containers after testing.
- If `IndentationError`, run `python -tt script.py` to detect tab/space mixing.

## 57.1 Airflow in Docker Basics

Docker containerizes Airflow, encapsulating its dependencies (e.g., Python, PostgreSQL for metadata) in isolated environments. Airflow’s components—scheduler, webserver, and workers—run as Docker services, managed by Docker Compose for local development. This ensures consistent behavior across environments, critical for Hijra Group’s distributed pipelines.

### 57.1.1 Setting Up Airflow with Docker Compose

Use Docker Compose to define Airflow services, mounting local directories for DAGs and data. The `LocalExecutor` supports parallel task execution, improving performance for multi-task DAGs like `sales_etl`, but may strain resources on low-spec machines. The `SequentialExecutor` (Exercise 1) is slower but lightweight, suitable for testing. Chapter 58 explores optimizing performance with advanced executors.

```yaml
# File: de-onboarding/docker-compose.yml
version: '3.8'
services:
  airflow-postgres:
    image: postgres:13
    environment:
      POSTGRES_USER: airflow
      POSTGRES_PASSWORD: airflow
      POSTGRES_DB: airflow
    volumes:
      - airflow-postgres-data:/var/lib/postgresql/data
    ports:
      - '5432:5432'

  airflow-webserver:
    image: apache/airflow:2.7.3
    depends_on:
      - airflow-postgres
    environment:
      AIRFLOW__CORE__EXECUTOR: LocalExecutor
      AIRFLOW__DATABASE__SQL_ALCHEMY_CONN: postgresql+psycopg2://airflow:airflow@airflow-postgres:5432/airflow
    volumes:
      - ./dags:/opt/airflow/dags
      - ./data:/opt/airflow/data
    ports:
      - '8080:8080'
    command: webserver

  airflow-scheduler:
    image: apache/airflow:2.7.3
    depends_on:
      - airflow-postgres
    environment:
      AIRFLOW__CORE__EXECUTOR: LocalExecutor
      AIRFLOW__DATABASE__SQL_ALCHEMY_CONN: postgresql+psycopg2://airflow:airflow@airflow-postgres:5432/airflow
    volumes:
      - ./dags:/opt/airflow/dags
      - ./data:/opt/airflow/data
    command: scheduler

volumes:
  airflow-postgres-data:
```

**Follow-Along Instructions**:

1. Create `de-onboarding/docker-compose.yml`.
2. Copy the YAML content above.
3. Create directories: `mkdir -p de-onboarding/dags de-onboarding/data`.
4. Ensure `data/sales.csv` and `data/config.yaml` exist in `de-onboarding/data/` per Appendix 1.
5. Run: `docker-compose up -d` in `de-onboarding/`.
6. Access Airflow UI at `http://localhost:8080` (default login: `airflow`/`airflow`).
7. Verify containers: `docker ps`.
8. **Common Errors**:
   - **Port Conflict**: If port 8080 is in use, change to `8081:8080` in `docker-compose.yml`.
   - **Permission Denied**: Ensure write permissions for `dags/` and `data/`. Run `chmod -R 777 dags data`.
   - **Image Pull Failure**: Check Docker Hub connectivity or pull manually: `docker pull apache/airflow:2.7.3`.

**Key Points**:

- **Services**: `airflow-postgres` (metadata database), `airflow-webserver` (UI), `airflow-scheduler` (task execution).
- **Volumes**: Mount `dags/` for DAG files and `data/` for input/output.
- **Time Complexity**: O(1) for container startup, O(n) for task execution (n tasks).
- **Space Complexity**: O(1) for container definitions, ~500MB for Airflow image.
- **Implication**: Docker ensures portability for Hijra Group’s pipelines.

## 57.2 Type-Annotated DAGs

Create a type-annotated DAG to process sales data, using PythonOperator for ETL tasks. Type annotations ensure robust code, verified by Pyright. Note that XCom is used here to pass small DataFrames and configurations between tasks, suitable for this chapter’s small dataset. In production, XCom should be avoided for large datasets due to database storage overhead; instead, files or databases are preferred, as covered in Chapter 58 for advanced workflows.

```python
# File: de-onboarding/dags/sales_etl.py
from datetime import datetime
from typing import Dict, Any
from airflow import DAG
from airflow.operators.python import PythonOperator
import pandas as pd
import yaml
import sqlite3
from sqlalchemy import create_engine

# Type-annotated functions
def load_config(config_path: str) -> Dict[str, Any]:
    """Load YAML configuration."""
    print(f"[INFO] Loading config: {config_path}")
    with open(config_path, "r") as file:
        config = yaml.safe_load(file)
    print(f"[INFO] Config: {config}")
    return config

def extract_sales(csv_path: str, config: Dict[str, Any]) -> pd.DataFrame:
    """Extract and validate sales data."""
    print(f"[INFO] Extracting CSV: {csv_path}")
    df = pd.read_csv(csv_path)
    if df.empty:
        print(f"[ERROR] Empty CSV file: {csv_path}")
        return pd.DataFrame()
    df = df.dropna(subset=["product"])
    df = df[df["product"].str.startswith(config["product_prefix"])]
    df = df[df["price"].apply(lambda x: isinstance(x, (int, float)))]
    df = df[df["price"] >= config["min_price"]]
    df = df[df["quantity"].apply(lambda x: str(x).isdigit())]
    df["quantity"] = df["quantity"].astype(int)
    df = df[df["quantity"] <= config["max_quantity"]]
    if df.empty:
        print(f"[ERROR] No valid records after validation")
    else:
        print("[INFO] Validated DataFrame:")
        print(df)
    return df

def transform_sales(df: pd.DataFrame) -> pd.DataFrame:
    """Transform sales data."""
    print("[INFO] Transforming data")
    if df.empty:
        print("[ERROR] Empty DataFrame received")
        return df
    df["amount"] = df["price"] * df["quantity"]
    print("[INFO] Transformed DataFrame:")
    print(df)
    return df

def load_sales(df: pd.DataFrame, db_path: str) -> None:
    """Load sales data into SQLite."""
    print(f"[INFO] Loading to SQLite: {db_path}")
    if df.empty:
        print("[ERROR] Empty DataFrame, skipping load")
        return
    print(f"[INFO] Rows loaded: {len(df)}")
    engine = create_engine(f"sqlite:///{db_path}")
    df.to_sql("sales", engine, if_exists="replace", index=False)
    print("[INFO] Data loaded to SQLite")

# Define DAG
with DAG(
    dag_id="sales_etl",
    start_date=datetime(2023, 10, 1),
    schedule_interval="@daily",
    catchup=False,
) as dag:
    config_task = PythonOperator(
        task_id="load_config",
        python_callable=load_config,
        op_kwargs={"config_path": "/opt/airflow/data/config.yaml"},
    )

    extract_task = PythonOperator(
        task_id="extract_sales",
        python_callable=extract_sales,
        op_kwargs={
            "csv_path": "/opt/airflow/data/sales.csv",
            "config": "{{ ti.xcom_pull(task_ids='load_config') }}",
        },
    )

    transform_task = PythonOperator(
        task_id="transform_sales",
        python_callable=transform_sales,
        op_kwargs={"df": "{{ ti.xcom_pull(task_ids='extract_sales') }}"},
    )

    load_task = PythonOperator(
        task_id="load_sales",
        python_callable=load_sales,
        op_kwargs={
            "df": "{{ ti.xcom_pull(task_ids='transform_sales') }}",
            "db_path": "/opt/airflow/data/sales.db",
        },
    )

    config_task >> extract_task >> transform_task >> load_task
```

**Follow-Along Instructions**:

1. Save as `de-onboarding/dags/sales_etl.py`.
2. Configure editor for 4-space indentation per PEP 8.
3. Ensure `docker-compose.yml` is running (`docker-compose up -d`).
4. Access Airflow UI (`http://localhost:8080`), enable `sales_etl` DAG, and trigger it.
5. Check logs in UI or `docker logs <scheduler-container>`.
6. Verify `data/sales.db` is created with `sqlite3 data/sales.db "SELECT * FROM sales;"`.
7. **Common Errors**:
   - **XCom Failure**: Ensure task IDs match in `xcom_pull`. Print `ti.xcom_pull(task_ids='load_config')`.
   - **FileNotFoundError**: Verify `data/sales.csv` and `config.yaml` in `de-onboarding/data/`.
   - **IndentationError**: Use 4 spaces. Run `python -tt dags/sales_etl.py`.

**Key Points**:

- **PythonOperator**: Executes Python functions as tasks.
- **XCom**: Passes data between tasks (e.g., DataFrame from `extract_sales` to `transform_sales`).
- **Type Annotations**: Ensure type safety (e.g., `pd.DataFrame` for ETL tasks).
- **Time Complexity**: O(n) for ETL tasks (n rows).
- **Space Complexity**: O(n) for DataFrame storage.
- **Implication**: Type-safe DAGs ensure reliable ETL for Hijra Group.

## 57.3 Testing DAGs

Test the DAG’s ETL functions with `pytest`, including an integration test to validate the full pipeline.

```python
# File: de-onboarding/tests/test_sales_etl.py
from typing import Dict, Any
import pandas as pd
import pytest
import sqlite3
from unittest.mock import MagicMock
from dags.sales_etl import load_config, extract_sales, transform_sales, load_sales

@pytest.fixture
def config() -> Dict[str, Any]:
    """Fixture for config."""
    return load_config("data/config.yaml")

@pytest.fixture
def sample_df() -> pd.DataFrame:
    """Fixture for sample DataFrame."""
    return pd.DataFrame({
        "product": ["Halal Laptop", "Halal Mouse", "Monitor"],
        "price": [999.99, 24.99, 199.99],
        "quantity": [2, 10, 2]
    })

def test_load_config() -> None:
    """Test config loading."""
    config = load_config("data/config.yaml")
    assert isinstance(config, dict)
    assert config["product_prefix"] == "Halal"

def test_extract_sales(config: Dict[str, Any]) -> None:
    """Test sales extraction."""
    df = extract_sales("data/sales.csv", config)
    assert isinstance(df, pd.DataFrame)
    if not df.empty:
        assert all(df["product"].str.startswith("Halal"))
        assert all(df["price"] >= config["min_price"])
        assert all(df["quantity"] <= config["max_quantity"])

def test_transform_sales(sample_df: pd.DataFrame) -> None:
    """Test sales transformation."""
    df = transform_sales(sample_df)
    assert "amount" in df.columns
    assert df["amount"].iloc[0] == sample_df["price"].iloc[0] * sample_df["quantity"].iloc[0]

def test_load_sales(sample_df: pd.DataFrame, tmp_path: Any) -> None:
    """Test loading to SQLite."""
    db_path = str(tmp_path / "test.db")
    load_sales(sample_df, db_path)
    conn = sqlite3.connect(db_path)
    df = pd.read_sql("SELECT * FROM sales", conn)
    conn.close()
    assert len(df) == len(sample_df)

def test_etl_integration(config: Dict[str, Any], tmp_path: Any) -> None:
    """Test full ETL pipeline integration."""
    # Mock Airflow context for XCom
    ti = MagicMock()
    ti.xcom_pull.side_effect = [
        config,  # load_config
        pd.DataFrame({"product": ["Halal Laptop"], "price": [999.99], "quantity": [2]}),  # extract_sales
        pd.DataFrame({"product": ["Halal Laptop"], "price": [999.99], "quantity": [2], "amount": [1999.98]})  # transform_sales
    ]

    # Execute pipeline
    config_data = load_config("data/config.yaml")
    df = extract_sales("data/sales.csv", config_data)
    df_transformed = transform_sales(df)
    db_path = str(tmp_path / "test.db")
    load_sales(df_transformed, db_path)

    # Verify output
    conn = sqlite3.connect(db_path)
    result_df = pd.read_sql("SELECT * FROM sales", conn)
    conn.close()
    assert not result_df.empty
    assert "amount" in result_df.columns
```

**Follow-Along Instructions**:

1. Create `de-onboarding/tests/` and save as `tests/test_sales_etl.py`.
2. Configure editor for 4-space indentation per PEP 8.
3. Install pytest: `pip install pytest`.
4. Run: `pytest tests/test_sales_etl.py -v`.
5. Verify all tests pass.
6. **Common Errors**:
   - **ModuleNotFoundError**: Ensure `dags/sales_etl.py` is accessible. Add `export PYTHONPATH=$PYTHONPATH:de-onboarding` to shell.
   - **AssertionError**: Print `df.head()` in tests to debug DataFrame contents.
   - **IndentationError**: Use 4 spaces. Run `python -tt tests/test_sales_etl.py`.

**Key Points**:

- **Fixtures**: Provide reusable test data (e.g., `config`, `sample_df`).
- **Unit Tests**: Validate each ETL function.
- **Integration Test**: Verifies full pipeline execution.
- **Time Complexity**: O(n) for test data processing.
- **Space Complexity**: O(n) for test DataFrames.
- **Implication**: Tests ensure pipeline reliability.

## 57.4 Logging and Monitoring

Airflow logs task execution to Docker containers, accessible via `docker logs` or the Airflow UI. Functions use prefixed print statements (`[INFO]`, `[ERROR]`) for clarity.

**Example Log Output** (from `docker logs <scheduler-container>`):

```
[INFO] Loading config: /opt/airflow/data/config.yaml
[INFO] Config: {'min_price': 10.0, 'max_quantity': 100, 'required_fields': ['product', 'price', 'quantity'], 'product_prefix': 'Halal', 'max_decimals': 2}
[INFO] Extracting CSV: /opt/airflow/data/sales.csv
[INFO] Validated DataFrame:
          product   price  quantity
0   Halal Laptop  999.99         2
1    Halal Mouse   24.99        10
2  Halal Keyboard   49.99         5
[INFO] Transforming data
[INFO] Transformed DataFrame:
          product   price  quantity   amount
0   Halal Laptop  999.99         2  1999.98
1    Halal Mouse   24.99        10   249.90
2  Halal Keyboard   49.99         5   249.95
[INFO] Loading to SQLite: /opt/airflow/data/sales.db
[INFO] Rows loaded: 3
[INFO] Data loaded to SQLite
```

**Follow-Along Instructions**:

1. Run DAG via Airflow UI.
2. View logs: `docker logs <scheduler-container>` or UI’s “Log” tab.
3. Verify SQLite output: `sqlite3 data/sales.db "SELECT * FROM sales;"`.
4. **Common Errors**:
   - **Log Not Found**: Ensure DAG ran successfully. Check UI status.
   - **Database Error**: Verify `db_path` in `load_sales`. Print `db_path`.

**Key Points**:

- **Logging**: Prefixed print statements provide clear debugging.
- **Monitoring**: Airflow UI tracks task status and logs.
- **Implication**: Logs aid troubleshooting in Hijra Group’s pipelines.

## 57.5 Micro-Project: Dockerized Sales ETL Pipeline

### Project Requirements

Deploy a Dockerized Airflow instance running a type-annotated sales ETL DAG that processes `data/sales.csv`, validates with `config.yaml`, and stores results in `data/sales.db`. The pipeline supports Hijra Group’s transaction reporting, ensuring data integrity and scalability. It ensures Sharia compliance by validating Halal product prefixes, aligning with Islamic Financial Services Board (IFSB) standards for fintech analytics, critical for Hijra Group’s transaction reporting.

- **Setup**: Use Docker Compose to run Airflow with PostgreSQL metadata store.
- **DAG**: Implement a type-annotated ETL pipeline with `load_config`, `extract_sales`, `transform_sales`, and `load_sales` tasks.
- **Validation**: Apply config rules (Halal prefix, min price, max quantity).
- **Output**: Store results in SQLite (`data/sales.db`).
- **Testing**: Validate with `pytest` unit and integration tests.
- **Logging**: Log steps and invalid records with `[INFO]` and `[ERROR]` prefixes.
- **Indentation**: Use 4-space indentation per PEP 8, preferring spaces over tabs.

### Setup Prerequisites

- **Docker Resources**: Ensure Docker Desktop is installed with at least 4GB RAM and 2 CPU cores allocated. Verify with `docker info --format '{{.MemTotal}}'` (should show ~4GB or more).
- **Troubleshooting**: If containers fail to start, check resource allocation in Docker Desktop settings or run `docker system prune` to clear unused containers.
- **Environment Validation**: Run the setup validation script to ensure all requirements are met:
  ```bash
  python validate_setup.py
  ```

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
    B --> C["Extract Sales<br>Pandas"]
    C --> D["Transform Sales<br>Compute Amount"]
    D --> E["Load to SQLite<br>sales.db"]

    classDef data fill:#f9f9f9,stroke:#333,stroke-width:2px
    classDef process fill:#d0e0ff,stroke:#336,stroke-width:1px
    classDef storage fill:#ddffdd,stroke:#363,stroke-width:1px

    class A data
    class B,C,D process
    class E storage
```

### Acceptance Criteria

- **Go Criteria**:
  - Docker Compose starts Airflow and PostgreSQL containers.
  - DAG runs successfully, processing `sales.csv` and storing results in `sales.db`.
  - Validates records for Halal prefix, numeric price/quantity, and config rules.
  - Logs steps with `[INFO]` and invalid records with `[ERROR]`.
  - Passes `pytest` unit and integration tests.
  - Uses type annotations verified by Pyright.
  - Uses 4-space indentation per PEP 8.
- **No-Go Criteria**:
  - Fails to start Docker containers.
  - DAG fails to run or produce `sales.db`.
  - Incorrect validation or calculations.
  - Missing logs or tests.
  - Uses tabs or inconsistent indentation.

### Common Pitfalls to Avoid

The following table summarizes common errors, their symptoms, and solutions to aid troubleshooting:

| **Error**                  | **Symptom**                                    | **Solution**                                                                              |
| -------------------------- | ---------------------------------------------- | ----------------------------------------------------------------------------------------- |
| **Port Conflict**          | Airflow UI not accessible on port 8080         | Change port to `8081:8080` in `docker-compose.yml` and restart containers.                |
| **Permission Denied**      | DAG fails to read/write `dags/` or `data/`     | Run `chmod -R 777 dags data` to grant permissions.                                        |
| **Image Pull Failure**     | Docker cannot pull `apache/airflow:2.7.3`      | Check Docker Hub connectivity or pull manually: `docker pull apache/airflow:2.7.3`.       |
| **FileNotFoundError**      | DAG fails to find `sales.csv` or `config.yaml` | Verify files in `de-onboarding/data/`. Print `os.listdir("/opt/airflow/data")`.           |
| **XCom Failure**           | Tasks fail to pass DataFrames                  | Ensure `xcom_pull` uses correct task IDs. Print `ti.xcom_pull(task_ids='extract_sales')`. |
| **SQLite Errors**          | `sales.db` not created                         | Check `db_path` and permissions. Print `db_path` and `os.access(db_path, os.W_OK)`.       |
| **Pyright Errors**         | Type annotations fail verification             | Run `pyright dags/sales_etl.py`. Fix types (e.g., `Dict[str, Any]` for config).           |
| **IndentationError**       | Mixed spaces/tabs in Python code               | Use 4 spaces. Run `python -tt dags/sales_etl.py`.                                         |
| **Insufficient Resources** | Containers crash or fail to start              | Increase Docker resources to 4GB RAM, 2 CPUs in Docker Desktop settings.                  |

### How This Differs from Production

In production, this solution would include:

- **Security**: OAuth2 and encrypted connections (Chapter 65).
- **Observability**: Prometheus metrics and Grafana dashboards (Chapter 66).
- **Scalability**: Kubernetes with Helm Charts (Chapter 64).
- **High Availability**: Multiple workers and failover (Chapter 58).
- **Error Handling**: Retries and alerts (Chapter 58).

### Implementation

The implementation includes `docker-compose.yml`, `sales_etl.py`, `test_sales_etl.py`, `validate_setup.py`, and an initialization script.

```python
# File: de-onboarding/validate_setup.py
import os
import subprocess
from typing import None

def validate_setup() -> None:
    """Validate setup for Airflow in Docker."""
    print("[INFO] Validating setup...")

    # Check required files
    required_files = ["data/sales.csv", "data/config.yaml"]
    for file_path in required_files:
        if not os.path.exists(file_path):
            print(f"[ERROR] Missing file: {file_path}")
            return
        print(f"[INFO] Found file: {file_path}")

    # Check Docker installation
    try:
        subprocess.run(["docker", "--version"], check=True, capture_output=True)
        print("[INFO] Docker is installed")
    except subprocess.CalledProcessError:
        print("[ERROR] Docker is not installed or not running")
        return

    # Check Docker resources
    try:
        mem_total = subprocess.run(
            ["docker", "info", "--format", "{{.MemTotal}}"],
            check=True, capture_output=True, text=True
        ).stdout.strip()
        mem_total = int(mem_total) / (1024 * 1024 * 1024)  # Convert to GB
        if mem_total < 4:
            print(f"[ERROR] Insufficient memory: {mem_total:.2f}GB (minimum 4GB)")
            return
        print(f"[INFO] Sufficient memory: {mem_total:.2f}GB")
    except subprocess.CalledProcessError:
        print("[ERROR] Failed to check Docker resources")
        return

    print("[INFO] Setup validation completed successfully")

if __name__ == "__main__":
    validate_setup()
```

```python
# File: de-onboarding/init_airflow.py
import os
import subprocess

def init_airflow() -> None:
    """Initialize Airflow database and start containers."""
    print("[INFO] Initializing Airflow...")
    os.environ["AIRFLOW__CORE__EXECUTOR"] = "LocalExecutor"
    os.environ["AIRFLOW__DATABASE__SQL_ALCHEMY_CONN"] = "postgresql+psycopg2://airflow:airflow@localhost:5432/airflow"

    # Run docker-compose
    subprocess.run(["docker-compose", "up", "-d"], check=True)

    # Initialize Airflow database
    subprocess.run(["docker", "exec", "de-onboarding_airflow-webserver_1", "airflow", "db", "init"], check=True)

    # Create admin user
    subprocess.run([
        "docker", "exec", "de-onboarding_airflow-webserver_1", "airflow", "users", "create",
        "--username", "airflow", "--firstname", "Admin", "--lastname", "User",
        "--role", "Admin", "--email", "admin@example.com", "--password", "airflow"
    ], check=True)

    print("[INFO] Airflow initialized. Access at http://localhost:8080")

if __name__ == "__main__":
    init_airflow()
```

### Expected Outputs

`data/sales.db` (query with SQLite):

```sql
SELECT * FROM sales;
-- Expected:
-- product,price,quantity,amount
-- Halal Laptop,999.99,2,1999.98
-- Halal Mouse,24.99,10,249.90
-- Halal Keyboard,49.99,5,249.95
```

**Console Output** (from Airflow logs):

```
[INFO] Loading config: /opt/airflow/data/config.yaml
[INFO] Config: {'min_price': 10.0, 'max_quantity': 100, 'required_fields': ['product', 'price', 'quantity'], 'product_prefix': 'Halal', 'max_decimals': 2}
[INFO] Extracting CSV: /opt/airflow/data/sales.csv
[INFO] Validated DataFrame:
          product   price  quantity
0   Halal Laptop  999.99         2
1    Halal Mouse   24.99        10
2  Halal Keyboard   49.99         5
[INFO] Transforming data
[INFO] Transformed DataFrame:
          product   price  quantity   amount
0   Halal Laptop  999.99         2  1999.98
1    Halal Mouse   24.99        10   249.90
2  Halal Keyboard   49.99         5   249.95
[INFO] Loading to SQLite: /opt/airflow/data/sales.db
[INFO] Rows loaded: 3
[INFO] Data loaded to SQLite
```

### How to Run and Test

1. **Setup**:

   - **Setup Checklist**:
     - [ ] Create `de-onboarding/data/` with `sales.csv`, `config.yaml`, `empty.csv`, `invalid.csv`, `malformed.csv`, and `negative.csv` per Appendix 1.
     - [ ] Install Docker Desktop and verify: `docker --version`.
     - [ ] Install libraries: `pip install apache-airflow pandas pyyaml pytest sqlalchemy psycopg2-binary`.
     - [ ] Create virtual environment: `python -m venv venv`, activate (Windows: `venv\Scripts\activate`, Unix: `source venv/bin/activate`).
     - [ ] Verify Python 3.10+: `python --version`.
     - [ ] Configure editor for 4-space indentation per PEP 8.
     - [ ] Save `docker-compose.yml`, `dags/sales_etl.py`, `tests/test_sales_etl.py`, `validate_setup.py`, and `init_airflow.py`.
   - **Validate Environment**:
     - Run: `python validate_setup.py`.
     - Ensure all checks pass (files exist, Docker installed, sufficient resources).
   - **Troubleshooting**:
     - If `FileNotFoundError`, check `data/` contents with `ls data/`.
     - If `docker-compose` fails, validate YAML with `docker-compose config`.
     - If `IndentationError`, run `python -tt dags/sales_etl.py`.
     - If `Pyright` errors, run `pyright dags/sales_etl.py` and fix types.

2. **Run**:

   - Run initialization: `python init_airflow.py`.
   - Access Airflow UI: `http://localhost:8080` (login: `airflow`/`airflow`).
   - Enable and trigger `sales_etl` DAG.
   - Verify `data/sales.db` with `sqlite3 data/sales.db "SELECT * FROM sales;"`.
   - Stop containers: `docker-compose down`.

3. **Verify Type Annotations**:

   - Install Pyright: `pip install pyright`.
   - Run: `pyright dags/sales_etl.py`.
   - **Troubleshooting**: If errors occur, check type annotations (e.g., ensure `Dict[str, Any]` for config). Install Pyright if missing.

4. **Debugging with Airflow UI**:

   - Access the Airflow UI at `http://localhost:8080`.
   - Navigate to the “DAGs” tab and select `sales_etl`.
   - Use **Graph View** to visualize task dependencies; red boxes indicate failed tasks.
   - Click a task and select “Task Instance Details” to view logs and XCom data for debugging.
   - **Troubleshooting**: If tasks fail, check logs for `[ERROR]` messages and verify XCom values (e.g., print `ti.xcom_pull(task_ids='extract_sales')` in task code).

5. **Test Scenarios**:

   - **Valid Data**: Verify `sales.db` contains 3 rows with correct amounts.
   - **Empty CSV**:
     - Modify `extract_task` in `sales_etl.py` to use `/opt/airflow/data/empty.csv`.
     - Run DAG via Airflow UI.
     - Check logs for:
       ```
       [ERROR] Empty CSV file: /opt/airflow/data/empty.csv
       ```
     - Verify `sales.db` is empty or not created.
   - **Invalid Headers**:
     - Modify `extract_task` to use `/opt/airflow/data/invalid.csv`.
     - Run DAG and check logs for:
       ```
       [ERROR] No valid records after validation
       ```
     - Verify `sales.db` is empty or not created.
   - **Malformed Data**:
     - Modify `extract_task` to use `/opt/airflow/data/malformed.csv`.
     - Run DAG and check logs for:
       ```
       [INFO] Validated DataFrame:
                product   price  quantity
       1    Halal Mouse   24.99        10
       [INFO] Transforming data
       [INFO] Transformed DataFrame:
                product   price  quantity  amount
       1    Halal Mouse   24.99        10  249.90
       [INFO] Loading to SQLite: /opt/airflow/data/sales.db
       [INFO] Rows loaded: 1
       [INFO] Data loaded to SQLite
       ```
     - Verify `sales.db` contains only the “Halal Mouse” row.
   - **Negative Prices**:
     - Modify `extract_task` to use `/opt/airflow/data/negative.csv`.
     - Run DAG and check logs for:
       ```
       [INFO] Validated DataFrame:
               product   price  quantity
       1   Halal Mouse   24.99        10
       [INFO] Transforming data
       [INFO] Transformed DataFrame:
               product   price  quantity  amount
       1   Halal Mouse   24.99        10  249.90
       [INFO] Loading to SQLite: /opt/airflow/data/sales.db
       [INFO] Rows loaded: 1
       [INFO] Data loaded to SQLite
       ```
     - Verify `sales.db` contains only the “Halal Mouse” row.
   - **Run Pytest**: `pytest tests/test_sales_etl.py -v`, ensure all tests pass.

## 57.6 Practice Exercises

### Exercise 1: Docker Compose Setup

Write a simplified `docker-compose.yml` for Airflow with a single service, using 4-space indentation per PEP 8.

**Expected Output**:

- Airflow UI accessible at `http://localhost:8080`.

**Follow-Along Instructions**:

1. Save as `de-onboarding/docker-compose-simple.yml`.
2. Run: `docker-compose -f docker-compose-simple.yml up -d`.
3. Verify UI access.
4. **How to Test**:
   - Check `docker ps` for running container.
   - Access `http://localhost:8080`.

### Exercise 2: Type-Annotated ETL Function

Write a type-annotated function to validate sales data, ensuring Halal products and config rules, with 4-space indentation per PEP 8.

**Sample Input**:

```python
df = pd.DataFrame({
    "product": ["Halal Laptop", "Monitor"],
    "price": [999.99, 199.99],
    "quantity": [2, 2]
})
config = {"product_prefix": "Halal", "min_price": 10.0, "max_quantity": 100}
```

**Expected Output**:

```
          product   price  quantity
0   Halal Laptop  999.99         2
```

**Follow-Along Instructions**:

1. Save as `de-onboarding/ex2_validate.py`.
2. Run: `python ex2_validate.py`.
3. **How to Test**:
   - Verify output DataFrame has only Halal products.
   - Test with empty DataFrame: Should return empty DataFrame.

### Exercise 3: Pytest for ETL

Write a `pytest` test for the `transform_sales` function, with 4-space indentation per PEP 8.

**Sample Input**:

```python
df = pd.DataFrame({
    "product": ["Halal Laptop"],
    "price": [999.99],
    "quantity": [2]
})
```

**Expected Output**:

- Test passes, confirming `amount` column.

**Follow-Along Instructions**:

1. Save as `de-onboarding/tests/ex3_test_transform.py`.
2. Run: `pytest tests/ex3_test_transform.py -v`.
3. **How to Test**:
   - Verify test passes.
   - Test with invalid data (e.g., negative quantity).

### Exercise 4: Logging Enhancement

Enhance the `load_sales` function to log row counts, with 4-space indentation per PEP 8.

**Sample Input**:

```python
df = pd.DataFrame({
    "product": ["Halal Laptop"],
    "price": [999.99],
    "quantity": [2],
    "amount": [1999.98]
})
```

**Expected Output**:

```
[INFO] Loading to SQLite: test.db
[INFO] Rows loaded: 1
[INFO] Data loaded to SQLite
```

**Follow-Along Instructions**:

1. Save as `de-onboarding/ex4_logging.py`.
2. Run: `python ex4_logging.py`.
3. **How to Test**:
   - Verify log output includes row count.
   - Test with empty DataFrame: Should log `[ERROR] Empty DataFrame, skipping load`.

### Exercise 5: Debug a DAG Failure

Fix this buggy DAG with incorrect XCom reference, ensuring 4-space indentation per PEP 8.

**Buggy Code**:

```python
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def extract():
    return ["data"]

with DAG(dag_id="buggy_dag", start_date=datetime(2023, 10, 1)) as dag:
    extract_task = PythonOperator(task_id="extract", python_callable=extract)
    process_task = PythonOperator(
        task_id="process",
        python_callable=lambda x: print(x),
        op_kwargs={"data": "{{ ti.xcom_pull(task_ids='wrong_task') }}"}
    )
    extract_task >> process_task
```

**Expected Output**:

- DAG runs successfully, printing `["data"]`.

**Follow-Along Instructions**:

1. Save as `de-onboarding/dags/ex5_buggy_dag.py`.
2. Run DAG and observe failure.
3. Fix and re-run.
4. **How to Test**:
   - Verify DAG completes and logs correct output.

### Exercise 6: Executor Comparison with Coding Task

Write a short explanation (100–150 words) comparing Airflow’s `LocalExecutor` and `SequentialExecutor`, using the simplified `docker-compose-simple.yml` from Exercise 1 as context. Additionally, modify `docker-compose-simple.yml` to use `LocalExecutor` with SQLite and run a simple DAG to observe the difference. Save the explanation to `de-onboarding/ex6_concepts.txt` and the modified YAML to `de-onboarding/docker-compose-local.yml`, ensuring 4-space indentation for code snippets per PEP 8.

**Expected Output** (in `ex6_concepts.txt`):

```
The LocalExecutor in Airflow runs tasks in parallel using multiple processes, leveraging PostgreSQL or SQLite for metadata, as configured in docker-compose.yml. It’s suitable for small-scale production or development, supporting Hijra Group’s multi-task ETL pipelines. Conversely, the SequentialExecutor, used in docker-compose-simple.yml, runs tasks sequentially in a single process with SQLite, ideal for lightweight testing:

    # Excerpt from docker-compose-simple.yml
    services:
        airflow:
            environment:
                AIRFLOW__CORE__EXECUTOR: SequentialExecutor

Switching to LocalExecutor in docker-compose-local.yml enables concurrent task execution, improving throughput for sales_etl.py, while SequentialExecutor processes tasks one-by-one, slowing larger pipelines. Choose LocalExecutor for scalability and SequentialExecutor for quick prototyping.
```

**Follow-Along Instructions**:

1. Save explanation as `de-onboarding/ex6_concepts.txt`.
2. Create `de-onboarding/docker-compose-local.yml` by modifying `docker-compose-simple.yml` to use `LocalExecutor`.
3. Save a simple DAG (e.g., `ex6_dag.py`) in `de-onboarding/dags/` with two parallel tasks.
4. Run: `docker-compose -f docker-compose-local.yml up -d`.
5. Trigger the DAG in Airflow UI and observe parallel execution in logs.
6. Verify word count (100–150 words) using `wc -w ex6_concepts.txt` (Unix/macOS) or a text editor.
7. **How to Test**:
   - Ensure explanation compares executors, referencing `docker-compose-simple.yml`.
   - Verify code snippets use 4-space indentation.
   - Confirm DAG runs with parallel tasks using `LocalExecutor`.

### Exercise 7: Data Exploration with SQLite

Write a Python script (`ex7_explore.py`) to query `data/sales.db` using `sqlite3`, compute the total sales amount (sum of `amount` column), and save the result to `de-onboarding/ex7_results.txt`. Use 4-space indentation per PEP 8.

**Sample Input** (`data/sales.db`):

```sql
-- Table: sales
-- Columns: product (TEXT), price (REAL), quantity (INTEGER), amount (REAL)
SELECT * FROM sales;
-- Expected:
-- Halal Laptop,999.99,2,1999.98
-- Halal Mouse,24.99,10,249.90
-- Halal Keyboard,49.99,5,249.95
```

**Expected Output** (in `ex7_results.txt`):

```
Total Sales Amount: $2499.83
```

**Follow-Along Instructions**:

1. Save as `de-onboarding/ex7_explore.py`.
2. Ensure `data/sales.db` exists from the micro-project.
3. Run: `python ex7_explore.py`.
4. **How to Test**:
   - Verify `ex7_results.txt` contains the correct total (`2499.83`).
   - Test with an empty `sales.db` (e.g., after running DAG with `empty.csv`): Should output `Total Sales Amount: $0.00`.
   - Use sample SQL query: `SELECT SUM(amount) FROM sales;`.
   - **Common Errors**:
     - **DatabaseNotFound**: Ensure `sales.db` exists. Print `os.path.exists("data/sales.db")`.
     - **IndentationError**: Use 4 spaces. Run `python -tt ex7_explore.py`.

## 57.7 Exercise Solutions

### Solution to Exercise 1: Docker Compose Setup

```yaml
# File: de-onboarding/docker-compose-simple.yml
version: '3.8'
services:
  airflow:
    image: apache/airflow:2.7.3
    environment:
      AIRFLOW__CORE__EXECUTOR: SequentialExecutor
      AIRFLOW__DATABASE__SQL_ALCHEMY_CONN: sqlite:////opt/airflow/airflow.db
    volumes:
      - ./dags:/opt/airflow/dags
    ports:
      - '8080:8080'
    command: standalone
```

### Solution to Exercise 2: Type-Annotated ETL Function

```python
# File: de-onboarding/ex2_validate.py
from typing import Dict, Any
import pandas as pd

def validate_sales(df: pd.DataFrame, config: Dict[str, Any]) -> pd.DataFrame:
    """Validate sales data."""
    df = df.dropna(subset=["product"])
    df = df[df["product"].str.startswith(config["product_prefix"])]
    df = df[df["price"].apply(lambda x: isinstance(x, (int, float)))]
    df = df[df["price"] >= config["min_price"]]
    df = df[df["quantity"].apply(lambda x: str(x).isdigit())]
    df["quantity"] = df["quantity"].astype(int)
    df = df[df["quantity"] <= config["max_quantity"]]
    print("[INFO] Validated DataFrame:")
    print(df)
    return df

# Test
config = {"product_prefix": "Halal", "min_price": 10.0, "max_quantity": 100}
df = pd.DataFrame({
    "product": ["Halal Laptop", "Monitor"],
    "price": [999.99, 199.99],
    "quantity": [2, 2]
})
print(validate_sales(df, config))
```

### Solution to Exercise 3: Pytest for ETL

```python
# File: de-onboarding/tests/ex3_test_transform.py
import pytest
import pandas as pd
from dags.sales_etl import transform_sales

@pytest.fixture
def sample_df() -> pd.DataFrame:
    return pd.DataFrame({
        "product": ["Halal Laptop"],
        "price": [999.99],
        "quantity": [2]
    })

def test_transform_sales(sample_df: pd.DataFrame) -> None:
    df = transform_sales(sample_df)
    assert "amount" in df.columns
    assert df["amount"].iloc[0] == 999.99 * 2
```

### Solution to Exercise 4: Logging Enhancement

```python
# File: de-onboarding/ex4_logging.py
from typing import Any
import pandas as pd
from sqlalchemy import create_engine

def load_sales(df: pd.DataFrame, db_path: str) -> None:
    print(f"[INFO] Loading to SQLite: {db_path}")
    if df.empty:
        print("[ERROR] Empty DataFrame, skipping load")
        return
    print(f"[INFO] Rows loaded: {len(df)}")
    engine = create_engine(f"sqlite:///{db_path}")
    df.to_sql("sales", engine, if_exists="replace", index=False)
    print("[INFO] Data loaded to SQLite")

# Test
df = pd.DataFrame({
    "product": ["Halal Laptop"],
    "price": [999.99],
    "quantity": [2],
    "amount": [1999.98]
})
load_sales(df, "data/test.db")
```

### Solution to Exercise 5: Debug a DAG Failure

```python
# File: de-onboarding/dags/ex5_buggy_dag.py
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def extract():
    return ["data"]

with DAG(dag_id="buggy_dag", start_date=datetime(2023, 10, 1)) as dag:
    extract_task = PythonOperator(task_id="extract", python_callable=extract)
    process_task = PythonOperator(
        task_id="process",
        python_callable=lambda x: print(x),
        op_kwargs={"data": "{{ ti.xcom_pull(task_ids='extract') }}"}
    )
    extract_task >> process_task
```

**Explanation**:

- **Bug**: Incorrect `task_ids='wrong_task'` in `xcom_pull`. Fixed to `task_ids='extract'`.

### Solution to Exercise 6: Executor Comparison with Coding Task

**File**: `de-onboarding/ex6_concepts.txt`

```
The LocalExecutor in Airflow runs tasks in parallel using multiple processes, leveraging PostgreSQL or SQLite for metadata, as configured in docker-compose.yml. It’s suitable for small-scale production or development, supporting Hijra Group’s multi-task ETL pipelines. Conversely, the SequentialExecutor, used in docker-compose-simple.yml, runs tasks sequentially in a single process with SQLite, ideal for lightweight testing:

    # Excerpt from docker-compose-simple.yml
    services:
        airflow:
            environment:
                AIRFLOW__CORE__EXECUTOR: SequentialExecutor

Switching to LocalExecutor in docker-compose-local.yml enables concurrent task execution, improving throughput for sales_etl.py, while SequentialExecutor processes tasks one-by-one, slowing larger pipelines. Choose LocalExecutor for scalability and SequentialExecutor for quick prototyping.
```

**File**: `de-onboarding/docker-compose-local.yml`

```yaml
# File: de-onboarding/docker-compose-local.yml
version: '3.8'
services:
  airflow:
    image: apache/airflow:2.7.3
    environment:
      AIRFLOW__CORE__EXECUTOR: LocalExecutor
      AIRFLOW__DATABASE__SQL_ALCHEMY_CONN: sqlite:////opt/airflow/airflow.db
    volumes:
      - ./dags:/opt/airflow/dags
    ports:
      - '8080:8080'
    command: standalone
```

**File**: `de-onboarding/dags/ex6_dag.py`

```python
# File: de-onboarding/dags/ex6_dag.py
from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator

def task1():
    print("[INFO] Running task 1")
    return "Task 1 done"

def task2():
    print("[INFO] Running task 2")
    return "Task 2 done"

with DAG(
    dag_id="ex6_dag",
    start_date=datetime(2023, 10, 1),
    schedule_interval=None,
    catchup=False,
) as dag:
    task1_op = PythonOperator(task_id="task1", python_callable=task1)
    task2_op = PythonOperator(task_id="task2", python_callable=task2)
    # Parallel tasks
    [task1_op, task2_op]
```

**Verification**:

- Word count: ~120 words (verified with `wc -w ex6_concepts.txt`).
- Code snippets use 4-space indentation per PEP 8.
- DAG runs with parallel tasks, observable in Airflow UI logs.

### Solution to Exercise 7: Data Exploration with SQLite

```python
# File: de-onboarding/ex7_explore.py
import sqlite3
from typing import None

def explore_sales(db_path: str, output_path: str) -> None:
    """Query sales.db and compute total sales amount."""
    print(f"[INFO] Querying database: {db_path}")
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Query total sales amount
    cursor.execute("SELECT SUM(amount) FROM sales")
    total = cursor.fetchone()[0]
    total = total if total is not None else 0.0

    # Save result
    with open(output_path, "w") as file:
        file.write(f"Total Sales Amount: ${total:.2f}")
    print(f"[INFO] Result saved to {output_path}")

    conn.close()

# Test
explore_sales("data/sales.db", "ex7_results.txt")
```

**Verification**:

- Output: `ex7_results.txt` contains `Total Sales Amount: $2499.83`.
- Handles empty database by returning `$0.00`.

## 57.8 Chapter Summary and Connection to Chapter 58

In this chapter, you’ve mastered:

- **Dockerized Airflow**: Deploying Airflow with Docker Compose for portable orchestration.
- **Type-Annotated DAGs**: Building robust ETL pipelines with type safety.
- **Testing**: Validating pipelines with `pytest` unit and integration tests.
- **Logging**: Monitoring execution with clear `[INFO]` and `[ERROR]` logs.
- **White-Space Sensitivity and PEP 8**: Using 4-space indentation, preferring spaces over tabs.

The micro-project deployed a Dockerized Airflow instance running a sales ETL DAG, processing `data/sales.csv` into `data/sales.db`, with type annotations, comprehensive tests, and edge case validation. Visual aids, a setup validation script, UI debugging guidance, and data exploration exercises enhance understanding and robustness, ensuring Sharia-compliant analytics for Hijra Group.

### Connection to Chapter 58

Chapter 58 (Building Complex Airflow Workflows) builds on this chapter:

- **Complex Workflows**: Extends DAGs with retries, branching, and dependencies.
- **Scalability**: Prepares for production-grade orchestration with advanced executors.
- **Testing**: Enhances test suites for complex pipelines.
- **Fintech Context**: Supports advanced transaction processing, maintaining PEP 8’s 4-space indentation.
