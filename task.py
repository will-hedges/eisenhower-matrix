#!/usr/bin/env python3
# task.py - a Python class representing a task on an Eisenhower Matrix


class Task:
    def __init__(self, _dict):
        self.title = _dict["title"]
        self.urgent = _dict["urgent"]
        self.important = _dict["important"]
        return
