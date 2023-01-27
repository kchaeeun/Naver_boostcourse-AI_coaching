#파일의 경로를 file_path로 설정
# ex) file_path = "./data-01-test-score.csv"
import csv
import pprint

file_path = './data-01-test-score.csv'

def read_file(file_path):
    read_list = []
    with open(file_path, 'r', encoding='cp949') as file: #with를 사용하면 저절로 닫침(메모리 누수x)
        read_csv = csv.reader(file)
        for row in read_csv:
            read_list.append(list(row))
            
    return read_list

pprint.pprint(read_file(file_path))
