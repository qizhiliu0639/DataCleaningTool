import csv



def run():
    csvFile = open("../Resource/Result_8.csv", "r")
    reader = csv.reader(csvFile)

    result = {}
    for item in reader:
        # 忽略第一行
        if reader.line_num == 1:
            continue
        print(item)

    csvFile.close()
    print(result)

if __name__ == "__main__":
    run()