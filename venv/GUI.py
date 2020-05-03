import tkinter as tk #imports tkinter to create GUI
from tkinter import * #imports everything in tkinter
from datetime import date #imports date so it can be added to shipment log
today = date.today()
d = today.strftime("%b-%d-%Y") #creates a variable of the date from the system in Jan-1-2020 format

def chart(pieces,order): #creates a chart for conversions based on piece count
    Names = [] #creates a list to hold variable names
    count = 1
    counter1 = 1
    counter2 = 0
    pieces2 = pieces
    for x in range(pieces*4): #creates the list of variable names neeeded to create the chart
        Names += ["e"+str(count)]
        count = count + 1
    def convertustometric():#function to take user input and convert it from US to metric. It displays the conversions and writes it to the shipment log
        counter3 = 0
        counter4 = 1
        counter5 = 0
        Names2 = []
        for x in range(pieces):
            Names2 += [float(Names[0+counter3].get()) * .0254]
            Names2 += [float(Names[1+counter3].get()) * .0254]
            Names2 += [float(Names[2+counter3].get()) * .0254]
            Names2 += [float(Names[3+counter3].get()) * .45359237]
            file1 = open("shipment_log.txt","a")
            file1.write("Order Number {} Date {} Piece {} measures {} x {} x {} meters and {} kgs\n".format(order,d,counter4,Names2[0+counter3],Names2[1+counter3],Names2[2+counter3],Names2[3+counter3]))
            file1.close()
            counter3 = counter3 + 4
            counter4 = counter4 + 1
        for x in range(pieces):
            Label(Converter,text="{} meters".format(Names2[0+counter5])).grid(row=3 + counter5,column=2)
            Label(Converter,text="{} meters".format(Names2[1+counter5])).grid(row=4 + counter5,column=2)
            Label(Converter,text="{} meters".format(Names2[2+counter5])).grid(row=5 + counter5,column=2)
            Label(Converter,text="{} KG".format(Names2[3+counter5])).grid(row=6 + counter5,column=2)
            counter5 = counter5 + 4

    def convertmetrictous():#function to take user input and convert it from metric to US. It displays the conversions and writes it to the shipment log
        counter6 = 0
        counter7 = 1
        counter8 = 0
        Names3 = []
        for x in range(pieces):
            Names3 += [float(Names[0+counter6].get()) * 39.37]
            Names3 += [float(Names[1+counter6].get()) * 39.37]
            Names3 += [float(Names[2+counter6].get()) * 39.37]
            Names3 += [float(Names[3+counter6].get()) * 2.205]
            file1 = open("shipment_log.txt","a")
            file1.write("Order Number {} Date {} Piece {} measures {} x {} x {} meters and {} kgs\n".format(order,d,counter7,Names3[0+counter6],Names3[1+counter6],Names3[2+counter6],Names3[3+counter6]))
            file1.close()
            counter6 = counter6 + 4
            counter7 = counter7 + 1
        for x in range(pieces):
            Label(Converter,text="{} meters".format(Names3[0+counter8])).grid(row=3 + counter8,column=2)
            Label(Converter,text="{} meters".format(Names3[1+counter8])).grid(row=4 + counter8,column=2)
            Label(Converter,text="{} meters".format(Names3[2+counter8])).grid(row=5 + counter8,column=2)
            Label(Converter,text="{} KG".format(Names3[3+counter8])).grid(row=6 + counter8,column=2)
            counter8 = counter8 + 4


    while pieces2 > 0:#creates the chart to enter measurmentrs based on piece count. Uses list created earlier so each text entry box has a unique name.
        Label(Converter,text="piece {} length".format(counter1)).grid(row=3 + counter2,column=0)
        Label(Converter,text="piece {} width".format(counter1)).grid(row=4 + counter2,column=0)
        Label(Converter,text="piece {} heigth".format(counter1)).grid(row=5 + counter2,column=0)
        Label(Converter,text="piece {} weigth".format(counter1)).grid(row=6 + counter2,column=0)
        length= DoubleVar()
        width= DoubleVar()
        heigth= DoubleVar()
        weigth= DoubleVar()
        Names[0+counter2] = Entry(Converter,textvariable=length)
        Names[1+counter2] = Entry(Converter,textvariable=width)
        Names[2+counter2] = Entry(Converter,textvariable=heigth)
        Names[3+counter2] = Entry(Converter,textvariable=weigth)
        Names[0+counter2].grid(row=3 + counter2,column=1)
        Names[1+counter2].grid(row=4 + counter2,column=1)
        Names[2+counter2].grid(row=5 + counter2,column=1)
        Names[3+counter2].grid(row=6 + counter2,column=1)
        counter1 = counter1 + 1
        counter2 = counter2 + 4
        pieces2 = pieces2 - 1
        ustometric = Button(Converter,text="Convert US to Metric",command= lambda: convertustometric()).grid(row=2,column=2)
        metrictous = Button(Converter,text="Convert Metric to US",command= lambda: convertmetrictous()).grid(row=2,column=0)
    return;

Converter=tk.Tk() #creates the main window
Converter.title("Measurement Converter") #labels the main window
x=Label(Converter,text="Order Number").grid(row=0) #creates a label for the ordernumber entry box and places it
y=Label(Converter,text="Number of pieces").grid(row=1) #creates a label for the pieces entry box and places it
order_number = IntVar() #creates a variable type for the order number
pieces = IntVar() #creates a variable type for the piece count
entry1 = Entry(Converter,textvariable=order_number) #creates a text entry box that corresponds to the order number variable
entry2 = Entry(Converter,textvariable=pieces) #creates a text entry box that corresponds to the piece count
entry1.grid(row=0,column=1) #places the order number entry box
entry2.grid(row=1,column=1) #places the piece count entry box

next = Button(Converter,text="next", command= lambda: chart(int(pieces.get()),int(order_number.get()))).grid(row=2,column=1)
#this is a button that calls the chart funtion when clicked
Converter.mainloop()

