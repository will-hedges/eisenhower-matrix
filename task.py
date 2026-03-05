#!/usr/bin/env python3
# task.py - a simple Python class representing a task on an Eisenhower matrix


from utils import input_with_default


class Task:
    def __init__(self, title, urgent, important, quadrant):
        self.title = title
        self.urgent = urgent
        self.important = important
        self.quadrant = quadrant
        return

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        self._title = title
        return

    @property
    def urgent(self):
        return self._urgent

    @urgent.setter
    def urgent(self, urgent):
        self._urgent = urgent

    @property
    def important(self):
        return self._important

    @important.setter
    def important(self, important):
        self._important = important
        return

    @property
    def quadrant(self):
        return self._quadrant

    @quadrant.setter
    def quadrant(self, quadrant):
        self._quadrant = quadrant
        return

    def update_title(self):
        """
        Takes a user-imput string and updates the Task's title property.
        Entering a blank value will cancel the update and return to the menu.
        """
        new_title = input_with_default(
            prompt="Enter a new title for this task: ", default=self.title
        )
        if new_title:
            self.title = new_title
        return

    def update_quadrant(self):
        match (self.urgent, self.important):
            case (True, True):
                self.quadrant = 1
            case (True, False):
                self.quadrant = 2
            case (False, True):
                self.quadrant = 3
            case (False, False):
                self.quadrant = 4
            case _:
                pass
        return

    def update_urgency(self):
        """Toggles the Task's urgency between True and False."""
        self.urgent = not self.urgent
        self.update_quadrant()
        return

    def update_importance(self):
        """Toggles the Task's importance between True and False."""
        self.important = not self.important
        self.update_quadrant()
        return
