# Log Analytics Engine

A Python-based **high-throughput log analytics and anomaly monitoring engine** built using Dask for scalable processing and Streamlit for visualization. The system ingests raw logs (batch or real-time), converts them into structured data, detects anomalous error patterns, and triggers email alerts while also providing an interactive dashboard for monitoring.

---

## Project Architecture Overview

The project follows a modular pipeline-based design:

Log Generation → Ingestion → Processing → Anomaly Detection → Alerting → Visualization

Each stage is isolated into its own folder to keep the system scalable, readable, and easy to extend.

---

## Folder Structure & File Details

### `anomaly/`

Handles anomaly detection logic.

**`detector.py`**
Uses Dask DataFrames to analyze ERROR-level logs. It groups errors by minute, computes statistical metrics (mean and standard deviation), and applies Z-score–based detection to flag anomalous spikes in error frequency.

---

### `config/`

Contains configuration and infrastructure setup files.

**`dask_config.py`**
Initializes a local Dask cluster with multiple workers and exposes the Dask dashboard for monitoring task execution.

**`email_config.py`**
Handles email alerting. When an anomaly is detected, this module sends an alert email with anomaly details (timestamp, error count, Z-score) to the administrator.

---

### `dashboard/`

Provides a visual monitoring interface.

**`app.py`**
A Streamlit-based dashboard that runs independently of `main.py`. It reads processed logs, performs anomaly detection, and visualizes anomaly scores over time using interactive Plotly charts. Users can also filter anomalies using a threshold slider.

---

### `data/`

Contains static sample log files for testing.

**`sample_log.log`**
A sample structured log file used to validate ingestion and parsing logic.

---

### `ingestion/`

Responsible for loading and parsing raw logs.

**`loader.py`**
Uses Dask Bag to read large log files efficiently.

**`parser.py`**
Parses each log line using regular expressions and converts raw text into structured records containing timestamp, level, service, and message.

---

### `log_generator/`

Simulates real-time log generation.

**`realtime_log_producer.py`**
Continuously generates logs with random services and log levels and appends them to a CSV file, simulating a live production system.

**`realtime_logs.csv`**
The output file where real-time logs are written and consumed by the pipeline.

---

### `processing/`

Builds the scalable analytics pipeline.

**`pipeline.py`**
Combines ingestion and parsing logic. It converts parsed log records into a Dask DataFrame with explicit schema metadata and prepares the data for downstream analytics.

---

### `router/`

**`service.py`**
Reserved for routing or service-level abstractions (future extensibility).

---

### `schema/`

Defines log data structure.

**`schema.py`**
Declares the expected schema for log fields, ensuring consistency across ingestion and processing stages.

---

### Root Files

**`main.py`**
The main execution entry point. It starts the Dask cluster, builds the log processing pipeline, runs anomaly detection, and sends email alerts when anomalies are found.

**`requirements.txt`**
Lists all Python dependencies required to run the project.

**`README.md`**
Project documentation.

---

## How to Run the Project

### 1. Clone the Repository

```
git clone https://github.com/yvsharshith/log-analytics-engine.git
cd log-analytics-engine
git checkout milestone-4
```

---

### 2. Set Up Environment

Make sure Python 3.8+ is installed.

```
pip install -r requirements.txt
```

---

### 3. Start Real-Time Log Generator (Optional but Recommended)

In a separate terminal:

```
python log_generator/realtime_log_producer.py
```

This will continuously generate logs into `realtime_logs.csv`.

---

### 4. Run the Main Analytics Engine

```
python main.py
```

This will:

* Start a Dask cluster
* Parse and process logs
* Detect anomalies
* Send email alerts if anomalies are found

---

### 5. Run the Dashboard

In another terminal:

```
streamlit run dashboard/app.py
```

The dashboard provides interactive anomaly visualizations and filtering.

---

## Example Log Format

```
2025-01-10 12:05:15,456 INFO auth User logged in from IP
```

Each log line consists of:

* Timestamp
* Log level
* Service name
* Message

---

## Author

**Harshith YVS**

---
