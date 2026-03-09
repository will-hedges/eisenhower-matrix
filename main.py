#!/usr/bin/env python3
# main.py - main program for Eisenhower matrix terminal app


import os

import pyinputplus as pyip

from eisenhower_matrix import EisenhowerMatrix
from task import Task
from utils import (
    get_new_task_from_user,
    get_user_main_menu_selection,
    get_user_task_selection,
    get_user_update_selection,
    load_matrix_from_json,
    write_matrix_to_json,
)


def main():
    # try to load saved tasks from local JSON file, if it exists.
    # If not, start with an empty list of tasks and prompt the user to add a
    # new one.
    try:
        json_tasks = load_matrix_from_json("matrix_tasks.json")
        json_tasks = [Task(**t) for t in json_tasks]
    except FileNotFoundError:
        json_tasks = []

    if not json_tasks:
        print("No tasks found in local JSON file.")
        add_new = pyip.inputYesNo("Create a new task? (Y/N) > ")
        if add_new:
            json_tasks.append(Task(**get_new_task_from_user()))

    # initialize the matrix
    eisenhowermatrix = EisenhowerMatrix(json_tasks)

    while True:
        try:
            write_matrix_to_json(eisenhowermatrix, "matrix_tasks.json")

            # clear the terminal, display the matrix, and get the user to
            # select an option from the main menu
            os.system("cls || clear")
            eisenhowermatrix.display()
            opt = get_user_main_menu_selection()

            # process the user's choice and update the task and matrix
            match opt:
                case "C":
                    new_task = get_new_task_from_user()
                    eisenhowermatrix.tasks.append(Task(**new_task))

                case "U":
                    # show the user a list of all tasks & let them select one
                    # then let them select which property to update
                    # then update the appropriate task properties (and
                    # matrix quadrants)
                    upd_task = get_user_task_selection(
                        eisenhowermatrix,
                        "Which task do you want to update?",
                    )
                    if upd_task:
                        upd_sel = get_user_update_selection(upd_task)
                        match upd_sel:
                            case "title":
                                upd_task.update_title()
                            case "urgency":
                                upd_task.update_urgency()
                            case "importance":
                                upd_task.update_importance()
                            case "urgency_and_importance":
                                upd_task.update_urgency()
                                upd_task.update_importance()
                            case "all":
                                upd_task.update_title()
                                upd_task.update_urgency()
                                upd_task.update_importance()
                            case _:
                                pass

                case "D":
                    del_task = get_user_task_selection(
                        eisenhowermatrix,
                        "Which task do you want to delete?",
                    )
                    eisenhowermatrix.tasks = [
                        t for t in eisenhowermatrix.tasks if t != del_task
                    ]

                case _:
                    break

        except KeyboardInterrupt:
            break
    return


if __name__ == "__main__":
    main()
