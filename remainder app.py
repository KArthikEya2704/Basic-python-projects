import tkinter as tk
from tkinter import messagebox
import threading
import time

class ReminderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Reminder App")
        self.root.geometry("300x200")

        # Labels and entries
        tk.Label(root, text="Enter your reminder:").pack(pady=5)
        self.reminder_text = tk.Entry(root, width=30)
        self.reminder_text.pack(pady=5)

        tk.Label(root, text="Set time (in seconds):").pack(pady=5)
        self.time_input = tk.Entry(root, width=10)
        self.time_input.pack(pady=5)

        # Buttons
        tk.Button(root, text="Set Reminder", command=self.set_reminder).pack(pady=10)

    def set_reminder(self):
        """Sets a reminder."""
        reminder = self.reminder_text.get()
        try:
            delay = int(self.time_input.get())
            if delay < 0:
                raise ValueError("Time must be non-negative.")
            threading.Thread(target=self.start_timer, args=(reminder, delay), daemon=True).start()
            messagebox.showinfo("Reminder Set", f"Reminder set for {delay} seconds.")
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid time in seconds.")

    def start_timer(self, reminder, delay):
        """Starts the countdown and shows the reminder."""
        time.sleep(delay)
        messagebox.showinfo("Reminder", reminder)

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = ReminderApp(root)
    root.mainloop()
