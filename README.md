# 1june-Supply-chain-
1 june_suppy chain analysis 

# Supply Chain Visibility & Inventory Analytics Platform

## Project Overview

This project simulates a real-world supply chain analytics platform using Databricks, PySpark, Delta Lake, and SQL.

The objective is to track inventory movement, shipment delays, vendor performance, and stock availability across multiple warehouses.

The solution follows the Medallion Architecture pattern:

Raw Data → Bronze → Silver → Gold → Analytics

---

## Business Problem

Organizations receive supply chain data from multiple sources:

- Vendor shipments
- Inventory systems
- Warehouse operations
- Order management platforms

Challenges include:

- Duplicate records
- Late-arriving shipment updates
- Missing inventory information
- Inconsistent vendor identifiers
- Delayed reporting

This project addresses these challenges using a layered data architecture.

---

## Architecture

Orders CSV
Shipments CSV
Inventory CSV
Vendor CSV

        ↓

Bronze Layer

        ↓

Silver Layer

        ↓

Gold Layer

        ↓

Analytics Views

---

## Technologies Used

- Python
- PySpark
- Databricks Community Edition
- Delta Lake
- SQL
- Pandas
- Pytest

---

## Bronze Layer

Stores source data without modification.

Tables:

- bronze_orders
- bronze_shipments
- bronze_inventory
- bronze_vendors

---

## Silver Layer

Applies:

- Deduplication
- Data validation
- Null handling
- Standardization

Tables:

- silver_orders
- silver_shipments
- silver_inventory
- silver_vendors

---

## Gold Layer

Business-ready datasets:

- gold_inventory_snapshot
- gold_vendor_performance
- gold_shipment_tracking

---

## Analytics Views

- analytics_inventory_risk
- analytics_vendor_scorecard
- analytics_delivery_delays

---

## Key Features

### Inventory Monitoring

Track current inventory across warehouses.

### Shipment Monitoring

Identify delayed shipments.

### Vendor Performance

Analyze supplier delivery performance.

### Late Arriving Data

Detect events arriving after business event time.

---

## Running the Project

1. Install requirements

```bash
pip install -r requirements.txt
```

2. Generate sample data

```bash
python scripts/generate_data.py
```

3. Run Bronze Notebook

4. Run Silver Notebook

5. Run Gold Notebook

6. Run Analytics Notebook

---

## Future Improvements

- Kafka Streaming
- Real-Time Dashboards
- Demand Forecasting
- SCD Type 2
- CDC Pipelines
- ML-Based Stock Prediction

---

## Resume Description

Built a Supply Chain Visibility Platform using Databricks, PySpark, Delta Lake, and SQL. Implemented Bronze/Silver/Gold architecture, shipment tracking, inventory monitoring, late-arriving data handling, and vendor performance analytics.
