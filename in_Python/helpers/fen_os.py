# Helper to go from Python to C using terminal instructions.

import os
import sys

def Py2C(fen_princ, stock:list):
    """Terminal instructions to run HANDY_calculs.c.

    Args:
        fen_princ (Tk): displayed window.
        stock (list): list containing scenario and file path OR chosen CC
    """

    os.system("gcc in_C/HANDY_calculs.c -o in_C/handy_calculs_exe")
    os.system("./in_C/handy_calculs_exe " + stock[0] + " " + stock[1] + " " + stock[2])
    fen_princ.destroy()


def sendScenario(fen_princ, scenario:str):
    """Send file path.
    """

    path = 0
    
    if scenario == "eg":
        path = ['eg_f', "Text/HANDY_egalitarian_basic.txt", f"{sys.executable}"]
    if scenario == "eq":
        path = ['eq_f', "Text/HANDY_equitable_basic.txt", f"{sys.executable}"]
    if scenario == "un":
        path = ['un_f', "Text/HANDY_unequal_basic.txt", f"{sys.executable}"]
    Py2C(fen_princ, path)


def sendCursors(fen_princ, scenario, valuecursor):
    """Send chosen CC.
    """
    cursor = 0
    if scenario == "eg":
        cursor = ["eg_c", f"{valuecursor}", f"{sys.executable}"]
    if scenario == "eq":
        cursor = ["eq_c", f"{valuecursor}", f"{sys.executable}"]
    if scenario == "un":
        cursor = ["un_c", f"{valuecursor}", f"{sys.executable}"]
    Py2C(fen_princ, cursor)
