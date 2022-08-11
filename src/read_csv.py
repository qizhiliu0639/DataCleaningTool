import csv



def run():
    csvFile = open("../Resource/Result_8.csv", "r")
    reader = csv.reader(csvFile)

    outputFile = open("../Output/output.csv","w")
    writer = csv.writer(outputFile)

    d = {
        "信息工程": "Engineer",

    }
    result = {}
    for item in reader:
        # 忽略第一行
        # print(reader.line_num)
        # if reader.line_num == 1:
        #     continue
        if item[6] == "信息工程":
            item[6] = "Engineer"
        writer.writerow(item)

    csvFile.close()
    print(result)

if __name__ == "__main__":
    run()