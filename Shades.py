from Tkinter import *
from time import *
from math import *

ALTURA = 600
LARGURA = 600
LADO = 150
PAUSA = 0.2
X_c = LARGURA/2
Y_c = ALTURA/2

canvas = Canvas(bg = 'gold', width = LARGURA, height = ALTURA)
canvas.pack()

angulo_q = (2 * pi)/50

cinza = 0
variando = 255/49.0

def quadrado():
    global X0, X1, Y0, Y1, angulo, cinza
    
    linha1 = canvas.create_line(X_c, Y_c, X_c+(LADO*cos(angulo)), Y_c-(LADO*sin(angulo)), width = 5, fill='#%02x%02x%02x' % (cinza, cinza, cinza))
    [X0, Y0, X1, Y1] = canvas.coords(linha1)
    canvas.update()
    sleep(PAUSA)
    angulo -= pi/2
    
    linha2 = canvas.create_line(X1, Y1, X1+(LADO*cos(angulo)), Y1-(LADO*sin(angulo)), width = 5, fill='#%02x%02x%02x' % (cinza, cinza, cinza))
    [X0, Y0, X1, Y1] = canvas.coords(linha2)
    canvas.update()
    sleep(PAUSA)
    angulo -= pi/2
    
    linha3 = canvas.create_line(X1, Y1, X1+(LADO*cos(angulo)), Y1-(LADO*sin(angulo)), width = 5, fill='#%02x%02x%02x' % (cinza, cinza, cinza))
    [X0, Y0, X1, Y1] = canvas.coords(linha3)
    canvas.update()
    sleep(PAUSA)
    angulo -= pi/2
    
    linha4 = canvas.create_line(X1, Y1, X1+(LADO*cos(angulo)), Y1-(LADO*sin(angulo)), width = 5, fill='#%02x%02x%02x' % (cinza, cinza, cinza))
    canvas.update()
    sleep(PAUSA)
    
    cinza += variando

#########################################################################################    

while True:
    for i in range(50):
        angulo = -(angulo_q*i)
        quadrado()
    cinza = 0
    canvas.delete(ALL)
    
mainloop()
