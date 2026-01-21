import pandas as pd

from src.transform import transform_retail_data


def sample_df():
    return pd.DataFrame({
        "InvoiceNo": ["10000", "C10001"],
        "StockCode": ["A", "B"],
        "Description": ["test product", "cancelled product"],
        "Quantity": [10, -5],
        "InvoiceDate": ["2011-01-01", "2011-01-02"],
        "UnitPrice": [2.5, 3.0],
        "CustomerID": [12345, None],
        "Country": ["United Kingdom", "United Kingdom"],
    })


def test_cancelled_invoices_removed():
    df = transform_retail_data(sample_df())
    assert df["InvoiceNo"].str.startswith("C").sum() == 0


def test_quantity_positive():
    df = transform_retail_data(sample_df())
    assert (df["Quantity"] > 0).all()


def test_total_price_calculation():
    df = transform_retail_data(sample_df())
    assert (df["TotalPrice"] == df["Quantity"] * df["UnitPrice"]).all()


def test_final_columns_exist():
    df = transform_retail_data(sample_df())
    expected_columns = {
        "InvoiceNo",
        "StockCode",
        "Description",
        "Quantity",
        "UnitPrice",
        "TotalPrice",
        "InvoiceDate",
        "InvoiceYear",
        "InvoiceMonth",
        "CustomerID",
        "Country",
    }
    assert set(df.columns) == expected_columns
