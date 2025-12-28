from config.dask_config import start_dask
from ingestion.loader import load_logs
from ingestion.parser import parse_log_line
import time

def main():
    client = start_dask()
    print(client)
    print(f"Dashboard link: {client.dashboard_link}")
    print("\n" + "="*50)
    
    bag = load_logs("/Users/harshithyvs/Desktop/log-analytics-engine/data/sample_log.log")
    parsed = bag.map(parse_log_line).filter(lambda x: x is not None)
    
    result = parsed.compute()
    print("\nParsed Logs:")
    for log in result:
        print(log)
    
    print("\n"+"="*50)
    print("Dashboard is running at: http://127.0.0.1:8790/status")
    print("Press Ctrl+C to exit...")
    print("="*50)
    
    #keep the script runinng so the dashboard stays active
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n\nShutting down Dask cluster...")
        client.close()

if __name__ == "__main__":
    main()
