#!/usr/bin/env python3
"""MongoDB operations with Pyhton using pymongo"""


def list_all(mongo_collection) -> list:
    """List all documents in Python"""
    documents = (mongo_collection.find({}))
    return documents
