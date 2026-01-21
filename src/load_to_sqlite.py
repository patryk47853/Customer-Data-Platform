import logging
import sqlite3
import pandas as pd


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)


DB_PATH = "../data/db/retail.db"
TABLE_NAME = "online_retail"

def load_to_sqlite(df: pd.DataFrame) -> None :
    logger.info("Connecting to SQLite database")

    conn = sqlite3.connect(DB_PATH)

    logger.info("Writing data to table '%s'", TABLE_NAME)

    df.to_sql(
        TABLE_NAME,
        conn,
        if_exists="replace",
        index=False
    )

    conn.close()
    logger.info("Finished writing data to SQLite table '%s'", TABLE_NAME)