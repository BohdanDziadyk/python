class File:
    def __init__(self, *args):
        self.filenames = []
        self.args = args
        for a in args:
            self.filenames.append(a)
        print(self.filenames)

    def creator(self):
        for f in self.filenames:
            f = open(mode="w", file=f"{f}.txt")

    def writer(self, text):
        for f in self.filenames:
            print(f)
        filename = input("filename:")
        for f in self.filenames:
            if f == filename:
                f = open(mode="w", file=f"{f}.txt")
                f.write(text)

    def explorer(self):
        for f in self.filenames:
            print(f)
        filename = input("filename:")
        for f in self.filenames:
            if f == filename:
                f = open(mode="r", file=f"{f}.txt")
                print(f.read())

    def trade_files(self,filename_1,filename_2):
        for f in self.filenames:
            if f == filename_1:
                file1 = open(mode="rw", file=f"{f}.txt")
        for f in self.filenames:
            if f == filename_2:
                file2 = open(mode="rw", file=f"{f}.txt")
        str1 = file1.read()
        print(str1)
        str2 = file2.read()
        print(str2)
        file1.write(str2)
        print(file1.read())
        file2.write(str1)
        print(file2.read())


file = File("file1", "file2", "file3")
file.creator()
file.writer("test text")
file.explorer()
file.writer("test test new")
file.trade_files("file1","file2")
