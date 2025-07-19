import pandas as pd
from .validators import validate_data

def run_etl(events_path, vehicles_path, zones_path, output_path, logger):
    # Load datasets
    df_events = pd.read_csv(events_path, parse_dates=["entry_time", "exit_time"])
    df_vehicles = pd.read_csv(vehicles_path)
    df_zones = pd.read_csv(zones_path)

    if logger:
        logger.info(f"Loaded {len(df_events)} parking events")
        logger.info(f"Loaded {len(df_vehicles)} vehicles")
        logger.info(f"Loaded {len(df_zones)} zones")

    # Merge and validate
    df_merged = df_events.merge(df_vehicles, on="vehicle_id", how="left") \
                         .merge(df_zones, on="zone_id", how="left")

    df_valid = validate_data(df_merged, logger)

    # 🔧 FIX: Ensure timestamp compatibility
    df_valid["entry_time"] = pd.to_datetime(df_valid["entry_time"]).dt.strftime('%Y-%m-%d %H:%M:%S')
    df_valid["exit_time"] = pd.to_datetime(df_valid["exit_time"]).dt.strftime('%Y-%m-%d %H:%M:%S')

    # Save to Parquet
    df_valid.to_parquet(output_path, index=False, engine="pyarrow", coerce_timestamps="ms")
  # You can also add coerce_timestamps='ms'
    if logger:
        logger.info(f"Saved {len(df_valid)} valid merged records to {output_path}")

'''
def run_etl(events_path, vehicles_path, zones_path, output_path, logger=None):
    # Load datasets from the provided file paths
    df_events = pd.read_csv(events_path, parse_dates=["entry_time", "exit_time"])
    df_vehicles = pd.read_csv(vehicles_path)
    df_zones = pd.read_csv(zones_path)

    if logger:
        logger.info(f"Loaded {len(df_events)} parking events")
        logger.info(f"Loaded {len(df_vehicles)} vehicles")
        logger.info(f"Loaded {len(df_zones)} zones")

    # Merge datasets
    df_merged = df_events.merge(df_vehicles, on="vehicle_id", how="left") \
                         .merge(df_zones, on="zone_id", how="left")

    # Validate data
    df_valid = validate_data(df_merged, logger)

    # Save to Parquet
    #df_valid.to_parquet(output_path, index=False)
    df_valid.to_parquet(output_path, index=False, engine="pyarrow", coerce_timestamps="ms")

    if logger:
        logger.info(f"Saved {len(df_valid)} valid merged records to {output_path}")
'''