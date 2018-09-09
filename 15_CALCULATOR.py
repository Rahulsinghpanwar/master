from tkinter import *

app = Tk()

app.title("calculator")

app.geometry("230x230")

app.resizable(0,0)

equa = ""

expression = StringVar()

'''row 0'''
operation = Label(app, textvariable = expression , fg = 'red')
operation.grid(columnspan = 3, ipadx = '10' , ipady = '10')

expression.set("enter any expression")


def express(num):
     global equa
     if equa == '':
          if num == 0:
               pass
          else:
               equa = equa + str(num)
               expression.set(equa)
     else:
          equa = equa + str(num)
          expression.set(equa)


def equals():
     global equa
     try:
          equa = str(eval(str(equa)))
          expression.set(equa)
     except ZeroDivisionError:
          equa = ''
          expression.set("can't divide by zero")

def back():
     global equa
     length = len(equa)-1
     equa = equa[:length]
     expression.set(equa)

'''row 0'''
backspace = Button(app,text = '<-', fg = 'blue',command = lambda:back())
backspace.grid(row = 0 , column = 3, ipadx = '20', ipady ='10')


'''row 1'''
button1 = Button(app,text = '1', fg = 'blue',command = lambda:express("1"))
button1.grid(row = 1 , column = 0, ipadx = '20', ipady ='10')

button2 = Button(app,text = '2', fg = 'blue',command = lambda:express("2"))
button2.grid(row = 1 , column = 1,  ipadx = '20', ipady ='10')

button3 = Button(app,text = '3', fg = 'blue',command = lambda:express("3"))
button3.grid(row = 1 , column = 2,  ipadx = '20', ipady ='10')

divide = Button(app,text = '/', fg = 'blue',command = lambda:express("/"))
divide.grid(row = 1 , column = 3,  ipadx = '24', ipady ='10')


'''row 2'''
button4 = Button(app,text = '4', fg = 'blue',command = lambda:express("4"))
button4.grid(row = 2 , column = 0 ,  ipadx = '20', ipady ='10')

button5 = Button(app,text = '5', fg = 'blue',command = lambda:express("5"))
button5.grid(row = 2 , column = 1 ,  ipadx = '20', ipady ='10')

button6 = Button(app,text = '6', fg = 'blue',command = lambda:express("6"))
button6.grid(row = 2 , column = 2,  ipadx = '20', ipady ='10')

multiply = Button(app,text = 'x', fg = 'blue',command = lambda:express("*"))
multiply.grid(row = 2 , column = 3,  ipadx = '24', ipady ='10')


'''row 3'''
button7 = Button(app,text = '7', fg = 'blue',command = lambda:express("7"))
button7.grid(row = 3 , column = 0,  ipadx = '20', ipady ='10')

button8 = Button(app,text = '8', fg = 'blue',command = lambda:express("8"))
button8.grid(row = 3 , column = 1,  ipadx = '20', ipady ='10')

button9 = Button(app,text = '9', fg = 'blue',command = lambda:express("9"))
button9.grid(row = 3 , column = 2,  ipadx = '20', ipady ='10')

minus = Button(app,text = '-', fg = 'blue',command = lambda:express("-"))
minus.grid(row = 3 , column = 3,  ipadx = '24', ipady ='10')

'''row 4'''
clear = Button(app,text = '.', fg = 'blue',command = lambda:express("."))
clear.grid(row = 4 , column = 0,  ipadx = '21.5', ipady ='10')

button0 = Button(app,text = '0', fg = 'blue',command = lambda:express("0"))
button0.grid(row = 4 , column = 1,  ipadx = '20', ipady ='10')

equal = Button(app,text = '=', fg = 'blue',command = lambda:equals())
equal.grid(row = 4 , column = 2,  ipadx = '19', ipady ='10')

plus = Button(app,text = '+', fg = 'blue',command = lambda:express("+"))
plus.grid(row = 4 , column = 3,  ipadx = '23', ipady ='10')


app.mainloop()
