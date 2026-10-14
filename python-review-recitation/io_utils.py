import datetime
import os

# --- CODE TO COMPLETE: File Reading & Writing ---


def write_todo_list(file_path, todos):
    """
    Writes a list of to-do dictionaries to a file.
    Each dictionary has keys: 'task', 'date', 'completed'.
    """
    try:
        with open(file_path, "w", encoding="utf-8") as file:
            file.write("To Do:\n")
            for todo in todos:
                status = "x" if todo.get("completed") else "o"
                date_val = todo.get("date")

                # Format date properly whether it's a datetime.date object or string
                if isinstance(date_val, (datetime.date, datetime.datetime)):
                    date_str = date_val.strftime("%Y-%m-%d")
                else:
                    date_str = str(date_val)

                task = todo.get("task", "").strip()
                # Matches the exact format in todo_list.txt: 'x YYYY-MM-DD: Task'
                file.write(f"{status} {date_str}: {task}\n")
    except IOError as e:
        print(f"Error saving to-do list to file: {e}")


def read_todo_list(file_path):
    """
    Reads a file and returns a list of to-do dictionaries.
    Each dictionary should have keys: 'task', 'date', 'completed'.
    """
    todos = []

    if not os.path.exists(file_path):
        return todos

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            for line_num, line in enumerate(file, start=1):
                line = line.strip()

                # Skip empty lines and the first header line
                if not line or (line_num == 1 and line == "To Do:"):
                    continue

                try:
                    # 1. Support both 'x ' / 'o ' (from todo_list.txt) AND '[x] ' / '[o] '
                    if line.startswith("x ") or line.startswith("o "):
                        completed = line[0] == "x"
                        remainder = line[2:]
                    elif line.startswith("[x] ") or line.startswith("[o] "):
                        completed = line[1] == "x"
                        remainder = line[4:]
                    else:
                        raise ValueError(
                            "Missing or invalid status indicator 'x' or 'o'."
                        )

                    # 2. Split the remaining string into Date and Task at the first ': '
                    if ": " not in remainder:
                        raise ValueError(
                            "Missing ': ' separator between date and task."
                        )

                    date_str, task = remainder.split(": ", 1)

                    # 3. Parse the date string into a datetime.date object
                    task_date = datetime.datetime.strptime(
                        date_str.strip(), "%Y-%m-%d"
                    ).date()

                    todos.append(
                        {
                            "task": task.strip(),
                            "date": task_date,
                            "completed": completed,
                        }
                    )
                except ValueError as e:
                    print(
                        f"Warning: Skipping malformed line {line_num} ('{line}') - {e}"
                    )

    except IOError as e:
        print(f"Error reading to-do list file: {e}")

    return todos


# --- Provided functions for input validation ---
def get_integer_input(prompt, min_val=1, max_val=float("inf")):
    while True:
        try:
            choice = input(prompt).strip()
            if not choice:
                return None
            val = int(choice)
            if min_val <= val <= max_val:
                return val
            else:
                print(
                    f"Invalid input. Please enter a number between {min_val} and {max_val}."
                )
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


def get_date_input(prompt):
    while True:
        date_str = input(prompt).strip()
        if not date_str:
            return None
        try:
            return datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD (e.g., 2025-12-31).")
