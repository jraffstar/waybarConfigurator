from tkinter import messagebox, ttk
from tkinter import *

window = Tk()
canvas = Canvas(width=10000, height=10000)



colours = ["white", "black", "purple", "yellow", "red", "blue", "skyblue", "mediumorchid", "mediumpurple", "magenta", "lightpink", "lightgrey", "lightcoral", "lawngreen", "indigo", "indianred", "hotpink"]

# Function to change the outline of the workspace indicator to whatever the user selects
def changeWorkspaceOutlineColour():
    print("Outline colour selected: " + outlineColourSelection.get())
    canvas.itemconfig(outline, outline=outlineColourSelection.get())

def changeWorkspaceBGColour():
    print("BG colour selected: " + bgColourSelection.get())
    canvas.itemconfig(activeWorkspace, fill=bgColourSelection.get())
    activeWorkspaceNumber.configure(bg=bgColourSelection.get())


def changeWorkspaceHoverColour():
    print("Hover colour selected: " + bgColourSelection.get())
    canvas.itemconfig(hoverWorkspace, fill=hoverColourSelection.get())
    hoveringWorkspaceNumber.configure(bg=hoverColourSelection.get())

def changeFontColour():
    print("Font colour selected: " + bgColourSelection.get())
    workspace1Number.configure(fg=fontColourSelection.get())
    activeWorkspaceNumber.configure(fg=fontColourSelection.get())
    workspace3Number.configure(fg=fontColourSelection.get())
    hoveringWorkspaceNumber.configure(fg=fontColourSelection.get())
    workspace5Number.configure(fg=fontColourSelection.get())


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
workspace1Number = Label(window, text="1", font="Arial, 56", bg="#222222")

activeWorkspaceLabel = Label(window, text="Active workspace", fg="#FFFFFF", bg="#111111")
activeWorkspace = canvas.create_rectangle(110,10,210,110,outline="", fill = "skyblue")
activeWorkspaceNumber = Label(window, text="2", font="Arial, 56", bg="skyblue")


workspace3= canvas.create_rectangle(210,10,310,110,outline="", fill = "#222222")
workspace3Number = Label(window, text="3", font="Arial, 56", bg="#222222")

hoveringWorkspaceLabel = Label(window, text="Hover colour", fg="#FFFFFF", bg="#111111")
hoverWorkspace = canvas.create_rectangle(310,10,410,110,outline="", fill = "#CCCCCC")
hoveringWorkspaceNumber = Label(window, text="4", font="Arial, 56", bg="#CCCCCC")

workspace5 = canvas.create_rectangle(410,10,510,110,outline="", fill = "#222222")
workspace5Number = Label(window, text="5", font="Arial, 56", bg="#222222")

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

activeWorkspaceLabel.place(x=110, y=120)
hoveringWorkspaceLabel.place(x=310, y=120)

workspace1Number.place(x=35, y=15)
activeWorkspaceNumber.place(x=135, y=15)
workspace3Number.place(x=237, y=15)
hoveringWorkspaceNumber.place(x=335, y=15)
workspace5Number.place(x=437, y=15)

canvas.place(relx=0, rely=0)

window.mainloop()