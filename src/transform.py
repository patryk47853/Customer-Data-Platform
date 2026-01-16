import logging
import pandas as pd


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)


def transform_retail_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Cleans and transforms Online Retail transactional data.
    """
    logger.info("Starting data transformation")
    logger.info("Initial dataset shape: %s", df.shape)

    # Remove cancelled invoices
    before = df.shape[0]
    df = df[~df["InvoiceNo"].str.startswith("C", na=False)]
    logger.info("Removed cancelled invoices: %s rows", before - df.shape[0])

    # Keep only positive quantities
    before = df.shape[0]
    df = df[df["Quantity"] > 0]
    logger.info("Removed non-positive quantities: %s rows", before - df.shape[0])

    # Keep only positive unit prices
    before = df.shape[0]
    df = df[df["UnitPrice"] > 0]
    logger.info("Removed non-positive unit prices: %s rows", before - df.shape[0])

    # Remove records without CustomerID
    before = df.shape[0]
    df = df[df["CustomerID"].notna()]
    logger.info("Removed missing CustomerID: %s rows", before - df.shape[0])

    # Remove records without Description
    before = df.shape[0]
    df = df[df["Description"].notna()]
    logger.info("Removed missing Description: %s rows", before - df.shape[0])

    # Normalize text columns
    df["Description"] = df["Description"].str.strip().str.upper()
    df["Country"] = df["Country"].str.strip().str.upper()
    logger.info("Normalized text columns (Description, Country)")

    # Convert InvoiceDate and extract components
    df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])
    df["InvoiceYear"] = df["InvoiceDate"].dt.year
    df["InvoiceMonth"] = df["InvoiceDate"].dt.month
    logger.info("Extracted InvoiceYear and InvoiceMonth")

    # Create total price column
    df["TotalPrice"] = df["Quantity"] * df["UnitPrice"]
    logger.info("Created TotalPrice column")

    # Final schema
    final_columns = [
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
    ]

    df = df[final_columns]

    logger.info("Final dataset shape: %s", df.shape)
    logger.info("Data transformation completed successfully")

    return df
