from os import listdir

path = "C:\\Users\\tyagi\\Desktop\\Language\\Python\\Algorithm\\"


class getResult:

    def __init__(self, path, args, exts):
        self.path = path
        self.args = args
        self.exts = exts
        
    for fileName in listdir(path):
        xx = str(fileName).spilt(".")[-1]
        print[xx]
        if fileName.endswith(".py"):
            print("\nFile name: " + fileName)
            file = open(path + fileName)
            line = file.readline()
            
            lineNumber = 1
            
            while(line != ''):
                if not line.find(text) == -1:
                    print(lineNumber)
                
                line = file.readline()
                lineNumber += 1
            
            file.close()


x = getResult(path, "Bir",".py" )