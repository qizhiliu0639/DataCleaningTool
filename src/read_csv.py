import csv


class mapping:
    def __init__(self):
        self.d = {}

    def add(self, key ,value):
        self.d[key] = value

def create_mapping():
    m = mapping()
    d = {"信息工程": "EE",
         "Software Engineer":"Engineer",
         "信息系统与信息管理":"IS"}
    for i in d:
        m.add(i, d[i])
    return m

def run():
    csvFile = open("../Resource/Result_8.csv", "r")
    reader = csv.reader(csvFile)

    outputFile = open("../Output/output.csv","w")
    writer = csv.writer(outputFile)

    m = create_mapping()

    d_1 = set()
    d_6 = set()
    for item in reader:
        # 忽略第一行
        # print(reader.line_num)
        if reader.line_num == 1:
            writer.writerow(item)
            continue
        d_1.add(item[0])
        d_6.add(item[6])
        if item[6] in m.d:
            item[6] = m.d[item[6]]
        else:
            item[6] = "other"

        writer.writerow(item)


    csvFile.close()
    print(d_6)
    print(d_1)

if __name__ == "__main__":
    run()