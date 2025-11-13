#!/usr/bin/env python3
# utils.py - utility module for todays_ematrix.py

import pyinputplus as pyip

from task import Task


def get_new_task_from_user():
    title = pyip.inputStr("Enter a title for your task: ")
    urg_impt = pyip.inputChoice(
        ["U", "I", "B"],
        "Task is [U]rgent, [I]mportant, [B]oth, or [N]either: ",
    )

    match urg_impt:
        case "U":
            # urgent but not important
            urgent = True
            important = False
        case "B":
            # urgent AND important
            urgent = True
            important = True
        case "N":
            # neither urgent nor important
            urgent = False
            important = False
        case _:
            """
            NOTE default case strictly necessary BUT pyip will catch this
            however, since we would expect urgent N important Y to be the
            "brunt" of our day-to-day work, we will make that the default
            i.e. important but not urgent
            """
            urgent = False
            important = True

    return Task({"title": title, "urgent": urgent, "important": important})


def get_user_task_selection(prompt, tasks):
    print()
    print(prompt)
    return pyip.inputMenu(tasks, numbered=True)


def delete_task_from_list(tasks, title):
    return [task for task in tasks if task["title"] != title]
