from tkinter import messagebox, ttk
from tkinter import *

window = Tk()
canvas = Canvas()

colours = ["black", "purple", "yellow", "red", "blue", "skyblue", "mediumorchid", "mediumpurple", "magenta", "lightpink", "lightgrey", "lightcoral", "lawngreen", "indigo", "indianred", "hotpink"]

# Function to change the outline of the workspace indicator to whatever the user selects
def changeWorkspaceOutlineColour():
    print("Outline colour selected: " + outlineColourSelection.get())
    canvas.itemconfig(workspace, outline=outlineColourSelection.get())

def changeWorkspaceBGColour():
    print("BG colour selected: " + bgColourSelection.get())
    canvas.itemconfig(workspace, fill=bgColourSelection.get())


outlineColourSelectionLabel = Label(window, text="Outline Colour")
outlineColourSelection = ttk.Combobox(state="readonly", values=colours)
outlineColourSelection.bind("<<ComboboxSelected>>", lambda event: changeWorkspaceOutlineColour())

bgColourSelectionLabel = Label(window, text="BG Colour")
bgColourSelection = ttk.Combobox(state="readonly", values=colours)
bgColourSelection.bind("<<ComboboxSelected>>", lambda event: changeWorkspaceBGColour())

# Display what a workspace button would look like
workspace = canvas.create_rectangle(10,10,110,110,outline = "black" ,fill = "#222222",width = 4)

# Additional configuration
window.configure(bg="#111111")
canvas.configure(bg="#111111")

# Place all widgits on the screen
outlineColourSelection.place(x=0, y=200)
outlineColourSelectionLabel.place(x=0, y=180)

bgColourSelection.place(x=200, y=200)
bgColourSelectionLabel.place(x=200, y=180)

canvas.place(relx=0, rely=0)


window.mainloop()