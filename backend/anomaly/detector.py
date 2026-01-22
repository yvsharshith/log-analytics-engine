import dask.dataframe as dd

def detect_anomaly(log_df, z_threshold=3):
    """
    Detects anomalies in log data based on Z-score method.
    
    Parameters:
    - log_df: Dask DataFrame with log data containing 'timestamp' and 'level' columns.
    - z_threshold: Z-score threshold to flag anomalies.
    
    Returns:
    - Dask DataFrame with anomalies flagged.
    """
    # Filter ERROR logs
    error_logs = log_df[log_df["level"] == "ERROR"]

    # IMPORTANT: set index with sorted=True
    error_logs = error_logs.set_index(
        "timestamp",
        sorted=False,          # allow Dask to sort
        drop=False
    )

    # Resample safely and Count errors per minute
    error_counts = (
        error_logs
        .resample("1T")
        .size()
        .rename("error_count")
        .reset_index()
    )

    # Compute statistics
    mean = error_counts["error_count"].mean().compute()
    std = error_counts["error_count"].std().compute()

    if std == 0:
        return error_counts.head(0)

    error_counts["z_score"] = (error_counts["error_count"] - mean) / std
    error_counts["is_anomaly"] = error_counts["z_score"].abs() > z_threshold

    return error_counts[error_counts["is_anomaly"]]

'''
# using pandas
import pandas as pd

def detect_anomaly(log_df, threshold=2):
    """
    Detect anomalies based on error count per minute
    """

    # 1. Convert to Pandas (safe for small data)
    pdf = log_df.compute()

    # 2. Ensure timestamp is datetime
    pdf["timestamp"] = pd.to_datetime(pdf["timestamp"])

    # 3. Filter ERROR logs
    error_logs = pdf[pdf["level"] == "ERROR"]

    if error_logs.empty:
        return error_logs.head(0)

    # 4. Count errors per minute
    error_counts = (
        error_logs
        .set_index("timestamp")
        .resample("1T")
        .size()
        .rename("error_count")
        .reset_index()
    )

    # 5. Apply threshold
    anomalies = error_counts[error_counts["error_count"] >= threshold]

    return anomalies

'''
    