import tkinter as tk
from tkinter import ttk, messagebox

# --- Operation Functions ---

def parse_input():
    """Parse and return list of float numbers from input."""
    try:
        nums = list(map(float, entry_input.get().split(',')))
        if len(nums) < 2:
            raise ValueError("At least two numbers required.")
        return nums
    except ValueError:
        messagebox.showerror("Input Error", "Please enter at least two valid numbers, separated by commas.")
        return None

def add():
    nums = parse_input()
    if nums:
        result_var.set(f"{sum(nums):.2f}")

def subtract():
    nums = parse_input()
    if nums:
        result = nums[0]
        for num in nums[1:]:
            result -= num
        result_var.set(f"{result:.2f}")

def multiply():
    nums = parse_input()
    if nums:
        result = 1
        for num in nums:
            result *= num
        result_var.set(f"{result:.2f}")

def divide():
    nums = parse_input()
    if nums:
        try:
            result = nums[0]
            for num in nums[1:]:
                result /= num
            result_var.set(f"{result:.2f}")
        except ZeroDivisionError:
            messagebox.showerror("Math Error", "Cannot divide by zero.")

def clear():
    entry_input.delete(0, tk.END)
    result_var.set("")

# --- GUI Setup ---

root = tk.Tk()
root.title("Modern GUI Calculator")
root.geometry("430x300")
root.configure(bg="#f0f4f7")

# --- Styling ---
style = ttk.Style()
style.configure("TButton", font=("Segoe UI", 10, "bold"), padding=6)
style.configure("TLabel", font=("Segoe UI", 11))
style.configure("Result.TLabel", font=("Segoe UI", 14, "bold"), foreground="#1f77b4")

# --- Title ---
tk.Label(root, text="Modern Multi-Number Calculator", font=("Segoe UI", 14, "bold"), bg="#f0f4f7", fg="#333").pack(pady=10)

# --- Input Field ---
ttk.Label(root, text="Enter numbers (comma separated):").pack(pady=(5, 2))
entry_input = ttk.Entry(root, width=40)
entry_input.pack(pady=(0, 10))

# --- Operation Buttons ---
frame_buttons = ttk.Frame(root)
frame_buttons.pack(pady=5)

ttk.Button(frame_buttons, text="+", width=7, command=add).grid(row=0, column=0, padx=5)
ttk.Button(frame_buttons, text="-", width=7, command=subtract).grid(row=0, column=1, padx=5)
ttk.Button(frame_buttons, text="×", width=7, command=multiply).grid(row=0, column=2, padx=5)
ttk.Button(frame_buttons, text="÷", width=7, command=divide).grid(row=0, column=3, padx=5)
ttk.Button(frame_buttons, text="Clear", width=7, command=clear).grid(row=0, column=4, padx=5)

# --- Result Display ---
ttk.Label(root, text="Result:").pack(pady=(20, 5))
result_var = tk.StringVar()
result_label = ttk.Label(root, textvariable=result_var, style="Result.TLabel")
result_label.pack()

# --- Run GUI ---
root.mainloop()
