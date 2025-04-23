---
title: 'Overview'
date: 2025-04-15T07:20:00+07:00
draft: false
weight: 1
---

## Introduction

The **Data Engineering Onboarding Curriculum** is a 71-chapter program transforming programmers into proficient data engineers, tailored for Hijra Group’s ecosystem. It emphasizes PostgreSQL, BigQuery, SQLite, Kubernetes (with Helm Charts), Airflow, dbt, Django, and FastAPI for building robust, testable data pipelines, web UIs, and APIs, aligning with Hijra Group’s needs for scalable analytics and containerized deployments using Uvicorn. Structured for ~52-minute sessions, it features eleven phases with checkpoints (Chapters 6, 11, 18, 24, 30, 37, 45, 59, 66) and micro-projects for practical application, with all Python code after Chapter 7 using type annotations verified by Pyright and tested using `unittest` and/or `pytest` after Chapter 9. The curriculum is designed to be followed in a development environment, with setup instructions to be provided in chapter implementations.

This curriculum equips learners to handle financial transaction data analytics via production-ready pipelines and web interfaces, culminating in capstone projects integrating security, observability, and scalability, with quality built-in from early type safety and testing.

### Prerequisite Guide

The curriculum assumes basic programming (variables, loops, functions), command-line skills, and familiarity with Python files for organizing code. For Hijra Group learners needing a refresher, recommended resources (~10–20 hours) include:

- **Python Basics**: Codecademy’s “Learn Python 3” or freeCodeCamp’s Python course.
- **Command-Line Skills**: LinuxCommand.org or shell command tutorials.
- **Data Structures**: Coursera’s “Python Data Structures” for lists, dictionaries, sets.
- **Web Fundamentals**: freeCodeCamp’s REST API tutorial for HTTP, REST, and MVC concepts.
- **Kubernetes Basics**: Kubernetes.io’s introductory tutorials for container orchestration and Helm.

**Development Environment**: Learners should prepare a development environment with Python 3.10+, a code editor (e.g., VS Code), and necessary libraries (e.g., pandas, numpy, psycopg2-binary, google-cloud-bigquery, apache-airflow, dbt-core, fastapi, uvicorn, djangorestframework, pyyaml, pytest, hypothesis). Install tools like PostgreSQL, Docker Desktop, and Google Cloud SDK for database, containerization, and cloud tasks. A virtual environment is recommended to manage dependencies, using `pip` for library installation. Detailed setup instructions will be provided in chapter implementations.

## Pedagogical Approach

The curriculum employs a rigorous framework aligned with **Common Content Structure and Pedagogical Patterns**:

### Content Structure

- **Introduction**: Links topic to data engineering, includes Mermaid workflow diagrams, and previews content.
- **Core Concepts**: Progresses from basic to advanced, detailing applications, implementations, and complexity.
- **Micro-Project**: Features dataset seeding, acceptance criteria, pitfalls, and run/test instructions.
- **Exercises**: Includes 3–5 coding, conceptual, and debugging tasks with sample data.
- **Connection**: Summarizes learning and previews the next chapter.

### Pedagogical Patterns

- **Progressive Learning**: Builds on prior chapters, introducing complex topics post-prerequisites.
- **Visible Outputs**: Emphasizes tangible results (e.g., data, UIs, APIs) for clarity.
- **Real-World Application**: Uses Hijra Group-specific scenarios (e.g., financial data).
- **Challenge Anticipation**: Highlights pitfalls with solutions.
- **Complete Experience**: Provides self-contained projects.
- **Gradual Complexity**: Starts simple, advancing to complex applications.
- **Flexible Pacing**: Splits advanced topics (e.g., Django, Kubernetes) into 2–3 sessions.

### Additional Guidelines

- **Examples**: Uses descriptive examples without code snippets.
- **Dataset Seeding**: Ensures simple dataset creation, stored in `data/` folder.
- **Complexity Analysis**: Explains implementations and time/space complexity.
- **Micro-Projects**: Details criteria, pitfalls, and production differences.
- **Exercises**: Reinforces concepts with setup instructions for Python 3.10+, Docker Desktop, and Google Cloud Console.
- **Accessible Language**: Uses beginner-friendly explanations.
- **Type Annotations**: All Python code after Chapter 7 includes type annotations, verified by Pyright, ensuring type-safe pipelines.
- **Testing**: All Python code after Chapter 9 is tested using `unittest` and/or `pytest` as much as possible, ensuring built-in quality.

## Curriculum Structure

The curriculum spans **eleven phases** with checkpoints for consolidation:

- **Phase 1: Python Foundations (1–6)**: Covers Python basics, concluding with Checkpoint 1 (Chapter 6).
- **Phase 2: Python Code Quality (7–11)**: Focuses on type safety, testing, and code quality tools, concluding with Checkpoint 2 (Chapter 11).
- **Phase 3A: Database Fundamentals I (12–18)**: Introduces SQL, SQLite, PostgreSQL basics, and schema design, ending with Checkpoint 3A (Chapter 18).
- **Phase 3B: Database Fundamentals II (19–24)**: Covers advanced querying, optimization, and type-safe integration, ending with Checkpoint 3B (Chapter 24).
- **Phase 4: Cloud Analytics (25–30)**: Focuses on BigQuery, ending with Checkpoint 4 (Chapter 30).
- **Phase 5: Analytical Storage (31–37)**: Covers **data lakes**, **marts**, ETL, ending with Checkpoint 5 (Chapter 37).
- **Phase 6: Advanced Processing (38–45)**: Explores NumPy, Pandas, concurrency, advanced testing, ending with Checkpoint 6 (Chapter 45).
- **Phase 7: Web and Database Integration (46–51)**: Covers Jupyter, database patterns, PostgreSQL, Django, FastAPI, and BI tools, focusing on web and database integration.
- **Phase 8: Pipeline Orchestration (52–59)**: Includes dbt, Airflow, and orchestration, ending with Checkpoint 7 (Chapter 59).
- **Phase 9: Production Deployment (60–66)**: Covers Docker, Kubernetes, Helm, security, observability, CI/CD, ending with Checkpoint 8 (Chapter 66).
- **Phase 10: Capstone Projects (67–71)**: Focuses on planning and implementing end-to-end pipelines with Helm, security, and web interfaces.

Checkpoints require an 80% passing score. Chapters are Easy (E), Moderate (M), or Advanced (A).

## Chapter Summaries

### Phase 1: Python Foundations (Chapters 1–6)

1. **Python Core Language Essentials**

   - **Complexity**: Easy (E)
   - **Description**: Introduces Python syntax, data types (strings, integers, lists, dictionaries, sets, tuples), control flow (if, loops), functions (defining, calling, parameters, return values), variable scope (global, local), and basic environment concepts (Python interpreter, virtual environments, `pip`). The micro-project analyzes a sales CSV to compute metrics using functions, building foundational skills for data engineering pipelines.
   - **Learning Outcomes**: Learners gain proficiency in Python syntax, data structures, functions, scope, and environment basics, preparing for data handling in Chapter 2.
   - **Micro-Project**: Process a sales CSV dataset (`data/sales.csv`) using a function (e.g., `calculate_sales`) to calculate total sales and top products, incorporating sets to identify unique products and outputting a formatted report.
   - **Role**: Establishes Python basics for data handling and pipeline development.

2. **Python Data Handling and Error Management**

   - **Complexity**: Easy (E)
   - **Description**: Teaches file handling, CSV/JSON/YAML processing with PyYAML, Python modules for reusable code, string manipulation (e.g., split, join, strip), and basic debugging (e.g., reading error messages, print statements), avoiding try/except as it’s not yet introduced. Modules are introduced as `.py` files, covering creation (e.g., `utils.py`), importing (`import utils`), and organization to reduce duplication. The micro-project processes sales data with string-based validation, module-based parsing, and debugging, preparing for type safety.
   - **Learning Outcomes**: Learners master file handling, YAML parsing, string manipulation, basic debugging, and creating/importing Python modules for code organization, ready for static typing in Chapter 7 and modular design in Chapter 5.
   - **Micro-Project**: Enhance a sales data processor using `data/sales.csv` and `config.yaml`, implementing parsing and string cleaning functions (e.g., `parse_csv`, `load_yaml`, `clean_text`) in a `utils.py` module, importing them into the main script for validation and JSON export, and debugging any parsing issues.
   - **Role**: Enables robust data processing, configuration parsing, debugging, and modular code organization.

3. **Essential Data Libraries (NumPy and Pandas Basics)**

   - **Complexity**: Moderate (M)
   - **Description**: Introduces NumPy arrays and Pandas DataFrames for efficient data manipulation, focusing on their role in data engineering. The micro-project refactors a sales processor for analytics, preparing for type-safe Pandas and databases.
   - **Learning Outcomes**: Learners acquire data processing skills, ready for static typing in Chapter 7 and Phase 2.
   - **Micro-Project**: Refactor a sales processor using Pandas and NumPy for analytics and visualization with `data/sales.csv`.
   - **Role**: Equips learners with data processing tools.

4. **Web Integration and APIs**

   - **Complexity**: Moderate (M)
   - **Description**: Teaches API integration with requests, covering HTTP, REST, and MVC fundamentals. The micro-project fetches financial transaction data, preparing for OOP and web frameworks.
   - **Learning Outcomes**: Learners master external data integration, ready for OOP in Chapter 5, static typing in Chapter 7, and web frameworks in Chapters 51–52.
   - **Micro-Project**: Fetch and transform financial transaction data from an API, saving to `data/transactions.csv`.
   - **Role**: Enables data source integration and web basics.

5. **Object-Oriented Programming for Data Engineering**

   - **Complexity**: Moderate (M)
   - **Description**: Introduces OOP (classes, inheritance, SOLID principles) for modular code, emphasizing organization of classes in Python modules. The micro-project builds an OOP-based transaction data fetcher, using a module to structure classes, preparing for type-safe OOP.
   - **Learning Outcomes**: Learners master scalable code design and module-based class organization, ready for static typing in Chapter 7 and Phase 2.
   - **Micro-Project**: Develop an OOP-based fetcher for transaction data with extensible classes, organized in a `fetcher.py` module and imported into the main script, using `data/transactions.csv`.
   - **Role**: Enhances code modularity for pipelines.

6. **Checkpoint 1: Python Foundations Review**

   - **Complexity**: Easy (E)
   - **Description**: Consolidates Python skills via a tool integrating file processing, API fetching, Pandas, and OOP, with sample data inputs for self-contained exercises. Exercises reinforce integration, ensuring readiness for code quality and databases.
   - **Learning Outcomes**: Learners solidify Python proficiency, ready for Phase 2’s focus on code quality.
   - **Micro-Project**: Build a tool integrating file processing, API fetching, Pandas, and OOP for sales data using `data/sales.csv`.
   - **Role**: Verifies foundational skills for advanced Python development.

### Phase 2: Python Code Quality (Chapters 7–11)

7. **Static Typing with Python**

   - **Complexity**: Moderate (M)
   - **Description**: Introduces Pyright for type safety with Generics, Any, and typed exception handling, emphasizing configuration for type checking. The micro-project builds a type-safe sales data processor, preparing for annotations and testing. All subsequent Python code includes type annotations verified by Pyright.
   - **Learning Outcomes**: Learners write type-safe code, reducing errors in pipelines, ready for annotations in Chapter 8 and testing in Chapter 9.
   - **Micro-Project**: Develop a type-safe sales data processor with generic filtering, verified by Pyright, using `data/sales.csv`.
   - **Role**: Establishes type safety for robust pipelines.

8. **Python Annotations and Decorators**

   - **Complexity**: Moderate (M)
   - **Description**: Enhances type-annotated code with Pyright-verified annotations and decorators for logging and testing. The micro-project adds annotations and decorators to a sales processor, preparing for testing.
   - **Learning Outcomes**: Learners master advanced Python constructs with type annotations, ready for testing in Chapter 9 and pipeline testing in Chapters 42–43.
   - **Micro-Project**: Enhance a sales processor with type annotations and a logging decorator using `data/sales.csv`.
   - **Role**: Strengthens code modularity for quality and testing.

9. **Introduction to Testing in Python**

   - **Complexity**: Moderate (M)
   - **Description**: Introduces type-annotated testing with `unittest` and `pytest`, emphasizing test organization in modules. The micro-project tests a sales data function with both frameworks, preparing for code quality. All subsequent Python code includes tests with `unittest` and/or `pytest` as much as possible.
   - **Learning Outcomes**: Learners master testing basics with `unittest` and `pytest`, organizing tests in modules, ready for code quality in Chapter 10, database integration in Chapter 16, and pipeline testing in Chapters 42–43.
   - **Micro-Project**: Test a type-annotated sales data processing function with `unittest` and `pytest`, comparing syntax and benefits, organizing tests in a `tests/test_processor.py` module and importing the processor from `processor.py`, using `data/sales.csv`.
   - **Role**: Establishes foundational testing for robust pipelines.

10. **Data Engineering Code Quality**

- **Complexity**: Moderate (M)
- **Description**: Introduces black, ruff, Pyright, and pre-commit hooks for maintainable, type-annotated code with testing, emphasizing module-based code organization. The micro-project sets up a pre-commit pipeline for a sales script, preparing for Docker and CI/CD.
- **Learning Outcomes**: Learners ensure high-quality code across multiple modules, ready for Checkpoint 2 in Chapter 11 and production deployment in Phase 9.
- **Micro-Project**: Configure a pre-commit pipeline with black, ruff, Pyright, and pytest for a type-annotated sales script, organized in modules (e.g., `utils.py`, `processor.py`), using `data/sales.csv`.
- **Role**: Ensures reliable, tested code for scalable pipelines.

11. **Checkpoint 2: Python Code Quality Review**

- **Complexity**: Easy (E)
- **Description**: Consolidates type safety, annotations, testing, and code quality tools from Chapters 7–10. The micro-project builds a tested, type-annotated sales data tool with a pre-commit pipeline, preparing for database fundamentals.
- **Learning Outcomes**: Learners solidify code quality skills, ready for Phase 3A’s database fundamentals.
- **Micro-Project**: Build a type-annotated sales data processing tool with a logging decorator, pytest tests, and a pre-commit pipeline using `data/sales.csv`.
- **Role**: Verifies proficiency in producing robust, tested Python code.

### Phase 3A: Database Fundamentals I (Chapters 12–18)

12. **SQL Fundamentals with SQLite**

- **Complexity**: Easy (E)
- **Description**: Introduces SQL with SQLite for data manipulation. The micro-project builds a tested SQL tool to query a sales database, preparing for Python-SQLite integration.
- **Learning Outcomes**: Learners gain SQL proficiency, ready for Python integration in Chapter 13.
- **Micro-Project**: Develop a SQL tool for optimized sales database queries with pytest tests using `data/sales.db`.
- **Role**: Lays database operation foundations.

13. **Python and SQLite Integration**

- **Complexity**: Moderate (M)
- **Description**: Integrates type-annotated Python with SQLite using `sqlite3`, YAML configs, and Pydantic for validation. The micro-project builds a tested data loader with validated sales data, preparing for PostgreSQL and type-safe programming.
- **Learning Outcomes**: Learners master programmatic database access with Pydantic and testing, ready for type-safe programming in Chapter 15 and advanced querying in Phase 3B.
- **Micro-Project**: Create a type-annotated Python data loader for SQLite sales data with YAML config, Pydantic validation, and pytest tests using `data/sales.csv` and `config.yaml`.
- **Role**: Enables dynamic, tested database operations with type safety.

14. **Advanced Database Operations with SQLite**

- **Complexity**: Moderate (M)
- **Description**: Explores advanced SQLite operations (transactions, views, triggers). The micro-project enhances a tested sales database, preparing for PostgreSQL.
- **Learning Outcomes**: Learners gain advanced database skills, ready for PostgreSQL in Chapter 16.
- **Micro-Project**: Enhance a sales database with transactions, views, and pytest tests using `data/sales.db`.
- **Role**: Strengthens database skills for enterprise systems.

15. **Type-Safe Database Programming**

- **Complexity**: Moderate (M)
- **Description**: Applies Pyright-verified typing to SQLite with type-annotated Pydantic and testing. The micro-project builds a tested, type-safe SQLite client, preparing for PostgreSQL and FastAPI.
- **Learning Outcomes**: Learners master type-safe database interactions, ready for PostgreSQL integration in Chapter 17 and integrated pipelines in Phase 3B.
- **Micro-Project**: Develop a type-safe SQLite client for sales data with Generics, type annotations, and pytest tests using `data/sales.db`.
- **Role**: Enhances database reliability for web frameworks.

16. **PostgreSQL Fundamentals**

- **Complexity**: Moderate (M)
- **Description**: Introduces PostgreSQL with `psycopg2` for production-grade databases. The micro-project sets up a tested sales database, preparing for Python integration.
- **Learning Outcomes**: Learners gain PostgreSQL proficiency, ready for Python integration in Chapter 17.
- **Micro-Project**: Set up a PostgreSQL sales database with optimized queries and pytest tests.
- **Role**: Transitions to enterprise databases.

17. **Python and PostgreSQL Integration**

- **Complexity**: Moderate (M)
- **Description**: Integrates type-annotated Python with PostgreSQL using Psycopg2 and YAML configs. The micro-project builds a tested sales data pipeline, preparing for schema design.
- **Learning Outcomes**: Learners master programmatic PostgreSQL, ready for schema design in Chapter 18 and advanced querying in Phase 3B.
- **Micro-Project**: Create a type-annotated PostgreSQL pipeline for sales data with YAML config and pytest tests using `config.yaml`.
- **Role**: Enables robust, tested database interactions.

18. **Checkpoint 3A: Database Fundamentals I Review**

- **Complexity**: Easy (E)
- **Description**: Consolidates SQL, SQLite, PostgreSQL basics, type-safe programming, and schema design skills from Chapters 12–17. The micro-project builds a tested database tool integrating SQLite and PostgreSQL basics, preparing for advanced database topics.
- **Learning Outcomes**: Learners solidify foundational database expertise, ready for Phase 3B’s advanced querying and optimization.
- **Micro-Project**: Build a type-annotated database tool integrating SQLite and PostgreSQL operations and schema design, validated with pytest tests using `data/sales.db`.
- **Role**: Verifies foundational database skills, bridging to Phase 3B.

### Phase 3B: Database Fundamentals II (Chapters 19–24)

19. **Advanced SQL Querying with SQLite**

- **Complexity**: Moderate (M)
- **Description**: Teaches advanced SQL querying techniques in SQLite, including joins, subqueries, and aggregations for complex analytics. The micro-project builds a tested query tool for sales data analysis, preparing for optimization.
- **Learning Outcomes**: Learners master complex SQL queries, ready for indexing and optimization in Chapter 20.
- **Micro-Project**: Develop a SQL query tool for advanced sales data analysis (e.g., multi-table joins, aggregations) with pytest tests using `data/sales.db`.
- **Role**: Enhances analytical querying skills for data engineering.

20. **SQLite Indexing and Optimization**

- **Complexity**: Moderate (M)
- **Description**: Covers indexing and query optimization in SQLite to improve performance. The micro-project optimizes a sales database with indexes, preparing for PostgreSQL optimization.
- **Learning Outcomes**: Learners optimize SQLite databases, ready for PostgreSQL querying in Chapter 21.
- **Micro-Project**: Optimize a sales database with indexes and query tuning, validated with pytest tests using `data/sales.db`.
- **Role**: Strengthens database performance for efficient data retrieval.

21. **Advanced PostgreSQL Querying**

- **Complexity**: Moderate (M)
- **Description**: Explores advanced PostgreSQL querying techniques, including common table expressions (CTEs) and window functions for complex analytics. The micro-project builds a tested query tool for transaction data, preparing for optimization.
- **Learning Outcomes**: Learners master advanced PostgreSQL queries, ready for indexing and optimization in Chapter 22.
- **Micro-Project**: Develop a PostgreSQL query tool for transaction data analysis (e.g., CTEs, window functions) with pytest tests using `data/transactions.csv`.
- **Role**: Enhances analytical capabilities for enterprise databases.

22. **PostgreSQL Indexing and Optimization**

- **Complexity**: Moderate (M)
- **Description**: Teaches indexing and query optimization in PostgreSQL to enhance performance. The micro-project optimizes a transaction database with indexes, preparing for integrated pipelines.
- **Learning Outcomes**: Learners optimize PostgreSQL databases, ready for type-safe integration in Chapter 23.
- **Micro-Project**: Optimize a transaction database with indexes and query tuning, validated with pytest tests using `data/transactions.csv`.
- **Role**: Prepares for efficient database operations in production systems.

23. **Type-Safe Database Integration**

- **Complexity**: Moderate (M)
- **Description**: Advances type-safe programming with integrated SQLite and PostgreSQL pipelines using `sqlite3`, `psycopg2`, and Pydantic. The micro-project builds a tested, type-safe data pipeline, preparing for cloud analytics.
- **Learning Outcomes**: Learners master integrated, type-safe database pipelines, ready for Phase 4’s cloud analytics.
- **Micro-Project**: Build a type-safe data pipeline integrating SQLite and PostgreSQL with Pydantic validation and pytest tests using `data/sales.csv` and `data/transactions.csv`.
- **Role**: Bridges database skills to cloud-based analytics.

24. **Checkpoint 3B: Database Fundamentals II Review**

- **Complexity**: Easy (E)
- **Description**: Consolidates advanced SQL, SQLite, PostgreSQL, type-safe programming, schema design, querying, and optimization skills from Chapters 12–23. The micro-project builds a comprehensive database tool, preparing for cloud analytics.
- **Learning Outcomes**: Learners solidify database expertise, ready for Phase 4’s cloud analytics.
- **Micro-Project**: Build a type-annotated database tool integrating SQLite and PostgreSQL queries, optimization, and pytest tests using `data/sales.db` and `data/transactions.csv`.
- **Role**: Finalizes database proficiency, bridging to Phase 4.

### Phase 4: Cloud Analytics (Chapters 25–30)

25. **BigQuery Fundamentals**

- **Complexity**: Moderate (M)
- **Description**: Introduces BigQuery for cloud analytics with `google-cloud-bigquery`. The micro-project creates a tested sales dataset, preparing for Python integration.
- **Learning Outcomes**: Learners gain BigQuery proficiency, ready for Python integration in Chapter 26.
- **Micro-Project**: Create a BigQuery sales dataset with key metric queries and pytest tests using `data/sales.csv`.
- **Role**: Establishes cloud analytics skills.

26. **Python and BigQuery Integration**

- **Complexity**: Moderate (M)
- **Description**: Teaches type-annotated programmatic BigQuery analytics with Python. The micro-project loads and queries tested sales data, preparing for advanced querying.
- **Learning Outcomes**: Learners master BigQuery automation, ready for advanced querying in Chapter 27.
- **Micro-Project**: Develop a type-annotated Python script to load and query sales data in BigQuery with pytest tests using `data/sales.csv`.
- **Role**: Enables automated cloud analytics.

27. **BigQuery Advanced Querying**

- **Complexity**: Moderate (M)
- **Description**: Explores advanced BigQuery querying (window functions, CTEs). The micro-project analyzes tested sales trends, preparing for data warehousing.
- **Learning Outcomes**: Learners gain complex query skills, ready for data warehousing in Chapter 28.
- **Micro-Project**: Query sales data for trends using window functions, CTEs, and pytest tests using `data/sales.csv`.
- **Role**: Strengthens querying for large-scale storage.

28. **BigQuery Data Warehousing**

- **Complexity**: Moderate (M)
- **Description**: Teaches **data warehouse** design in BigQuery with star schemas. The micro-project builds a tested sales **data warehouse**, preparing for optimization.
- **Learning Outcomes**: Learners master **data warehouse** design, ready for optimization in Chapter 29 and data lakes in Chapter 31.
- **Micro-Project**: Design a sales **data warehouse** with fact/dimension tables and pytest tests using `data/sales.csv`.
- **Role**: Establishes **data warehouse** proficiency.

29. **BigQuery Optimization Techniques**

- **Complexity**: Moderate (M)
- **Description**: Optimizes BigQuery queries for performance and cost. The micro-project enhances a tested sales **data warehouse**, preparing for **data lakes**.
- **Learning Outcomes**: Learners optimize BigQuery, ready for Phase 5’s analytical storage.
- **Micro-Project**: Optimize sales **data warehouse** queries with partitioning and pytest tests using `data/sales.csv`.
- **Role**: Enhances **data warehouse** efficiency.

30. **Checkpoint 4: Cloud Analytics Review**

- **Complexity**: Easy (E)
- **Description**: Consolidates BigQuery and **data warehousing** skills. The micro-project builds a type-safe, tested analytics tool with type annotations, preparing for **data lakes** and **marts**.
- **Learning Outcomes**: Learners solidify cloud analytics, ready for Phase 5’s analytical storage.
- **Micro-Project**: Build a Pyright-verified sales analytics tool with BigQuery using type-annotated code and pytest tests using `data/sales.csv`.
- **Role**: Bridges to analytical storage systems.

### Phase 5 PSY: Analytical Storage (Chapters 31–37)

31. **Data Lakes with Google Cloud Storage**

- **Complexity**: Moderate (M)
- **Description**: Introduces GCS **data lake** creation with type-annotated `google-cloud-storage` and YAML configs. The micro-project sets up a tested financial transaction **data lake**, preparing for **data marts**.
- **Learning Outcomes**: Learners master **data lake** management, ready for data marts in Chapter 32 and advanced Python in Chapter 34.
- **Micro-Project**: Create a GCS **data lake** for transaction data with type-annotated YAML config and pytest tests using `data/transactions.csv` and `config.yaml`.
- **Role**: Establishes **data lake** proficiency.

32. **Data Marts with BigQuery**

- **Complexity**: Moderate (M)
- **Description**: Teaches **data mart** design in BigQuery for analytics, focusing on data freshness and performance. The micro-project builds a tested sales **data mart**, preparing for web frameworks.
- **Learning Outcomes**: Learners create targeted analytics, ready for Google Sheets integration in Chapter 33 and web frameworks in Chapters 51–52.
- **Micro-Project**: Design a sales **data mart** with optimized queries and pytest tests using `data/sales.csv`.
- **Role**: Completes analytical storage for reporting.

33. **BigQuery and Google Sheets Integration**

- **Complexity**: Moderate (M)
- **Description**: Exports **data mart** results to Sheets with type-annotated `gspread`. The micro-project creates tested stakeholder visualizations, preparing for web reporting.
- **Learning Outcomes**: Learners master reporting, ready for advanced Python in Chapter 34 and web frameworks in Chapters 51–52.
- **Micro-Project**: Export sales **data mart** results to Sheets with visualizations using type-annotated code and pytest tests using `data/sales.csv`.
- **Role**: Enables stakeholder communication.

34. **Advanced Python for Data Engineering**

- **Complexity**: Moderate (M)
- **Description**: Enhances type-annotated Python for **data lake** processing with `PyYAML` and logging. The micro-project processes tested transaction data, preparing for concurrency.
- **Learning Outcomes**: Learners refine Python skills with type annotations and testing, ready for GCS features in Chapter 35 and type-safe processing in Chapter 41.
- **Micro-Project**: Process **data lake** transaction data with type-annotated YAML config, logging, and pytest tests using `data/transactions.csv` and `config.yaml`.
- **Role**: Strengthens Python for advanced processing.

35. **Google Cloud Storage Advanced Features**

- **Complexity**: Moderate (M)
- **Description**: Explores advanced GCS features with type-annotated `google-cloud-storage` and YAML configs. The micro-project enhances a tested transaction **data lake**, preparing for production storage.
- **Learning Outcomes**: Learners master **data lake** operations, ready for advanced Python in Chapter 37.
- **Micro-Project**: Enhance a **data lake** with secure access, type-annotated YAML config, and pytest tests using `data/transactions.csv` and `config.yaml`.
- **Role**: Prepares for integrated storage solutions.

36. **Advanced Python for Data Engineering**

- **Complexity**: Moderate (M)
- **Description**: Further develops type-annotated Python for **data lake** processing with `PyYAML` and optimization. The micro-project optimizes tested transaction data processing, preparing for concurrency.
- **Learning Outcomes**: Learners enhance Python efficiency with type annotations and testing, ready for Checkpoint 5 in Chapter 37.
- **Micro-Project**: Optimize **data lake** transaction processing with type-annotated YAML config and pytest tests using `data/transactions.csv` and `config.yaml`.
- **Role**: Prepares for advanced processing.

37. **Checkpoint 5: Analytical Storage Review**

- **Complexity**: Easy (E)
- **Description**: Consolidates **data lake**, **data warehouse**, and **data mart** skills with robust ETL. The micro-project builds a tested ETL pipeline with type-annotated logging and validation, preparing for advanced processing.
- **Learning Outcomes**: Learners solidify storage expertise, ready for Phase 6’s advanced processing.
- **Micro-Project**: Build a robust type-annotated ETL pipeline from **data lake** to **data mart** with YAML config, logging, and pytest tests using `data/transactions.csv` and `config.yaml`.
- **Role**: Bridges to advanced data processing with testable pipelines.

### Phase 6: Advanced Processing (Chapters 38–45)

38. **Advanced NumPy**

- **Complexity**: Moderate (M)
- **Description**: Deepens type-annotated NumPy expertise with `numpy` for analytics. The micro-project analyzes tested sales data, preparing for Pandas.
- **Learning Outcomes**: Learners master numerical processing, ready for Pandas in Chapter 39.
- **Micro-Project**: Analyze sales data using type-annotated NumPy techniques with pytest tests using `data/sales.csv`.
- **Role**: Enhances computation for processing.

39. **Advanced Pandas**

- **Complexity**: Moderate (M)
- **Description**: Explores advanced type-annotated Pandas with `pandas` for data manipulation. The micro-project processes tested sales data, preparing for concurrency.
- **Learning Outcomes**: Learners master data manipulation, ready for concurrency in Chapter 40.
- **Micro-Project**: Process sales data with type-safe Pandas code and pytest tests using `data/sales.csv`.
- **Role**: Strengthens scalable processing.

40. **Concurrency in Python**

- **Complexity**: Advanced (A)
- **Description**: Teaches type-annotated concurrency with `aiohttp` for parallel processing. The micro-project parallelizes tested sales data processing with retries, preparing for type-safe processing.
- **Learning Outcomes**: Learners master concurrency, ready for type-safe processing in Chapter 41.
- **Micro-Project**: Parallelize sales data processing with type-annotated asyncio, retry logic, and pytest tests using `data/sales.csv`.
- **Role**: Enables efficient pipeline processing.

41. **Type-Safe Data Processing**

- **Complexity**: Moderate (M)
- **Description**: Applies type-annotated Pydantic and Pyright for type-safe processing with `pydantic`. The micro-project processes tested sales data with validation and logging, preparing for advanced testing and FastAPI.
- **Learning Outcomes**: Learners ensure pipeline reliability, ready for pipeline testing in Chapter 42 and FastAPI in Chapter 52.
- **Micro-Project**: Process sales data with type-annotated Pydantic models, Pyright-verified code, logging, and pytest tests using `data/sales.csv`.
- **Role**: Enhances reliability for robust pipelines and web frameworks.

42. **Testing Data Pipelines**

- **Complexity**: Moderate (M)
- **Description**: Advances type-annotated `pytest` testing for pipelines with `pytest`. The micro-project tests a sales pipeline with comprehensive test suites, preparing for advanced testing.
- **Learning Outcomes**: Learners ensure pipeline quality, ready for advanced testing in Chapter 43 and web frameworks in Chapters 51–52.
- **Micro-Project**: Test a type-annotated sales pipeline with pytest unit, integration, and mocking tests using `data/sales.csv`.
- **Role**: Prepares for robust, testable pipelines.

43. **Advanced Testing Techniques**

- **Complexity**: Moderate (M)
- **Description**: Explores advanced type-annotated testing with `hypothesis` for edge cases. The micro-project tests a sales pipeline for robustness, preparing for production.
- **Learning Outcomes**: Learners master advanced testing, ready for Checkpoint 6 in Chapter 44.
- **Micro-Project**: Test a type-annotated sales pipeline with property-based and performance tests using `data/sales.csv`.
- **Role**: Enhances pipeline robustness for production.

44. **Checkpoint 6: Advanced Data Processing Review**

- **Complexity**: Easy (E)
- **Description**: Consolidates type-annotated NumPy, Pandas, concurrency, and testing skills. The micro-project builds a robust, tested sales pipeline, preparing for web frameworks and orchestration.
- **Learning Outcomes**: Learners solidify processing expertise, ready for Phase 7’s web and database integration.
- **Micro-Project**: Build a type-safe, tested sales pipeline with type-annotated logging, validation, and pytest tests using `data/sales.csv`.
- **Role**: Bridges to web and database integration.

### Phase 7: Web and Database Integration (Chapters 46–51)

46. **Jupyter Notebooks for Data Development**

- **Complexity**: Moderate (M)
- **Description**: Teaches type-annotated Jupyter with `jupyter` for data exploration. The micro-project analyzes sales data in a notebook, preparing for BI and web frameworks.
  - **Pitfalls**: Kernel not starting (solution: ensure `ipykernel` installed). Missing dependencies (solution: install `pandas`, `matplotlib`).
- **Learning Outcomes**: Learners master interactive analysis, ready for database patterns in Chapter 48 and BI tools in Chapter 50.
- **Micro-Project**: Analyze sales data in a Jupyter Notebook with visualizations and pytest tests using `data/sales.csv`.
- **Role**: Bridges processing to reporting and web integration.

47. **Data Access Patterns for Applications**

- **Complexity**: Moderate (M)
- **Description**: Teaches type-annotated database patterns (DAO, Repository) with `psycopg2`. The micro-project implements tested patterns for a task database, preparing for PostgreSQL and web frameworks.
- **Learning Outcomes**: Learners ensure modular database access, ready for PostgreSQL in Chapter 48 and web frameworks in Chapters 51–52.
- **Micro-Project**: Implement type-annotated DAO patterns for a task database with pytest tests using `data/tasks.db`.
- **Role**: Enhances database modularity for web applications.

48. **Advanced PostgreSQL Features**

- **Complexity**: Moderate (M)
- **Description**: Explores advanced PostgreSQL features with type-annotated `psycopg2`. The micro-project enhances a tested task database, preparing for optimization.
- **Learning Outcomes**: Learners master advanced PostgreSQL, ready for optimization in Chapter 49.
- **Micro-Project**: Enhance a task database with type-annotated JSONB, search queries, and pytest tests.
- **Role**: Strengthens production database skills.

49. **PostgreSQL Performance Optimization**

- **Complexity**: Moderate (M)
- **Description**: Teaches PostgreSQL optimization with type-annotated `psycopg2`. The micro-project optimizes tested task database queries, preparing for production-grade integration.
- **Learning Outcomes**: Learners enhance database efficiency, ready for BigQuery optimization in Chapter 50.
- **Micro-Project**: Optimize task database queries with type-annotated indexing and pytest tests.
- **Role**: Prepares for efficient database operations in web applications.

50. **BigQuery Advanced Optimization**

- **Complexity**: Moderate (M)
- **Description**: Enhances BigQuery performance with type-annotated `google-cloud-bigquery`. The micro-project optimizes a tested sales **data warehouse**, preparing for BI reporting.
- **Learning Outcomes**: Learners master BigQuery optimization, ready for BI tools in Chapter 51.
- **Micro-Project**: Optimize a sales **data warehouse** with type-annotated clustering and pytest tests using `data/sales.csv`.
- **Role**: Strengthens **data warehouse** operations for analytics.

51. **Data Visualization and BI Tools**

- **Complexity**: Moderate (M)
- **Description**: Teaches type-annotated BI visualization with Metabase and `metabase-api`. The micro-project creates a tested sales dashboard, preparing for Django and FastAPI.
- **Learning Outcomes**: Learners master BI reporting, ready for Django in Chapter 52 and FastAPI in Chapter 53.
- **Micro-Project**: Create a sales dashboard from a **data mart** with type-annotated Metabase and pytest tests using `data/sales.csv`.
- **Role**: Enables stakeholder reporting for web applications.

### Phase 8: Pipeline Orchestration (Chapters 52–59)

52. **Introduction to Django**

- **Complexity**: Moderate (M)
- **Description**: Introduces type-annotated Django for UI (dashboards) and API development with PostgreSQL/SQLite, using Uvicorn, Docker, and libraries (`django`, `djangorestframework`, `PyYAML`). The micro-project builds a robust, tested Django app with a sales dashboard and DRF API, preparing for FastAPI.
- **Learning Outcomes**: Learners master Django for web applications with robust testing, ready for FastAPI in Chapter 53 and capstone projects in Chapters 67–71.
- **Micro-Project**: Build a type-annotated Django app with UI dashboard and DRF API for sales **data mart** with YAML config, logging, and pytest tests (unit, integration, mocking) using `data/sales.csv`.
- **Role**: Enables robust UI and API development for analytics.

53. **Introduction to FastAPI**

- **Complexity**: Moderate (M)
- **Description**: Introduces type-annotated FastAPI for type-safe API and UI development with PostgreSQL/SQLite, using Uvicorn, Docker, and libraries (`fastapi`, `pydantic`, `PyYAML`). The micro-project builds a robust, tested FastAPI app with a UI and API for transaction data, preparing for dbt.
- **Learning Outcomes**: Learners master FastAPI for APIs and UIs with robust testing, ready for dbt in Chapter 54 and capstone projects in Chapters 67–71.
- **Micro-Project**: Build a type-annotated FastAPI app with UI (Jinja2) and API for transaction **data mart** with YAML config, logging, and pytest tests (unit, integration, mocking) using `data/transactions.csv`.
- **Role**: Enhances high-performance API and UI development.

54. **dbt for Data Transformation**

- **Complexity**: Moderate (M)
- **Description**: Introduces type-annotated dbt for robust **data warehouse** transformations with `dbt-core` and data quality tests. The micro-project builds tested sales data models, preparing for orchestration.
- **Learning Outcomes**: Learners master transformations with testing, ready for scheduling in Chapter 55.
- **Micro-Project**: Build type-annotated dbt models for sales data with YAML config, logging, and pytest-validated data quality tests using `data/sales.csv`.
- **Role**: Enables reliable, testable transformations for pipelines.

55. **Simple Scheduling with Python**

- **Complexity**: Moderate (M)
- **Description**: Teaches robust type-annotated scheduling with APScheduler and `apscheduler`. The micro-project schedules tested ETL tasks with error handling, preparing for Airflow.
- **Learning Outcomes**: Learners acquire scheduling skills, ready for Airflow in Chapter 56.
- **Micro-Project**: Schedule type-annotated ETL tasks for sales data with YAML config, error handling, and pytest tests using `data/sales.csv` and `config.yaml`.
- **Role**: Bridges to professional orchestration.

56. **Airflow Fundamentals**

- **Complexity**: Moderate (M)
- **Description**: Introduces robust type-annotated Airflow orchestration with `apache-airflow`. The micro-project orchestrates a tested sales ETL process, preparing for Dockerized Airflow.
- **Learning Outcomes**: Learners master Airflow basics, ready for Dockerized Airflow in Chapter 57.
- **Micro-Project**: Orchestrate a type-annotated sales ETL process with Airflow DAG, YAML config, logging, and pytest tests using `data/sales.csv` and `config.yaml`.
- **Role**: Establishes robust orchestration skills.

57. **Airflow in Docker**

- **Complexity**: Moderate (M)
- **Description**: Teaches robust type-annotated Dockerized Airflow with `apache-airflow`. The micro-project deploys Airflow with a tested DAG, preparing for complex workflows.
- **Learning Outcomes**: Learners master containerized Airflow, ready for complex workflows in Chapter 58.
- **Micro-Project**: Deploy type-annotated Airflow in Docker with a sales ETL DAG, YAML config, and pytest tests using `data/sales.csv` and `config.yaml`.
- **Role**: Enhances orchestration portability.

58. **Building Complex Airflow Workflows**

- **Complexity**: Moderate (M)
- **Description**: Teaches advanced, robust type-annotated Airflow workflows with `apache-airflow` and retries. The micro-project orchestrates a tested multi-step ETL process, preparing for production-grade orchestration.
- **Learning Outcomes**: Learners master complex orchestration with robust testing, ready for Checkpoint 7 in Chapter 59.
- **Micro-Project**: Orchestrate a type-annotated sales ETL process with retries, YAML config, logging, and pytest tests using `data/sales.csv` and `config.yaml`.
- **Role**: Prepares for production-grade, testable workflows.

59. **Checkpoint 7: Pipeline Orchestration Review**

- **Complexity**: Easy (E)
- **Description**: Consolidates type-annotated dbt, Airflow, Django, and FastAPI skills for robust pipelines. The micro-project builds a tested Airflow pipeline with a FastAPI endpoint, preparing for deployment.
- **Learning Outcomes**: Learners solidify orchestration expertise, ready for Phase 9’s production deployment.
- **Micro-Project**: Build a robust type-annotated Airflow pipeline with PostgreSQL, BigQuery, dbt, FastAPI, logging, and pytest tests using `data/sales.csv`.
- **Role**: Bridges to production deployment with testable pipelines.

### Phase 9: Production Deployment (Chapters 60–66)

60. **Docker for Data Applications**

- **Complexity**: Moderate (M)
- **Description**: Advances type-annotated Docker with `pandas`, `psycopg2` for robust data apps. The micro-project packages a tested sales pipeline, preparing for Kubernetes.
- **Learning Outcomes**: Learners master advanced Docker, ready for Kubernetes in Chapter 61.
- **Micro-Project**: Package a type-annotated sales pipeline in Docker with Compose, YAML config, and pytest tests using `data/sales.csv` and `config.yaml`.
- **Role**: Strengthens containerization for deployments.

61. **Kubernetes Fundamentals**

- **Complexity**: Advanced (A)
- **Description**: Introduces type-annotated Kubernetes and Helm Charts with `kubernetes`. The micro-project deploys a tested minimal pod and Helm Chart, preparing for advanced deployments.
- **Learning Outcomes**: Learners gain Kubernetes and Helm basics, ready for advanced deployments in Chapter 62.
- **Micro-Project**: Deploy a type-annotated minimal pod and Helm Chart for a data application with pytest validation.
- **Role**: Introduces production-grade orchestration with Helm.

62. **Deploying Data Applications to Kubernetes**

- **Complexity**: Advanced (A)
- **Description**: Teaches robust type-annotated Kubernetes deployments with `kubernetes`. The micro-project deploys a tested stateful sales pipeline, preparing for PostgreSQL.
- **Learning Outcomes**: Learners master deployments, ready for PostgreSQL in Kubernetes in Chapter 63.
- **Micro-Project**: Deploy a type-annotated stateful sales pipeline with StatefulSets and pytest tests using `data/sales.csv`.
- **Role**: Advances Kubernetes for database deployment.

63. **PostgreSQL in Kubernetes**

- **Complexity**: Advanced (A)
- **Description**: Runs type-annotated PostgreSQL in Kubernetes with `psycopg2`. The micro-project deploys a tested sales database, preparing for Airflow.
- **Learning Outcomes**: Learners master stateful deployments, ready for Airflow in Kubernetes in Chapter 64.
- **Micro-Project**: Deploy a type-annotated PostgreSQL sales database with backups and pytest tests.
- **Role**: Enables scalable database management.

64. **Airflow in Kubernetes**

- **Complexity**: Moderate (M)
- **Description**: Deploys robust type-annotated Airflow in Kubernetes with `apache-airflow` using Helm Charts. The micro-project deploys a tested sales ETL with Helm, preparing for security and observability.
- **Learning Outcomes**: Learners master production Airflow with Helm, ready for security in Chapter 65 and observability in Chapter 66.
- **Micro-Project**: Deploy type-annotated Airflow in Kubernetes with a sales ETL Helm Chart, YAML config, logging, and pytest tests using `data/sales.csv` and `config.yaml`.
- **.cgi**: Enables scalable, testable orchestration with Helm.

65. **Security Best Practices for Data Pipelines**

- **Complexity**: Moderate (M)
- **Description**: Teaches type-annotated API security, data encryption, Kubernetes security, and PII handling (identification, masking, GDPR/PDPA compliance). The micro-project secures a tested sales pipeline with encrypted connections, API authentication, PII masking, and Helm secrets, preparing for observability.
- **Learning Outcomes**: Learners master pipeline security and PII protection, ready for observability in Chapter 66 and capstone planning in Chapter 67.
- **Micro-Project**: Secure a type-annotated sales pipeline with OAuth2, PostgreSQL encryption, PII masking (e.g., hashing customer IDs), Helm-managed secrets, and pytest tests using `data/sales.csv`.
- **Role**: Ensures secure, compliant pipelines for production.

66. **Pipeline Monitoring and Observability**

- **Complexity**: Moderate (M)
- **Description**: Introduces type-annotated distributed tracing (Jaeger), advanced alerting (Grafana/Slack), and query performance metrics. The micro-project builds a tested monitoring dashboard for a sales pipeline, preparing for capstone projects.
- **Learning Outcomes**: Learners master pipeline observability, ready for capstone planning in Chapter 67.
- **Micro-Project**: Implement a type-annotated monitoring dashboard for a sales pipeline with Jaeger tracing, Grafana alerts, and pytest-validated metrics using `data/sales.csv`.
- **Role**: Enhances pipeline visibility for production.

### Phase 10: Capstone Projects (Chapters 67–71)

67. **Checkpoint 8: Production Deployment Review**

- **Complexity**: Easy (E)
- **Description**: Consolidates type-annotated Docker, Kubernetes, Helm, security, observability, and monitoring skills. The micro-project builds a tested Kubernetes pipeline with a Django dashboard, preparing for capstone projects.
- **Learning Outcomes**: Learners solidify deployment expertise, ready for capstone planning in Chapter 68.
- **Micro-Project**: Build a robust type-annotated Kubernetes pipeline with Django dashboard, Helm Chart, logging, PII masking, observability, and pytest tests using `data/sales.csv`.
- **Role**: Bridges to capstone projects with testable pipelines.

68. **Capstone Project Planning**

- **Complexity**: Moderate (M)
- **Description**: Guides robust type-annotated pipeline planning with FastAPI and Helm integration. The micro-project defines a tested transaction data pipeline, preparing for implementation.
- **Learning Outcomes**: Learners develop planning skills, ready for capstone implementation in Chapters 69–71.
- **Micro-Project**: Define a robust type-annotated financial transaction pipeline with BigQuery, Airflow, FastAPI, Helm, PII protection, and test plans using pytest, leveraging `data/transactions.csv`.
- **Role**: Sets the stage for capstone implementation.

69. **Capstone Project Implementation Part 1**

- **Complexity**: Advanced (A)
- **Description**: Builds robust type-annotated storage and ingestion for **data lakes** and **warehouses**. The micro-project implements a tested Kubernetes-based ingestion with Helm, preparing for transformation.
- **Learning Outcomes**: Learners implement robust storage, ready for transformation in Chapter 70.
- **Micro-Project**: Build robust type-annotated ingestion for a transaction pipeline with PostgreSQL/BigQuery, Helm Chart, logging, PII masking, and pytest tests using `data/transactions.csv`.
- **Role**: Lays the capstone foundation with testable pipelines.

70. **Capstone Project Implementation Part 2**

- **Complexity**: Advanced (A)
- **Description**: Develops robust type-annotated **data mart** transformation with dbt, Airflow, and scalability techniques (partitioning, resource optimization). The micro-project implements a tested transaction **data mart** transformation, preparing for integration.
- **Learning Outcomes**: Learners master transformation and scalability, ready for integration in Chapter 71.
- **Micro-Project**: Implement robust type-annotated transaction **data mart** transformations with dbt/Airflow, partitioned tables, Helm resource limits, logging, and pytest tests, including a scalability exercise for Kubernetes pod scaling, using `data/transactions.csv`.
- **Role**: Advances capstone functionality with scalable, testable pipelines.

71. **Capstone Project Implementation Part 3**

- **Complexity**: Advanced (A)
- **Description**: Integrates robust type-annotated pipeline with **data lakes**, **warehouses**, and FastAPI. The micro-project connects a tested transaction pipeline with Helm, preparing for deployment.
- **Learning Outcomes**: Learners achieve end-to-end integration, ready for final deployment.
- **Micro-Project**: Integrate a robust type-annotated transaction pipeline with FastAPI API, Helm Chart, logging, PII protection, observability, and comprehensive pytest tests using `data/transactions.csv`.
- **Role**: Completes pipeline integration with testable pipelines.

## Outro

The **Data Engineering Onboarding Curriculum** equips learners to excel in Hijra Group’s data engineering ecosystem, progressing from Python fundamentals to robust, testable, and secure data pipelines with Django/FastAPI interfaces and Kubernetes Helm deployments. Through 71 chapters across eleven phases, nine checkpoints, and micro-projects (e.g., financial transaction pipelines with type annotations, validation, logging, PII protection, observability, scalability, Helm Charts, and comprehensive testing using `unittest` and `pytest`), learners master PostgreSQL, BigQuery, Kubernetes, Airflow, and dbt, delivering actionable insights via capstone projects in Phase 10. Designed for a development environment, with setup instructions to be provided in chapter implementations, the curriculum ensures hands-on learning aligned with practical upskilling goals.
