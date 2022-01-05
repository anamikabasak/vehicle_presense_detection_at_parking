import os

from utils.dataloader import selfData, collate_fn
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import Dataset, DataLoader
import torchvision
from torchvision import transforms

def create_dir(path):
    try:
        if not os.path.exists(path):
            os.makedirs(path)
    except OSError:
        print(f"ERROR: creating directory with name {path}")

def test(img_path, target_path, transforms, net):
    print("\nTesting starts now...")
    test_dataset = selfData(img_path, target_path, transforms)
    test_loader = DataLoader(test_dataset, batch_size=1, shuffle=True, num_workers=0, collate_fn=collate_fn)
    correct = 0
    total = 0
    item = 1

    final_result_dir = "/Users/raktimraihan/Desktop/parking_lot_occupancy_detection-master/finalresult"
    create_dir(final_result_dir)

    with torch.no_grad():
        for data in test_loader:
            images, labels, images_path = data
            print("Testing on batch {}".format(item))
            labels = list(map(int, labels))
            labels = torch.Tensor(labels)
            if torch.cuda.is_available():
                device = torch.device("cuda:0")
                images = images.to(device)
                labels = labels.to(device)
            outputs = net(images)
            _, predicted = torch.max(outputs.data, 1)
            print(images_path, predicted)
            file = open(final_result_dir+"/final_result.txt","a+")
            image_name_combined = str(images_path).rsplit("/")
            image_name = str(image_name_combined[-1]).rsplit(".")
            parking_spot = str(image_name[1]).split("-")
            predicted_value = str(predicted.numpy()[0])
            file.write(image_name[0]+" "+ parking_spot[1]+" "+ str(predicted_value)+"\n")

            total += labels.size(0)
            # correct += (predicted == labels).sum().item()
            item += 1
            file.close()

    return 1  # (correct/total)
