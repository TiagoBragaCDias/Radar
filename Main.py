# Membros do Grupo
# Tiago Braga Camargo Dias
# Gabriel Pereira Silva Defensor Moreira
# Beatriz Helena
# Leonardo Rufino Costa

from graphics import *

Xmax = 800
Ymax = 600
Background = color_rgb(16, 16, 37)
win = GraphWin("TelaRadar", Xmax, Ymax)
win.setBackground(Background)

def PontoRadar(x,y,color,size):
    x = x+Xmax/2

    y = Ymax/2 - y

    if size == 1:

        win.plotPixel(x,y,color)

    if size == 2:

        win.plotPixel(x,y,color)

        win.plotPixel(x+1,y,color)

        win.plotPixel(x,y-1,color)

        win.plotPixel(x+1,y-1,color)

    if size == 3:

        win.plotPixel(x,y,color)

        win.plotPixel(x+1,y,color)

        win.plotPixel(x+1,y-1,color)
        
        win.plotPixel(x+1, y+1, color)

        win.plotPixel(x,y-1,color)

        win.plotPixel(x, y+1, color)

        win.plotPixel(x-1,y,color)

        win.plotPixel(x-1,y-1,color)

        win.plotPixel(x-1,y+1,color)
    return

def RetaRadar(x1,y1,x2,y2,color,size):
    x = x1
    y = y1
    p = 0
    DX = x2-x1
    DY = y2-y1
    xInc = 1
    yInc = 1
    if DX < 0:
        xInc = -1
        DX = -DX
    if DY < 0:

        yInc = -1

        DY = -DY

    if DY <= DX:

        p = DX/2
        while x != x2:
            PontoRadar(x,y,color,size)
            p = p-DY
            if p < 0:
                y = y+yInc
                p = p+DX
            x = x+xInc
            continue
    else:
        p = DY/2
        while y != y2:
            PontoRadar(x,y,color,size)
            p = p-DX
            if p < 0:
                x = x+xInc
                p = p+DY
            y = y+yInc
            continue
        PontoRadar(x,y,color,size)

def PontilhadaRadar(x1,y1,x2,y2,color,size):
    x = x1
    y = y1
    p = 0
    conta = 0
    DX = x2-x1
    DY = y2-y1
    xInc = 1
    yInc = 1
    if DX < 0:
        xInc = -1
        DX = -DX
    if DY < 0:
        yInc = -1
        DY = -DY
    if DY <= DX:
        p = DX/2
        while x != x2:
            if (conta % 5 == 0):
                PontoRadar(x,y,color,size)
            conta = conta + 1
            p = p-DY
            if p < 0:
                y = y+yInc
                p = p+DX
            x = x+xInc
            continue
    else:
        p = DY/2
        while y != y2:
            if (conta % 5 == 0):
                PontoRadar(x,y,color,size)
            conta = conta + 1
            p = p-DX
            if p < 0:
                x = x+xInc
                p = p+DY
            y = y+yInc
            continue
        PontoRadar(x,y,color,size)

def TracejadaRadar(x1, y1, x2, y2, color, size):
    x = x1
    y = y1
    p = 0
    contador = 0
    dx = x2 - x1
    dy = y2 - y1
    xInc = 1
    yInc = 1
    if dx < 0:
        xInc = -1
        dx = -dx
    if dy < 0:
        yInc = -1
        dy = -dy
    if dy <= dx:
        p = dx / 2
        while x != x2:
            if contador < 10:
                PontoRadar(x, y, color, size)
            contador = contador + 1

            if contador == 20:
                contador = contador * 0
            p = p - dy
            if p < 0:
                y = y + yInc
                p = p + dx
            x = x + xInc
            continue
    else:
        p = dy / 2
        while y != y2:
            if contador < 10:
                PontoRadar(x, y, color, size)
            contador = contador + 1

            if contador == 20:
                contador = contador * 0
            p = p - dx
            if p < 0:
                x = x + xInc
                p = p + dy
            y = y + yInc
            continue

def CirculoRadar(xc,yc,r,color,size):
    x = 0
    y = r
    p = 5/4-r
    PontoRadar(x,y,color,size)
    while x<y:
        x = x+1
        if p<0:
            p = p + (2*x) + 1
        else:
            y = y-1
            p = p + (2*x) + 1 - (2*y)
            x = x + xc
            y = y + yc

        PontoRadar(x, y, color, size)
        PontoRadar(y, x, color, size)
        PontoRadar(y, -x, color, size)
        PontoRadar(-x, y, color, size)
        PontoRadar(-x, -y, color, size)
        PontoRadar(-y, -x, color, size)
        PontoRadar(-y, x, color, size)
        PontoRadar(x, -y, color, size)

def Texto(x, y, palavra, color, size, estilo):
    t = Text(Point(x, y), palavra)
    t.setOutline(color)
    t.setSize(size)
    t.setStyle(estilo)
    t.draw(win)
    return

def Projetar(x,y,z,f,F,color,size):
    xl = x * f / (F - z)
    yl = y * f / (F - z)
    PontoRadar(xl,yl,color,size)
    return

def Tela_Fundo():
    win = GraphWin("Tela Radar", 1000, 1000)
    win.setBackground(Background)
    win.close()
    while True:
        CirculoRadar(0,0,90,"green",1)
        CirculoRadar(0,0,130,"green",1)
        CirculoRadar(0, 0, 170, "green", 1)
        CirculoRadar(0, 0, 210, "green", 1)
        CirculoRadar(0, 0, 250, "green", 1)
        CirculoRadar(0, 0, 290, "green2", 1)
        TracejadaRadar(230, -180, -230, 180, "green", 1)
        TracejadaRadar(-230, -180, 230, 180, "green", 1)
        TracejadaRadar(0, 290, 0, -290, "green", 1)
        TracejadaRadar(290, 0, -290, 0, "green", 1)
        Texto(400, 22, "0o", "green", 10, "bold")
        Texto(665, 300, "90o", "green", 10, "bold")
        Texto(400, 560, "180o", "green", 10, "bold")
        Texto(140,300, "270o", "green", 10, "bold")
        Projetar(1000, 2000, 3000, 100, 5000, "red",3)

while True:
    Texto(665, 300, "0o", "red", 10, "bold")
    Texto(400, 22, "90o", "red", 10, "bold")
    Texto(400, 560, "180o", "red", 10, "bold")
    Texto(140, 300, "270o", "red", 10, "bold")
    CirculoRadar(0, 0, 10, "green2", 1)
    CirculoRadar(0, 0, 30, "green2", 1)
    CirculoRadar(0, 0, 60, "green2", 1)
    CirculoRadar(0, 0, 90, "green2", 1)
    CirculoRadar(0, 0, 130, "green2", 1)
    CirculoRadar(0, 0, 170, "green2", 1)
    CirculoRadar(0, 0, 210, "green2", 1)
    CirculoRadar(0, 0, 250, "green2", 1)
    CirculoRadar(0, 0, 290, "green2", 1)
    TracejadaRadar(290, 0, -290, 0, "green2", 1)
    TracejadaRadar(0, 290, 0, -290, "green2", 1)
    TracejadaRadar(-230, -180, 230, 180, "green2", 2)
    TracejadaRadar(230, -180, -230, 180, "green2", 2)
    Projetar(1000, 2000, 3000, 100, 5000, "green2", 3)
    