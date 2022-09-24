from dirWatcher import watcherFunction
import PySimpleGUI as sg
import multiprocessing as mp
from modifyConfig import modifyConfig, modifyAliveStatus
def main(watcherOngoing):
    subLayOut = [
    sg.Text("Download Folder"),
    sg.In(size=(25, 1), enable_events=True, key="-FOLDER-"),
    sg.FolderBrowse(),
    sg.Button("OK"),
    sg.Button("STOP"),
    ]

    window = sg.Window(title="AutoOpen", layout=[[subLayOut]], margins=(100,50))

    ongoing = True

    while ongoing == True:
        event, values = window.read(timeout=300)
        if event == "OK":
            print(values["-FOLDER-"])
            modifyConfig(values["-FOLDER-"])
            watcherOngoing.value = 1
        if event == "STOP":
            watcherOngoing.value = 0
        if event == sg.WIN_CLOSED:
            watcherOngoing.value = 0
            modifyAliveStatus("dead")
            break
 
if __name__ == '__main__':
    modifyAliveStatus("alive")
    watcherOngoing = mp.Value('i',0)
    proc2 = mp.Process(target=watcherFunction, args=(watcherOngoing, ))
    proc2.start()
    proc1 = mp.Process(target=main, args=(watcherOngoing,  ))
    proc1.start()
    proc1.join()            
    proc2.join()