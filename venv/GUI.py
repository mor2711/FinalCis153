import tkinter as tk
from tkinter import *
list = []
def chart(pieces,order):
    def convert():
        counter2 = 0
        while counter1 > 0:
            a = e1.grid(row=3 + counter2,column=1) * 39.37
            b = e2.grid(row=4 + counter2,column=1) * 39.37
            c = e3.grid(row=5 + counter2,column=1) * 39.37
            d = e4.grid(row=6 + counter2,column=1) * 2.205
            file1 = open(shipments,"a")
            file1.writelines("Order Number {} Piece number {} Length {} Width {} Heigth {} Weigth {}"+ "\n".format(float(a),float(b),float(c),float(d)))
            file1.close
            chart.counter1= chart.counter1 - 1
            counter2 = counter2 + 4
        return;
    counter1 = 1
    counter2 = 0
    while pieces > 0:
        Label(Converter,text="piece {} length".format(counter1)).grid(row=3 + counter2,column=0)
        Label(Converter,text="piece {} width".format(counter1)).grid(row=4 + counter2,column=0)
        Label(Converter,text="piece {} heigth".format(counter1)).grid(row=5 + counter2,column=0)
        Label(Converter,text="piece {} weigth".format(counter1)).grid(row=6 + counter2,column=0)
        length= DoubleVar()
        width= DoubleVar()
        heigth= DoubleVar()
        weigth= DoubleVar()
        e1 = Entry(Converter,textvariable=length)
        e2 = Entry(Converter,textvariable=width)
        e3 = Entry(Converter,textvariable=heigth)
        e4 = Entry(Converter,textvariable=weigth)
        e1.grid(row=3 + counter2,column=1)
        e2.grid(row=4 + counter2,column=1)
        e3.grid(row=5 + counter2,column=1)
        e4.grid(row=6 + counter2,column=1)

        pieces = pieces -1
        counter1 = counter1 + 1
        counter2 = counter2 + 4
        process = Button(Converter,text="Convert",command= lambda: convert()).grid(row=2,column=2)
    return;
Converter=tk.Tk()
Converter.title("Measurement Converter")
x=Label(Converter,text="Order Number").grid(row=0)
y=Label(Converter,text="Number of pieces").grid(row=1)
order_number = IntVar()
pieces = IntVar()
entry1 = Entry(Converter,textvariable=order_number)
entry2 = Entry(Converter,textvariable=pieces)
entry1.grid(row=0,column=1)
entry2.grid(row=1,column=1)

next = Button(Converter,text="next", command= lambda: chart(int(pieces.get()),int(order_number.get()))).grid(row=2,column=1)

Converter.mainloop()
