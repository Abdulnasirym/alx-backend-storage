#!/usr/bin/env python3
"""A python module"""

def insert_school(mongo_collection, **kwargs):
    """inserts a new document"""
    new_document = mongo_collection.insert_one(kwargs)
    return new_document.inserted_id
