import sys
import os
import pandas as pd
import tempfile

# Add root to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from airport_parking_toolkit.etl import run_etl

def test_run_etl(tmp_path):
    # Create sample input CSVs
    events_df = pd.DataFrame({
        "event_id": [1],
        "vehicle_id": ["V1"],
        "zone_id": ["Z1"],
        "entry_time": ["2023-01-01 08:00"],
        "exit_time": ["2023-01-01 10:00"],
        "paid_amount": [20.0]
    })
    vehicles_df = pd.DataFrame({
        "vehicle_id": ["V1"],
        "plate_number": ["ABC123"],
        "type": ["car"],
        "owner_name": ["John Doe"]
    })
    zones_df = pd.DataFrame({
        "zone_id": ["Z1"],
        "zone_name": ["Short-Term"],
        "rate_per_hour": [10.0],
        "is_valet": [False]
    })

    events_path = tmp_path / "events.csv"
    vehicles_path = tmp_path / "vehicles.csv"
    zones_path = tmp_path / "zones.csv"
    output_path = tmp_path / "output.parquet"

    events_df.to_csv(events_path, index=False)
    vehicles_df.to_csv(vehicles_path, index=False)
    zones_df.to_csv(zones_path, index=False)

    # Run ETL
    run_etl(str(events_path), str(vehicles_path), str(zones_path), str(output_path), logger=None)

    # Check output
    assert output_path.exists()
    output_df = pd.read_parquet(output_path)
    assert len(output_df) == 1
