import matplotlib.pyplot as plt
import numpy as np


He_e = 14
He_sig = 2.56
He_N = 2

Xe_e  = 50
Xe_sig  = 3.98
Xe_N = 54


def pot(myrange, erg, sig, N):
    newrange = myrange.copy()
    for index, item in enumerate(myrange):
        newrange[index] =4 * N * erg * ((sig/item) ** 12 - (sig/item) ** 6)
    
    return newrange

def force(myrange, erg, sig, N):
    newrange = myrange.copy()
    for index, item in enumerate(myrange):
        newrange[index] =4 * N * erg * (-12/item *(sig/item) ** 12 + 6/item * (sig/item) ** 6)
    
    return newrange


def plot_repulsive_force(myrange, hexe):


    if hexe == 'he':
        erg = He_e
        sig = He_sig
        N = He_N
    elif hexe == 'xe':
        erg = Xe_e
        sig = Xe_sig
        N = Xe_N
        
    fig,ax = plt.subplots()

    ax.plot(myrange, pot(myrange, erg, sig, N), label = '', color = 'C0')
    ax.plot(myrange, pot)
    ax.set_ylim(-10000,10000)
    ax.axhline(0)
    ax.axhline(0)

    plt.show()
    # plt.savefig(hexe + "_force.png")
