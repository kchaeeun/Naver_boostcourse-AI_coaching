import csv

file_path = "./data-01-test-score.csv"

class ReadCSV():
    def __init__(self, file_path):
        self.file_path = file_path

    def read_file(self):
        self.read_list = []
        with open(file_path, 'r', encoding='cp949') as file:
            read_csv = csv.reader(file)
            for row in read_csv:
                self.read_list.append(list(map(int,row)))
            
    def merge_list(self):
        avg_list = []
        for line in self.read_list:
            a,b,c,d = line
            avg = ((a+b+c+d)/4)
            avg_list.append(avg)
        avg_list.sort()
        return avg_list

read_csv = ReadCSV(file_path)
read_csv.read_file()
print(read_csv.merge_list())