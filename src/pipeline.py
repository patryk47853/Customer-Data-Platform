import logging
import pandas as pd

from transform import transform_retail_data
from load_to_sqlite import load_to_sqlite


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)


RAW_DATA_PATH = "../data/raw/Online_Retail.csv"
PROCESSED_DATA_PATH = "../data/processed/online_retail_clean.csv"


def main():
    logger.info("Starting ETL pipeline")

    # EXTRACT
    logger.info("Loading raw data from CSV")
    df_raw = pd.read_csv(
        RAW_DATA_PATH,
        encoding="ISO-8859-1"
    )
    logger.info("Raw data loaded: %s rows", df_raw.shape[0])

    # TRANSFORM
    df_clean = transform_retail_data(df_raw)

    # LOAD
    logger.info("Saving processed data")
    df_clean.to_csv(
        PROCESSED_DATA_PATH,
        index=False
    )
    logger.info("Processed data saved to %s", PROCESSED_DATA_PATH)

    load_to_sqlite(df_clean)
    logger.info("ETL pipeline completed successfully")


if __name__ == "__main__":
    main()
