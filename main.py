"""
main.py - Main entry point with error handling
"""
import tkinter as tk
from periodic_table.gui import PeriodicTableApp

def main():
    try:
        root = tk.Tk()
        app = PeriodicTableApp(root)
        root.mainloop()
    except Exception as e:
        print(f"An error occurred: {e}")
        # Optionally show error to user
        tk.messagebox.showerror("Error", f"An error occurred: {e}")
    finally:
        if 'root' in locals():
            root.destroy()

if __name__ == "__main__":
    main()