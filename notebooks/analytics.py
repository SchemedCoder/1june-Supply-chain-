from pyspark.sql import SparkSession
from pyspark.sql.functions import *

spark = (
    SparkSession.builder
    .appName("SupplyChainAnalytics")
    .getOrCreate()
)

# ------------------------
# Inventory Risk
# ------------------------

inventory_risk = (
    spark.table(
        "gold_inventory_snapshot"
    )
    .filter(
        col("current_stock") < 100
    )
)

inventory_risk.createOrReplaceTempView(
    "analytics_inventory_risk"
)

# ------------------------
# Vendor Scorecard
# ------------------------

vendor_scorecard = (
    spark.table(
        "gold_vendor_performance"
    )
    .orderBy(
        desc("avg_delay")
    )
)

vendor_scorecard.createOrReplaceTempView(
    "analytics_vendor_scorecard"
)

# ------------------------
# Delayed Shipments
# ------------------------

delayed_shipments = (
    spark.table(
        "gold_shipment_tracking"
    )
    .filter(
        col(
            "delivery_delay_days"
        ) > 3
    )
)

delayed_shipments.createOrReplaceTempView(
    "analytics_delivery_delays"
)

# ------------------------
# Late Arrivals
# ------------------------

late_arrivals = (
    spark.table(
        "silver_shipments"
    )
    .filter(
        col(
            "is_late_arrival"
        ) == True
    )
)

late_arrivals.createOrReplaceTempView(
    "analytics_late_arrivals"
)

print(
    "Analytics Views Created"
)

print(
    f"Inventory Risk Rows : {inventory_risk.count()}"
)

print(
    f"Late Arrivals : {late_arrivals.count()}"
)

