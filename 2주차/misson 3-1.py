#파일의 경로를 file_path로 설정
# ex) file_path = "./data-01-test-score.csv"
def read_file(file_path):

    with open(file_path) as file:
        read_csv = file.readlines()
    read_csv = [line.rstrip('\n') for line in lines]
    import pprint
    pprint.pprint(lines)

file_path = "./data-01-test-score.csv"
read_csv = ReadCSV(filepath)
print(read_csv.read_file())
