#!/usr/bin/env python3
"""
This module contains a function `schools_by_topic` that retrieves
all school documents from a MongoDB collection containing a specific topic.
"""

def schools_by_topic(mongo_collection, topic):
    """
    Returns a list of school documents that have a specific topic.

    Args:
        mongo_collection: A pymongo collection object.
        topic (str): The topic to search for in the school's topics list.

    Returns:
        A list of school documents matching the topic. Empty list if none found.
    """
    if not mongo_collection:
        return []

    # Find all documents where the 'topics' field contains the given topic
    return list(mongo_collection.find({"topics": topic}))
