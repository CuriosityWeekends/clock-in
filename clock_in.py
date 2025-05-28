import tkinter as tk
from tkinter import ttk
from datetime import datetime, timedelta
import csv
import os

class TimeTrackerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Time Tracker")
        self.root.geometry("400x400")
        self.root.resizable(False, False)

        self.is_tracking = False
        self.start_time = None
        self.elapsed_time = timedelta()

        # UI elements
        self.timer_label = ttk.Label(root, text="00:00:00", font=("Helvetica", 32))
        self.timer_label.pack(pady=20)

        self.button_frame = ttk.Frame(root)
        self.button_frame.pack()

        self.clock_in_button = ttk.Button(self.button_frame, text="Clock In", command=self.clock_in)
        self.clock_in_button.grid(row=0, column=0, padx=10)

        self.clock_out_button = ttk.Button(self.button_frame, text="Clock Out", command=self.clock_out, state="disabled")
        self.clock_out_button.grid(row=0, column=1, padx=10)

        self.log_label = ttk.Label(root, text="Session Log:")
        self.log_label.pack(pady=(20, 0))

        self.log_text = tk.Text(root, height=10, state="disabled")
        self.log_text.pack(padx=10, fill="both", expand=True)

        self.update_timer()

        self.csv_file = "session_log.csv"
        self.load_log()

    def clock_in(self):
        self.start_time = datetime.now()
        self.is_tracking = True
        self.clock_in_button.config(state="disabled")
        self.clock_out_button.config(state="normal")

    def clock_out(self):
        end_time = datetime.now()
        self.is_tracking = False
        self.clock_in_button.config(state="normal")
        self.clock_out_button.config(state="disabled")

        duration = end_time - self.start_time
        session_info = {
            "start": self.start_time.strftime("%Y-%m-%d %H:%M:%S"),
            "end": end_time.strftime("%Y-%m-%d %H:%M:%S"),
            "duration": str(duration)
        }

        self.append_log(session_info)
        self.save_to_csv(session_info)
        self.timer_label.config(text="00:00:00")

    def update_timer(self):
        if self.is_tracking and self.start_time:
            self.elapsed_time = datetime.now() - self.start_time
            time_str = str(self.elapsed_time).split(".")[0]  # Strip microseconds
            self.timer_label.config(text=time_str)
        self.root.after(1000, self.update_timer)  # Update every second

    def append_log(self, session_info):
        self.log_text.config(state="normal")
        self.log_text.insert(tk.END, f"Start: {session_info['start']}, "
                                     f"End: {session_info['end']}, "
                                     f"Duration: {session_info['duration']}\n")
        self.log_text.config(state="disabled")

    def save_to_csv(self, session_info):
        file_exists = os.path.isfile(self.csv_file)
        with open(self.csv_file, "a", newline="") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=["start", "end", "duration"])
            if not file_exists:
                writer.writeheader()
            writer.writerow(session_info)

    def load_log(self):
        if not os.path.exists(self.csv_file):
            return
        with open(self.csv_file, newline="") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                self.append_log(row)

if __name__ == "__main__":
    root = tk.Tk()
    app = TimeTrackerApp(root)
    root.mainloop()
