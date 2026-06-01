from pyspark.sql import SparkSession

spark = (
    SparkSession.builder
    .appName("SupplyChainBronze")
    .getOrCreate()
)

# Orders

orders_df = spark.read \
    .option("header", True) \
    .option("inferSchema", True) \
    .csv("data/sample/orders.csv")

orders_df.write \
    .format("delta") \
    .mode("overwrite") \
    .saveAsTable("bronze_orders")

# Shipments

shipments_df = spark.read \
    .option("header", True) \
    .option("inferSchema", True) \
    .csv("data/sample/shipments.csv")

shipments_df.write \
    .format("delta") \
    .mode("overwrite") \
    .saveAsTable("bronze_shipments")

# Inventory

inventory_df = spark.read \
    .option("header", True) \
    .option("inferSchema", True) \
    .csv("data/sample/inventory.csv")

inventory_df.write \
    .format("delta") \
    .mode("overwrite") \
    .saveAsTable("bronze_inventory")

# Vendors

vendors_df = spark.read \
    .option("header", True) \
    .option("inferSchema", True) \
    .csv("data/sample/vendors.csv")

vendors_df.write \
    .format("delta") \
    .mode("overwrite") \
    .saveAsTable("bronze_vendors")

print("Bronze Layer Loaded Successfully")
