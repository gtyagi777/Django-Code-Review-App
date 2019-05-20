from os import listdir
from os import walk
import app_cmp.config as cfg


class searchInFiles:

    def __init__(self, _args, _path):
        self.searchTextList = _args
        self.searchFileList = _path
        self.searchTextDict = {}

    def getValues(self):

        for text in self.searchTextList:
            self.searchTextDict[text] = list()

        for _file in self.searchFileList:
            content = open(_file)
            line = content.readline()
            lineNumber = 1
            while(line != ""):
                for text in self.searchTextList:
                    if not line.find(text) == -1:
                        self.searchTextDict[text].append(
                                [root, file, lineNumber, line])
                line = content.readline()
                lineNumber += 1

            content.close()

            return self.searchTextDict

        def handleDb(self):
            import django
            django.setup()


def main():
    x = searchInFiles(["input", "path"]).getValues()


if __name__ == "__main__":
    main()
