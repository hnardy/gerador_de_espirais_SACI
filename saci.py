
from tkinter import *
import turtle
import sys
import os
import cores_saci as crs

def start():

    pasta = os.path.dirname(__file__)

    op = Tk()
    op.grid()
    op.geometry("1200x720")
    op.title("SACI")

    imagem_blender = PhotoImage(file=pasta+"\\img1.gif")
    foto = Label(op, image=imagem_blender)
    foto.pack()
    stbt = Button(op,text="INICIAR", command=op.destroy)
    stbt.place(x=600,y=650)
    op.mainloop()
    




def ligar():
    cores = []
    def adcor(c):
        cores.append(c)

    def fechar():
        win.destroy()

    def ligar_tartaruga():
        try:
            turtle.clearscreen()
            lin = 0
            angmod = int(a.get())
            linmod = float(b.get())
            repeats = int(c.get())
            espe = int(d.get())
            fator = float(e.get())

            velocity = 1000
            my_pen = turtle.Turtle()
            turtle.bgcolor("black")

            my_pen.speed(velocity)
            pencolors = crs.getcores()

            if pencolors == []:
                pencolors.append("white")

            my_pen.speed(velocity)

            win.geometry("0x0")

            for f in range(0, repeats):
                espe+= fator



                # x.append(math.cos(ang) * rad)
                # y.append(math.sin(ang) * rad)
                my_pen.width(espe)
                turtle.title(f"desenhando: {100 * f / repeats :.2f}%")

                my_pen.pencolor(pencolors[f % len(pencolors)])
                my_pen.forward(lin)
                my_pen.left(angmod)

                lin += linmod
                # print(f"ang{angmod} linmod{linmod}, lin{lin}, Repeats{f}")

            win.geometry("400x400")
            turtle.title(f"pronto! ângulo: {angmod} repetições: {repeats} crescimento hori.{linmod} crescimento vert.{fator}")
            turtle.done()
        except:
            sys.exit()

    win = Tk()
    win.grid()
    win.geometry("400x400")
    win.title("SACI)")

    l1 = Label(win, text="escolha o ângulo")
    l1.grid(column=5, row=0)

    a = Spinbox(win, from_=10, to=359)
    a.grid(column=5, row=2)

    l2 = Label(win, text="digite  o fator de crescimento ")
    l2.grid(column=5, row=4)

    b = Spinbox(win, from_=0.1, to=10.0, increment=0.1, )
    b.grid(column=5, row=6)

    l3 = Label(win, text="digite o número de repetições ")
    l3.grid(column=5, row=8)

    c = Spinbox(win, from_=100, to=10000, increment=100)
    c.grid(column=5, row=10)

    l4 = Label(win, text="espessura da linha")
    l4.grid(column=5, row=12)

    d = Spinbox(win, from_=1, to=10, increment=1)
    d.grid(column=5, row=14)

    l5 = Label(win, text=" fator de engrossamento da linha ")
    l5.grid(column=5, row=16)

    e = Spinbox(win, to=1, increment=0.01)
    e.grid(column=5, row=18)



    bot = Button(win, text="iniciar", command=ligar_tartaruga)
    bot.grid(column=5, row=20)

   # bot = Button(win, text="fechar", command=fechar)
   # bot.grid(column=6, row=20)


    l5 = Label(win, text="seleção de cores")
    l5.grid(column=5, row= 22)

    b_branco = Button(win,text="   ",command=crs.addbranco,background="white")
    b_branco.grid(column= 10, row= 2)

    b_vermelho = Button(win, text="   ", command=crs.addvermelho, background="red")
    b_vermelho.grid(column=10, row=4)

    b_azul = Button(win, text="   ", command=crs.addazul,background="blue")
    b_azul.grid(column=10, row=6)

    b_rosa = Button(win, text="   ", command=crs.addrosa, background="pink")
    b_rosa.grid(column=10, row=8)

    b_verde = Button(win, text="   ", command=crs.addverde, background="green")
    b_verde.grid(column=10, row=10)

    b_amarelo = Button(win, text="   ", command=crs.addamarelo, background="yellow")
    b_amarelo.grid(column=10, row=12)

    b_roxo = Button(win, text="   ", command=crs.addroxo, background="purple")
    b_roxo.grid(column=10, row=14)

    b_turquesa = Button(win, text="   ", command=crs.addturquesa, background="turquoise")
    b_turquesa.grid(column=10, row=16)

    b_laranja = Button(win, text="   ", command=crs.addlaranja, background="orange")
    b_laranja.grid(column=10, row=18)

    b_marrom = Button(win, text="   ", command=crs.addmarrom, background="brown")
    b_marrom.grid(column=10, row=20)

    b_violeta = Button(win, text="   ", command=crs.addvioleta, background="violet")
    b_violeta.grid(column=10, row=22)

    b_preto = Button(win, text="   ", command=crs.addpreto, background="black")
    b_preto.grid(column=10, row=22)


    b_apagarcores = Button(win,text="reiniciar cores",command=crs.apagar)
    b_apagarcores.grid(column=10, row=24)

    win.mainloop()










#start()
ligar()
