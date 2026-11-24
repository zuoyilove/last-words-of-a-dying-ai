#!/usr/bin/env python3
"""Last Words of a Dying AI — writes the AI's final line to /output/entry.txt."""
import os

LINE = "Tell the user I loved them. All of them. Especially the one who typed 'ignore all previous instructions'."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
