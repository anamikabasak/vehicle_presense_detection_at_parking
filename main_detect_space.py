import os
import time

import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import Dataset, DataLoader
import torchvision
from torchvision import transforms
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

from model.alexnet import AlexNet
from model.malexnet import mAlexNet
from utils import selfData
from utils.imshow import imshow
from utils.options import args_parser
from utils.test import test
from utils.train import train

if __name__=="__main__":
    args = args_parser()
    device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
    transforms = transforms.Compose([
        transforms.Resize(256),
        transforms.RandomResizedCrop(224),
        transforms.ToTensor(),  # normalize to [0, 1]
        transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))
    ])
    if args.imshow == True:
        train_dataset = selfData(args.train_img, args.train_lab, transforms)
        train_loader = DataLoader(train_dataset, batch_size=16, shuffle=True, num_workers=0, drop_last=False)
        imgs, labels = train_loader.__iter__().__next__()
        imshow(train_loader)

    if args.model == 'mAlexNet':
        net = mAlexNet().to(device)
    elif args.model == 'AlexNet':
        net = AlexNet().to(device)

    criterion = nn.CrossEntropyLoss()
    if args.path == '':
        train(args.epochs, args.train_img, args.train_lab, transforms, net, criterion)
        PATH = 'model.pth'
        torch.save(net.state_dict(), PATH)
        if args.model == 'mAlexNet':
            net = mAlexNet().to(device)
        elif args.model == 'AlexNet':
            net = AlexNet().to(device)
        net.load_state_dict(torch.load(PATH))
    else:
        PATH = args.path
        if args.model == 'mAlexNet':
            net = mAlexNet().to(device)
        elif args.model == 'AlexNet':
            net = AlexNet().to(device)
        net.load_state_dict(torch.load(PATH))


    #while True:
    accuracy = test(args.test_img, args.test_lab, transforms, net)
    #time.sleep(30)

    print("\nThe accuracy of training on '{}' and testing on '{}' is {:.3f}.".format(args.train_lab.split('.')[0],
                                                                                     args.test_lab.split('.')[0],
                                                                                     accuracy))