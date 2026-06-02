from pyspark.sql import SparkSession
from pyspark.sql.functions import *

spark = (
    SparkSession.builder
    .appName("SupplyChainGold")
    .getOrCreate()
)

# --------------------
# Inventory Snapshot
# --------------------

inventory_snapshot = (
    spark.table("silver_inventory")
    .groupBy(
        "warehouse_id",
        "product_id"
    )
    .agg(
        sum("stock_quantity")
        .alias("current_stock")
    )
)

inventory_snapshot.write \
    .format("delta") \
    .mode("overwrite") \
    .saveAsTable(
        "gold_inventory_snapshot"
    )

# --------------------
# Vendor Performance
# --------------------

vendor_performance = (
    spark.table("silver_shipments")
    .groupBy("vendor_id")
    .agg(
        avg(
            "delivery_delay_days"
        ).alias("avg_delay"),

        count("*")
        .alias("shipment_count")
    )
)

vendor_performance.write \
    .format("delta") \
    .mode("overwrite") \
    .saveAsTable(
        "gold_vendor_performance"
    )

# --------------------
# Shipment Tracking
# --------------------

shipment_tracking = (
    spark.table("silver_shipments")
)

shipment_tracking.write \
    .format("delta") \
    .mode("overwrite") \
    .saveAsTable(
        "gold_shipment_tracking"
    )

print("Gold Layer Created")
