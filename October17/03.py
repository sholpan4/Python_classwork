def read_large_file(file):
    with open(file, 'r', encoding='utf-8') as myFile:
        print(dir(myFile))  #list of mehods an svoisvt from object =list[str]
        print(myFile.__dict__)
        # for line in myFile:
        line = '\n'
        while line != '':  #while there is not the end of the string
            line = myFile.readline()
            yield line

def process_line(line):
    print(line)

for line in read_large_file("big_data.txt"):
    process_line(line)