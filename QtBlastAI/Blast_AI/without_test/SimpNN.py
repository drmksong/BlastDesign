import torch
import torch.nn as nn

col_size = 5
out_size = 3

class SimpNN(nn.Module):
    def __init__(self, input_size=col_size, hidden_layer_size=300, output_size=out_size):
        super().__init__()
        self.hidden_layer_size = hidden_layer_size
        self.drop1 = nn.Dropout(0.01)        
        self.drop2 = nn.Dropout(0.02)        
        self.relu = nn.LeakyReLU()
        self.linear1 = nn.Linear(input_size, self.hidden_layer_size)
        self.linear2 = nn.Linear(self.hidden_layer_size, 200)
        self.linear3 = nn.Linear(200, output_size)        
        # self.linear3 = nn.Linear(100, 20)
        # self.linear4 = nn.Linear(20, output_size)

    def forward(self, input):
        out = self.linear1(input)
        out = self.relu(out)
        out = self.drop2(out)
        out = self.linear2(out)
        out = self.relu(out)
        out = self.drop1(out)        
        pred = self.linear3(out)        
        # lstm_out = self.linear3(lstm_out)        
        # predictions = self.linear4(lstm_out)        
        return pred
