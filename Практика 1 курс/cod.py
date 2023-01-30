import requests
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import *
from tkinter import ttk
import tkinter.font as tkFont
from fake_useragent import UserAgent
import webbrowser


def get_matters():
    data = ['programming', 'data-science', 'technology', 'self-improvement',
            'writing', 'relationships', 'machine-learning', 'productivity', 'politics']
    return data


def get_content(url):
    headers = {
        'User-Agent': UserAgent().ff}
    page = requests.get(
        f'https://medium.com/tag/{url}/archive/2023/01/23', headers=headers)
    soup = BeautifulSoup(page.text, 'html.parser')
    all = soup.find_all(
        'div', 'postArticle postArticle--short js-postArticle js-trackPostPresentation js-trackPostScrolls')
    data = dict()
    for i in all:
        try:
            title = i.find('h3').text
            page_url = i.find_all('a')[2]['href']
            artist = i.find(
                'div', 'postMetaInline postMetaInline-authorLockup ui-captionStrong u-flex1 u-noWrapWithEllipsis').find('a').text
            read_time = i.find('span', 'readingTime')['title']
            data[title] = {'url': page_url,
                           'artist': artist, 'time': read_time}
        except:
            pass

    return data


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.url = 'https://medium.com/'
        self.title(self.url)
        self.matters = get_matters()

        width = 898
        height = 521
        screenwidth = self.winfo_screenwidth
        screenheight = self.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height,
                                    (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(alignstr)
        self.resizable(width=False, height=False)

        self.GListBox_64 = Listbox(self)
        self.GListBox_64["borderwidth"] = "1px"
        ft = tkFont.Font(family='Arial', size=10)
        self.GListBox_64["bg"] = "#FFEFD5"
        self.GListBox_64["font"] = ft
        self.GListBox_64["fg"] = "#000000"
        self.GListBox_64["justify"] = "left"
        self.GListBox_64.place(x=10, y=80, width=326, height=364)
        self.GListBox_64.bind('<<ListboxSelect>>', self.Get_Info)

        self.var = tk.StringVar(self, self.matters[0])
        GListBox_277 = ttk.Combobox(self, textvariable=self.var)
        ft = tkFont.Font(family='Arial', size=10)
        GListBox_277["font"] = ft
        GListBox_277["values"] = self.matters
        GListBox_277["justify"] = "center"
        GListBox_277.place(x=10, y=20, width=322, height=30)

        self.var_time = tk.StringVar(self, 'None select')
        GListBox_278 = ttk.Combobox(self, textvariable=self.var_time)
        ft = tkFont.Font(family='Arial', size=10)
        GListBox_278["font"] = ft
        GListBox_278["values"] = [i for i in range(1, 11)]
        GListBox_278["justify"] = "center"
        GListBox_278.place(x=380, y=270, width=500, height=40)

        filter_GButton_887 = tk.Button(self)
        filter_GButton_887["bg"] = "#4682B4"
        ft = tkFont.Font(family='Arial', size=10)
        filter_GButton_887["font"] = ft
        filter_GButton_887["fg"] = "#000000"
        filter_GButton_887["justify"] = "center"
        filter_GButton_887["text"] = "Filter"
        filter_GButton_887.place(x=380, y=320, width=500, height=40)
        filter_GButton_887["command"] = self.Filter

        GButton_887 = tk.Button(self)
        GButton_887["bg"] = "#4682B4"
        ft = tkFont.Font(family='Arial', size=10)
        GButton_887["font"] = ft
        GButton_887["fg"] = "#000000"
        GButton_887["justify"] = "center"
        GButton_887["text"] = "GET CONTENT"
        GButton_887.place(x=10, y=460, width=321, height=36)
        GButton_887["command"] = self.GButton_887_command

        GLabel_590 = tk.Label(self, text='Title:', anchor=E)
        ft = tkFont.Font(family='Arial', size=10)
        GLabel_590["bg"] = "#556B2F"
        GLabel_590["font"] = ft
        GLabel_590["fg"] = "#000000"
        GLabel_590["justify"] = "left"
        GLabel_590.place(x=380, y=20, width=130, height=30)

        GLabel_591 = tk.Label(self, text='Artist:', anchor=E)
        ft = tkFont.Font(family='Arial', size=10)
        GLabel_591["bg"] = "#556B2F"
        GLabel_591["font"] = ft
        GLabel_591["fg"] = "#000000"
        GLabel_591["justify"] = "left"
        GLabel_591.place(x=380, y=100, width=130, height=30)

        GLabel_592 = tk.Label(self, text='Time for reading:', anchor=E)
        ft = tkFont.Font(family='Arial', size=10)
        GLabel_592["bg"] = "#556B2F"
        GLabel_592["font"] = ft
        GLabel_592["fg"] = "#000000"
        GLabel_592["justify"] = "left"
        GLabel_592.place(x=380, y=180, width=130, height=30)

        self.GLabel_500 = tk.Label(self, text='-', anchor=W)
        ft = tkFont.Font(family='Arial', size=10)
        self.GLabel_500["bg"] = "#556B2F"
        self.GLabel_500["font"] = ft
        self.GLabel_500["fg"] = "#000000"
        self.GLabel_500["justify"] = "left"
        self.GLabel_500.place(x=550, y=20, width=300, height=30)

        self.GLabel_501 = tk.Label(self, text='-', anchor=W)
        ft = tkFont.Font(family='Arial', size=10)
        self.GLabel_501["bg"] = "#556B2F"
        self.GLabel_501["font"] = ft
        self.GLabel_501["fg"] = "#000000"
        self.GLabel_501["justify"] = "left"
        self.GLabel_501.place(x=550, y=100, width=130, height=30)

        self.GLabel_502 = tk.Label(self, text='-', anchor=W)
        ft = tkFont.Font(family='Arial', size=10)
        self.GLabel_502["bg"] = "#556B2F"
        self.GLabel_502["font"] = ft
        self.GLabel_502["fg"] = "#000000"
        self.GLabel_502["justify"] = "left"
        self.GLabel_502.place(x=550, y=180, width=130, height=30)

        GButton_100 = Button(self, text='View page', font="arial, 9")
        GButton_100 = tk.Button(self)
        GButton_100["bg"] = "#4682B4"
        ft = tkFont.Font(family='Arial', size=10)
        GButton_100["font"] = ft
        GButton_100["fg"] = "#000000"
        GButton_100["justify"] = "center"
        GButton_100["text"] = "GET CONTENT"
        GButton_100.place(x=380, y=220, width=500, height=40)
        GButton_100["command"] = self.Read

    def Filter(self):
        t = int(self.var_time.get())
        data = dict()
        for key, value in self.content.items():
            if int(value['time'].split(' ')[0]) < t:
                data[key] = value

        self.GListBox_64.delete(0, END)
        [self.GListBox_64.insert(0, i) for i in list(data.keys())]

    def Read(self):
        try:
            url = self.content[self.GListBox_64.get(
                self.GListBox_64.curselection()[0])]['url']
            webbrowser.open_new(url)
        except IndexError:
            print("Слишком большое кол-во запросов")

    def GButton_887_command(self):
        matter = self.var.get()
        self.content = get_content(matter)
        self.GListBox_64.delete(0, END)
        [self.GListBox_64.insert(0, i) for i in list(self.content.keys())]

    def Get_Info(self, event):
        selected = self.GListBox_64.get(self.GListBox_64.curselection()[0])
        self.GLabel_500['text'] = selected
        self.GLabel_501['text'] = self.content[selected]['artist']
        self.GLabel_502['text'] = self.content[selected]['time']


if __name__ == '__main__':
    root = App()
    root['bg'] = "#808000"
    root.mainloop()
