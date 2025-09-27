# workspace_logger.py
from datetime import datetime
import argparse
import os

LOG_FILE = os.path.expanduser("~/repos/workspace-logger/workspace_log.txt")

def log_entry(mode: str, note: str = ""):
    timestamp = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    entry = f"[{timestamp}] Mode: {mode}"
    if note:
        entry += f" | Note: {note}"
    with open(LOG_FILE, "a") as f:
        f.write(entry + "\n")
    print(f"Logged: {entry}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Log workspace mode and notes.")
    parser.add_argument("--mode", required=True, help="Workspace mode (e.g., focus, flow)")
    parser.add_argument("--note", help="Optional note to include")
    args = parser.parse_args()
    log_entry(args.mode, args.note)