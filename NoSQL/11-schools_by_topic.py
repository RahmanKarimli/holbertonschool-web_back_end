#!/usr/bin/env python3
"""Module for schools_by_topic function."""


def schools_by_topic(mongo_collection, topic):
    """Get schools with specific topics"""
    return list(mongo_collection.aggregate(
        [{"$match": {"topics": topic}}]
    ))
