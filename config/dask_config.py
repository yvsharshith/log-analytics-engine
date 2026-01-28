from dask.distributed import LocalCluster, Client 

def start_dask():
    cluster = LocalCluster(
        n_workers = 2,
        threads_per_worker = 2,
        memory_limit= "2GB",
        dashboard_address=":8790"
    )
    return Client(cluster)

