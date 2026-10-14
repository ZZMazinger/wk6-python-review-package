import datetime

from io_utils import write_todo_list, read_todo_list

# --- CODE TO COMPLETE: Todo Class ---
# The Todo class represents a single task.
# It should have a task name, a due date, and a completion status (all as private variables).
# You need to fill in the methods to manage these attributes.
# HINT: The main_cli.py file expects a `to_dict` method that returns a dictionary like:
# {'task': 'task name', 'date': datetime.date(2025, 1, 1), 'completed': False}
# Also, the __str__ method should format the output nicely.


class Todo:
    """
    Represents a single To-Do item. Stores task name, date, and completion status.
    """

    def __init__(
        self, name, date, completed=False
    ):  # what should the default value be?
        self.task = {}
        self.task["task_name"] = name
        self.task["date"] = date
        self.task["completed"] = completed

    def get_task(self):
        return self.task["task_name"]

    def get_date(self):
        return self.task["date"]

    def is_completed(self):
        return self.task["completed"]

    def set_task(self, new_task):
        self.task["task_name"] = new_task

    def set_date(self, new_date):
        self.task["date"] = new_date

    def set_completed(self, status):
        self.task["completed"] = status

    def toggle_completion(self):
        self.task["completed"] = not self.task["completed"]

    def to_dict(self):
        """
        Converts the Todo object to dictionary format with keys like:
        {'task': 'task name', 'date': datetime.date(2025, 1, 1), 'completed': False}
        """
        return self.task

    def __str__(self):
        status = "Completed" if self.task["completed"] else "Not Completed"
        return f"Task: {self.task['task_name']}, Due Date: {self.task['date']}, Status: {status}"


# --- CODE TO COMPLETE: TodoList Class ---
# The TodoList class manages a collection of Todo objects.
# This is the central hub for adding, removing, and updating tasks.
# It should store a list of Todo objects (private variable).


class TodoList:
    """
    Manages a collection of Todo objects for a specific list.
    """
    def __init__(self, name, items, date):
        # TODO: Your code here
        self.__name = name
        self.__items = items
        self.new_name = 
        self.new_items
        self.task_name = self.new_name
        self.__date = date
        self.list = []


    def get_name(self):
        # TODO: Your code here: Return the list's name
        print(f"This is your list's name: {self.__name}")
        return self.__name

    def get_items(self):
        # TODO: Your code here: Return the list of Todo items
        print(f"These are the items in your list: {self.__items}")
        return self.__items

    def set_name(self, new_name):
        # TODO: Your code here: Update the list's name
        self.__name = new_name
        return self.__name

    def set_items(self, new_items):
        # TODO: Your code here: Update the list of Todo items
        self.__items = new_items
        return self.__items

    def add_task(self, task_name, date):
        # TODO: Your code here: Create a new Todo object and add it to the list of items
        # return self.list.add(date, task_name)
        todo = Todo(task_name, date)
        self.list.append(todo)

    def remove_task(self, index):
        """Removes a task by its 0-based index."""
        # TODO Your code here: Safely remove the item at the specified index.
        
        return list.remove(index)
        
        

    # REPLACE_THIS = None
    def mark_complete(self, index, status=True): # what might the default status be for mark complete?
        """Sets the completion status of a task by its 0-based index."""
        # TODO Your code here: Use the index to find the correct Todo object and update its status.
        self.list[index].set_completed(status)

    def save_to_file(self, file_path):
        """
        Use the functions implemented by another group (io_utils.py).
        """
        write_todo_list(file_path, self.list)

    def load_from_file(self, file_path):
        """
        Use the functions implemented by another group (io_utils.py).
        """
        self.list = read_todo_list(file_path)

    def __str__(self):
        """
        Returns a formatted string representing the list.
        """
        return f"Todo List: {self.__name}"