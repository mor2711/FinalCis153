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
        print("Piece {} is {} x {} x {} inches".format(counter,lengthin,widthin,heightin))
        number_of_pieces = int(number_of_pieces) - 1
        counter = counter + 1
    return;
meterstoinches()




