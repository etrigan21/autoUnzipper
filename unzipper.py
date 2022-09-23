import zipfile, os


def checkForZipAndUnzip(arr):
    for i in arr:
        print(i)
        if i.endswith('.zip'):
            endPointDir = "./" + i.replace(".zip","")
            exist = os.path.isdir(endPointDir)
            if exist:
                endPointDir = checkIfDirExists(endPointDir)
            os.mkdir(endPointDir)
            with zipfile.ZipFile(i, "r") as zip_ref:
                zip_ref.extractall(endPointDir)

def checkIfDirExists(endPointDir):
    notUnique = True
    counter = 1
    newName = endPointDir
    while notUnique:
        newName = endPointDir + "(" + str(counter) +")"
        notUnique = os.path.isdir(newName)
        counter+=1
    print(newName)
    return newName