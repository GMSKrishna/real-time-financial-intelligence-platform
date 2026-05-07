import schedule
import time
import subprocess
import logging
import sys
from datetime import datetime

# Logging configuration
logging.basicConfig(
    filename="logs/pipeline.log",
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)

def run_pipeline():

    logging.info("Pipeline started")

    print("=" * 50)
    print(f"Pipeline started at: {datetime.now()}")
    print("=" * 50)

    # Current Python executable from venv
    python_executable = sys.executable

    # Run ingestion
    subprocess.run(
        [python_executable, "-m", "ingestion.fetch_data"]
    )

    # Run ETL
    subprocess.run(
        [python_executable, "-m", "processing.etl"]
    )

    logging.info("Pipeline completed successfully")

    print("Pipeline execution completed")

# Schedule every minute
schedule.every(1).minutes.do(run_pipeline)

print("Scheduler started...")

# Initial run
run_pipeline()

while True:

    schedule.run_pending()

    time.sleep(1)