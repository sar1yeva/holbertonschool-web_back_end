#!/usr/bin/env python3
"""
This module contains a function `update_topics` that updates the
topics of school documents in a MongoDB collection based on the school name.
"""

def update_topics(mongo_collection, name, topics):
    """
    Updates the topics of all school documents with a given name.

    Args:
        mongo_collection: A pymongo collection object.
        name (str): The name of the school to update.
        topics (list of str): The new list of topics for the school.

    Returns:
        The number of documents updated.
    """
    if not mongo_collection:
        return 0

    result = mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
    return result.modified_count
