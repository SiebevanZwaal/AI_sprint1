import json
from tkinter import *
from tkinter import Label


def lees():
    f = open('data/steam.json', "r")

    data = json.loads(f.read())
    f.close()
    return data


def raampje(game):
    window = Tk()
    window['bg'] = 'black'
    fr1 = Frame(master=window, bg='black')
    fr1.pack()
    img = PhotoImage(file='steamlogo.gif')
    lblogo= Label(master=fr1, image=img, border=0)
    lblogo.pack()
    lb1 = Label(master=fr1, text=game, fg='white', bg='black')
    lb1.pack(pady=10)
    window.mainloop()



def sorteerbeer(wb,sortop):
    return sorted(wb, key=lambda i: i[sortop])


def main():
    games =sorteerbeer(lees(),'appid')
    for game in games:
        raampje(game['name'])
        break


if __name__ == '__main__':
    main()
