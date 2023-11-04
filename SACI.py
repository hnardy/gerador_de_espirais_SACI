from tkinter import *
import turtle
import sys



def ligar():
    def fechar():
        win.destroy()


    def ligar_tartaruga():
      try:
            turtle.clearscreen()
            angmod, linmod, repeats = 0, 0, 0
            lin = 0
            angmod = int(a.get())
            linmod = float(b.get())
            repeats = int(c.get())
            velocidade = int(d.get())

            my_pen = turtle.Turtle()
            my_pen.width(5)
            turtle.bgcolor("black")

            velocity = velocidade
            my_pen.speed(velocity)
            colors = ["red", "turquoise", "green", "pink", "blue", "yellow", "purple", "white"]

            win.geometry("0x0")

            for f in range(0, repeats):
                my_pen.speed(velocity)
                # x.append(math.cos(ang) * rad)
                # y.append(math.sin(ang) * rad)

                my_pen.pencolor(colors[f % len(colors)])
                my_pen.forward(lin)
                my_pen.left(angmod)

                lin += linmod
                velocity += velocidade
                #print(f"ang{angmod} linmod{linmod}, lin{lin}, Repeats{f}")

            win.geometry("400x400")
            turtle.done()
      except:
          sys.exit()


    win = Tk()
    win.grid()
    win.geometry("400x400")
    win.title("SACI (nome provisório)")

    l1 = Label(win, text= "escolha o ângulo")
    l1.grid(column=5, row=0)

    a = Spinbox(win, from_=10, to= 359)
    a.grid(column=5,row=2)

    l2 = Label(win, text="digite a regra de crescimento (recomendado 0.2)")
    l2.grid(column=5, row=4)

    b = Spinbox(win, from_=0.1, to= 10.0,increment=0.1,)
    b.grid(column=5,row=6)

    l3 = Label(win, text="digite o número de repetições (recomendado 500)")
    l3.grid(column=5,row=8)

    c = Spinbox(win,from_=100, to=1000,increment=100)
    c.grid(column=5, row=10)

    l4 = Label(win, text="velocidade")
    l4.grid(column=5,row=12)

    d = Spinbox(win,from_=1000, to=10000,increment=100)
    d.grid(column=5, row=14)

    bot = Button(win,text="iniciar",command=ligar_tartaruga)
    bot.grid(column=5,row=16)

    bot = Button(win, text="fechar", command=fechar)
    bot.grid(column=6, row=16)

    win.mainloop()



ligar()
