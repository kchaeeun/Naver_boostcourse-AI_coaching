#파일의 경로를 file_path로 설정
#ex) file_path = "./data-01-test-score.csv"

import csv
import pprint

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
            return self.read_list
            
    def merge_list(self):
        sum_list = []
        for line in self.read_list:
            s_list = sum(line)
            sum_list.append(s_list)
        return sum_list

read_csv = ReadCSV(file_path)
pprint.pprint(read_csv.read_file())
print(read_csv.merge_list())















           
