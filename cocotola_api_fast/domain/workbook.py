class Workbook(object):
    def __init__(self, name: str, lang2: str):
        self.__name = name
        self.__lang2 = lang2

    @property
    def name(self):
        return self.__name

    @property
    def lang2(self):
        return self.__lang2
