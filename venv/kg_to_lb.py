from datetime import date#imports date so the date can be added to the output to shipmen_log.txt
def meterstoinches():#function to take user input and convert it from metric to US. It displays the conversions and writes it to the shipment log
    order_number = input("What is the order number?")
    number_of_pieces = input("How many pieces are in the shipment?")
    today = date.today()
    d = today.strftime("%b-%d-%Y")
    counter = 1
    while int(number_of_pieces) > 0:
        lengthm = input("What is the length in meters for piece {} ?".format(counter))
        lengthin = float(lengthm) * 39.37
        widthm = input("What is the width in meters for piece {} ?".format(counter))
        widthin = float(widthm) * 39.37
        heightm = input("What is the height in meters for piece {} ?".format(counter))
        heightin = float(heightm) * 39.37
        weightkg = input("What is the weight in kgs for piece {} ?".format(counter))
        weightlb = float(weightkg) * 2.205
        file1 = open("shipment_log.txt","a")
        file1.write("Order Number {} Date {} Piece {} measures {} x {} x {} inches and {} lbs\n".format(order_number,d,counter,lengthin,widthin,heightin,weightlb))
        file1.close()
        print("Piece {} measures {} x {} x {} inches and weighs {} lbs".format(counter,lengthin,widthin,heightin,weightlb))
        number_of_pieces = int(number_of_pieces) - 1
        counter = counter + 1
    return;
# meterstoinches()

def ustometric():#function to take user input and convert it from US to metric. It displays the conversions and writes it to the shipment log
    order_number = input("What is the order number?")
    number_of_pieces = input("How many pieces are in the shipment?")
    today = date.today()
    d = today.strftime("%b-%d-%Y")
    counter = 1
    while int(number_of_pieces) > 0:
        lengthm = input("What is the length in ?".format(counter))
        lengthin = float(lengthm) * .0254
        widthm = input("What is the width in meters for piece {} ?".format(counter))
        widthin = float(widthm) * .0254
        heightm = input("What is the height in meters for piece {} ?".format(counter))
        heightin = float(heightm) * .0254
        weightkg = input("What is the weight in kgs for piece {} ?".format(counter))
        weightlb = float(weightkg) * .45359237
        file1 = open("shipment_log.txt","a")
        file1.write("Order Number {} Date {} Piece {} measures {} x {} x {} meters and {} kgs\n".format(order_number,d,counter,lengthin,widthin,heightin,weightlb))
        file1.close()
        print("Piece {} measures {} x {} x {} meters and kgs {} lbs".format(counter,lengthin,widthin,heightin,weightlb))
        number_of_pieces = int(number_of_pieces) - 1
        counter = counter + 1
    return;
# ustometric()

#this asks what the user wants to do
answer = int(input("What would you like to do? \n Enter 1 to convert Metric to US. \n Enter 2 to convert US to Metric. \n Enter 3 to view shipment log. \n Enter 4 to search shipment log."))
if answer == 1:
    meterstoinches()#runs conversion function
if answer == 2:
    ustometric()#runs conversion function
if answer == 3:
    file1 = open("shipment_log.txt","r")#displays entire shipment log
    for line in file1.readlines():
        print(str(line))
        file1.close()
if answer == 4:
    file1 = open("shipment_log.txt","r")#this section searches each line for the input given by the user and displays all matching lines
    searchterm1 = input("Enter an order number or date in the following format Jan-1-2020")
    searchterm2 = len(searchterm1)+2
    searchterm3 = searchterm1.center(searchterm2)
    for line in file1.readlines():
        if line.__contains__(searchterm3):
            print(line)
