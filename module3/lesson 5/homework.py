class MyFile:
    def __init__(self, file_name, mode, encoding='utf-8'):
        self.file_name = file_name
        self.mode = mode
        self.encoding = encoding

    def __enter__(self):
        self.file = open(self.file_name, self.mode, encoding=self.encoding)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()


with MyFile('file.txt', 'w') as file:
    content = file.write('Hello')
    # print(content)

class Iterator:
    def __init__(self):
        self.num = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.num += 1
        return self.num

for i in Iterator():
    print(i)