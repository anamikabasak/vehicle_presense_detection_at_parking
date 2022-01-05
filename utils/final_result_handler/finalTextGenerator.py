import os


if __name__ == "__main__":
    file_open_final = open("/Users/raktimraihan/Desktop/parking_lot_occupancy_detection-master/finalresult/final_result.txt","r+")
    file_raw_image = open("/Users/raktimraihan/Desktop/parking_lot_occupancy_detection-master/custom_label/image_list.txt", "r+")

    for line in sorted(file_open_final.readlines()):
        i = line.split(" ")
        time = i[0].split("-")
        print("Time: "+str(round(int(time[0])/30,2)+5)+" Spot= "+i[1]+" Frame ID= "+i[0]+" Occupancy= "+i[2])


    file_raw_image.close()
    file_raw_image.close()