import cv2
import numpy as np
from utils.dataloader import selfData
import matplotlib.image as mpimg
import matplotlib.pyplot as plt

img = cv2.imread("colors.jpg")
import os


def create_dir(path):
    try:
        if not os.path.exists(path):
            os.makedirs(path)
    except OSError:
        print(f"ERROR: creating directory with name {path}")


if __name__ == "__main__":
    cropped_image_path = "/Users/raktimraihan/Desktop/parking_lot_occupancy_detection-master/custom_cropped_image"
    cropped_image_label = "/Users/raktimraihan/Desktop/parking_lot_occupancy_detection-master/custom_cropped_image_label"
    cropped_image_label_text = "image_list_cropped.txt"
    custom_image_label_root = "/Users/raktimraihan/Desktop/parking_lot_occupancy_detection-master/custom_images"

    create_dir(cropped_image_path)
    create_dir(cropped_image_label)

    file_txt_crop = open(cropped_image_label + "/" + cropped_image_label_text, "w+")
    file_txt_main_image = open(
        "/Users/raktimraihan/Desktop/parking_lot_occupancy_detection-master/custom_label/image_list.txt", "r+")

    for aline in file_txt_main_image:
        values = aline.split(" ")
        print(values[0])
        image = cv2.imread(custom_image_label_root + "/" + values[0])
        print(image.shape)

        img = mpimg.imread(custom_image_label_root + "/" + values[0])
        imgplot = plt.imshow(img)
        plt.show()

        cropped_image = image[50:350, 50:300]
        resized_image = cv2.resize(cropped_image,(145,145), interpolation=cv2.INTER_LINEAR)
        cv2.imwrite(cropped_image_path+"/"+values[0]+"-part01.jpg", resized_image)
        file_txt_crop.write(values[0]+"-part01.jpg"+" 0\n")

        cropped_image = image[50:300, 280:540]
        resized_image = cv2.resize(cropped_image, (145, 145), interpolation=cv2.INTER_LINEAR)
        cv2.imwrite(cropped_image_path + "/" + values[0] + "-part02.jpg", resized_image)
        file_txt_crop.write(values[0] + "-part02.jpg" + " 0\n")

        cropped_image = image[150:1000, 1140:1760]
        resized_image = cv2.resize(cropped_image, (145, 145), interpolation=cv2.INTER_LINEAR)
        cv2.imwrite(cropped_image_path + "/" + values[0] + "-part03.jpg", resized_image)
        file_txt_crop.write(values[0] + "-part03.jpg" + " 0\n")

    file_txt_crop.close()
    file_txt_main_image.close()
