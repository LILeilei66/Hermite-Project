import numpy as np
from pylab import *
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib.widgets import Button

def hermite_surface(p0,p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12,p13,p14,p15,u,v):
    u3 = u*u*u
    u2 = u*u

    v3 = v*v*v
    v2 = v*v
       
    U = array([[u3,u2,u,1]])
    V = array([[v3,v2,v,1]])
    H = array([[2,-2,1,1],[-3,3,-2,-1],[0,0,1,0],[1,0,0,0]])

    Ghx = array([[p0[0],p1[0],p4[0],p5[0]],[p2[0],p3[0],p6[0],p7[0]],[p8[0],p9[0],p12[0],p13[0]],[p10[0],p11[0],p14[0],p15[0]]])
    Ghy = array([[p0[1],p1[1],p4[1],p5[1]],[p2[1],p3[1],p6[1],p7[1]],[p8[1],p9[1],p12[1],p13[1]],[p10[1],p11[1],p14[1],p15[1]]])
    Ghz = array([[p0[2],p1[2],p4[2],p5[2]],[p2[2],p3[2],p6[2],p7[2]],[p8[2],p9[2],p12[2],p13[2]],[p10[2],p11[2],p14[2],p15[2]]])

    x = sum(np.dot(np.dot(np.dot(np.dot(U,H),Ghx),H.T),V.T))
    y = sum(np.dot(np.dot(np.dot(np.dot(U,H),Ghy),H.T),V.T))
    z = sum(np.dot(np.dot(np.dot(np.dot(U,H),Ghz),H.T),V.T))

    return x,y,z

def draw_surface(p0,p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12,p13,p14,p15):
    D = 100 # densidade da superficie
    x_list = np.ndarray((D, D))
    y_list = np.ndarray((D, D))
    z_list = np.ndarray((D, D))
    for vu in range(0, D):
        for vv in range(0, D):
            u, v = float(vu) / float(D-1), float(vv) / float(D-1)
            x, y, z = hermite_surface(p0,p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12,p13,p14,p15,u,v)
 
            x_list[vu, vv] = x
            y_list[vu, vv] = y
            z_list[vu, vv] = z
 
    return x_list, y_list, z_list

eixo = subplot(111, projection='3d')
subplots_adjust(bottom=0.10)

p0f = [0, 0, 10]
p1f = [10, 0, 0]
p2f = [0, 10, 8]
p3f = [18, 10, 0]
p4f = [16, 0, 0] 
p5f = [0, 0, -16] 
p6f = [24, 0, 0]
p7f = [0, 0, -14]
p8f = [0, 10, -2]
p9f = [8, 10, 0]
p10f = [0, 10, -2]
p11f = [8, 10, 0]
p12f = [8, 0, 0]
p13f = [0, 0, 2]
p14f = [8, 0, 0]
p15f = [0, 0, 2]

p0s = [0, 10, 8]
p1s = [18, 10, 0]
p2s = [0, 20, 15]
p3s = [20, 12, 0]
p4s = [18, 0, 0] 
p5s = [0, 0, -18] 
p6s = [24, 0, 0]
p7s = [0, 0, -14]
p8s = [0, 10, -2]
p9s = [8, 10, 0]
p10s = [0, 7, 2]
p11s = [5, 10, 0]
p12s = [0, 0, 0]
p13s = [0, 0, 0]
p14s = [0, 0, 0]
p15s = [0, 0, 0]


xf, yf, zf = draw_surface(p0f,p1f,p2f,p3f,p4f,p5f,p6f,p7f,p8f,p9f,p10f,p11f,p12f,p13f,p14f,p15f)
surface1 = eixo.plot_wireframe(xf,yf,zf, color='Purple')
#surface1 = eixo.plot_surface(xf,yf,zf, rstride=1, cstride=1, cmap=cm.winter, linewidth=0, antialiased=True)

xs, ys, zs = draw_surface(p0s,p1s,p2s,p3s,p4s,p5s,p6s,p7s,p8s,p9s,p10s,p11s,p12s,p13s,p14s,p15s)
#surface2 = eixo.plot_surface(xs,ys,zs, rstride=1, cstride=1, cmap=cm.autumn, linewidth=0, antialiased=False)
surface2 = eixo.plot_wireframe(xs,ys,zs, color='orange')

surf_new = 0

axcolor = 'lightgoldenrodyellow'

g_1 = axes([0.8, 0.025, 0.1, 0.04])
buttonG1 = Button(g_1, 'G1', color=axcolor, hovercolor='0.975')

def calc_g1(event):
    p0s = [0, 10, 8]
    p1s = [18, 10, 0]
    p2s = [0, 20, 15]
    p3s = [20, 12, 0]
    p4s = [24, 0, 0] 
    p5s = [0, 0, -14] 
    p6s = [24, 0, 0]
    p7s = [0, 0, -14]
    p8s = [0, 30, -6]
    p9s = [24, 30, 0]
    p10s = [0, 7, 2]
    p11s = [5, 10, 0]
    p12s = [24, 0, 0]
    p13s = [0, 0, 6]
    p14s = [0, 0, 0]
    p15s = [0, 0, 0]
    
    surface2.remove()
    xs, ys, zs = draw_surface(p0s,p1s,p2s,p3s,p4s,p5s,p6s,p7s,p8s,p9s,p10s,p11s,p12s,p13s,p14s,p15s)
    
    surf_new = eixo.plot_wireframe(xs,ys,zs, color='orange')
    #surf_new = eixo.plot_surface(xs,ys,zs, rstride=1, cstride=1, cmap=cm.autumn, linewidth=0, antialiased=False)
    
    
buttonG1.on_clicked(calc_g1)

show()

