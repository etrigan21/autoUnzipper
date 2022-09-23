from dirWatcher import watcherFunction
import PySimpleGUI as sg


subLayOut = [
    sg.Text("Download Folder"),
    sg.In(size=(25, 1), enable_events=True, key="-FOLDER-"),
    sg.FolderBrowse(),
    sg.Button("OK"),
    sg.Button("STOP")
]

window = sg.Window(title="AutoOpen", layout=[[subLayOut]], margins=(100,50))

ongoing = True

while True:
    event, values = window.read()
    if event == "-FOLDER-":
        print(values["-FOLDER-"])
    if event == "OK":
        print(values["-FOLDER-"])
        while ongoing:
            watcherFunction(values["-FOLDER-"])
    if event == "STOP":
        print("kill watcher loop")
        ongoing = False