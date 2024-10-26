from tkinter import *
from tkinter import filedialog as fd
from tkinter import ttk
import requests


def upload():
    file_path = fd.askopenfilename()
    if file_path:
        files = {'file': open(file_path, 'rb')}
        response = requests.post('https://file.io', files=files)
        if response.status_code == 200:
            link = response.json()['link']
            entry.insert(0, link)


window = Tk()
window.title("Сохранение файлов в облаке")
window.geometry("400x200")

button = ttk.Button(window, text="Загрузить файл", command=upload)
button.pack()

entry = ttk.Entry(window)
entry.pack()

window.mainloop()