#!/usr/bin/env python3
"""A python module"""

def schools_by_topic(mongo_collection, topic):
    """returns the list of school having a specific topic"""
    school_list = mongo_collection.find({"topic": topic})
    return list(school_list)
