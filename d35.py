def saveList(myList, myFilename):
    outputFile = open(myFilename, "w")
    for item in myList:
        outputFile.write(item + "\n")
    outputFile.close()

def loadList(myFilename):
    newList = []
    inputFile = open(myFilename, "r")
    for line in inputFile:
        newList.append(line)
    return newList

List = ["1", "2", "3", "4"]
print(saveList(List, "list.txt"))
print(loadList("list.txt"))
print(saveList(List, "list.txt"))
print(loadList("list.txt"))
