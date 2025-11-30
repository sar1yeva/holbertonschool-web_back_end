#!/usr/bin/env python3
"""
Script that provides some stats about Nginx logs stored in MongoDB.
"""

from pymongo import MongoClient

def main():
    """
    Connects to the MongoDB 'logs' database and retrieves statistics
    about the 'nginx' collection.

    Prints:
        - Total number of logs
        - Number of logs per HTTP method (GET, POST, PUT, PATCH, DELETE)
        - Number of GET requests to /status
    """
    # Connect to MongoDB
    client = MongoClient("mongodb://localhost:27017/")
    db = client.logs
    collection = db.nginx

    # Total number of logs
    total_logs = collection.count_documents({})
    print(f"{total_logs} logs")

    # Methods statistics
    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    # Status check
    status_count = collection.count_documents({"method": "GET", "path": "/status"})
    print(f"{status_count} status check")

if __name__ == "__main__":
    main()

