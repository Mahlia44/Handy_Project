import os
from tkinter import *

from fen2 import init_fen2
from fen1 import init_fen1

def backFen1(fen_princ:Tk):
    """Back to window 1, Fen1.

    Args:
        fen_princ (Tk): displayed window.
    """
    init_fen1(reset=True)
    fen_princ.destroy()

def backFen2(fen_princ:Tk, scenario:str):
    """ BAack to window 2, Fen2.

    Args:
        fen_princ (Tk): displayed window.
        scenario (str): type of scenario.
    """
    args = {}
    args["fileName"] = "in_C/results_python_file.txt"
    args["scenario"] = scenario
    print(args)
    init_fen2(args)
    fen_princ.destroy()

def moveButton(fen_princ:Tk, n:int,  scenario:str):
    """Buttons always displayed on right top to move from
    window to another.

    Args:
        fen_princ (Tk): displayed window.
        n (int): number of actual window.
        scenario (str): type of scenario.
    """

    quit_button = Button(fen_princ, text = "QUIT", borderwidth=0, bg="lightcoral",command = lambda:quit()).place(x=1155, y=25)
    if n==2:
        home_button = Button(fen_princ, text = "HOME", bg='lightskyblue',command = lambda:backFen1(fen_princ)).place(x=1150, y=60)
    if n==3:
        home_button = Button(fen_princ, text = "HOME", bg="navajowhite",command = lambda:backFen1(fen_princ)).place(x=1150, y=60)
        again_button = Button(fen_princ, text = "NEW VALUES",bg='lightgreen', command = lambda:backFen2(fen_princ, scenario)).place(x=1130, y=95)