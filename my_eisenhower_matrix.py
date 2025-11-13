#!/usr/bin/env python3
# my_eisenhower_matrix.py - TODO

import json

import pyinputplus as pyip

from eisenhower_matrix import EisenhowerMatrix
from task import Task
from utils import get_new_task_from_user, get_user_task_selection


def main():
    """
    check to see if the .json exists
    if it does, load the tasks into Task classes
    if it doesn't, show a message
    if the file exists but is empty... TODO
    """
    try:
        with open("matrix_tasks.json", "r") as jf:
            data = json.load(jf)
        tasks = [Task(subdict) for subdict in data["tasks"]]
    except FileNotFoundError:
        print("No tasks found in local JSON file.")
        add_new = pyip.inputYesNo("Create a new task (Y/N): ")
        if add_new == "yes":
            tasks = list(get_new_task_from_user())
        else:
            return

    # main loop
    while True:
        eisenhowermatrix = EisenhowerMatrix(tasks)
        eisenhowermatrix.display()

        opt = pyip.inputChoice(
            ["C", "U", "D", "E"],
            "\n".join(
                (
                    "Do you want to",
                    "  [C]reate a new task",
                    "  [U]pdate an existing task",
                    "  [D]elete a task",
                    "  [E]xit (or press <Enter>)",
                    ": ",
                )
            ),
            blank=True,
        )

        try:
            match opt:
                case "C":
                    new_task = get_new_task_from_user()
                    tasks.append(new_task)

                case "U":
                    upd_task = get_user_task_selection(
                        "Which task do you want to update?",
                        [task.title for task in tasks],
                    )
                    pass
                case "D":
                    del_task = get_user_task_selection(
                        "Which task do you want to delete?",
                        [task.title for task in tasks],
                    )
                    pass
                case _:
                    # NOTE this should catch "E" or blank
                    break
        except KeyboardInterrupt:
            # handle ctrl+C gracefully
            break

    # TODO write out to JSON
    return


if __name__ == "__main__":
    main()
