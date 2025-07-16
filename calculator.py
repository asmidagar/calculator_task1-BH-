# Calculator CLI App using Python (Multi-number Support)

# --- Operation Functions ---

def add(numbers):
    """Returns the sum of all numbers."""
    return sum(numbers)

def subtract(numbers):
    """Returns the result of sequential subtraction."""
    result = numbers[0]
    for num in numbers[1:]:
        result -= num
    return result

def multiply(numbers):
    """Returns the product of all numbers."""
    result = 1
    for num in numbers:
        result *= num
    return result

def divide(numbers):
    """Returns the result of sequential division. Handles division by zero."""
    result = numbers[0]
    try:
        for num in numbers[1:]:
            result /= num
    except ZeroDivisionError:
        return "Error! Division by zero is undefined."
    return result

# --- Display Menu ---
def display_menu():
    print("\n===== CLI Calculator =====")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

# --- Get Numbers from User ---
def get_numbers():
    try:
        count = int(input("How many numbers do you want to operate on? (2 or more): "))
        if count < 2:
            print("Please enter at least two numbers.")
            return None
        numbers = []
        for i in range(count):
            num = float(input(f"Enter number {i + 1}: "))
            numbers.append(num)
        return numbers
    except ValueError:
        print("Invalid input! Only numeric values are acceptable.")
        return None

# --- Main Program Logic ---

def main():
    while True:
        display_menu()
        choice = input("Choose an operation (1-5): ")

        if choice == '5':
            print("Thank you for using the calculator. Goodbye!")
            break

        if choice not in ['1', '2', '3', '4']:
            print("Invalid choice! Please enter a number between 1 and 5.")
            continue

        numbers = get_numbers()
        if numbers is None:
            continue

        # Operation mapping
        operations = {
            '1': add,
            '2': subtract,
            '3': multiply,
            '4': divide
        }

        # Perform operation and print result
        result = operations[choice](numbers)
        print(f"🔹 Result: {result}")

# --- Entry Point ---
if __name__ == "__main__":
    main()
