import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pandas as pd
from airport_parking_toolkit.validators import validate_data

def test_validate_data():
    df = pd.DataFrame({
        "vehicle_id": ["V1", None],
        "entry_time": ["2023-01-01 08:00", "2023-01-01 09:00"],
        "exit_time": ["2023-01-01 10:00", "2023-01-01 08:00"],
        "paid_amount": [20, -10]
    })
    cleaned = validate_data(df, logger=None)
    assert len(cleaned) == 1

def validate_data(df, logger=None):  
    df = df.dropna(subset=["vehicle_id", "entry_time", "exit_time"])
    df = df[df["exit_time"] >= df["entry_time"]]
    df = df[df["paid_amount"] >= 0]

    if logger:
        logger.info("Validation complete")

    return df

