#!/usr/bin/env python3
# eisenhower_matrix.py - a Python class representing an Eisenhower matrix

from utils import show_quadrant_with_header, sort_tasks_by_title


class EisenhowerMatrix:
    def __init__(self, tasks):
        self.tasks = tasks
        self.quadrant_1 = [t for t in tasks if t.quadrant == 1]
        self.quadrant_2 = [t for t in tasks if t.quadrant == 2]
        self.quadrant_3 = [t for t in tasks if t.quadrant == 3]
        self.quadrant_4 = [t for t in tasks if t.quadrant == 4]
        return

    @property
    def tasks(self):
        return self._tasks

    @tasks.setter
    def tasks(self, tasks):
        self._tasks = tasks

    @property
    def quadrant_1(self):
        return self._quadrant_1

    @quadrant_1.setter
    def quadrant_1(self, tasks):
        self._quadrant_1 = sort_tasks_by_title(tasks)
        return

    @property
    def quadrant_2(self):
        return self._quadrant_2

    @quadrant_2.setter
    def quadrant_2(self, tasks):
        self._quadrant_2 = sort_tasks_by_title(tasks)
        return

    @property
    def quadrant_3(self):
        return self._quadrant_3

    @quadrant_3.setter
    def quadrant_3(self, tasks):
        self._quadrant_3 = sort_tasks_by_title(tasks)
        return

    @property
    def quadrant_4(self):
        return self._quadrant_4

    @quadrant_4.setter
    def quadrant_4(self, tasks):
        self._quadrant_4 = sort_tasks_by_title(tasks)
        return

    def update_quadrants(self):
        self.quadrant_1 = [t for t in self.tasks if t.quadrant == 1]
        self.quadrant_2 = [t for t in self.tasks if t.quadrant == 2]
        self.quadrant_3 = [t for t in self.tasks if t.quadrant == 3]
        self.quadrant_4 = [t for t in self.tasks if t.quadrant == 4]
        return

    def display(self):
        self.update_quadrants()

        show_quadrant_with_header(
            "Quadrant 1: Urgent and Important",
            self.quadrant_1,
        )
        show_quadrant_with_header(
            "Quadrant 2: Urgent but Not Important", self.quadrant_2
        )
        show_quadrant_with_header(
            "Quadrant 3: Not Urgent but Important", self.quadrant_3
        )
        show_quadrant_with_header(
            "Quadrant 4: Not Urgent and Not Important", self.quadrant_4
        )
        return
