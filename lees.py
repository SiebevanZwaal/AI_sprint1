import json
from tkinter import *
from tkinter import Label


def lees():
    f = open('data/steam.json', "r")

    data = json.loads(f.read())

    woordenboeken = {}
    for i in data:
        woordenboeken[int(i['appid'] / 10)] = {
            'appid': i['appid'],
            'name': i['name'],
            'release_date': i['release_date'],
            'english': i['english'],
            'developer': i['developer'],
            'publisher': i['publisher'],
            'platforms': i['platforms'],
            'required_age': i['required_age'],
            'categories': i['categories'],
            'genres': i['genres'],
            'steamspy_tags': i['steamspy_tags'],
            'achievements': i['achievements'],
            'positive_ratings': i['positive_ratings'],
            'negative_ratings': i['negative_ratings'],
            'average_playtime': i['average_playtime'],
            'median_playtime': i['median_playtime'],
            'owners': i['owners'],
            'price': i['price']
        }

    f.close()
    return woordenboeken


def raampje():
    global window
    global fr1
    window = Tk()
    window['bg'] = 'black'
    fr1 = Frame(master=window, bg='black')
    fr1.pack()
    img = PhotoImage(file='steamlogo.gif')
    lblogo= Label(master=fr1, image=img, border=0)
    lblogo.pack()

def naam1():
    lb1 = Label(master=fr1, text=games[1]['name'], fg='white', bg='black')
    lb1.pack(pady=10)
    window.mainloop()

def sorteerbeer(wb):
    return wb



games = sorteerbeer(lees())
raampje()
naam1()

