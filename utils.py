#!/usr/bin/env python3
# utils.py - utility functions for Eisenhower matrix terminal app


import json

import keyboard
import pyinputplus as pyip


def get_new_task_from_user():
    """
    Gets the user to input a Task title, urgency and importance, and
    creates a new Task object. If the user enters a blank title, will
    cancel and return to the main menu.
    """
    print()

    title = pyip.inputStr(
        prompt="Enter a title for your task: ",
        blank=True,
    ).strip()
    if not title:
        return

    urg_impt = pyip.inputChoice(
        ["B", "I", "U", "N"],
        prompt="\n".join(
            (
                f"'{title}' is",
                " [B]oth urgent AND important (Q1)",
                " [I]mportant (Q2)",
                " [U]rgent (Q3)",
                " [N]either (Q4)",
                "> ",
            )
        ),
    )

    match urg_impt:
        case "B":
            # BOTH urgent AND important (Quadrant 1)
            urgent = True
            important = True
            quadrant = 1
        case "U":
            # URGENT but not important (Quadrant 3)
            urgent = True
            important = False
            quadrant = 3
        case "N":
            # NEITHER urgent nor important (Quadrant 4)
            urgent = False
            important = False
            quadrant = 4
        case _:
            """
            NOTE default case necessary BUT pyip will catch this since we
            would expect urgent N important Y (Quadrant 2) to be the
            majority of our day-to-day work, so make that the default
            """
            urgent = False
            important = True
            quadrant = 2

    return {
        "title": title,
        "urgent": urgent,
        "important": important,
        "quadrant": quadrant,
    }


def get_task_quadrant(urgent, important):
    match (urgent, important):
        case (True, True):
            return 1
        case (True, False):
            return 2
        case (False, True):
            return 3
        case (False, False):
            return 4
        case _:
            return


def get_user_main_menu_selection():
    return pyip.inputChoice(
        ["C", "U", "D", "E"],
        "\n".join(
            (
                "Do you want to",
                " [C]reate a new task",
                " [U]pdate an existing task",
                " [D]elete a task",
                " [E]xit (or press <Enter>)",
                "> ",
            )
        ),
        blank=True,
    )


def get_user_task_selection(EisenhowerMatrix, prompt):
    """
    Displays a prompt and a list of all tasks in the EisenhowerMatrix, and
    gets the user to select one.

        Params:
            EisenhowerMatrix (EisenhowerMatrix): the EisenhowerMatrix instance
            prompt (str): the prompt to display to the user
        Returns:
            (Task): the Task object corresponding to the user's selection,
                        or None if the user enters a blank string
    """
    print()
    print(prompt)
    task_title = pyip.inputMenu(
        [t.title for t in EisenhowerMatrix.tasks],
        numbered=True,
        blank=True,
    )
    if task_title:
        return next(t for t in EisenhowerMatrix.tasks if t.title == task_title)
    return


def get_user_update_selection(task):
    """
    Allows the user to select the property they want to update on a Task.
    If the user enters a blank value, will cancel and return to the main
    menu.

        Params:
            task (Task): the Task object the user wants to update

        Returns:
            (str): the property the user wants to update on the Task
    """
    curr_quad = task.quadrant
    quad_if_urg_upd = get_task_quadrant(not task.urgent, task.important)
    quad_if_imp_upd = get_task_quadrant(task.urgent, not task.important)
    quad_if_urg_and_imp_upd = get_task_quadrant(
        not task.urgent,
        not task.important,
    )

    print()
    prop_sel = pyip.inputMenu(
        [
            f"Title",
            f"Urgency    (Q{curr_quad} -> Q{quad_if_urg_upd})",
            f"Importance (Q{curr_quad} -> Q{quad_if_imp_upd})",
            f"Urgency and Importance (Q{curr_quad} -> Q{quad_if_urg_and_imp_upd})",
            f"All",
        ],
        prompt="\n".join(
            (
                "What do you want to update on this task?",
                "",
                f"   Title: '{task.title}'",
                f"   Urgent: {task.urgent}",
                f"   Important: {task.important}",
                "",
                "",
            )
        ),
        numbered=True,
        blank=True,
    )

    if prop_sel.startswith("Urgency and Importance"):
        return "urgency_and_importance"
    elif prop_sel.startswith("Title"):
        return "title"
    elif prop_sel.startswith("Urgency"):
        return "urgency"
    elif prop_sel.startswith("Importance"):
        return "importance"
    elif prop_sel.startswith("All"):
        return "all"
    else:
        return


def input_with_default(prompt, default):
    """
    Displays a prompt to the user and pre-fills the input with a default value.
    The user can edit the pre-filled value or accept it by pressing Enter.

        Params:
            prompt (str): the prompt to display to the user
            default (str): the default value to pre-fill the input with
    """
    keyboard.write(default)
    return input(prompt)


def load_matrix_from_json(json_fp):
    """
    Loads tasks from a JSON file and returns them as a list of Task objects.

        Params:
            json_fp (str): the file path to load the JSON from

        Returns:
            list: a list of Task objects loaded from the JSON file
    """
    with open(json_fp, "r") as json_file:
        data = json.load(json_file)
        return [task for task in data["tasks"]]


def show_quadrant_with_header(header, quadrant_tasks):
    """
    Displays a header for a quadrant and a bulleted list of Tasks
    """
    print("\n" + header)
    if quadrant_tasks:
        for qt in quadrant_tasks:
            print(f" * {qt.title}")
    else:
        print(" " + "N/A")
    return


def sort_tasks_by_title(task_list):
    return sorted(task_list, key=lambda t: t.title.lower())


def write_matrix_to_json(EisenhowerMatrix, json_fp):
    """
    Writes out the tasks in an EisenhowerMatrix to a JSON file.

        Params:
            EisenhowerMatrix (EisenhowerMatrix): the EisenhowerMatrix to write out
            json_fp (str): the file path to write the JSON to
    """
    task_data = {"tasks": []}
    for task in EisenhowerMatrix.tasks:
        task_obj = {
            "title": task.title,
            "urgent": task.urgent,
            "important": task.important,
            "quadrant": task.quadrant,
        }
        task_data["tasks"].append(task_obj)

    with open(json_fp, "w") as json_file:
        json.dump(task_data, json_file, indent=2)
