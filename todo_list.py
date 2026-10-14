import datetime as datetime

from ai_ppp_python_review_solutions import write_todo_list, read_todo_list

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
    REPLACE_ME = None
    def __init__(self, task, date, completed=REPLACE_ME): # what should the default value be?
        # TODO: Your code here
        pass

    def get_task(self):
        # TODO: Your code here
        pass

    def get_date(self):
        # TODO: Your code here
        pass

    def is_completed(self):
        # TODO: Your code here
        pass

    def set_task(self, new_task):
        # TODO: Your code here
        pass

    def set_date(self, new_date):
        # TODO: Your code here
        pass

    def set_completed(self, status):
        # TODO: Your code here
        pass

    def toggle_completion(self):
        # TODO: Your code here
        pass

    def to_dict(self):
        """
        Converts the Todo object to dictionary format with keys like: 
        {'task': 'task name', 'date': datetime.date(2025, 1, 1), 'completed': False}
        """
        # TODO: Your code here
        pass

    def __str__(self):
        # TODO: Your code here
        pass


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
        pass

    def get_name(self):
        # TODO: Your code here: Return the list's name
        print(f"This is your list's name: {self.__name}")
        # return self.__name
        
        pass

    def get_items(self):
        # TODO: Your code here: Return the list of Todo items
        print(f"These are the items in your list: {self.__items}")
        pass

    def set_name(self, new_name):
        # TODO: Your code here: Update the list's name
        self.__name = new_name
        
        pass

    def set_items(self, new_items):
        # TODO: Your code here: Update the list of Todo items
        list = self.list_names.main_cli
        list = list.append(new_items) # how list is referenced?
        return list
        
        
        pass

    def add_task(self, task_name, date):
        # TODO: Your code here: Create a new Todo object and add it to the list of items
        return self.list.add(date, task_name)
        
        pass

    def remove_task(self, index):
        """Removes a task by its 0-based index."""
        # TODO Your code here: Safely remove the item at the specified index.
        
        return list.remove(index)
        
        pass

    REPLACE_THIS = None
    def mark_complete(self, index, status=REPLACE_THIS): # what might the default status be for mark complete?
        """Sets the completion status of a task by its 0-based index."""
        # TODO Your code here: Use the index to find the correct Todo object and update its status.
        pass

    def save_to_file(self, file_path):
        """
        Use the functions implemented by another group (io_utils.py).
        """
        pass

    def load_from_file(self, file_path):
        """
        Use the functions implemented by another group (io_utils.py).
        """
        pass

    def __str__(self):
        """
        Returns a formatted string representing the list.
        """
        pass
