import json
from tkinter import *
from matplotlib import pyplot as plt



def lees():
    '''reads json file with game data'''
    f = open('steam.json', "r")
    data = json.loads(f.read())
    f.close()
    return data

def kiesraam():
    '''creates a tkinter window where user can choose what he wants to sort the gameslist on'''
    global window
    global firstvalue
    global secondvalue
    window = Tk()
    window['bg'] = 'black'
    window.geometry("500x140")
    Welkomlabel=Label(window,text='Welkom bij het Steamlibrary keuzemenu\nKies hier wat u van de data wilt zien en welk sorteer algoritme u wilt gebruiken\n',bg='black',fg='white',font='DejaVu 10')
    kieslijst =[
    "appid",
    "name",
    "release_date",
    "english",
    "developer",
    "publisher",
    "platforms",
    "required_age",
    "categories",
    "genres",
    "steamspy_tags",
    "achievements",
    "positive_ratings",
    "negative_ratings",
    "average_playtime",
    "median_playtime",
    "owners",
    "price"
    ]

    algoritmelijst = [
    "bubble(kost 5.5 minuten)",
    "Quicksort iterative",
    "Merge sort"
    ]

    firstvalue =StringVar(window)
    firstvalue.set(kieslijst[4])
    secondvalue = StringVar(window)
    secondvalue.set(algoritmelijst[2])
    kieslabel = OptionMenu(window, firstvalue, *kieslijst)
    kieslabel['font'] ='DejaVu 10'
    algoritmelabel = OptionMenu(window, secondvalue, *algoritmelijst)
    algoritmelabel['font'] = 'DejaVU 10'
    doorknop =Button(window, text='lijst met games gesorteerd op bovenstaand item en algortime ophalen',command= lijstophalen,font='DejaVu 10')
    Welkomlabel.pack()
    kieslabel.pack()
    algoritmelabel.pack()
    doorknop.pack()
    window.mainloop()


def lijstophalen():
    '''collects item that the user selected in "Kiesraam"'''
    global sortop
    global algoritme
    sortop = firstvalue.get()
    algoritme = secondvalue.get()
    if algoritme == "bubble(kost 5.5 minuten)":
        algoritme = 1
    elif algoritme == "Merge sort":
        algoritme = 3
    else:
        algoritme =2
    window.destroy()


def terugnaarkies():
    '''opens choosing window again'''
    global omgekeerd
    global leeslijst0
    global listy
    global window

    if not search:
        window.destroy()
    else:
        window.destroy()
        swindow.destroy()

    kiesraam()
    leeslijst0 = lees()
    omgekeerd = False
    if algoritme == 3:
        merge_sort(leeslijst0, 0, len(leeslijst0) - 1)
        if omgekeerd:
            leeslijst0.reverse()
    elif algoritme == 2:
        qsI(leeslijst0, 0, len(leeslijst0) - 1)
    else:
        sorteerbeer(leeslijst0)
    listy = []
    for game in leeslijst0:
        listy.append([game['name'], game[sortop]])
    window = Tk()
    window['bg'] = 'black'
    naam1()



def naam1():
    '''initiates the tkinter window to display games and steam logo'''
    global img
    global fr1
    global fr2
    global gamescount

    fr1 = Frame(master=window, bg='black')
    fr1.grid(row=0,column=0)#.pack()
    fr2 =Frame(master=window, bg='black')
    fr2.grid(row=1,column=0)#.pack()
    img = PhotoImage(file='steamlogo.gif')
    lblogo = Label(master=fr1, image=img, border=0)
    lblogo.grid(row=0,column=0,columnspan=2)
    gamescount = 0
    createlabels(listy)
    statknop = Button(master=fr2,text='klik hier om de statistiek te bekijken',command=statistiek,font='DejaVu 10')
    statknop.grid(row=1,column=0,columnspan=2)
    verderbutton = Button(master=fr2, text="volgende vijf games =>", command=vijfgamesverder,font='DejaVu 10')
    verderbutton.grid(row=0,column=1)
    terugbutton = Button(master=fr2, text="<= vorige vijf games", command=vijfgamesterug,font='DejaVu 10')
    terugbutton.grid(row=0,column=0)
    zoekknop = Button(fr2,text='klik hier om te zoeken op gegevens',command=zoekraam,font='DejaVu 10')
    zoekknop.grid(row=2,column=0,columnspan=2)
    rechoosebutton=Button(master=fr2,text='klik hier om andere data te selecteren',command=terugnaarkies,font='DejaVu 10')
    rechoosebutton.grid(row=3,column=0,columnspan=2)

def vijfgamesverder():
    '''is used when "verderbutton" is pressed to display five next games'''
    global gamescount
    gamescount +=5
    weergeven(listy, gamescount)
    window.mainloop()

def vijfgamesterug():
    '''is used when "terugbutton" is pressed to display five last games'''
    global gamescount
    gamescount -=5
    weergeven(listy, gamescount)
    window.mainloop()

def createlabels(lst1):
    '''creates labels which contain first five games'''
    global lb1
    global lb2
    global lb3
    global lb4
    global lb5
    global lb1a
    global lb2a
    global lb3a
    global lb4a
    global lb5a

    if omgekeerd:
        lbh = Label(master=fr1, text=f'Dit zijn vijf games descending gesorteerd op {sortop}:\n',
                    fg='white', bg='black',font='DejaVu 10')
        lbh.grid(row=1,column=0,columnspan=2)#.pack()


    else:
        lbh = Label(master=fr1, text=f'Dit zijn vijf games ascending gesorteerd op {sortop}:\n',
                    fg='white', bg='black',font='DejaVu 10')
        lbh.grid(row=1,column=0,columnspan=2)#.pack()


    lb1 = Label(master=fr1, text=str(lst1[0][0]), fg='white', bg='black',font='DejaVu 10')
    lb2 = Label(master=fr1, text=str(lst1[1][0]), fg='white', bg='black',font='DejaVu 10')
    lb3 = Label(master=fr1, text=str(lst1[2][0]), fg='white', bg='black',font='DejaVu 10')
    lb4 = Label(master=fr1, text=str(lst1[3][0]), fg='white', bg='black',font='DejaVu 10')
    lb5 = Label(master=fr1, text=str(lst1[4][0]), fg='white', bg='black',font='DejaVu 10')
    if sortop != 'price':
        lb1a = Label(master=fr1, text=str(lst1[0][1]), fg='white', bg='black',font='DejaVu 10')
        lb2a = Label(master=fr1, text=str(lst1[1][1]), fg='white', bg='black',font='DejaVu 10')
        lb3a = Label(master=fr1, text=str(lst1[2][1]), fg='white', bg='black',font='DejaVu 10')
        lb4a = Label(master=fr1, text=str(lst1[3][1]), fg='white', bg='black',font='DejaVu 10')
        lb5a = Label(master=fr1, text=str(lst1[4][1]), fg='white', bg='black',font='DejaVu 10')
    else:
        lb1a = Label(master=fr1, text='€'+str(lst1[0][1]), fg='white', bg='black',font='DejaVu 10')
        lb2a = Label(master=fr1, text='€'+str(lst1[1][1]), fg='white', bg='black',font='DejaVu 10')
        lb3a = Label(master=fr1, text='€'+str(lst1[2][1]), fg='white', bg='black',font='DejaVu 10')
        lb4a = Label(master=fr1, text='€'+str(lst1[3][1]), fg='white', bg='black',font='DejaVu 10')
        lb5a = Label(master=fr1, text='€'+str(lst1[4][1]), fg='white', bg='black',font='DejaVu 10')
    lb1.grid(row=2,column=0)
    lb2.grid(row=3,column=0)
    lb3.grid(row=4,column=0)
    lb4.grid(row=5,column=0)
    lb5.grid(row=6,column=0)
    lb1a.grid(row=2, column=1)
    lb2a.grid(row=3, column=1)
    lb3a.grid(row=4, column=1)
    lb4a.grid(row=5, column=1)
    lb5a.grid(row=6, column=1)
    if algoritme == 2 or algoritme == 3:
        if omgekeerd:
            omdraaiknop = Button(master=fr1, text='Weergeef de games in ascending volgorde', command=omdraaien,font='DejaVu 10')
            omdraaiknop.grid(row=7,column=0,columnspan=2)

        else:
            omdraaiknop = Button(master=fr1, text='Weergeef de games in descending volgorde', command=omdraaien,font='DejaVu 10')
            omdraaiknop.grid(row=7,column=0,columnspan=2)



def weergeven(lst1,count):
    '''changes text in labels to a certain five games depending on count'''
    for i in range(0,5):
        if len(lst1[count+i][0]) > 49:
            lst1[count+i][0] = lst1[count+i][0][:46]+'...'
        else:
            lst1[count+i][0] =lst1[count+i][0] + ' '* (49 - len(lst1[count+i][0]))
    lb1["text"] = str(lst1[count][0])
    lb2["text"] = str(lst1[count+1][0])
    lb3["text"] = str(lst1[count+2][0])
    lb4["text"] = str(lst1[count+3][0])
    lb5["text"] = str(lst1[count+4][0])
    if sortop != 'price':
        lb1a["text"] = str(lst1[count][1])
        lb2a["text"] = str(lst1[count + 1][1])
        lb3a["text"] = str(lst1[count + 2][1])
        lb4a["text"] = str(lst1[count + 3][1])
        lb5a["text"] = str(lst1[count + 4][1])
    else:
        lb1a["text"] = '€'+str(lst1[count][1])
        lb2a["text"] = '€'+str(lst1[count + 1][1])
        lb3a["text"] = '€'+str(lst1[count + 2][1])
        lb4a["text"] = '€'+str(lst1[count + 3][1])
        lb5a["text"] = '€'+str(lst1[count + 4][1])
    lb1.grid(row=2, column=0)
    lb2.grid(row=3, column=0)
    lb3.grid(row=4, column=0)
    lb4.grid(row=5, column=0)
    lb5.grid(row=6, column=0)
    lb1a.grid(row=2, column=1)
    lb2a.grid(row=3, column=1)
    lb3a.grid(row=4, column=1)
    lb4a.grid(row=5, column=1)
    lb5a.grid(row=6, column=1)

def omdraaien():
    '''changes sorting from asc to desc or from desc to asc depending on whether "omgekeerd" contains False or True and sorts again'''
    global omgekeerd
    global listy
    global window
    if omgekeerd == False:
        omgekeerd = True
    else:
        omgekeerd = False

    if omgekeerd:
        print('lijst word descending geprint')
    else:
        print('lijst word ascending geprint')

    window.destroy()
    leeslijst1 = lees()
    if algoritme ==3:
        merge_sort(leeslijst1, 0, len(leeslijst1) - 1)
        if omgekeerd:
            leeslijst1.reverse()
    elif algoritme == 2:
        qsI(leeslijst1, 0, len(leeslijst1) - 1)
    else:
        sorteerbeer(leeslijst1)
    listy = []
    for game in leeslijst1:
        listy.append([game['name'], game[sortop]])

    window = Tk()
    window['bg'] = 'black'
    naam1()
    window.mainloop()

def zoekraam():
    global swindow
    global search
    global invoerzoek
    search = True
    swindow = Tk()
    swindow['bg'] = 'black'
    swindow.geometry("600x500")
    zoeklabel = Label(swindow, text='U kunt nu alleen zoeken op ' + sortop,font='DejaVu 10')
    zoeklabel.grid(row=0, column=0)
    invoerzoek = Entry(swindow,text='enter what you want the '+ str(sortop) + ' to contain',font='DejaVu 10')
    invoerzoek.grid(row=0,column=1)
    zoekknop = Button(swindow,text='klik hier om te zoeken naar bovenstaande gegevens',command=zoeken,font='DejaVu 10')
    zoekknop.grid(row=1,column=0,columnspan=2)
    terugkiesknop=Button(swindow,text='klik hier om op andere data te zoeken',command=terugnaarkies,font='DejaVu 10')
    terugkiesknop.grid(row=2,column=0,columnspan=2)
    swindow.mainloop()


def zoeken():
    global zoekframeingebruik
    global zoekframe
    global zoeklijst
    target = invoerzoek.get()
    if sortop == 'price':
        target = float(target)
    elif sortop == 'appid' or sortop == 'english' or sortop == 'required_age' or sortop =='achievements' or sortop == 'positive_ratings' or sortop =='negative_ratings' or sortop == 'average_playtime' or sortop == 'median_playtime':
        target = int(target)
    zoeklijst = []

    if zoekframeingebruik:
        zoekframe.destroy()
    zoekframe = Frame(swindow,bg='black')
    zoekframe.grid(row=3,column=0,columnspan=2)
    zoekframeingebruik = True
    if binary_search_recursive(leeslijst0,target):
        lcount = 0
        for i in leeslijst0:

            if i[sortop] == target:
                Label(zoekframe, text=i['name'],bg= 'black',fg ='white',font='DejaVu 10').grid(row=lcount, column=0)
                Label(zoekframe, text=i[sortop],bg= 'black',fg ='white',font='DejaVu 10').grid(row=lcount, column=1)
                lcount += 1



def binary_search_recursive(lst, target):
    #global zoeklijst
    if len(lst) == 0:
        return False
    else:
        mini = lst.index(lst[0])
        maxi = lst.index(lst[-1])
        mid = int((maxi + mini) / 2)

        if target == lst[mid][sortop]:
            return True
        elif target < lst[mid][sortop]:
            return binary_search_recursive(lst[:mid], target)
        elif target > lst[mid][sortop]:
            return binary_search_recursive(lst[mid + 1:], target)


def statistiek():
    '''this function is supossed to open another frame in the gui and show the statistics of the game-data'''
    fr1.grid_forget()#.pack_forget()
    fr2.grid_forget()#.pack_forget()
    global fr3
    fr3 = Frame(master=window, bg ='black')
    fr3.grid(row=0,column=0)#.pack()
    statknop = Button(master=fr3, text='klik hier terug te gaan naar de games', command=gamesterug, font='DejaVu 10')
    statknop.pack(side='bottom')
    if sortop in nlist:
        gemv = round(mean(listy),2)
        medv = median(listy)
        varv = round(var(listy),2)
        stdv = round(std(listy),2)
        modv = modes(listy)
        slb1 = Label(master=fr3, text='het gemiddelde van de ' + sortop + ' is ' + str(gemv), bg='black', fg='white',
                     font='DejaVu 10')
        slb2 = Label(master=fr3, text='de mediaan van de ' + sortop + ' is ' + str(medv), bg='black', fg='white',
                     font='DejaVu 10')
        slb3 = Label(master=fr3, text='de variatie van de ' + sortop + ' is ' + str(varv), bg='black', fg='white',
                     font='DejaVu 10')
        slb4 = Label(master=fr3, text='de standaard deviatie van de ' + sortop + ' is ' + str(stdv), bg='black',
                     fg='white', font='DejaVu 10')
        slb5 = Label(master=fr3, text='de mode van de ' + sortop + ' is ' + str(modv[0]) + ' en die komt ' + str(
            modv[1]) + ' keer voor', bg='black', fg='white', font='DejaVu 10')
        slb1.pack()
        slb2.pack()
        slb3.pack()
        slb4.pack()
        slb5.pack()
    elif sortop == "platforms" or sortop == "genres" or sortop =="steamspy_tags" or sortop == "categories":
        listx = []
        for i in range(len(listy)):
            listx.append([])
            listx[i].append(listy[i][0])
            listx[i].append(listy[i][1].split(';'))
        freqs = freq1(listx)
        length = 0
        freqlst = []
        naam_x = []
        proc_y = []
        for v in freqs.values():
            length += v
        for k, v in freqs.items():
            proc = round((v / length) * 100)
            freqlst.append([k, proc])
        freqlst = quicksort(freqlst)
        for i in freqlst:
            if i[1] > 5:
                naam_x.append(i[0])
                proc_y.append(i[1])
        plt.plot(naam_x, proc_y)
        plt.grid(True)
        plt.xlabel(sortop)
        plt.ylabel('procenten')
        plt.title('Procent games die ondergenoemde ' + sortop + ' hebben')
        plt.show()
    else:
        freqs = freq(listy)
        length = 0
        freqlst = []
        naam_x = []
        proc_y = []
        for v in freqs.values():
            length += v
        for k, v in freqs.items():
            proc = (v / length) * 100
            freqlst.append([k, proc])
        count = 0
        for i in freqlst:
            if i[1] > 0.1 and i[0]!='????' and i[0] !='?????' :
                naam_x.append(i[0])
                proc_y.append(i[1])
                count +=1
            if count > 5:
                break
        plt.plot(naam_x, proc_y)
        plt.grid(True)
        plt.xlabel('categories')
        plt.ylabel('procenten')
        plt.title('Procent games die ondergenoemde categorie hebben')
        plt.show()



def gamesterug():
    fr3.grid_forget()
    naam1()



def sorteerbeer(lst):
    for x in range(len(lst)):
        for i in range(len(lst)):  # swappen
            t = lst[i]
            if lst[i] != lst[-1]:
                if lst[i][sortop] > lst[i + 1][sortop]:
                    lst[i] = lst[i + 1]
                    lst[i + 1] = t

    return


def quicksort(lst,sorton=1): #werkt alleen met kleinere lijsten
    lst_smaller = []
    lst_larger = []
    if len(lst) <=1:
        return lst
    else:
        mid = lst.pop()
    for i in lst:
        if i[sorton] > mid[sorton]:
            lst_larger.append(i)
        else:
            lst_smaller.append(i)
    return quicksort(lst_smaller) + [mid] + quicksort(lst_larger)


def qsI(arr, l, h):
    '''this is a sorting function used to sort the json file with gamedata from steam'''
    size = h - l + 1
    stack = [0] * size
    top = 0
    stack[top] = l
    top = top + 1
    stack[top] = h

    while top >= 0:
        h = stack[top]
        top = top - 1
        l = stack[top]
        top = top - 1

        p = partition(arr, l, h)

        if p - 1 > l:
            top = top + 1
            stack[top] = l
            top = top + 1
            stack[top] = p - 1

        if p + 1 < h:
            top = top + 1
            stack[top] = p + 1
            top = top + 1
            stack[top] = h

def merge_sort(arr, l,r):
    if l<r:
        m = (l+r)//2
        merge_sort(arr, l,m)
        merge_sort(arr, m+1,r)
        merge(arr,l,m,r)

def merge(arr,l,m,r):
    Larr = arr[l:m+1]
    Rarr =arr[m+1:r+1]
    if sortop in nlist:
        Larr.append({'naam':'naam1',sortop:sys.maxsize})
        Rarr.append({'naam':'naam1',sortop:sys.maxsize})
    else:
        Larr.append({'naam': 'naam1', sortop: '𒐫'*999})
        Rarr.append({'naam': 'naam1', sortop: '𒐫'*999})
    j = i = 0

    for e in range(l,r+1):
        if Larr[i][sortop] <= Rarr[j][sortop]:
            arr[e]= Larr[i]
            i+=1
        else:
            arr[e]= Rarr[j]
            j+=1


def partition(arr, l ,r):
    '''this is a partition function used by the "qsI" function to sort part of a list and return the index of the pivot created'''
    m= len(arr)//2

    if l > m:  # in deze scenarios is l niet de kleinste en m niet de grootste

        if l < r: #als l kleiner is dan r en groter dan m is l in het midden en is l dus de median
            arr[l],arr[r] =arr[r],arr[l]

        elif m > r: # als m groter is dan r en kleiner dan l betekend het dat m in het midden zit
            arr[m], arr[r] = arr[r], arr[m]

    else:  # in deze scenarios is m niet de kleinste en l niet de grootste

        if l > r: # als l groter is dan r en kleiner dan m dan is l de mediaan
            arr[l],arr[r] =arr[r],arr[l]

        elif m < r:# als m kleiner is dan r en groter dan l dan is m de mediaan
            arr[m], arr[r] = arr[r], arr[m]

    i = l - 1
    if omgekeerd:
        for j in range(l,r):
            if arr[j][sortop] > arr[r][sortop]:
                i += 1
                arr[j], arr[i] = arr[i], arr[j]
        arr[i+1], arr[r] = arr[r], arr[i+1]
        return i+1
    else:
        for j in range(l,r):
            if arr[j][sortop] < arr[r][sortop]:
                i += 1
                arr[j], arr[i] = arr[i], arr[j]
        arr[i+1], arr[r] = arr[r], arr[i+1]
        return i+1




def mean(lst):
    '''statistics function to calculate mean'''
    cal = 0
    for i in lst:
        cal +=i[1]
    return cal / len(lst)

def median(lst):
    '''statistics function to find median'''
    if (len(lst)/2) % 1 >= 0.5:
        halflen = len(lst)//2
    else:
        halflen = len(lst)//2 -1

    if len(lst) % 2 == 0:
        return (lst[halflen][1] + lst[halflen +1][1])/2
    else:
        return  float(lst[halflen][1])

def var(lst):
    '''returns variation'''
    gem = mean(lst)
    a = 0
    for i in lst:
        a += (i[1]-gem)*(i[1]-gem)
    return a / len(lst)


def std(lst):
    '''returns standard deviation'''
    return var(lst)**0.5


def freq(lst):
    '''returns a list of numbers and their frequency'''
    freqs = {}
    for i in lst:
        if i[1] in freqs:
            freqs[i[1]] +=1
        else:
            freqs[i[1]] = 1

    return freqs

def modes(lst):
    '''returns mode and highest frequency'''
    flst= freq(lst)
    maxi = 1

    for v in flst.values():
        if maxi < v:
            maxi = v

    for k,v in flst.items():
        if maxi == v:
            maxt = k


    return [maxt, maxi]

def freq1(lst):
    '''returns a list of numbers and their frequency'''
    freqs = {}
    for i in lst:
        if type(i[1]) == type('str'):
            if i[1] in freqs:
                freqs[i[1]] += 1
            else:
                freqs[i[1]] = 1
        else:
            for e in i[1]:
                if e in freqs:
                    freqs[e] += 1
                else:
                    freqs[e] = 1

    return freqs


def modes1(lst):
    '''returns mode and highest frequency'''
    flst= freq1(lst)
    maxi = 1

    for v in flst.values():
        if maxi < v:
            maxi = v

    for k,v in flst.items():
        if maxi == v:
            maxt = k


    return [maxt, maxi]




def main():
    '''driver code'''
    global omgekeerd
    global leeslijst0
    global listy
    global window
    global zoekframeingebruik
    global search
    global nlist
    nlist = ["appid","english","required_age", "achievements","positive_ratings","negative_ratings","average_playtime","median_playtime","price"]
    search = False
    zoekframeingebruik = False
    kiesraam()
    leeslijst0 = lees()
    omgekeerd = False
    if algoritme == 3:
        print('merge sort')
        merge_sort(leeslijst0, 0, len(leeslijst0) - 1)
        if omgekeerd:
            leeslijst0.reverse()
    elif algoritme == 2 :
        print('quicksort iterative')
        qsI(leeslijst0, 0, len(leeslijst0) - 1)

    else:
        print('bubble sort')
        sorteerbeer(leeslijst0)

    listy = []
    for game in leeslijst0:
        listy.append([game['name'], game[sortop]])
    window = Tk()
    window['bg'] = 'black'
    window.geometry("600x600")
    naam1()
    window.mainloop()


if __name__ == '__main__':
    main()
