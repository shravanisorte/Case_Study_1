def validate_data(df, logger=None):
    df = df.dropna(subset=["vehicle_id", "entry_time", "exit_time"])
    df = df[df["exit_time"] >= df["entry_time"]]
    df = df[df["paid_amount"] >= 0]

    if logger:
        logger.info("Validation complete")

    return df
