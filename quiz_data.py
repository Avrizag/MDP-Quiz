


from tkinter import *
from tkinter import ttk
import time


n= ttk.Notebook()
f1= ttk.Frame(n)
f2= ttk.Frame(n)
f3= ttk.Frame(n)
f4= ttk.Frame(n)
f5= ttk.Frame(n)
f6= ttk.Frame(n)
f7= ttk.Frame(n)
f8= ttk.Frame(n)
f9= ttk.Frame(n)
f10= ttk.Frame(n)
fCorrect = ttk.Frame(n)
fend = ttk.Frame(n)


window= ttk.Frame(n)
COUNT = 0
score =0

def increment():
    global COUNT
    COUNT = COUNT+1



def main():
    global score
    n.add(f1, text="One")



    Label(f1, text="What does www stand for in a website browser?").grid(row=1,column=2)
    Button(f1, text="World Wide Web",command=correct).grid(row=3,column=1)
    Button(f1, text="world war wide", command=incorrect).grid(row=3,column=2)
    Button(f1, text="wide world web", command=incorrect).grid(row=3,column=3)


    Label(f2, text="How long is an Olympic swimming pool (in meters)?").grid(row=2,column=2)
    Button(f2, text="30",command=incorrect2).grid(row=3,column=1)
    Button(f2, text="50", command=correct2).grid(row=3,column=2)
    Button(f2, text="60", command=incorrect2).grid(row=3,column=3)

    Label(f3, text="What geometric shape is generally used for stop signs?").grid(row=2,column=2)
    Button(f3, text="triangle",command=incorrect3).grid(row=3,column=1)
    Button(f3, text="Octagon", command=correct3).grid(row=3,column=2)
    Button(f3, text="circle", command=incorrect3).grid(row=3,column=3)

    Label(f4, text="How many languages are written from right to left?").grid(row=2,column=2)
    Button(f4, text="12",command=correct4).grid(row=3,column=1)
    Button(f4, text="30", command=incorrect4).grid(row=3,column=2)
    Button(f4, text="5", command=incorrect4).grid(row=3,column=3)


    Label(f5, text="What does the 'from ____ import' command do?").grid(row=2,column=2)
    Button(f5, text="Import an image",command=incorrect5).grid(row=3,column=1)
    Button(f5, text="Import text", command=incorrect5).grid(row=3,column=2)
    Button(f5, text="Import a module", command=correct5).grid(row=3,column=3)

    Label(f6, text="What is the name of the biggest technology company in South Korea?").grid(row=2,column=2)
    Button(f6, text="Sony",command=incorrect6).grid(row=3,column=1)
    Button(f6, text="Lg", command=incorrect6).grid(row=3,column=2)
    Button(f6, text="Samsung", command=correct6).grid(row=3,column=3)

    Label(f7, text="Which animal can be seen on the Porsche logo?").grid(row=2, column=2)
    Button(f7, text="Bull", command=incorrect7).grid(row=3, column=1)
    Button(f7, text="Elephant", command=incorrect7).grid(row=3, column=2)
    Button(f7, text="Horse", command=correct7).grid(row=3, column=3)

    Label(f8, text="Who was the first woman to win a Nobel Prize (in 1903)?").grid(row=2, column=2)
    Button(f8, text="Marie Curie", command=correct8).grid(row=3, column=1)
    Button(f8, text="Toni Morrison", command=incorrect8).grid(row=3, column=2)
    Button(f8, text="Shirin Ebadi", command=incorrect8).grid(row=3, column=3)

    Label(f9, text="What is cynophobia ?").grid(row=2, column=2)
    Button(f9, text="Fear of dogs", command=correct9).grid(row=3, column=1)
    Button(f9, text="Fear of falling", command=incorrect9).grid(row=3, column=2)
    Button(f9, text="Fear of spiders", command=incorrect9).grid(row=3, column=3)

    Label(f10, text="Who was the first woman pilot to fly solo across the Atlantic?").grid(row=2, column=2)
    Button(f10, text="Toni Morrison", command=incorrect10).grid(row=3, column=1)
    Button(f10, text="Amelia Earhart", command=correct10).grid(row=3, column=2)
    Button(f10, text="Harriet Quimby", command=incorrect10).grid(row=3, column=3)

    Label(fCorrect, text="You are correct !").grid(row=2, column=2)
    Label(fCorrect, text="do you want to keep playing ?").grid(row=4, column=2)
    Button(fCorrect, text="Yes, i want to keep playing", command=stay).grid(row=5, column=1)
    Button(fCorrect, text="No, I want to quit", command=quit1).grid(row=5, column=3)








def correct():
    global score
    score = 1
    n.hide(f1)
    increment()
    Label(fend, text="End of the game").grid(row=2, column=2)
    Label(fend, text="your score is {}".format(score)).grid(row=3, column=2)
    Label(fCorrect, text="your score is {}".format(score)).grid(row=3, column=2)
    n.add(fCorrect)



def incorrect():
    global score
    score = 0
    Label(fend, text="End of the game").grid(row=2, column=2)
    Label(fend, text="your score is {}".format(score)).grid(row=3, column=2)
    n.hide(f1)
    n.add(fend)

def correct2():
    global score
    score = 6
    Label(fend, text="End of the game").grid(row=2, column=2)
    Label(fend, text="your score is {}".format(score)).grid(row=3, column=2)
    Label(fCorrect, text="your score is {}".format(score)).grid(row=3, column=2)
    n.hide(f2)
    increment()

    n.add(fCorrect)

def incorrect2():
    global score
    score = 0
    Label(fend, text="End of the game").grid(row=2, column=2)
    Label(fend, text="your score is {}".format(score)).grid(row=3, column=2)
    n.hide(f2)
    n.add(fend)

def correct3():
    global score
    score = 16
    Label(fend, text="End of the game").grid(row=2, column=2)
    Label(fend, text="your score is {}".format(score)).grid(row=3, column=2)
    Label(fCorrect, text="your score is {}".format(score)).grid(row=3, column=2)
    n.hide(f3)
    increment()
    n.add(fCorrect)

def incorrect3():
    global score
    score = 0
    Label(fend, text="End of the game").grid(row=2, column=2)
    Label(fend, text="your score is {}".format(score)).grid(row=3, column=2)
    n.hide(f3)
    n.add(fend)

def correct4():
    global score
    score = 66
    Label(fend, text="End of the game").grid(row=2, column=2)
    Label(fend, text="your score is {}".format(score)).grid(row=3, column=2)
    Label(fCorrect, text="your score is {}".format(score)).grid(row=3, column=2)
    n.hide(f4)
    increment()
    n.add(fCorrect)

def incorrect4():
    global score
    score = 0
    Label(fend, text="End of the game").grid(row=2, column=2)
    Label(fend, text="your score is {}".format(score)).grid(row=3, column=2)
    n.hide(f4)
    n.add(fend)

def correct5():
    global score
    score = 166
    Label(fend, text="End of the game").grid(row=2, column=2)
    Label(fend, text="your score is {}".format(score)).grid(row=3, column=2)
    Label(fCorrect, text="your score is {}".format(score)).grid(row=3, column=2)
    n.hide(f5)
    increment()
    n.add(fCorrect)

def incorrect5():
    global score
    score = 0
    Label(fend, text="End of the game").grid(row=2, column=2)
    Label(fend, text="your score is {}".format(score)).grid(row=3, column=2)
    n.hide(f5)
    n.add(fend)

def correct6():
    global score
    score = 666
    Label(fend, text="End of the game").grid(row=2, column=2)
    Label(fend, text="your score is {}".format(score)).grid(row=3, column=2)
    Label(fCorrect, text="your score is {}".format(score)).grid(row=3, column=2)
    n.hide(f6)
    increment()
    n.add(fCorrect)

def incorrect6():
    global score
    score = 0
    Label(fend, text="End of the game").grid(row=2, column=2)
    Label(fend, text="your score is {}".format(score)).grid(row=3, column=2)
    n.hide(f6)
    n.add(fend)

def correct7():
    global score
    score = 1666
    Label(fend, text="End of the game").grid(row=2, column=2)
    Label(fend, text="your score is {}".format(score)).grid(row=3, column=2)
    Label(fCorrect, text="your score is {}".format(score)).grid(row=3, column=2)
    n.hide(f7)
    increment()
    n.add(fCorrect)

def incorrect7():
    global score
    score = 0
    Label(fend, text="End of the game").grid(row=2, column=2)
    Label(fend, text="your score is {}".format(score)).grid(row=3, column=2)
    n.hide(f7)
    n.add(fend)

def correct8():
    global score
    score = 6666
    Label(fend, text="End of the game").grid(row=2, column=2)
    Label(fend, text="your score is {}".format(score)).grid(row=3, column=2)
    Label(fCorrect, text="your score is {}".format(score)).grid(row=3, column=2)
    n.hide(f8)
    increment()
    n.add(fCorrect)

def incorrect8():
    global score
    score = 0
    Label(fend, text="End of the game").grid(row=2, column=2)
    Label(fend, text="your score is {}".format(score)).grid(row=3, column=2)
    n.hide(f8)
    n.add(fend)

def correct9():
    global score
    score = 16666
    Label(fend, text="End of the game").grid(row=2, column=2)
    Label(fend, text="your score is {}".format(score)).grid(row=3, column=2)
    Label(fCorrect, text="your score is {}".format(score)).grid(row=3, column=2)
    n.hide(f9)
    increment()
    n.add(fCorrect)

def incorrect9():
    global score
    score = 0
    Label(fend, text="End of the game").grid(row=2, column=2)
    Label(fend, text="your score is {}".format(score)).grid(row=3, column=2)
    n.hide(f9)
    n.add(fend)

def correct10():
    global score
    score = 31666
    Label(fend, text="End of the game").grid(row=2, column=2)
    Label(fend, text="your score is {}".format(score)).grid(row=3, column=2)
    Label(fCorrect, text="your score is {}".format(score)).grid(row=3, column=2)
    n.hide(f10)
    increment()
    n.add(fend)

def incorrect10():
    global score
    score = 0
    Label(fend, text="End of the game").grid(row=2, column=2)
    Label(fend, text="your score is {}".format(score)).grid(row=3, column=2)
    n.hide(f10)
    n.add(fend)

def stay():
    if COUNT == 1:
        n.forget(fCorrect)
        n.add(f2, text="Two")

    elif COUNT == 2:
        n.forget(fCorrect)
        n.add(f3, text="Three")

    elif COUNT == 3:
        n.forget(fCorrect)
        n.add(f4, text="Four")

    elif COUNT == 4:
        n.forget(fCorrect)
        n.add(f5, text="Five")

    elif COUNT == 5:
        n.forget(fCorrect)
        n.add(f6, text="Six")

    elif COUNT == 6:
        n.forget(fCorrect)
        n.add(f7, text="Seven")

    elif COUNT == 7:
        n.forget(fCorrect)
        n.add(f8, text="Eight")

    elif COUNT == 8:
        n.forget(fCorrect)
        n.add(f9, text="Nine")

    elif COUNT == 9:
        n.forget(fCorrect)
        n.add(f10, text="Ten")


def quit1():
    n.forget(fCorrect)
    n.add(fend)



main()


n.pack()

n.mainloop()