from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.window import Window

spark = (
    SparkSession.builder
    .appName("SupplyChainSilver")
    .getOrCreate()
)

# --------------------
# Orders
# --------------------

orders = spark.table("bronze_orders")

orders_clean = (
    orders
    .dropDuplicates(["order_id"])
    .filter(col("quantity") > 0)
)

orders_clean.write \
    .format("delta") \
    .mode("overwrite") \
    .saveAsTable("silver_orders")

# --------------------
# Shipments
# --------------------

shipments = spark.table(
    "bronze_shipments"
)

shipments_clean = (
    shipments
    .withColumn(
        "is_late_arrival",
        when(
            datediff(
                col("ingest_time"),
                col("event_time")
            ) > 1,
            lit(True)
        ).otherwise(lit(False))
    )
)

shipments_clean.write \
    .format("delta") \
    .mode("overwrite") \
    .saveAsTable("silver_shipments")

# --------------------
# Inventory
# --------------------

inventory = spark.table(
    "bronze_inventory"
)

inventory_clean = (
    inventory
    .filter(
        col("stock_quantity") >= 0
    )
)

inventory_clean.write \
    .format("delta") \
    .mode("overwrite") \
    .saveAsTable("silver_inventory")

# --------------------
# Vendors
# --------------------

vendors = spark.table(
    "bronze_vendors"
)

vendors_clean = (
    vendors
    .filter(
        col("vendor_rating") >= 0
    )
)

vendors_clean.write \
    .format("delta") \
    .mode("overwrite") \
    .saveAsTable("silver_vendors")

print("Silver Layer Created")
