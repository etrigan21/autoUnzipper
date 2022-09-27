import zipfile, os


def checkForZipAndUnzip(arr):
    for i in arr:
        print(i)
        if i.endswith('.zip'):
            endPointDir = "./" + i.replace(".zip","")
            exist = os.path.isdir(endPointDir)
            if exist:
                endPointDir = checkIfDirExists(endPointDir)
            try: 
                os.mkdir(endPointDir)
                with zipfile.ZipFile(i, "r") as zip_ref:
                    zip_ref.extractall(endPointDir)
                os.remove(i)
            except Exception as e:
                print("Something went wrong")
                print("exception", e)

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