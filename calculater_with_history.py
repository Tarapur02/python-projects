HISTORY_FILE = "history.txt"

def show_history():
    try:
        with open(HISTORY_FILE, "r") as file:
            lines = file.readlines()
            if not lines:
                print("No history found.")
            else:
                for line in reversed(lines):
                    print(line.strip())
    except FileNotFoundError:
        print("No history file found.")


def clear_history():
    open(HISTORY_FILE, "w").close()
    print("History cleared.")


def save_history(equation, result):
    with open(HISTORY_FILE, "a") as file:
        file.write(f"{equation} = {result}\n")


def calculator(user_input):
    try:
        if "+" in user_input:
            a, b = user_input.split("+")
            result = float(a) + float(b)
        elif "-" in user_input:
            a, b = user_input.split("-")
            result = float(a) - float(b)
        elif "*" in user_input:
            a, b = user_input.split("*")
            result = float(a) * float(b)
        elif "/" in user_input:
            a, b = user_input.split("/")
            if float(b) == 0:
                print("Division by zero not allowed.")
                return
            result = float(a) / float(b)
        else:
            print("Invalid input. Example: 2+3")
            return

        if result.is_integer():
            result = int(result)

        print("Result:", result)
        save_history(user_input, result)

    except ValueError:
        print("Invalid numbers entered.")


def main():
    while True:
        user_input = input(
            "Enter expression (2+3) or commands (history, clean, exit): "
        ).strip()

        if user_input == "exit":
            print("Goodbye!")
            break
        elif user_input == "history":
            show_history()
        elif user_input == "clean":
            clear_history()
        else:
            calculator(user_input)


main()
