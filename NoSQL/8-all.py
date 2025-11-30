#!/usr/bin/env python3
"""
This module contains a function `list_all` that lists all documents
in a MongoDB collection using PyMongo.
"""
def list_all(mongo_collection):
    """
    Lists all documents in a MongoDB collection.

    Args:
        mongo_collection: A pymongo collection object.

    Returns:
        A list of documents. Empty list if no documents found.
    """
    if not mongo_collection:
        return []

    # Convert the cursor to a list
    documents = list(mongo_collection.find())
    return documents
