from tkinter import *

# button commands


def btClick1():
    try:
        float(ed1.get()) and float(ed2.get())
        soma = float(ed1.get()) + float(ed2.get())
        lb5['text'] = lb5['text'] + str(soma)
    except ValueError:
        lb5['text'] = 'erro: digite números'


def btClick2():
    try:
        resposta = eval(ed1.get())
        lb5['text'] = resposta
    except SyntaxError:
        lb5['text'] = 'ops algo de errado aconteceu.'
    except ZeroDivisionError:
        lb5['text'] = 'Não é possivel dividir por 0'


def btClick5():
    lb5['text'] = ''
    texto.set('')


var = ""


def mostra(a):
    global var, ed1
    if a.widget == bt0:
        var = "0"
        ed1.insert(END, var)
    elif a.widget == bt1:
        var = "1"
        ed1.insert(END, var)
    elif a.widget == bt2:
        var = "2"
        ed1.insert(END, var)
    elif a.widget == bt3:
        var = "3"
        ed1.insert(END, var)
    elif a.widget == bt4:
        var = "4"
        ed1.insert(END, var)
    elif a.widget == bt5:
        var = "5"
        ed1.insert(END, var)
    elif a.widget == bt6:
        var = "6"
        ed1.insert(END, var)
    elif a.widget == bt7:
        var = "7"
        ed1.insert(END, var)
    elif a.widget == bt8:
        var = "8"
        ed1.insert(END, var)
    elif a.widget == bt9:
        var = "9"
        ed1.insert(END, var)
    elif a.widget == btsoma:
        var = "+"
        ed1.insert(END, var)
    elif a.widget == btsubtrai:
        var = "-"
        ed1.insert(END, var)
    elif a.widget == btmulti:
        var = "*"
        ed1.insert(END, var)
    elif a.widget == btpotenc:
        var = "**"
        ed1.insert(END, var)
    elif a.widget == btdivide:
        var = "/"
        ed1.insert(END, var)


# interface look
janela = Tk()
janela.title("Calculadora")
janela['bg'] = 'turquoise'
janela.geometry('470x330')

lb1 = Label(janela, text='Simple Calculator', bg='turquoise', fg='black')
lb1.place(x=135, y=10)

lb2 = Label(janela, text='valor1', bg='turquoise')
lb2.place(x=45, y=55)
texto = StringVar()
ed1 = Entry(janela, width=18, textvariable=texto)
ed1.place(x=30, y=80)

lbextra = Label(janela, text='=', bg='turquoise')
lbextra.place(x=200, y=80)
lb5 = Label(janela, bg='turquoise', fg='red')
lb5.place(x=230, y=80)
lb6 = Label(janela, text='resultado', bg='turquoise')
lb6.place(x=220, y=55)

# botões dos operadores aritimeticos
btsoma = Button(janela, width=4, text='+', bg='dark orange')
btsoma.place(x=10, y=140)
btsubtrai = Button(janela, width=4, text='-', bg='dark orange')
btsubtrai.place(x=90, y=140)
btmulti = Button(janela, width=4, text='x', bg='dark orange')
btmulti.place(x=10, y=180)
btdivide = Button(janela, width=4, text='%', bg='dark orange')
btdivide.place(x=90, y=180)
btlimpa = Button(janela, width=13, text='C',
                 command=btClick5, bg='dark orange')
btlimpa.place(x=10, y=260)
btpotenc = Button(janela, width=4, text='x²', bg='dark orange')
btpotenc.place(x=10, y=220)

# botões dos numeros
bt1 = Button(janela, width=4, text='1', bg='gold')
bt1.place(x=180, y=120)
bt2 = Button(janela, width=4, text='2', bg='gold')
bt2.place(x=250, y=120)
bt3 = Button(janela, width=4, text='3', bg='gold')
bt3.place(x=180, y=160)
bt4 = Button(janela, width=4, text='4', bg='gold')
bt4.place(x=250, y=160)
bt5 = Button(janela, width=4, text='5', bg='gold')
bt5.place(x=180, y=200)
bt6 = Button(janela, width=4, text='6', bg='gold')
bt6.place(x=250, y=200)
bt7 = Button(janela, width=4, text='7', bg='gold')
bt7.place(x=180, y=240)
bt8 = Button(janela, width=4, text='8', bg='gold')
bt8.place(x=250, y=240)
bt9 = Button(janela, width=4, text='9', bg='gold')
bt9.place(x=180, y=280)
bt0 = Button(janela, width=4, text='0', bg='gold')
bt0.place(x=250, y=280)
btigual = Button(janela, width=4, text='=', command=btClick2, bg='dark orange')
btigual.place(x=90, y=220)

bt0.bind("<Button-1>", mostra)
bt1.bind("<Button-1>", mostra)
bt2.bind("<Button-1>", mostra)
bt3.bind("<Button-1>", mostra)
bt4.bind("<Button-1>", mostra)
bt5.bind("<Button-1>", mostra)
bt6.bind("<Button-1>", mostra)
bt7.bind("<Button-1>", mostra)
bt8.bind("<Button-1>", mostra)
bt9.bind("<Button-1>", mostra)
btsoma.bind("<Button-1>", mostra)
btsubtrai.bind("<Button-1>", mostra)
btmulti.bind("<Button-1>", mostra)
btdivide.bind("<Button-1>", mostra)
btpotenc.bind("<Button-1>", mostra)

janela.mainloop()
