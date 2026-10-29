def create_list_of_parking_slot():
    parking_slot_list = []
    for number in range(1,21) :
        slot_name = "SPACE " + str(number) + ", AVAILABLE";
        parking_slot_list.append([slot_name])
    return parking_slot_list

parking_lot = create_list_of_parking_slot()

def collect_slot_to_secure():
    slot_to_secure = int(input("Enter Space to Book: "))
    return slot_to_secure
    

def slot_availability_checker():
    slot_number = collect_slot_to_secure()
    slot_name = "SPACE " + str(slot_number) + ", AVAILABLE"     
    if parking_lot[slot_number -1][0] == slot_name:
        parking_lot[slot_number -1][0] = "SPACE " + str(slot_number) + ", BOOKED"
        print("Slot is Available, Slot has now been Booked")
        return parking_lot
    else:
        print("Slot is not Available")
        return parking_lot

    
def filled_car_slot_checker():
    if parking_lot[0][0] == "SPACE " + str(1) + ", BOOKED" and parking_lot[1][0] == "SPACE " + str(2) + ", BOOKED" and parking_lot[2][0] == "SPACE " + str(3) + ", BOOKED" and parking_lot[3][0] == "SPACE " + str(4) + ", BOOKED" and parking_lot[4][0] == "SPACE " + str(5) + ", BOOKED" and parking_lot[5][0] == "SPACE " + str(6) + ", BOOKED" and parking_lot[6][0] == "SPACE " + str(7) + ", BOOKED" and parking_lot[7][0] == "SPACE " + str(8) + ", BOOKED" and parking_lot[8][0] == "SPACE " + str(9) + ", BOOKED" and parking_lot[9][0] == "SPACE " + str(10) + ", BOOKED" and parking_lot[10][0] == "SPACE " + str(11) + ", BOOKED" and parking_lot[11][0] == "SPACE " + str(12) + ", BOOKED" and parking_lot[12][0] == "SPACE " + str(13) + ", BOOKED" and parking_lot[13][0] == "SPACE " + str(14) + ", BOOKED" and parking_lot[14][0] == "SPACE " + str(15) + ", BOOKED" and parking_lot[15][0] == "SPACE " + str(16) + ", BOOKED" and parking_lot[16][0] == "SPACE " + str(17) + ", BOOKED" and parking_lot[17][0] == "SPACE " + str(18) + ", BOOKED" and parking_lot[18][0] == "SPACE " + str(19) + ", BOOKED" and parking_lot[19][0] == "SPACE " + str(20) + ", BOOKED":
        return True
    else:
        return False


print(parking_lot)
while (filled_car_slot_checker() == False):
    print(slot_availability_checker())

