import numpy as np
from pylab import *
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button, RadioButtons

def hermite(p0, p1, t0, t1, u):
        
    x = ((2*u**3 - 3*u**2 + 1)*p0[0]+
    (-2*u**3 +  3*u**2)*p1[0]+
    (u**3 - 2*u**2 + u)*t0[0]+
    (u**3 - u**2)*t1[0])
        
    y = ((2*u**3 - 3*u**2 + 1)*p0[1]+
    (-2*u**3 +  3*u**2)*p1[1]+
    (u**3 - 2*u**2 + u)*t0[1]+
    (u**3 - u**2)*t1[1])
    return x, y

def desenha_curva(p0,p1,t0,t1):
    u=0
    x_list = list()
    y_list = list()
    while u < 1.01:
        x,y = hermite(p0,p1,t0,t1,u)
        x_list.append(x)
        y_list.append(y)
        u=u+0.01
    return x_list, y_list

eixo = subplot(111)
subplots_adjust(left=0.22, bottom=0.38)
p0 = [132, 38]
p1 = [90, 45]
t0 = [54, 12]
t1 = [68, 30]
x,y = desenha_curva(p0,p1,t0,t1)

l, = plot(x,y, lw=2, color='red')
axcolor = 'lightgoldenrodyellow'

eixo_pix = axes([0.25, 0.30, 0.60, 0.03], axisbg=axcolor)
eixo_piy = axes([0.25, 0.25, 0.60, 0.03], axisbg=axcolor)
eixo_tix = axes([0.25, 0.20, 0.60, 0.03], axisbg=axcolor)
eixo_tiy = axes([0.25, 0.15, 0.60, 0.03], axisbg=axcolor)


slidexpi = Slider(eixo_pix, 'ponto 1 x', 0, 200, valinit=p1[0])
slideypi = Slider(eixo_piy, 'ponto 1 y', 0, 200, valinit=p1[1])
slidexti = Slider(eixo_tix, 'tangente 1 x', -300, 300, valinit=t1[0])
slideyti = Slider(eixo_tiy, 'tangente 1 y', -100, 100, valinit=t1[1])


def atualiza_curva(val):
    pix = slidexpi.val
    piy = slideypi.val
    tix = slidexti.val
    tiy = slideyti.val
    p0 = [132, 38]
    p1 = [pix, piy]
    t0 = [54, 9]
    t1 = [tix, tiy]
    l.set_data(desenha_curva(p0,p1,t0,t1))
    draw()
    
slidexpi.on_changed(atualiza_curva)
slideypi.on_changed(atualiza_curva)
slidexti.on_changed(atualiza_curva)
slideyti.on_changed(atualiza_curva)

reset_eixo = axes([0.8, 0.025, 0.1, 0.04])
button = Button(reset_eixo, 'Reset', color=axcolor, hovercolor='0.975')

def reset(event):
    slidexpi.reset()
    slideypi.reset()
    slidexti.reset()
    slideyti.reset()
button.on_clicked(reset)

rax = axes([0.025, 0.5, 0.15, 0.15], axisbg=axcolor)
radio = RadioButtons(rax, ('red', 'blue','green','purple', 'orange'), active=0)
def colorfunc(label):
    l.set_color(label)
    draw()
radio.on_clicked(colorfunc)

show()

