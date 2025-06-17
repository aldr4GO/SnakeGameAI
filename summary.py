import torch
from torchinfo import summary

from model import Linear_QNet, QTrainer

model = Linear_QNet(11,256,3)
model.load_state_dict(torch.load("model_weights\model.pth"))

print("weights loaded successfuly !!!")

print(summary(model, input_size=(11,)))