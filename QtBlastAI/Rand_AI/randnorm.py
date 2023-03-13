import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np
import pandas as pd
import time
import math

class GenRand(nn.Module):
  def __init__(self, input_size=20, hidden_size=10, output_size=1):
    super().__init__()
    self.lay_num = 3
    self.hidden_size = hidden_size
    self.lstm = nn.LSTM(input_size = input_size, hidden_size=hidden_size, num_layers=self.lay_num)
    self.linear1 = nn.Linear(hidden_size, 10)
    self.linear2 = nn.Linear(10, output_size)    
    self.drop = nn.Dropout(0.001)

  def forward(self, input_seq):
    self.hidden_cell = (torch.zeros(self.lay_num,1,self.hidden_size).cuda(),
                        torch.zeros(self.lay_num,1,self.hidden_size).cuda())

    lstm_out, self.hidden_cell = self.lstm(input_seq.view(-1,1,len(input_seq)), self.hidden_cell)
    lstm_out = self.drop(lstm_out)
    lstm_out = self.linear1(lstm_out.view(-1,self.hidden_size))
    lstm_out = self.drop(lstm_out)
    pred = self.linear2(lstm_out)        

    return pred


def genData(num_series):
  n_elem = 100 # number of element in each series              
  train_data = []

  for na in range(num_series):
    mu = np.random.uniform(1,10)
    std = np.random.uniform(0.2,2)
    rn = np.random.normal(mu,std,n_elem)
    # print(f'mu is {mu}, std is {std}')
    train_data.append(rn)

  return train_data


def ana(tr):
  tr = np.array(tr)
  sum = np.sum(tr)
  ave = np.average(tr)
  std = np.std(tr)
  
  return ave, std


def create_inout_seq(input_data, tw):
  inout_seq = []
  L = len(input_data)
  for i in range(L-tw):
      train_seq = input_data[i:i+tw].reshape(-1,1)
      train_label = input_data[i+tw:i+tw+1].reshape(-1,1)
      # train_label = torch.squeeze(train_label,dim=1)
      inout_seq.append((train_seq ,train_label))
  return inout_seq


def trainModel(model, loss_func, optim, train_seq):
  steps = 500
  model.train()


  for i in range(steps):
    y_p_sum = 0
    y_p_ave = 0
    y_p_std = 0

    y_l_sum = 0
    y_l_ave = 0
    y_l_std = 0

    # y_pred = []
    # y_label = []

    y_pred = torch.zeros(len(train_seq)).cuda()
    y_label = torch.zeros(len(train_seq)).cuda()

    count = 0
    optim.zero_grad()      
    for seq, label in train_seq:

      # print(seq)
      # print(f'label = {label}')
      
      y_p = model(seq)
      
      y_pred[count] = y_p[0]
      y_label[count] = label[0]

      y_p_sum = y_p_sum + y_p[0]
      y_l_sum = y_l_sum + label[0]
      count = count + 1

      # print('-------------------------------------')
      # print(y_pred)
      # print('-------------------------------------')

    y_p_ave = y_p_sum/count
    y_l_ave = y_l_sum/count

    for y_p in y_pred:
      y_p_std = y_p_std + (y_p-y_p_ave)* (y_p-y_p_ave)
      
    y_p_std = (y_p_std) / count

    # print(y_p_sum, y_p_ave, y_p_std)
    
    # y_l_std = 0

    for y_l in y_label:
      y_l_std = y_l_std + (y_l-y_l_ave)* (y_l-y_l_ave)
      
    y_l_std = (y_l_std) / count

    # print(y_l_sum, y_l_ave, y_l_std)

    loss = loss_func(y_p_ave,y_l_ave)  + loss_func(y_p_std,y_l_std)
    # loss = loss_func(y_pred,y_label)
    loss.backward(retain_graph = True)
    optim.step()

    # print(f'average prediction {y_p_ave} std prediction {y_p_std}')
    # print(f'average label {y_l_ave} std label {y_l_std}')
    if i % 10 == 0:
      print(f'i = {i}, loss =  {loss.item()}')

  return y_pred, y_label


def main():
  num_series = 10
  train_window = 20
  epoch = 1
  model = GenRand(train_window,10,1)
  model.cuda()
  loss_func = nn.MSELoss()
  optim = torch.optim.Adam(model.parameters(), lr=0.001)

  train_data = genData(num_series)

  start = time.time()

  for ep in range(epoch):
    for tr in train_data:
      # print (tr)
      ave,std = ana (tr)
      # print(f'average is {ave}, standard deviation is {std}')

      tr = torch.FloatTensor(tr).cuda()
      io_seq = create_inout_seq(tr,train_window)

      # print(np.array(io_seq).shape)
      # io_seq = torch.FloatTensor(io_seq).view(-1)

      trainModel(model, loss_func, optim, io_seq)        

      # print ('io_seq is')
      # print(io_seq)

  end = time.time()

  print(f'time taken for the training is {end - start}')

  #   for tr in train_data:
  #     out = trainModel(model, tr)

if __name__ == "__main__":
  main()