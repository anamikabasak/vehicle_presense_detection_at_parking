from subprocess import call
import torch

if __name__ == "__main__":
    call(["python", "/Users/raktimraihan/Desktop/parking_lot_occupancy_detection-master/utils/imageCaptureHandler"
                    "/imageCapture.py"])
    call(["python", "/Users/raktimraihan/Desktop/parking_lot_occupancy_detection-master/utils/imageCropHandler/imageCrop.py"])
    call(["python", "../../main_detect_space.py"])
    call(["python", "/Users/raktimraihan/Desktop/parking_lot_occupancy_detection-master/utils/final_result_handler/finalTextGenerator.py"])
