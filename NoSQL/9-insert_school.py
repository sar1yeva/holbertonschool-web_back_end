#!/usr/bin/env python3
"""
This module contains a function `insert_school` that inserts a new document
into a MongoDB collection using keyword arguments and returns the new document's _id.
"""

def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new document into a MongoDB collection.

    Args:
        mongo_collection: A pymongo collection object.
        **kwargs: Arbitrary keyword arguments representing the document fields.

    Returns:
        The _id of the inserted document.
    """
    if not mongo_collection:
        return None

    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
