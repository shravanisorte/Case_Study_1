from airport_parking_toolkit.etl import run_etl
from airport_parking_toolkit.logger import setup_logger

def main():
    # Hardcoded file paths
    events_path = r"C:\Users\shravani.raju\Desktop\Case_Study_WEEK1\airport_parking_dataset\parking_events.csv"
    vehicles_path = r"C:\Users\shravani.raju\Desktop\Case_Study_WEEK1\airport_parking_dataset\vehicles.csv"
    zones_path = r"C:\Users\shravani.raju\Desktop\Case_Study_WEEK1\airport_parking_dataset\parking_zones.csv"
    output_path = r"C:\Users\shravani.raju\Desktop\Case_Study_WEEK1\airport_parking_dataset\final_output.parquet"

    logger = setup_logger("parking_etl.log")
    logger.info("ETL started")

    run_etl(events_path, vehicles_path, zones_path, output_path, logger)

if __name__ == "__main__":
    main()
