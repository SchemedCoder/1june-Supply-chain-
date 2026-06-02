import pandas as pd


def test_inventory_has_stock():

    data = {
        "warehouse_id": [1, 2],
        "product_id": [10, 20],
        "stock_quantity": [100, 50]
    }

    df = pd.DataFrame(data)

    assert (
        df["stock_quantity"] >= 0
    ).all()


def test_inventory_no_null_products():

    data = {
        "product_id": [1, 2, 3]
    }

    df = pd.DataFrame(data)

    assert (
        df["product_id"]
        .isnull()
        .sum()
        == 0
    )
