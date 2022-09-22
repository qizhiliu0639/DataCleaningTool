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

def extract_offer_information(item):
    if item[0].lower() == 'o' or item[0].lower() == 'o':
        item[0] = 1
    else:
        item[0] = 0
    return item


def run():
    csvFile = open("../Resource/Result_8.csv", "r", encoding='utf-8')
    reader = csv.reader(csvFile)

    outputFile = open("../Output/NTU_CCA.csv","w", encoding='utf-8')
    writer = csv.writer(outputFile)

    m = create_mapping()

    d_1 = set()
    d_6 = set()
    for item in reader:
        # print(item)
        # 忽略第一行
        # print(reader.line_num)
        if reader.line_num == 1:
            writer.writerow(item)
            continue
        d_1.add(item[4])
        if item[2][:7] == 'Nanyang' and item[3][0].lower() == 'c':
            print(item)
            item = extract_offer_information(item)
            writer.writerow(item)


    csvFile.close()
    print(d_6)
    print(d_1)

if __name__ == "__main__":
    run()