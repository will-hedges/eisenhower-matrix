#!/usr/bin/env python3
# eisenhower_matrix.py - a Python class representing an Eisenhower matrix


def show_quadrant_with_header(header, tasks_in_quadrant):
    """
    Displays a header for a quadrant and a bulleted list of Tasks
    """
    print("\n" + " " + header + "\n")

    if tasks_in_quadrant:
        for task in tasks_in_quadrant:
            print(f" * {task.title}")
    else:
        print(" " * 3 + "N/A")

    print()
    return


def sort_tasks_by_title(task_list):
    return sorted(task_list, key=lambda t: t.title.lower())


class EisenhowerMatrix:
    def __init__(self, tasks):
        self.quadrant_1 = [t for t in tasks if t.quadrant == 1]
        self.quadrant_2 = [t for t in tasks if t.quadrant == 2]
        self.quadrant_3 = [t for t in tasks if t.quadrant == 3]
        self.quadrant_4 = [t for t in tasks if t.quadrant == 4]
        self.tasks = (
            self.quadrant_1 + self.quadrant_2 + self.quadrant_3 + self.quadrant_4
        )
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

    def reset(self):
        self.quadrant_1 = [t for t in self.tasks if t.quadrant == 1]
        self.quadrant_2 = [t for t in self.tasks if t.quadrant == 2]
        self.quadrant_3 = [t for t in self.tasks if t.quadrant == 3]
        self.quadrant_4 = [t for t in self.tasks if t.quadrant == 4]
        self.tasks = (
            self.quadrant_1 + self.quadrant_2 + self.quadrant_3 + self.quadrant_4
        )
        return

    def display(self):
        self.reset()

        print()
        print("  **  Eisenhower Matrix  **  ")
        show_quadrant_with_header("!!! TOP PRIORITY !!!", self.quadrant_1)
        show_quadrant_with_header("### Day-to-Day ###", self.quadrant_2)
        show_quadrant_with_header("--- Tomorrow? ---", self.quadrant_3)
        show_quadrant_with_header("zzz Low Priority zzz", self.quadrant_4)
        print()

        return

    """
    !@#$%^&*()_+-=~`|\/?.,<>;:'"
    """
