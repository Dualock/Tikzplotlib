import matplotlib.pyplot as plt
import numpy as np
plt.rcParams["figure.figsize"] = (8,5)
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
    #plt.plot(x, y,  color='black', linestyle = 'dotted', label = 'y = x2')
    plt.scatter(x_1, y_1, label= "pares ordenados", color= "green", marker= "o", s=30)
    # function to show the plot               
    plt.xlim(-4,4)
    plt.ylim(-2,10)
    # Legend
    #plt.legend(loc='center right')
    '''
    # Moving axis to center
    ax = plt.gca()  # gca stands for 'get current axis'
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.spines['bottom'].set_position(('data',0))
    ax.yaxis.set_ticks_position('left')
    ax.spines['left'].set_position(('data',0))
    '''
    plt.axvline(0, color = 'black', alpha = 0.5)
    plt.axhline(0, color = 'black', alpha = 0.5)
    # giving a title to my graph
    plt.title('Gráfica de la parabola general')
    import tikzplotlib
    tikzplotlib.save("parabola_general.tex", flavor="latex")
    plt.show()

def concava_arriba():
    # setting the x - coordinates
    x = np.arange(-10, 10, 0.1)
    # setting the corresponding y - coordinates
    y = np.power(x,2)
    # plotting the points
    plt.plot(x, y,  color='green')
    plt.title('Concava hacia arriba')
    # naming the y axis
    '''
    ax = plt.gca()  # gca stands for 'get current axis'
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.spines['bottom'].set_position(('data',0))
    ax.yaxis.set_ticks_position('left')
    ax.spines['left'].set_position(('data',0))
    '''
    plt.axvline(0, color = 'black', alpha = 0.5)
    plt.axhline(0, color = 'black', alpha = 0.5)
    plt.xlim(-4,4)
    plt.ylim(-4,4)
    import tikzplotlib
    tikzplotlib.save("concava_arriba.tex", flavor="latex")
    plt.show()

def concava_abajo():
    # setting the x - coordinates
    x = np.arange(-10, 10, 0.1)
    # setting the corresponding y - coordinates
    y = -np.power(x,2)
    # plotting the points
    plt.plot(x, y,  color='red')
    plt.title('Concava hacia abajo')
    # naming the y axis
    '''
    ax = plt.gca()  # gca stands for 'get current axis'
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.spines['bottom'].set_position(('data',0))
    ax.yaxis.set_ticks_position('left')
    ax.spines['left'].set_position(('data',0))
    '''
    plt.axvline(0, color = 'black', alpha = 0.5)
    plt.axhline(0, color = 'black', alpha = 0.5)
    plt.xlim(-4,4)
    plt.ylim(-4,4)
    import tikzplotlib
    tikzplotlib.save("concava_abajo.tex", flavor="latex")
    plt.show()


def Eje_simetria():
    # setting the x - coordinates
    x = np.arange(-10, 10, 0.1)
    # setting the corresponding y - coordinates
    y = np.power(x-1,2) + 2
    fig = plt.figure()
    ax = fig.add_subplot()
    # plotting the points
    ax.plot(x, y,  color='blue')
    plt.title('Eje de simetria')
    # naming the y axis
    '''
    ax = plt.gca()  # gca stands for 'get current axis'
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.spines['bottom'].set_position(('data',0))
    ax.yaxis.set_ticks_position('left')
    ax.spines['left'].set_position(('data',0))
    '''
    ax.axvline(0, color = 'black', alpha = 0.5)
    ax.axhline(0, color = 'black', alpha = 0.5)
    plt.xlim(-4,4)
    plt.ylim(-4,9)
    ax.plot([1], [2], 'o')
    ax.axvline(1, color = 'red', linestyle = 'dotted')
    plt.xticks([-4,-3,-2,-1,0,1,2,3,4])
    ax.annotate("x=1 es el eje de simetria",
            xy=(1, 0.2), xycoords='data',
            xytext=(1.3, 1), textcoords='data',
            arrowprops=dict(arrowstyle="->",
                            connectionstyle="arc3"),
            )
    import tikzplotlib
    tikzplotlib.save("eje.tex", flavor="latex")
    plt.show()


def Vertice():
            # setting the x - coordinates
    x = np.arange(-10, 10, 0.1)
    # setting the corresponding y - coordinates
    y = np.power(x-1,2) + 2
    fig = plt.figure()
    ax = fig.add_subplot()
    # plotting the points
    ax.plot(x, y,  color='blue')
    plt.title('Vertice de una parabola')
    # naming the y axis
    '''
    ax = plt.gca()  # gca stands for 'get current axis'
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.spines['bottom'].set_position(('data',0))
    ax.yaxis.set_ticks_position('left')
    ax.spines['left'].set_position(('data',0))
    '''
    ax.axvline(0, color = 'black', alpha = 0.5)
    ax.axhline(0, color = 'black', alpha = 0.5)
    plt.xlim(-4,4)
    plt.ylim(-4,9)

    ax.plot([1], [2], 'o')
    ax.annotate('Vertice (1,2)', xy=(1, 2), xytext=(0.5, 1))
    
    import tikzplotlib
    tikzplotlib.save("vertice.tex", flavor="latex")
    plt.show()
def Corte_ejes():
    print('s')
def traslacion_horizontal():
    # setting the x - coordinates
    x = np.arange(-10, 10, 0.1)
    # setting the corresponding y - coordinates
    y = np.power(x+2,2)
    y2 = np.power(x,2)
    y3 = np.power(x-2,2)
    fig = plt.figure()
    ax = fig.add_subplot()
    # plotting the points
    ax.plot(x, y,  color='blue')
    ax.plot(x, y2, color = 'red')
    ax.plot(x, y3, color = 'green')
    plt.title('Traslacion horizontal')
    # naming the y axis
    '''
    ax = plt.gca()  # gca stands for 'get current axis'
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.spines['bottom'].set_position(('data',0))
    ax.yaxis.set_ticks_position('left')
    ax.spines['left'].set_position(('data',0))
    '''
    ax.axvline(0, color = 'black', alpha = 0.5)
    ax.axhline(0, color = 'black', alpha = 0.5)
    plt.xlim(-5,5)
    plt.ylim(-4,9)
    ax.annotate(r'$y = x^2$', xy=(1, 2), xytext=(2.10, 4), color = 'red')
    ax.annotate(r'$y = (x+2)^2$', xy=(1, 2), xytext=(0.2, 4.5), color = 'blue')
    ax.annotate(r'$y = (x-2)^2$', xy=(1, 2), xytext=(3.55, 2), color = 'green')
    import tikzplotlib
    tikzplotlib.save("traslacion_h.tex", flavor="latex")
    plt.show()
def traslacion_vertical():
    # setting the x - coordinates
    x = np.arange(-10, 10, 0.1)
    # setting the corresponding y - coordinates
    y = np.power(x,2)-3

    fig = plt.figure()
    ax = fig.add_subplot()
    # plotting the points
    ax.plot(x, y,  color='blue')
    plt.title('Traslacion vertical')
    # naming the y axis
    ax.axvline(0, color = 'black', alpha = 0.5)
    ax.axhline(0, color = 'black', alpha = 0.5)
    plt.xlim(-5,5)
    plt.ylim(-4,9)
    ax.annotate(r'$y = x^2-3$', xy=(1, 2), xytext=(3.25, 6), color = 'blue')
    import tikzplotlib
    tikzplotlib.save("traslacion_v.tex", flavor="latex")
    plt.show()
def diferente_apertura():
    # setting the x - coordinates
    x = np.arange(-10, 10, 0.1)
    # setting the corresponding y - coordinates
    y = np.power(x,2)
    y1 = np.power(2*x,2)
    y2 = np.power(3*x,2)
    y3 = -np.power(x,2)
    y4 = -np.power(2*x,2)
    y5 = -np.power(3*x,2)

    fig = plt.figure()
    ax = fig.add_subplot()
    # plotting the points
    ax.plot(x, y,  color='green')
    ax.plot(x, y1,  color='red')
    ax.plot(x, y2,  color='orange')
    ax.plot(x, y3,  color='blue')
    ax.plot(x, y4,  color='brown')
    ax.plot(x, y5,  color='purple')
    plt.title('Aperturas de las parabolas')
    # naming the y axis
    ax.axvline(0, color = 'black', alpha = 0.5)
    ax.axhline(0, color = 'black', alpha = 0.5)
    plt.xlim(-4,4)
    plt.ylim(-10,10)
    ax.annotate(r'$y = x^2$', xy=(1, 2), xytext=(2, 3.50), color = 'green')
    ax.annotate(r'$y = 2x^2$', xy=(1, 2), xytext=(1.5, 5), color = 'red')
    ax.annotate(r'$y = 3x^2$', xy=(1, 2), xytext=(0.05, 6), color = 'orange')
    ax.annotate(r'$y = -x^2$', xy=(1, 2), xytext=(2, -3.50), color = 'blue')
    ax.annotate(r'$y = -2x^2$', xy=(1, 2), xytext=(1.2, -5), color = 'brown')
    ax.annotate(r'$y = -3x^2$', xy=(1, 2), xytext=(0.01, -7), color = 'purple')
    import tikzplotlib
    tikzplotlib.save("aperturas.tex", flavor="latex")
    plt.show()
def Ejemplo1():
        # setting the x - coordinates
    x = np.arange(-10, 10, 0.1)
    # setting the corresponding y - coordinates
    y = 1.5*np.power(x,2)+5*x -1

    fig = plt.figure()
    ax = fig.add_subplot()
    # plotting the points
    ax.plot(x, y,  color='blue')
    plt.title('Grafica de la funcion')
    # naming the y axis
    ax.axvline(0, color = 'black', alpha = 0.5)
    ax.axhline(0, color = 'black', alpha = 0.5)
    ax.plot([-5/3], [-31/6], 'o', color = 'black')
    ax.annotate(r'$(\frac{-5}{3}, \frac{-31}{6})$', xy=(1, 2), xytext=(-2, -6.5), color = 'black')
    ax.plot([0], [-1], 'o', color = 'black')
    ax.annotate(r'$(0, -1)$', xy=(1, 2), xytext=(0.05, -1), color = 'black')
    plt.xlim(-5,5)
    plt.ylim(-9,9)
    import tikzplotlib
    tikzplotlib.save("ej1.tex", flavor="latex")
    plt.show()


Ejemplo1()


