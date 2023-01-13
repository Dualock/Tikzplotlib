import matplotlib.pyplot as plt
import numpy as np
def parabola_basica():
    # x axis values
    x_1 = [-3,-2,-1,0,1,2,3]
    # corresponding y axis values
    y_1 = [9,4,1,0,1,4,9]


    # setting the x - coordinates
    x = np.arange(-4, 4, 0.1)
    # setting the corresponding y - coordinates
    y = np.power(x,2)
    # plotting the points
    plt.style.use("ggplot")
    plt.plot(x, y,  color='black', linestyle = 'dotted')
    plt.scatter(x_1, y_1, label= "none", color= "green", marker= "o", s=30)
    # function to show the plot               
    plt.axhline(0, color="black", alpha=0.3)
    plt.axvline(0, color="black", alpha=0.3)
    plt.xlim(-5,5)
    plt.ylim(-5,5)
    import tikzplotlib
    tikzplotlib.save("mytikz.tex", flavor="context")
    plt.show()

def concava_arriba():
    print('s')
def concava_abajo():
    print('s')
def Eje_simetria():
    print('s')
def Vertice():
    print('s')
def Corte_ejes():
    print('s')
def traslacion_horizontal():
    print('s')
def traslacion_vertical():
    print('s')
def diferente_apertura():
    print('s')
def Ejemplo1():
    print('s')
def Ejemplo2():
    print('s')
parabola_basica()