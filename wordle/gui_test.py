from tkinter import *
from tkinter import ttk

# Calculation method
def calculate(*args):
    try:
        value = float(feet.get())
        meters.set(int(0.3048 * value * 10000.0 + 0.5)/10000.0)
    except ValueError:
        pass

# Setup main application window
root = Tk()
root.title("Wordle")

# Frame widget, holds contents of UI
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# Feet entry widget
feet = StringVar()
feet_entry = ttk.Entry(mainframe, width=7, textvariable=feet)
feet_entry.grid(column=2, row=1, sticky=(W, E))

# Meters label widget
meters = StringVar()
ttk.Label(mainframe, textvariable=meters).grid(column=2, row=2, sticky=(W, E))

# Button widget
ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=3, row=3, sticky=W)

# label widgets
ttk.Label(mainframe, text="feet").grid(column=3, row=1, sticky=W)
ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=E)
ttk.Label(mainframe, text="meters").grid(column=3, row=2, sticky=W)

# Loop through all widgets in main window
for child in mainframe.winfo_children():
    # Add padding to each widget
    child.grid_configure(padx=5, pady=5)
# Focus on the feet entry widget text box
feet_entry.focus()
# Call calculate method when return (enter) is pressed
root.bind("<Return>", calculate)

# Run the main event loop
root.mainloop()