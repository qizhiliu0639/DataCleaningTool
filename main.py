# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import tkinter as tk  # 使用Tkinter前需要先导入
import os
from tkinter import filedialog, dialog
window = tk.Tk()
window.title('数据清洗工具')
window.geometry('600x400')
text1 = tk.Text(window, width=50, height=10, bg='orange', font=('Arial', 12))
text1.pack()

def get_mapping(key, value):
    key_2 = key.split(",")
    value_2 = value.split(",")
    d = {}
    if len(key_2) != value_2:
        return d

    for i in range(len(key_2)):
        d[key_2[i]] = value_2[i]

    text1.insert(str(d))
    print(d)
    return d



# def open_file():
#     '''
#         打开文件
#         :return:
#         '''
#     global file_path
#     global file_text
#     file_path = filedialog.askopenfilename(title=u'选择文件', initialdir=(os.path.expanduser('H:/')))
#     print('打开文件：', file_path)
#     if file_path is not None:
#         with open(file=file_path, mode='r+', encoding='utf-8') as file:
#             file_text = file.read()

def run():

    e1 = tk.Label(window, text='key', font=('Arial', 12), width=50, height=2)
    e2 = tk.Entry(window, show=None, font=('Arial', 14))
    e3 = tk.Label(window, text='value', font=('Arial', 12), width=50, height=2)
    e4 = tk.Entry(window, show=None, font=('Arial', 14))
    # e5 = tk.Label(window, text='password', font=('Arial', 12), width=50, height=2)
    # e6 = tk.Entry(window, show=None, font=('Arial', 14))
    e1.pack()
    e2.pack()
    e3.pack()
    e4.pack()
    # e5.pack()
    # e6.pack()


    # bt1 = tk.Button(window, text='打开文件', width=15, height=2, command=open_file)
    # bt1.pack()
    bt2 = tk.Button(window, text='test', width=15, height=2, command=get_mapping(e2.get(), e4.get()))
    bt2.pack()

    window.mainloop()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    run()
