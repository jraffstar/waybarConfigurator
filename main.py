from tkinter import messagebox, ttk
from tkinter import *

from webcolors import name_to_hex

window = Tk()
canvas = Canvas(width=10000, height=10000)

window.geometry("800x600")

f = open("style.css", "a")



colours = ["white", "black", "purple", "yellow", "red", "blue", "skyblue", "mediumorchid", "mediumpurple", "magenta", "lightpink", "lightgrey", "lightcoral", "lawngreen", "indigo", "indianred", "hotpink"]

def color_name_to_code(color_name):
    try:
        color_code = name_to_hex(color_name)
        return color_code

    except ValueError:
        return None

# Function to change the outline of the workspace indicator to whatever the user selects
def changeWorkspaceOutlineColour():
    color = outlineColourSelection.get()
    print("Outline colour selected: " + color)
    canvas.itemconfig(outline, outline=color)

def changeWorkspaceBGColour():
    color = bgColourSelection.get()
    print("BG colour selected: " + color)
    canvas.itemconfig(activeWorkspace, fill=color)
    # Change the number color if you want it to match the bg
    canvas.itemconfig(activeWorkspaceNumber, fill=color)

def changeWorkspaceHoverColour():
    color = hoverColourSelection.get()
    print("Hover colour selected: " + color)
    canvas.itemconfig(hoverWorkspace, fill=color)
    # Change the text color on hover workspace
    canvas.itemconfig(hoverWorkspaceTNumber, fill=color)

def changeFontColour():
    color = fontColourSelection.get()
    print("Font colour selected: " + color)
    canvas.itemconfig(workspace1Number, fill=color)
    canvas.itemconfig(activeWorkspaceNumber, fill=color)
    canvas.itemconfig(workspace3Number, fill=color)
    canvas.itemconfig(hoverWorkspaceTNumber, fill=color)
    canvas.itemconfig(workspace5Number, fill=color)

def writetofile():
    # Convert color names to hex codes safely
    fontcol = color_name_to_code(fontColourSelection.get()) or "#000000"
    hovcol = color_name_to_code(hoverColourSelection.get()) or "#CCCCCC"
    bgcol = color_name_to_code(bgColourSelection.get()) or "#222222"
    outlinecol = color_name_to_code(outlineColourSelection.get()) or "#0000FF"

    # Write to file using your original format
    f = open("style.css", "w")  # overwrite previous content
    f.write("#window { \n   color: " + str(fontcol) + ";\n}\n\n")
    f.write("#workspaces button:hover { \n  background-color: " + str(hovcol) + ";\n}\n\n")
    f.write("#workspaces button.active { \n background-color: " + str(bgcol) + ";\n}\n\n")
    f.write("#workspaces { \n   border-style: solid;\n  border-color: " + str(outlinecol) + ";\n}\n\n")
    f.close()

writeChanges = ttk.Button(window, text="write", command=lambda: writetofile())

outlineColourSelectionLabel = Label(window, text="Outline Colour")
outlineColourSelection = ttk.Combobox(state="readonly", values=colours)
outlineColourSelection.bind("<<ComboboxSelected>>", lambda event: changeWorkspaceOutlineColour())

bgColourSelectionLabel = Label(window, text="Active workspace colour")
bgColourSelection = ttk.Combobox(state="readonly", values=colours)
bgColourSelection.bind("<<ComboboxSelected>>", lambda event: changeWorkspaceBGColour())

hoverColourSelectionLabel = Label(window, text="Workspace hover colour")
hoverColourSelection = ttk.Combobox(state="readonly", values=colours)
hoverColourSelection.bind("<<ComboboxSelected>>", lambda event: changeWorkspaceHoverColour())

fontColourSelectionLabel = Label(window, text="Font colour")
fontColourSelection = ttk.Combobox(state="readonly", values=colours)
fontColourSelection.bind("<<ComboboxSelected>>", lambda event: changeFontColour())

# Display what a workspace button would look like
outline = canvas.create_rectangle(8,8,512,112,outline = "skyblue" ,fill = "#222222",width = 4)

workspace1 = canvas.create_rectangle(10,10,110,110,outline="", fill = "#222222")

activeWorkspaceLabel = Label(window, text="Active workspace", fg="#FFFFFF", bg="#111111")
activeWorkspace = canvas.create_rectangle(110,10,210,110,outline="", fill = "skyblue")

workspace3= canvas.create_rectangle(210,10,310,110,outline="", fill = "#222222")
workspace3Number = Label(window, text="3", font="Arial, 56", bg="#222222")

hoveringWorkspaceLabel = Label(window, text="Hover colour", fg="#FFFFFF", bg="#111111")
hoverWorkspace = canvas.create_rectangle(310,10,410,110,outline="", fill = "#CCCCCC")

workspace5 = canvas.create_rectangle(410,10,510,110,outline="", fill = "#222222")

workspace1Number = canvas.create_text(60, 60, text="1", font=("Arial", 56), fill="black")

activeWorkspaceNumber = canvas.create_text(160, 60, text="2", font=("Arial", 56), fill="black")

workspace3Number = canvas.create_text(260, 60, text="3", font=("Arial", 56), fill="black")

hoverWorkspaceTNumber = canvas.create_text(360, 60, text="4", font=("Arial", 56), fill="black")

workspace5Number = canvas.create_text(460, 60, text="5", font=("Arial", 56), fill="black")

# Additional configuration
window.configure(bg="#111111")
canvas.configure(bg="#111111")

# Place all widgits on the screen
outlineColourSelection.place(x=0, y=200)
outlineColourSelectionLabel.place(x=0, y=180)

bgColourSelection.place(x=200, y=200)
bgColourSelectionLabel.place(x=200, y=180)

hoverColourSelection.place(x=400, y=200)
hoverColourSelectionLabel.place(x=400, y=180)

fontColourSelection.place(x=600, y=200)
fontColourSelectionLabel.place(x=600, y=180)

writeChanges.place(x=0, y=300)

canvas.place(relx=0, rely=0)

window.mainloop()