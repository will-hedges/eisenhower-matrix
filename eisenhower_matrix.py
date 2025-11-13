#!/usr/bin/env python3
# eisenhower_matrix.py - a Python class representing an Eisenhower Matrix


def show_quadrant_with_header(header, tasks):
    """
    Displays a header for a quadrant and a numbered list of Tasks
    """
    print("\n" + header)
    if tasks:
        for index, task in enumerate(tasks):
            print(f" {index + 1}. {task.title}")
    else:
        print(" " + "N/A")
    return


class EisenhowerMatrix:
    def __init__(self, tasks):
        """
        Creates an Eisenhower Matrix from a list of Task objects
        """
        self.quadrant_1 = []
        self.quadrant_2 = []
        self.quadrant_3 = []
        self.quadrant_4 = []

        for task in tasks:
            if task.urgent is True:
                # CRISES
                if task.important is True:
                    self.quadrant_1.append(task)
                # DELEGATE
                elif task.important is False:
                    self.quadrant_3.append(task)
            elif task.urgent is False:
                # DAY TO DAY
                if task.important is True:
                    self.quadrant_2.append(task)
                # AVOID - TIME WASTERS
                elif task.important is False:
                    self.quadrant_4.append(task)
        return

    def display(self):
        """
        Displays the Eisenhower Matrix, with tasks grouped by quadrant
        """
        show_quadrant_with_header("!!! URGENT & IMPORTANT !!!", self.quadrant_1)
        show_quadrant_with_header("--- Day-to-Day ---", self.quadrant_2)
        show_quadrant_with_header("___ Delegate? ___", self.quadrant_3)
        show_quadrant_with_header("~~~ Time-Wasters ~~~", self.quadrant_4)
        # add a blank line
        print()
        return
