from faker import Faker
import pandas as pd
import random
from datetime import datetime, timedelta
import os

fake = Faker()

os.makedirs("data/sample", exist_ok=True)

NUM_VENDORS = 100
NUM_PRODUCTS = 500
NUM_WAREHOUSES = 50
NUM_ORDERS = 5000
NUM_SHIPMENTS = 10000

# -------------------
# Vendors
# -------------------

vendors = []

for vendor_id in range(1, NUM_VENDORS + 1):
    vendors.append(
        {
            "vendor_id": vendor_id,
            "vendor_name": fake.company(),
            "country": fake.country(),
            "vendor_rating": round(random.uniform(2.5, 5.0), 2)
        }
    )

vendors_df = pd.DataFrame(vendors)

vendors_df.to_csv(
    "data/sample/vendors.csv",
    index=False
)

print("vendors.csv created")

# -------------------
# Inventory
# -------------------

inventory = []

for warehouse_id in range(1, NUM_WAREHOUSES + 1):

    for product_id in range(1, NUM_PRODUCTS + 1):

        inventory.append(
            {
                "warehouse_id": warehouse_id,
                "product_id": product_id,
                "stock_quantity": random.randint(10, 1000),
                "last_updated": fake.date_between(
                    start_date="-30d",
                    end_date="today"
                )
            }
        )

inventory_df = pd.DataFrame(inventory)

inventory_df.to_csv(
    "data/sample/inventory.csv",
    index=False
)

print("inventory.csv created")

# -------------------
# Orders
# -------------------

orders = []

for order_id in range(1, NUM_ORDERS + 1):

    order_date = fake.date_between(
        start_date="-90d",
        end_date="today"
    )

    orders.append(
        {
            "order_id": order_id,
            "product_id": random.randint(1, NUM_PRODUCTS),
            "warehouse_id": random.randint(1, NUM_WAREHOUSES),
            "quantity": random.randint(1, 50),
            "order_date": order_date
        }
    )

# duplicate rows

orders.append(orders[100])
orders.append(orders[200])

orders_df = pd.DataFrame(orders)

orders_df.to_csv(
    "data/sample/orders.csv",
    index=False
)

print("orders.csv created")

# -------------------
# Shipments
# -------------------

shipments = []

statuses = [
    "CREATED",
    "IN_TRANSIT",
    "DELIVERED",
    "DELAYED"
]

for shipment_id in range(1, NUM_SHIPMENTS + 1):

    event_date = fake.date_between(
        start_date="-90d",
        end_date="today"
    )

    ingest_delay = random.randint(0, 5)

    ingest_time = (
        pd.Timestamp(event_date)
        + pd.Timedelta(days=ingest_delay)
    )

    shipments.append(
        {
            "shipment_id": shipment_id,
            "vendor_id": random.randint(1, NUM_VENDORS),
            "warehouse_id": random.randint(1, NUM_WAREHOUSES),
            "status": random.choice(statuses),
            "delivery_delay_days": random.randint(0, 10),
            "event_time": event_date,
            "ingest_time": ingest_time
        }
    )

shipments_df = pd.DataFrame(shipments)

shipments_df.to_csv(
    "data/sample/shipments.csv",
    index=False
)

print("shipments.csv created")

print("\nAll datasets generated successfully")
