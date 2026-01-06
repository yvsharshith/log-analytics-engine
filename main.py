from config.dask_config import start_dask
from processing.pipeline import build_pipeline
import time

def main():
    client = start_dask()
    print(client)
    print(f"Dashboard link: {client.dashboard_link}")
    print("\n" + "="*50)
    
    start = time.time()
    log_df = build_pipeline("data/sample_log.log")
    print("start time", start)
    
    total_logs = log_df.count().compute()
    end = time.time()
    
    print("total logs parssed:", total_logs)
    print("time taken", end)
    
    input("press enter....")
    
if __name__ == "__main__":
    main()
