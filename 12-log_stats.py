#!/usr/bin/env python3
"""A python3 Module"""

from pymongo import MongoClient

def log_start():
    """Provide some stats about Nginx"""
    params = MongoClient()
    caller = params.logs
    collection_caller = caller.nginx

    log_counter = collection_caller.count_document({})
    print(f"{log_counter} logs")

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods: ")

    for method in methods:
        counts_method = collection_caller.count_documents({"method": method})
        print(f"\tmethod {method}: {counts_method}")
   
    status_check = collection_caller.count_documents({"method": "GET", "path": "/status"})
    print(f"{status_check} status check")


if __name__ == "__main__":
    log_start()
