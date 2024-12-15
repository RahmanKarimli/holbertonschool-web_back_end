#!/usr/bin/env python3
"""Module for logging stats"""
from pymongo import MongoClient


def log_stats():
    """Prints statistics about Nginx logs stored in MongoDB."""
    client = MongoClient()
    db = client.logs
    collection = db.nginx

    print(f"{collection.count_documents({})} logs")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods: ")
    for method in methods:
        print(f"\tmethod: {method}: {collection.count_documents({"method": method})}")
    print(f"{collection.count_documents({"method": "GET", "path": "/status"})} status check")


if __name__ == "__main__":
    log_stats()
