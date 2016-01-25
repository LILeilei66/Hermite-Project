import numpy as np
from pylab import *
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button, RadioButtons

def hermite(p0, p1, t0, t1, t):
    t2 = t*t
    t3 = t*t2
  
    x = ((2*t3 - 3*t2 + 1)*p0[0]+
    (-2*t3 +  3*t2)*p1[0]+
    (t3 - 2*t2 + t)*t0[0]+
    (t3 - t2)*t1[0])
        
    y = ((2*t3 - 3*t2 + 1)*p0[1]+
    (-2*t3 +  3*t2)*p1[1]+
    (t3 - 2*t2 + t)*t0[1]+
    (t3 - t2)*t1[1])
        
    return x, y

def catmull_rom(p0, p1, p2, p3, t):
    t2 = t*t
    t3 = t*t2
    
    x = (0.5 *((2 * p1[0]) +
        (-p0[0] + p2[0]) * t +
        (2*p0[0] - 5*p1[0] + 4*p2[0] - p3[0]) * t2 +
        (-p0[0] + 3*p1[0]- 3*p2[0] + p3[0]) * t3))
    
    y = (0.5 *((2 * p1[1]) +
        (-p0[1] + p2[1]) * t +
        (2*p0[1] - 5*p1[1] + 4*p2[1] - p3[1]) * t2 +
        (-p0[1] + 3*p1[1]- 3*p2[1] + p3[1]) * t3))
    
    return x, y

def desenha_curva_hermite(p0,p1,t0,t1):
    u=0
    x_list = list()
    y_list = list()
    while u < 1.01:
        x,y = hermite(p0,p1,t0,t1,u)
        x_list.append(x)
        y_list.append(y)
        u=u+0.01
    return x_list, y_list

def desenha_curva_catmull(p0,p1,p2,p3):
    t=0
    x_list = list()
    y_list = list()
    while t < 1.01:
        x,y = catmull_rom(p0,p1,p2,p3,t)
        x_list.append(x)
        y_list.append(y)
        t=t+0.01
  
    return x_list, y_list

eixo = subplot(111)
subplots_adjust(left=0.22, bottom=0.38)
p0 = [132, 38]
p1 = [90, 45]
t0 = [54, 12]
t1 = [68, 30]
x,y = desenha_curva_hermite(p0,p1,t0,t1)

l, = plot(x,y, lw=2, color='red')
axcolor = 'lightgoldenrodyellow'

p0c = [70, 28]
p1c = [82, 45]
p2c = [56, 38]
p3c = [60, 10]
x,y = desenha_curva_catmull(p0c,p1c,p2c,p3c)
v, = plot(x,y, lw=2, color='blue')

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
    t0 = [54, 12]
    t1 = [tix, tiy]
    l.set_data(desenha_curva_hermite(p0,p1,t0,t1))
    draw()
    
slidexpi.on_changed(atualiza_curva)
slideypi.on_changed(atualiza_curva)
slidexti.on_changed(atualiza_curva)
slideyti.on_changed(atualiza_curva)

reset_eixo = axes([0.8, 0.025, 0.1, 0.04])
buttonR = Button(reset_eixo, 'Reset H', color=axcolor, hovercolor='0.975')

reset_catmull = axes([0.6, 0.025, 0.1, 0.04])
buttonRC = Button(reset_catmull, 'Reset C', color=axcolor, hovercolor='0.975')

c_0 = axes([0.2, 0.025, 0.1, 0.04])
buttonC0 = Button(c_0, 'C0', color=axcolor, hovercolor='0.975')

c_1 = axes([0.4, 0.025, 0.1, 0.04])
buttonC1 = Button(c_1, 'C1', color=axcolor, hovercolor='0.975')

rax = axes([0.025, 0.5, 0.15, 0.15], axisbg=axcolor)
radio = RadioButtons(rax, ('red', 'blue','green','purple', 'orange'), active=0)

def resetHermite(event):
    slidexpi.reset()
    slideypi.reset()
    slidexti.reset()
    slideyti.reset()
buttonR.on_clicked(resetHermite)

def resetCatmull(event):
    p0 = [70, 28]
    p1 = [82, 45]
    p2 = [56, 38]
    p3 = [60, 10]
    v.set_data(desenha_curva_catmull(p0,p1,p2,p3))
    draw()
buttonRC.on_clicked(resetCatmull)

def cont_helper(p0,p1,p2,p3):
    pix = slidexpi.val
    piy = slideypi.val
    pxt = pix - p1[0]
    pyt = piy - p1[1]
    t=0
    x_list = list()
    y_list = list()
    while t < 1.01:
       x,y = catmull_rom(p0,p1,p2,p3,t)
       x_list.append(x+pxt)
       y_list.append(y+pyt)
       t=t+0.01
    return x_list, y_list

def cont_0(event):
    p0 = [70, 28]
    p1 = [82, 45]
    p2 = [56, 38]
    p3 = [60, 10]
    v.set_data(cont_helper(p0,p1,p2,p3))
    draw()
buttonC0.on_clicked(cont_0)

def cont_1(event):
    p0 = [70, 28]
    p1 = [82, 45]
    p2 = [56, 38]
    p3 = [60, 10]

    pix = slidexpi.val
    piy = slideypi.val
    p1h = [90, 45]
    t0 = [3*(p1h[0]-pix), 3*(p1h[1]-piy)] 
    dx = 0.2*(p2[0]-p0[0])
    dy = 0.2*(p2[1]-p0[1])
		
    if dx < t0[0]:
        while dx < t0[0] :
            p0[0]-=1
            dx = 0.2*(p2[0]-p0[0])
            dy = 0.2*(p2[1]-p0[1])
    else:
        while dx > t0[0]:
            p0[0]+=1
            dx = 0.2*(p2[0]-p0[0])
            dy = 0.2*(p2[1]-p0[1])
            
    dy = p1[1]-dy

    if dy > t0[1]:
        
        while dy > t0[1]:
            p0[1] -=1
            dy = 0.2*(p2[1]-p0[1])
            dy = p1[1]-dy
    else:
        while dy < t0[1]:
            p0[1] +=1
            dy = 0.2*(p2[1]-p0[1])
            dy = p1[1] - dy
    
    p0_new=[dx,dy]
    v.set_data(cont_helper(p0_new,p1,p2,p3))
    draw()
buttonC1.on_clicked(cont_1)

def colorfunc(label):
    l.set_color(label)
    draw()
radio.on_clicked(colorfunc)

show()

