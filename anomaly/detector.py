import dask.dataframe as dd


def detect_anomaly(log_df, z_threshold=3):
    log_df["timestamp"] = dd.to_datetime(log_df["timestamp"])

    error_logs = log_df[log_df["level"] == "ERROR"]

    if error_logs.shape[0].compute() == 0:
        return error_logs.head(0)

    error_logs["minute"] = error_logs["timestamp"].dt.floor("min")

    error_counts = (
        error_logs
        .groupby("minute")
        .size()
        .rename("error_count")
        .reset_index()
    )

    mean = error_counts["error_count"].mean().compute()
    std = error_counts["error_count"].std().compute()

    if std == 0:
        return error_counts.head(0).compute()

    error_counts["anomaly_score"] = (error_counts["error_count"] - mean) / std
    error_counts["is_anomaly"] = error_counts["anomaly_score"].abs() > z_threshold

    return error_counts[error_counts["is_anomaly"]].compute()