# Time Tracker App

A simple desktop time tracker application built with Python and Tkinter.  
Allows you to clock in/out, track session durations, and save logs in CSV format.

---

## Features

- Start/stop tracking time with Clock In / Clock Out buttons
- Real-time timer display
- Session logs saved to \`session_log.csv\`
- Session history shown inside the app
- Linux \`.desktop\` launcher included for easy start

---

## Installation

### Requirements

- Python 3.x  
- \`tkinter\` library (usually included with Python)  
- Git (optional, for cloning repo)

---

### Steps to run

1. **Clone this repository** (or download the source):

   \`\`\`bash
   git clone https://github.com/CuriosityWeekends/clock-in.git
   cd clock-in
   \`\`\`

2. **Install tkinter** (if not installed):

   \`\`\`bash
   sudo apt update
   sudo apt install python3-tk
   \`\`\`

3. **Run the application:**

   \`\`\`bash
   python3 time_tracker.py
   \`\`\`

---

## Optional: Create Desktop Launcher (Ubuntu/Linux)

1. Copy the \`.desktop\` file included in the repo to your local applications folder:

   \`\`\`bash
   cp time_tracker.desktop ~/.local/share/applications/
   \`\`\`

2. Make sure the launcher has execution permission:

   \`\`\`bash
   chmod +x ~/.local/share/applications/time_tracker.desktop
   \`\`\`

3. You should now be able to find **Time Tracker** in your applications menu.

---

## How to Use

- Click **Clock In** to start tracking time.
- The timer will show elapsed time.
- Click **Clock Out** to stop tracking and save the session.
- Your session logs will be saved in \`session_log.csv\` and shown in the log window.
- The app resets timer after each session.

---

## License

This project is licensed under the MIT License.

---

## Contact

For questions or contributions, feel free to open an issue or pull request on GitHub.

---

*Happy tracking!* ⏰
