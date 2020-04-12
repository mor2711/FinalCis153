def meterstoinches():
    number_of_pieces = input("How many pieces are in the shipment?")
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
        print("Piece {} measures {} x {} x {} inches and weighs {} lbs".format(counter,lengthin,widthin,heightin,weightlb))
        number_of_pieces = int(number_of_pieces) - 1
        counter = counter + 1
    return;
# meterstoinches()

def ustometric():
    number_of_pieces = input("How many pieces are in the shipment?")
    counter = 1
    while int(number_of_pieces) > 0:
        lengthm = input("What is the length in meters for piece {} ?".format(counter))
        lengthin = float(lengthm) * .0254
        widthm = input("What is the width in meters for piece {} ?".format(counter))
        widthin = float(widthm) * .0254
        heightm = input("What is the height in meters for piece {} ?".format(counter))
        heightin = float(heightm) * .0254
        weightkg = input("What is the weight in kgs for piece {} ?".format(counter))
        weightlb = float(weightkg) * .45359237
        print("Piece {} measures {} x {} x {} meters and kgs {} lbs".format(counter,lengthin,widthin,heightin,weightlb))
        number_of_pieces = int(number_of_pieces) - 1
        counter = counter + 1
    return;
ustometric()


