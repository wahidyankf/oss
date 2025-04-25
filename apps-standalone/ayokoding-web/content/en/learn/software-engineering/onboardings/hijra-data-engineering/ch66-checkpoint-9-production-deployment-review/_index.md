---
title: '66 - Checkpoint 9: Production Deployment Review'
date: 2025-04-17T07:20:00+07:00
draft: false
weight: 67
---

**Complexity: Easy (E)**

## 66.0 Introduction: Why This Matters for Data Engineering

In data engineering, deploying robust, secure, and observable pipelines to production is critical for delivering scalable analytics at Hijra Group. This checkpoint consolidates skills from Chapters 60–65, covering Docker, Kubernetes, Helm Charts, PostgreSQL, Airflow, security, and observability. These ensure pipelines handle financial transaction data reliably, with PII protection for GDPR/PDPA compliance and observability for real-time monitoring. Building on prior phases, particularly Phase 8’s orchestration and Phase 7’s web integration, this chapter verifies your ability to deploy a type-annotated, tested Kubernetes pipeline with a Django dashboard, aligning with Hijra Group’s need for production-grade systems.

This chapter uses Python 3.10+, type annotations (Pyright-verified, Chapter 7), and testing (`pytest`, Chapter 9), with all code adhering to **PEP 8’s 4-space indentation**, preferring spaces over tabs to avoid `IndentationError`. The micro-project integrates `data/sales.csv` processing with Helm-managed deployments, PII masking, file-based logging, and Prometheus metrics, preparing for Phase 10’s capstone projects.

### Data Engineering Workflow Context

The following diagram illustrates the production deployment pipeline:

```mermaid
flowchart TD
    A["Raw Data (CSV)"] --> B["Dockerized Pipeline"]
    B --> C["Kubernetes Cluster"]
    C --> D["Helm Chart Deployment"]
    D --> E["PostgreSQL Database"]
    D --> F["Airflow DAGs"]
    D --> G["Django Dashboard"]
    E --> H["Secure Data Storage (PII Masked)"]
    F --> I["Orchestrated ETL"]
    G --> J["Observability Metrics (Prometheus)"]
    I --> K["Processed Data"]
    J --> L["Monitoring Dashboard"]

    classDef data fill:#f9f9f9,stroke:#333,stroke-width:2px
    classDef process fill:#d0e0ff,stroke:#336,stroke-width:1px
    classDef storage fill:#ddffdd,stroke:#363,stroke-width:1px
    classDef monitoring fill:#ffddaa,stroke:#933,stroke-width:1px

    class A,H,K data
    class B,C,D,F,I process
    class E storage
    class G,J,L monitoring
```

### Building On and Preparing For

- **Building On**:
  - **Chapter 60 (Docker)**: Containerizes pipelines for portability.
  - **Chapter 61–62 (Kubernetes)**: Deploys applications with Helm Charts.
  - **Chapter 63 (PostgreSQL in Kubernetes)**: Manages stateful databases.
  - **Chapter 64 (Airflow in Kubernetes)**: Orchestrates ETL with Helm.
  - **Chapter 65 (Security)**: Implements PII masking, encryption, OAuth2.
  - **Phase 8 (Orchestration)**: Leverages Airflow and Django (Chapters 52–59).
  - **Phase 7 (Web Integration)**: Uses Django for dashboards (Chapter 52).
- **Preparing For**:
  - **Chapter 67 (Capstone Planning)**: Plans end-to-end pipelines with Helm.
  - **Chapters 68–70 (Capstone Implementation)**: Builds scalable, secure pipelines.

### What You’ll Learn

This chapter reviews:

1. **Dockerized Pipelines**: Packaging applications with Docker Compose.
2. **Kubernetes Deployments**: Using Helm Charts for scalability.
3. **PostgreSQL Integration**: Secure, stateful data storage.
4. **Airflow Orchestration**: Scheduling ETL tasks.
5. **Django Dashboard**: Visualizing sales metrics with OAuth2.
6. **Security**: PII masking and API authentication.
7. **Observability**: File-based logging and Prometheus metrics.
8. **Testing**: Comprehensive `pytest` suites for reliability.

The micro-project builds a type-annotated Kubernetes pipeline processing `data/sales.csv`, with a Django dashboard, Helm Chart, PII masking, observability, and `pytest` tests, ensuring production readiness.

**Follow-Along Tips**:

- Create `de-onboarding/data/` with `sales.csv`, `empty.csv`, `invalid.csv`, `malformed.csv` per Appendix 1.
- Install dependencies: `pip install pandas psycopg2-binary django djangorestframework django-oauth-toolkit pyyaml pytest apache-airflow kubernetes prometheus-client`.
- Install Docker Desktop, Helm, `kubectl`, `minikube`, and `yamllint`.
- Configure editor for **4-space indentation** per PEP 8 (VS Code: “Editor: Tab Size” = 4, “Editor: Insert Spaces” = true, “Editor: Detect Indentation” = false). Run `python -tt app.py` or use Pylint to detect tab/space mixing.
- Use print statements (e.g., `print(df.head())`) for debugging.
- Verify file paths with `ls data/` (Unix/macOS) or `dir data\` (Windows).
- Check YAML syntax with `yamllint docker-compose.yml`.

## 66.1 Core Concepts

### 66.1.1 Dockerized Pipelines

Docker containers package applications with dependencies, ensuring consistency. A `Dockerfile` defines the image, and `docker-compose.yml` orchestrates services like PostgreSQL, Django, and Airflow.

- **Implementation**: Containers use ~500MB for a Python app, with O(1) startup time.
- **Time Complexity**: O(1) for container startup.
- **Space Complexity**: O(n) for image layers (n dependencies).

### 66.1.2 Kubernetes and Helm

Kubernetes manages container orchestration, with Helm Charts simplifying deployments. Pods scale dynamically, handling thousands of transactions.

- **Implementation**: Helm Charts (~10KB) define Deployments and Services.
- **Time Complexity**: O(n) for pod scaling (n pods).
- **Space Complexity**: O(n) for pod resources.

### 66.1.3 PostgreSQL in Kubernetes

PostgreSQL in StatefulSets ensures persistent storage, with backups for reliability.

- **Implementation**: Stores ~1MB for 10,000 sales records, O(log n) query time for indexed tables.
- **Time Complexity**: O(log n) for indexed queries.
- **Space Complexity**: O(n) for n records.

### 66.1.4 Airflow in Kubernetes

Airflow schedules ETL tasks in Kubernetes, using Helm for deployment. DAGs process sales data daily.

- **Implementation**: DAGs (~5KB) execute O(n) tasks for n records.
- **Time Complexity**: O(n) for task execution.
- **Space Complexity**: O(n) for task metadata.

### 66.1.5 Django Dashboard

Django with DRF provides a dashboard secured with OAuth2, serving ~100 requests/second.

- **Implementation**: O(n) rendering for n records.
- **Time Complexity**: O(n) for dashboard queries.
- **Space Complexity**: O(n) for session data.

### 66.1.6 Security and PII Protection

OAuth2 secures APIs, and PII (e.g., customer IDs) is masked with SHA-256, ensuring GDPR/PDPA compliance.

- **Implementation**: Hashing is O(1) per record, ~64 bytes per hash.
- **Time Complexity**: O(n) for masking n records.
- **Space Complexity**: O(n) for hashed data.

### 66.1.7 Observability

File-based logging (`/var/log/sales.log`) and Prometheus metrics track pipeline health, with ~10MB logs daily for 1,000 transactions.

- **Implementation**: O(n) for logging n events.
- **Time Complexity**: O(n) for metric collection.
- **Space Complexity**: O(n) for log storage.

## 66.2 Micro-Project: Kubernetes Sales Pipeline with Django Dashboard

### Project Requirements

Build a type-annotated Kubernetes pipeline processing `data/sales.csv`, with a Django dashboard, Helm Chart, PII masking, observability, and `pytest` tests. The pipeline supports Hijra Group’s transaction analytics, ensuring scalability and security.

- **Load**: Read `data/sales.csv` with Pandas.
- **Validate**: Ensure Halal products and valid data using `utils.py`.
- **Store**: Save to PostgreSQL with PII masking (hash customer IDs).
- **Orchestrate**: Use Airflow DAG to schedule ETL.
- **Visualize**: Display metrics in a Django dashboard with OAuth2.
- **Deploy**: Use Kubernetes with Helm Chart and secrets.
- **Secure**: Implement OAuth2 and encryption.
- **Monitor**: Log to `/var/log/sales.log` and expose Prometheus metrics at `/metrics`.
- **Test**: Write `pytest` tests for all components, including edge cases (`empty.csv`, `invalid.csv`, `malformed.csv`).
- **Indentation**: Use **4-space indentation** per PEP 8, preferring spaces over tabs.

### Dataset Seeding

Per Appendix 1, create `de-onboarding/data/` with:

- `sales.csv`: Sales transaction data.
- `empty.csv`: Empty CSV for edge case testing.
- `invalid.csv`: Invalid headers for error handling.
- `malformed.csv`: Non-numeric quantities for type validation.

**Instructions**:

1. Create `de-onboarding/data/`.
2. Copy `sales.csv`, `empty.csv`, `invalid.csv`, `malformed.csv` from Appendix 1.
3. Verify with `ls data/` (Unix/macOS) or `dir data\` (Windows).
4. Check file existence in scripts using `os.path.exists(csv_path)`.

**Sample Input** (`data/sales.csv`):

```csv
product,price,quantity
Halal Laptop,999.99,2
Halal Mouse,24.99,10
Halal Keyboard,49.99,5
,29.99,3
Monitor,invalid,2
Headphones,5.00,150
```

### Data Processing Flow

```mermaid
flowchart TD
    A["CSV<br>sales.csv"] --> B["Dockerized Pipeline"]
    B --> C["Kubernetes Pod"]
    C --> D["PostgreSQL (PII Masked)"]
    C --> E["Airflow DAG"]
    C --> F["Django Dashboard (OAuth2)"]
    D --> G["Validated Data"]
    E --> H["ETL Process"]
    F --> I["Sales Metrics"]
    H --> J["Processed Data"]
    I --> K["Prometheus Metrics"]

    classDef data fill:#f9f9f9,stroke:#333,stroke-width:2px
    classDef process fill:#d0e0ff,stroke:#336,stroke-width:1px
    classDef storage fill:#ddffdd,stroke:#363,stroke-width:1px
    classDef monitoring fill:#ffddaa,stroke:#933,stroke-width:1px

    class A,G,J data
    class B,C,E,H process
    class D storage
    class F,I,K monitoring
```

### Acceptance Criteria

- **Go Criteria**:
  - Loads and validates `sales.csv`, handling edge cases (`empty.csv`, `invalid.csv`, `malformed.csv`).
  - Stores data in PostgreSQL with hashed customer IDs.
  - Schedules ETL with Airflow DAG.
  - Displays metrics in Django dashboard with OAuth2 authentication.
  - Deploys via Kubernetes Helm Chart with secrets.
  - Secures with OAuth2 and PostgreSQL encryption.
  - Logs to `/var/log/sales.log` and exposes Prometheus metrics at `/metrics`.
  - Passes `pytest` tests (unit, integration, edge cases).
  - Uses 4-space indentation per PEP 8.
- **No-Go Criteria**:
  - Fails to deploy or process data.
  - Missing security, observability, or edge case handling.
  - Fails tests or uses incorrect indentation.

### Common Pitfalls to Avoid

1. **Docker Build Failures**:
   - **Problem**: Missing dependencies in `requirements.txt`.
   - **Solution**: Verify `requirements.txt` includes `prometheus-client`. Run `docker build . -t sales-pipeline`.
2. **Kubernetes Errors**:
   - **Problem**: Helm Chart YAML syntax error.
   - **Solution**: Run `helm lint charts/sales-pipeline` and `yamllint charts/sales-pipeline/templates/deployment.yaml`. Print `kubectl get pods`.
3. **PostgreSQL Connection**:
   - **Problem**: Connection refused.
   - **Solution**: Verify `DB_HOST` environment variable. Print `psycopg2.connect` params.
4. **Airflow DAG Issues**:
   - **Problem**: DAG not triggered.
   - **Solution**: Check logs with `kubectl logs`. Print DAG definition.
5. **Airflow Metadata Errors**:
   - **Problem**: Fails to connect to metadata database.
   - **Solution**: Verify `AIRFLOW__DATABASE__SQL_ALCHEMY_CONN` and run `airflow db init`. Print connection string.
6. **Airflow Webserver Access**:
   - **Problem**: Webserver not accessible at `http://localhost:8080`.
   - **Solution**: Check port conflicts with `docker ps`. Port-forward with `docker-compose port airflow-webserver 8080`.
7. **Django OAuth2 Failure**:
   - **Problem**: Invalid token.
   - **Solution**: Verify token endpoint with `curl -X POST http://localhost:8000/o/token/`. Print `requests.post` response.
8. **PII Masking**:
   - **Problem**: Unmasked data stored.
   - **Solution**: Print `hashlib.sha256` output for customer IDs.
9. **Edge Case Failures**:
   - **Problem**: `empty.csv` or `malformed.csv` crashes pipeline.
   - **Solution**: Check `df.empty` and type validation in `process_sales`. Print `df.head()`.
10. **IndentationError**:
    - **Problem**: Mixed spaces/tabs.
    - **Solution**: Use 4 spaces. Run `python -tt app.py` or `pylint app.py`.
11. **YAML Syntax Errors**:
    - **Problem**: Invalid `docker-compose.yml` or Helm Chart.
    - **Solution**: Run `yamllint docker-compose.yml`. Print file content for debugging.
12. **Prometheus Setup Errors**:
    - **Problem**: `ServiceMonitor` not detected.
    - **Solution**: Verify Prometheus operator namespace (`kubectl get pods -n monitoring`) and CRDs (`kubectl get crd`). Reinstall with `helm install --namespace monitoring`.

### How This Differs from Production

In production, this solution would include:

- **High Availability**: Multi-node Kubernetes clusters with redundancy.
- **Advanced Monitoring**: Grafana dashboards for visualization (Chapter 67).
- **CI/CD**: Automated deployments via GitHub Actions or Jenkins.
- **Scalability**: Auto-scaling for millions of records with Kubernetes HorizontalPodAutoscaler.
- **Compliance Audits**: Regular GDPR/PDPA audits with audit logs.

### Implementation

```python
# File: de-onboarding/utils.py
import hashlib
from typing import Dict, Any

def hash_pii(data: str) -> str:
    """Hash PII data using SHA-256."""
    return hashlib.sha256(data.encode()).hexdigest()

def validate_sale(sale: Dict[str, Any]) -> bool:
    """Validate sale record."""
    required_fields = ["product", "price", "quantity"]
    if not all(sale.get(field) for field in required_fields):
        print(f"Invalid sale: missing fields {sale}")
        return False
    if not sale["product"].startswith("Halal"):
        print(f"Invalid sale: non-Halal product {sale}")
        return False
    try:
        price = float(sale["price"])
        quantity = int(sale["quantity"])
        if price <= 0 or quantity <= 0 or quantity > 100:
            print(f"Invalid sale: invalid price/quantity {sale}")
            return False
    except (ValueError, TypeError):
        print(f"Invalid sale: non-numeric price/quantity {sale}")
        return False
    return True
```

```python
# File: de-onboarding/app.py
import pandas as pd
import psycopg2
from typing import Dict, List
from django.http import JsonResponse, HttpResponse
from django.views import View
from oauth2_provider.decorators import protected_resource
from prometheus_client import Counter, generate_latest
import logging
import os
from utils import hash_pii, validate_sale

# Prometheus metrics
sales_processed = Counter("sales_processed_total", "Total sales processed")

# Configure file-based logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("/var/log/sales.log"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class SalesProcessor:
    """Process sales data and store in PostgreSQL."""
    def __init__(self):
        self.db_config = {
            "dbname": os.environ.get("DB_NAME", "sales_db"),
            "user": os.environ.get("DB_USER", "postgres"),
            "password": os.environ.get("DB_PASSWORD", "password"),
            "host": os.environ.get("DB_HOST", "postgres-service"),
            "port": os.environ.get("DB_PORT", "5432")
        }
        self.conn = psycopg2.connect(**self.db_config)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self) -> None:
        """Create sales table."""
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS sales (
                id SERIAL PRIMARY KEY,
                customer_id VARCHAR(64),
                product TEXT,
                price FLOAT,
                quantity INTEGER
            )
        """)
        self.conn.commit()
        logger.info("Created sales table")

    def process_sales(self, csv_path: str) -> Dict[str, any]:
        """Process sales CSV."""
        if not os.path.exists(csv_path):
            logger.error(f"CSV not found: {csv_path}")
            return {"total_sales": 0.0, "valid_count": 0}

        logger.info(f"Loading CSV: {csv_path}")
        df = pd.read_csv(csv_path)
        if df.empty:
            logger.warning("Empty CSV provided")
            return {"total_sales": 0.0, "valid_count": 0}

        valid_sales = []
        for idx, row in df.iterrows():
            sale = row.to_dict()
            sale["customer_id"] = hash_pii(f"customer_{idx}")
            if validate_sale(sale):
                valid_sales.append(sale)
                sales_processed.inc()  # Increment Prometheus counter
            else:
                logger.warning(f"Skipped invalid sale: {sale}")

        self.store_sales(valid_sales)
        return {
            "total_sales": sum(s["price"] * s["quantity"] for s in valid_sales),
            "valid_count": len(valid_sales)
        }

    def store_sales(self, sales: List[Dict[str, any]]) -> None:
        """Store sales in PostgreSQL."""
        for sale in sales:
            self.cursor.execute("""
                INSERT INTO sales (customer_id, product, price, quantity)
                VALUES (%s, %s, %s, %s)
            """, (sale["customer_id"], sale["product"], float(sale["price"]), int(sale["quantity"])))
        self.conn.commit()
        logger.info(f"Stored {len(sales)} sales")

class SalesView(View):
    """Django view for sales metrics."""
    @protected_resource()
    def get(self, request):
        processor = SalesProcessor()
        results = processor.process_sales("data/sales.csv")
        logger.info(f"Served sales metrics: {results}")
        return JsonResponse(results)

def metrics(request):
    """Expose Prometheus metrics."""
    return HttpResponse(generate_latest(), content_type="text/plain")
```

```python
# File: de-onboarding/dags/sales_dag.py
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from app import SalesProcessor

def run_sales_processor():
    """Run sales processor."""
    processor = SalesProcessor()
    results = processor.process_sales("data/sales.csv")
    print(f"Processed sales: {results}")

with DAG("sales_etl", start_date=datetime(2025, 4, 25), schedule_interval="@daily") as dag:
    process_task = PythonOperator(
        task_id="process_sales",
        python_callable=run_sales_processor
    )
```

```python
# File: de-onboarding/tests/test_sales_processor.py
import pytest
import pandas as pd
from app import SalesProcessor
from utils import hash_pii

@pytest.fixture
def processor():
    return SalesProcessor()

def test_sales_processor(processor):
    results = processor.process_sales("data/sales.csv")
    assert results["valid_count"] == 3
    assert abs(results["total_sales"] - 2499.83) < 0.01

def test_empty_csv(processor):
    results = processor.process_sales("data/empty.csv")
    assert results["valid_count"] == 0
    assert results["total_sales"] == 0.0

def test_invalid_csv(processor):
    results = processor.process_sales("data/invalid.csv")
    assert results["valid_count"] == 0
    assert results["total_sales"] == 0.0

def test_malformed_csv(processor):
    results = processor.process_sales("data/malformed.csv")
    assert results["valid_count"] == 1  # Only Halal Mouse is valid
    assert abs(results["total_sales"] - 249.90) < 0.01

def test_pii_masking(processor):
    processor.process_sales("data/sales.csv")
    processor.cursor.execute("SELECT customer_id FROM sales LIMIT 1")
    customer_id = processor.cursor.fetchone()[0]
    assert len(customer_id) == 64  # SHA-256 hash length

def test_oauth_protected_endpoint():
    from django.test import Client
    client = Client()
    response = client.get("/sales/")
    assert response.status_code == 401  # Unauthorized without token
```

```yaml
# File: de-onboarding/requirements.txt
pandas
psycopg2-binary
django
djangorestframework
django-oauth-toolkit
pyyaml
pytest
apache-airflow
kubernetes
prometheus-client
```

```yaml
# File: de-onboarding/docker-compose.yml
version: '3.8'
services:
  postgres:
    image: postgres:latest
    environment:
      POSTGRES_DB: sales_db
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: password
    volumes:
      - postgres_data:/var/lib/postgresql/data
  web:
    build: .
    ports:
      - '8000:8000'
    environment:
      DB_NAME: sales_db
      DB_USER: postgres
      DB_PASSWORD: password
      DB_HOST: postgres-service
      DB_PORT: 5432
    volumes:
      - logs:/var/log
    depends_on:
      - postgres
  airflow-webserver:
    image: apache/airflow:latest
    environment:
      AIRFLOW__CORE__EXECUTOR: LocalExecutor
      AIRFLOW__DATABASE__SQL_ALCHEMY_CONN: postgresql+psycopg2://postgres:password@postgres-service:5432/sales_db
    ports:
      - '8080:8080'
    volumes:
      - ./dags:/opt/airflow/dags
    depends_on:
      - postgres
    command: airflow webserver
  airflow-scheduler:
    image: apache/airflow:latest
    environment:
      AIRFLOW__CORE__EXECUTOR: LocalExecutor
      AIRFLOW__DATABASE__SQL_ALCHEMY_CONN: postgresql+psycopg2://postgres:password@postgres-service:5432/sales_db
    volumes:
      - ./dags:/opt/airflow/dags
    depends_on:
      - postgres
    command: >
      bash -c "airflow db init && airflow scheduler"
volumes:
  postgres_data:
  logs:
```

```yaml
# File: de-onboarding/charts/sales-pipeline/values.yaml
database:
  name: sales_db
  user: postgres
  host: postgres-service
  port: '5432'
  passwordSecret:
    name: db-credentials
    key: password
```

```yaml
# File: de-onboarding/charts/sales-pipeline/templates/deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: sales-pipeline
spec:
  replicas: 2
  selector:
    matchLabels:
      app: sales-pipeline
  template:
    metadata:
      labels:
        app: sales-pipeline
    spec:
      containers:
        - name: web
          image: sales-pipeline:latest
          ports:
            - containerPort: 8000
          env:
            - name: DB_NAME
              value: { { .Values.database.name } }
            - name: DB_USER
              value: { { .Values.database.user } }
            - name: DB_PASSWORD
              valueFrom:
                secretKeyRef:
                  name: { { .Values.database.passwordSecret.name } }
                  key: { { .Values.database.passwordSecret.key } }
            - name: DB_HOST
              value: { { .Values.database.host } }
            - name: DB_PORT
              value: { { .Values.database.port } }
          volumeMounts:
            - name: logs
              mountPath: /var/log
      volumes:
        - name: logs
          emptyDir: {}
```

```yaml
# File: de-onboarding/charts/sales-pipeline/templates/prometheus.yaml
apiVersion: monitoring.coreos.com/v1
kind: ServiceMonitor
metadata:
  name: sales-pipeline-monitor
  labels:
    app: sales-pipeline
spec:
  selector:
    matchLabels:
      app: sales-pipeline
  endpoints:
    - port: web
      path: /metrics
```

### Expected Outputs

- **Database**: `sales` table with 3 valid records, customer IDs hashed (64-character SHA-256).
- **Dashboard**: JSON response at `/sales/` with `total_sales: 2499.83`, `valid_count: 3`, requiring OAuth2 token.
- **Logs**: Entries in `/var/log/sales.log` (e.g., “Stored 3 sales”).
- **Metrics**: Prometheus metrics at `/metrics` (e.g., `sales_processed_total`).
- **Tests**: All `pytest` tests pass, including edge cases.

**Sample Log** (`/var/log/sales.log`):

```
2025-04-25 10:00:00,123 - INFO - Created sales table
2025-04-25 10:00:01,456 - INFO - Loading CSV: data/sales.csv
2025-04-25 10:00:01,789 - WARNING - Skipped invalid sale: {'product': nan, 'price': 29.99, 'quantity': 3}
2025-04-25 10:00:02,012 - INFO - Stored 3 sales
```

**Sample Metrics** (`/metrics`):

```
# HELP sales_processed_total Total sales processed
# TYPE sales_processed_total counter
sales_processed_total 3.0
```

### How to Run and Test

1. **Setup**:

   - Create `de-onboarding/data/` with `sales.csv`, `empty.csv`, `invalid.csv`, `malformed.csv` per Appendix 1.
   - Install dependencies: `pip install -r requirements.txt`.
   - Install Docker Desktop, Helm, `kubectl`, `minikube`, `yamllint`.
   - Install `minikube`: `minikube start --driver=docker`. Verify with `kubectl cluster-info`.
   - Install Prometheus operator: `helm install prometheus prometheus-community/kube-prometheus-stack --namespace monitoring --create-namespace`. Verify CRDs with `kubectl get crd`. Troubleshoot conflicts with `helm uninstall prometheus --namespace monitoring`.
   - Configure editor for 4-space indentation per PEP 8.
   - Run PostgreSQL: `docker-compose up -d postgres`.
   - Initialize Airflow database: `docker-compose run airflow-scheduler airflow db init`.
   - Verify YAML: `yamllint docker-compose.yml`.
   - Create Kubernetes Secret: `kubectl create secret generic db-credentials --from-literal=password=password`.
   - Access Airflow webserver: `http://localhost:8080`. Troubleshoot port conflicts with `docker ps` and reassign ports if needed (e.g., `docker-compose.yml: ports: "8081:8080"`).

2. **Run Locally**:

   - Build Docker: `docker build . -t sales-pipeline`.
   - Run Compose: `docker-compose up`.
   - Access dashboard: `curl -H "Authorization: Bearer <token>" http://localhost:8000/sales/`.
   - View metrics: `curl http://localhost:8000/metrics`.
   - Access Airflow: `http://localhost:8080`.

3. **Deploy to Kubernetes**:

   - Start cluster: `minikube start`.
   - Install Helm Chart: `helm install sales-pipeline charts/sales-pipeline`.
   - Verify pods: `kubectl get pods`.
   - Verify Prometheus: `kubectl get servicemonitor -n monitoring`.
   - Port-forward: `kubectl port-forward svc/sales-pipeline 8000:8000`.

4. **Test**:
   - Run: `pytest tests/test_sales_processor.py -v`.
   - Verify database: `psql -h localhost -U postgres -d sales_db -c "SELECT * FROM sales;"`.
   - Check logs: `cat /var/log/sales.log` (or Docker volume).
   - Test edge cases:
     ```python
     processor = SalesProcessor()
     print(processor.process_sales("data/empty.csv"))  # {'total_sales': 0.0, 'valid_count': 0}
     print(processor.process_sales("data/invalid.csv"))  # {'total_sales': 0.0, 'valid_count': 0}
     print(processor.process_sales("data/malformed.csv"))  # {'total_sales': 249.90, 'valid_count': 1}
     ```

## 66.3 Practice Exercises

### Exercise 1: Dockerized Sales Processor

Write a Dockerized sales processor processing `data/sales.csv`, validating Sharia-compliant product prefixes (per IFSB standards), with 4-space indentation.

**Expected Output**:

```
Total Sales: 2499.83
Valid Count: 3
```

**Instructions**:

1. Save as `de-onboarding/ex1_docker.py`.
2. Create `Dockerfile` with `python:3.10` base image.
3. Run: `docker build -t ex1 . && docker run ex1`.
4. Test: Verify output, log file `/var/log/sales.log`, and Sharia-compliant prefix validation (e.g., “Halal”).

### Exercise 2: Helm Chart Deployment

Create a Helm Chart for the sales pipeline, deploying to Kubernetes.

**Expected Output**:

```
NAME: sales-pipeline
STATUS: deployed
```

**Instructions**:

1. Save as `de-onboarding/charts/ex2/`.
2. Run: `helm install ex2 charts/ex2`.
3. Test: `kubectl get pods` shows running pods.
4. Debug: Use `helm lint` for YAML errors.

### Exercise 3: PII Masking and Malformed CSV Test

Write a `pytest` test for PII masking and handling `malformed.csv` in `SalesProcessor`.

**Expected Output**:

```
test_pii_masking ... ok
test_malformed_csv ... ok
```

**Instructions**:

1. Save as `de-onboarding/tests/test_ex3.py`.
2. Run: `pytest test_ex3.py`.
3. Test: Verify customer IDs are 64-character hashes and `malformed.csv` processes only valid rows (e.g., Halal Mouse).

### Exercise 4: Debug Kubernetes Pod Crash

Fix a crashing pod due to misconfigured `DB_HOST`.

**Buggy Code** (`charts/sales-pipeline/templates/deployment.yaml`):

```yaml
env:
  - name: DB_HOST
    value: wrong-service
```

**Expected Output**:

```
kubectl get pods
NAME              READY   STATUS    RESTARTS
sales-pipeline    1/1     Running   0
```

**Instructions**:

1. Save buggy `deployment.yaml`.
2. Run: `helm install sales-pipeline charts/sales-pipeline`.
3. Debug: Check logs with `kubectl logs`. Fix `DB_HOST` to `postgres-service`.
4. Test: Re-run Helm install and verify pod status.

### Exercise 5: Helm Benefits with ConfigMap

Explain why Helm Charts simplify Kubernetes deployments, and create a ConfigMap template, saving to `de-onboarding/ex5_helm.txt` and `de-onboarding/ex5_helm/templates/configmap.yaml`.

**Expected Output** (`ex5_helm.txt`):

```
Helm Charts simplify Kubernetes deployments by providing templated, reusable configurations, reducing YAML duplication. They enable versioning, rollback, and dependency management (e.g., PostgreSQL charts), unlike raw manifests, which require manual updates. For Hijra Group, Helm streamlines pipeline deployments, ensuring consistency across environments.
```

**Expected Output** (`ex5_helm/templates/configmap.yaml`):

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: sales-config
data:
  environment: production
```

**Instructions**:

1. Write explanation in `ex5_helm.txt`.
2. Create `ex5_helm/templates/configmap.yaml`.
3. Test: Verify files with `cat ex5_helm.txt` and `yamllint ex5_helm/templates/configmap.yaml`.

## 66.4 Chapter Summary and Connection to Chapter 67

You’ve consolidated skills in Docker, Kubernetes, Helm, PostgreSQL, Airflow, Django, security, and observability, deploying a type-annotated pipeline with a secure Django dashboard. The micro-project processes `sales.csv`, stores data with PII masking, schedules ETL with Airflow, and monitors with Prometheus and file-based logging. Edge case testing (`empty.csv`, `invalid.csv`, `malformed.csv`) ensures robustness, while OAuth2 and Helm secrets secure the pipeline. The 4-space indentation per PEP 8 ensures maintainable code.

**Connection to Chapter 67**: Chapter 67 plans capstone projects, building on this checkpoint’s deployment skills to design end-to-end pipelines with FastAPI and Helm, using `transactions.csv` for broader analytics, extending `sales.csv`’s structure for time-series analysis.
