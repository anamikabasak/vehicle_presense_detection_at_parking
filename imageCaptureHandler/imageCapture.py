import numpy as np
import cv2
import os


def create_dir(path):
    try:
        if not os.path.exists(path):
            os.makedirs(path)
    except OSError:
        print(f"ERROR: creating directory with name {path}")


if __name__ == "__main__":
    videos_path = "/Users/raktimraihan/Desktop/parking_lot_occupancy_detection-master/video/inside_garage_13.mp4"
    save_dir = "/Users/raktimraihan/Desktop/parking_lot_occupancy_detection-master/custom_images";
    label_text_dir = "/Users/raktimraihan/Desktop/parking_lot_occupancy_detection-master/custom_label"
    label_text_file_name = 'image_list.txt'

    create_dir(save_dir)
    create_dir(label_text_dir)

    file = open(label_text_dir + "/" + label_text_file_name, "w+");

    cap = cv2.VideoCapture(videos_path)
    fps = cap.get(cv2.CAP_PROP_FPS)
    index = 1
    gap = 150
    count = 1
    print("FPS= " + str(round(fps, 2)) + ", Interval=" + str(round((gap / fps), 2)) + " frames.")

    while (cap.isOpened()):
        ret, frame = cap.read()
        if ret == False:
            break
        if index == 1:
            cv2.imwrite(save_dir + '/' + str(index) + '-cam1.jpg', frame)
            file.write(str(index) + '-cam1.jpg ' + str(count * round(gap / fps, 2)) + "\n")
            count += 1
        if index % gap == 0:
            cv2.imwrite(save_dir + '/' + str(index) + '-cam1.jpg', frame)
            file.write(str(index) + '-cam1.jpg ' + str(count * round(gap / fps, 2)) + "\n")
            count += 1
        index += 1

    file.close()
    cap.release()
    cv2.destroyAllWindows()
