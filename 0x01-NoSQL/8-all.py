#!/usr/bin/env python3
"""Python module"""

def list_all(mongo_collection):
    """list all document in a collection"""
    if mongo_collection == None:
        return []
    return List(mongo_collection.find())
