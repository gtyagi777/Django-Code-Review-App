from os import listdir
from os import walk
import app_cmp.config as cfg
import json


class getResult:

    def __init__(self, _args):
        self.searchTextList = _args
        self.searchTextDict = {}

    def getValues(self):

        searchTextList = self.searchTextList

        for text in self.searchTextList:
            self.searchTextDict[text] = list()

        for root, directories, files in walk(cfg.path):
            for file in files:
                ext = file.split(".")[1]

                if ext in cfg._config["ext"]:
                    if not root.endswith("\\"):
                        root += "\\"
                    content = open(root + file)

                    line = content.readline()
                    lineNumber = 1
                    while(line != ""):
                        for text in self.searchTextList:
                            if not line.find(text) == -1:
                                self.searchTextDict[text].append(
                                    [root, file, lineNumber])
                        line = content.readline()
                        lineNumber += 1

                    content.close()
            return self.searchTextDict

        def handleDb(self):
            import django
            django.setup()


def main():
    x = getResult(["input"]).getValues()
    print(json.dumps(x, indent=4))


if __name__ == "__main__":
    main()
