import os
import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np
import pandas as pd
import time
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import MinMaxScaler

# global variable
sub = './separated/'
scaler = MinMaxScaler()

#            0    1    2    3    4         5          6           23          24 
# input : [ exp, det, rot, roc, cen, scale dist, vibration ... scale dist, vibration ] 
# output: [  sd, vib ]
class GenBlast(nn.Module):
  def __init__(self, input_size=24, hidden_size=50, output_size=2):
    super().__init__()
    self.lay_num = 3
    self.hidden_size = hidden_size
    self.lstm = nn.LSTM(input_size = input_size, hidden_size=hidden_size, num_layers=self.lay_num)
    self.linear1 = nn.Linear(hidden_size, 30)
    self.linear2 = nn.Linear(30, output_size)    
    self.drop = nn.Dropout(0.01)

  def forward(self, input_seq):
    self.hidden_cell = (torch.zeros(self.lay_num,1,self.hidden_size).cuda(),
                        torch.zeros(self.lay_num,1,self.hidden_size).cuda())

    lstm_out, self.hidden_cell = self.lstm(input_seq.view(-1,1,len(input_seq)), self.hidden_cell)
    lstm_out = self.drop(lstm_out)
    lstm_out = self.linear1(lstm_out.view(-1,self.hidden_size))
    lstm_out = self.drop(lstm_out)
    pred = self.linear2(lstm_out)        

    return pred

def evalModel(model, loss_func, inp_valid, lab_valid):
  nseq = 100
  model.eval()
  model.cuda()

  count = 0
  y_pred = torch.zeros(len(inp_valid),3).cuda()
  y_label = torch.zeros(len(inp_valid),3).cuda()

  with torch.no_grad():  
    for inp, lab in zip(inp_valid, lab_valid):
      inp_iter = inp
      pred_lst = np.zeros((nseq,2),dtype=np.float)    
      
      for i in range(nseq):    
        # print(inp, lab)      
        y_p = model(inp_iter)
        # print(y_p.size())

        pred_lst[i,0] = y_p[0,0].item()
        pred_lst[i,1] = y_p[0,1].item()

        inp_iter[5] = y_p[0,0].item()
        inp_iter[6] = y_p[0,1].item()

      # print(len(pred_lst),inp_iter)

      K,n,s = lin_reg(pred_lst[:,0].reshape(-1,1),pred_lst[:,1].reshape(-1,1))

      y_pred[count] = torch.FloatTensor([K,n,s])
      y_label[count] = lab

      # print('prediction: ',y_pred[count])
      # print('truth',y_label[count])

      count = count + 1

    # print('prediction: ',y_pred)
    # print('truth',y_label)
    
    loss = loss_func(y_pred[:,0],y_label[:,0]) 
    loss = loss + loss_func(y_pred[:,1],y_label[:,1])
    loss = loss + loss_func(y_pred[:,2],y_label[:,2])
        
    valid_err = loss.item()
    # print(valid_err)

  return valid_err


def trainModel(model, loss_func, optim, inp_train, lab_train):
  nseq = 100
  model.train()
  model.cuda()

  count = 0
  y_pred = torch.zeros(len(inp_train),3).cuda()
  y_label = torch.zeros(len(inp_train),3).cuda()
  
  optim.zero_grad()      
  
  for inp, lab in zip(inp_train, lab_train):
    inp_iter = inp
    pred_lst = np.zeros((nseq,2),dtype=np.float)    
    
    for i in range(nseq):    
      # print(inp, lab)      
      y_p = model(inp_iter)
      # print(y_p.size())

      pred_lst[i,0] = y_p[0,0].item()
      pred_lst[i,1] = y_p[0,1].item()

      inp_iter[5] = y_p[0,0].item()
      inp_iter[6] = y_p[0,1].item()

    # print(len(pred_lst),inp_iter)

    K,n,s = lin_reg(pred_lst[:,0].reshape(-1,1),pred_lst[:,1].reshape(-1,1))

    y_pred[count] = torch.FloatTensor([K,n,s])
    y_label[count] = lab

    # print('prediction: ',y_pred[count])
    # print('truth',y_label[count])

    count = count + 1

  # print('prediction: ',y_pred)
  # print('truth',y_label)
  
  loss = loss_func(y_pred[:,0],y_label[:,0]) 
  loss = loss + loss_func(y_pred[:,1],y_label[:,1])
  loss = loss + loss_func(y_pred[:,2],y_label[:,2])
  loss.requires_grad = True
  
  train_err = loss.item()
  # print(train_err)
  
  loss.backward(retain_graph = True)
  optim.step()

  return train_err

  #     # print(seq)
  #     # print(f'label = {label}')
      
  #     y_p = model(seq)
      
  #     y_pred[count] = y_p[0]
  #     y_label[count] = label[0]

  #     y_p_sum = y_p_sum + y_p[0]
  #     y_l_sum = y_l_sum + label[0]
  #     count = count + 1

  #     # print('-------------------------------------')
  #     # print(y_pred)
  #     # print('-------------------------------------')

  #   y_p_ave = y_p_sum/count
  #   y_l_ave = y_l_sum/count

  #   for y_p in y_pred:
  #     y_p_std = y_p_std + (y_p-y_p_ave)* (y_p-y_p_ave)
      
  #   y_p_std = (y_p_std) / count

  #   # print(y_p_sum, y_p_ave, y_p_std)
    
  #   # y_l_std = 0

  #   for y_l in y_label:
  #     y_l_std = y_l_std + (y_l-y_l_ave)* (y_l-y_l_ave)
      
  #   y_l_std = (y_l_std) / count

  #   # print(y_l_sum, y_l_ave, y_l_std)

  #   loss = loss_func(y_p_ave,y_l_ave)  + loss_func(y_p_std,y_l_std)
  #   # loss = loss_func(y_pred,y_label)
  #   loss.backward(retain_graph = True)
  #   optim.step()

  #   # print(f'average prediction {y_p_ave} std prediction {y_p_std}')
  #   # print(f'average label {y_l_ave} std label {y_l_std}')
  #   if i % 10 == 0:
  #     print(f'i = {i}, loss =  {loss.item()}')

  # return y_pred, y_label


# def lin_reg(fl):
#   df = pd.read_csv(sub+fl)
#   x = df['SR SD'].to_numpy().reshape(-1,1)
#   y = df['최대입자속도'].to_numpy().reshape(-1,1)
#   x = np.log(x)
#   y = np.log(y)
#   # print(x,y)

#   lin_fit = LinearRegression()
#   lin_fit.fit(x,y)
#   print(f'b = {np.exp(lin_fit.intercept_)}, a = {lin_fit.coef_}') 
#   return np.exp(lin_fit.intercept_), lin_fit.coef_

# return the analysis of the points
def lin_reg(x,y):
  x = np.log(np.abs(x))
  y = np.log(np.abs(y))

  lin_fit = LinearRegression()
  lin_fit.fit(x,y)

  n = lin_fit.coef_[0,0]
  K = lin_fit.intercept_[0]

  sqr = np.sqrt(K*K+n*n)
  D = (n*x-y+K)/sqr # distance to the regression line of every point

  # Ave = np.mean(D)
  s = np.std(D)

  # print(f'K = {np.exp(K)}, n = {n}, s = {s}') 

  return np.exp(K), n, s


# def synthesis(flist):
#   sqrf = 'sqr_data.csv'
#   df = pd.read_csv(sqrf)

#   print(df)

#   for fl in flist[:1]:
#     code = fl.split('_')
#     code[5] = code[5].split('.')[0]
#     exp = 0 if code[1]=='a' else int(code[1])+1
#     det = 0 if code[2]=='a' else int(code[2])+1
#     rot = 0 if code[3]=='a' else int(code[3])+1
#     roc = 0 if code[4]=='a' else int(code[4])+1
#     cen = 0 if code[5]=='a' else int(code[5])+1
    
#     print(f'화약 {exp} 뇌관 {det} 암종{rot} 암석{roc} 심발{cen}')

#     cond = (df['exp'] == exp) & (df['det'] == det) & (df['rot'] == rot)
#     cond = cond & (df['roc'] == roc) & (df['cen'] == cen)
#     loc = df.loc[cond]
    
#     K = loc.iloc[0]['K']
#     n = loc.iloc[0]['n']
#     s = loc.iloc[0]['s']

#     print(f'K = {K:3.3}, n = {n:3.3}, s = {s:3.3}')
    
#     b, a = lin_reg(fl)

#   return df


def sd_vib(key_in, df):
  sd = 0
  vib = 0

  exp = (key_in[0])
  det = (key_in[1])
  rot = (key_in[2])
  roc = (key_in[3])
  cen = (key_in[4])

  # print('######################')
  # print(key_in[0], exp)
  # print(exp,det,rot,roc,cen)

  cond = (df['exp'] == exp) & (df['det'] == det) & (df['rot'] == rot)
  cond = cond & (df['roc'] == roc) & (df['cen'] == cen)
  loc = df.loc[cond]
  
  # print(loc)

  K = loc.iloc[0]['K']
  n = loc.iloc[0]['n']
  s = loc.iloc[0]['s']

  sd = 100 
  vib = K*pow(sd,n)
  # vib = n*np.log(sd) + np.log(K)
  # vib = np.exp(vib) 
 
  return sd, vib, K, n, s


# key_in : [ exp, det, rot, roc, cen ]
# return : [ exp, det, rot, roc, cen, scale dist, vibration ] 
# return only once when it kick starts
# def create_in(key_in,df):
#   in_seq = key_in
#   sd,vib, K, n, s = sd_vib(key_in,df)
  
#   in_seq.append([sd,vib])
#   truth = [K, n, s]

#   return (in_seq, truth)


# input : [ exp, det, rot, roc, cen, scale dist, vibration ] 
# label : [ K, n, s]
def format_data(df):
  input_np = df.to_numpy()
  input = np.hstack([input_np[:,3:],input_np[:,:2]])

  for index, inp in enumerate(input):
    sd, vib, _,_,_ = sd_vib(inp,df)
    input[index,5] = sd
    input[index,6] = vib

  # print(input[:2])
  
  label = torch.FloatTensor(scaler.fit_transform(input_np[:,:3])).cuda()
  input = torch.FloatTensor(input).cuda()

  return input,label


def main():

  epoch = 1
  nstep = 10
  model = GenBlast()
  model.cuda()
  loss_func = nn.MSELoss()
  optim = torch.optim.Adam(model.parameters(), lr=0.001)

  tor_name = 'blast_train.pt'
  min_vl = 10000.0

  if os.path.isfile(tor_name) == True:
      print(tor_name,' exists loading is in progress')
      checkpoint = torch.load(tor_name)
      model.load_state_dict(checkpoint['model_state_dict'])
      optim.load_state_dict(checkpoint['optimizer_state_dict'])
      loss = checkpoint['loss']

  sqrf = 'sqr_data.csv'
  df = pd.read_csv(sqrf)

  input, label = format_data(df)

  ntot = df['exp'].size
  ntrain = int(ntot*0.95)
  nvalid  = int(ntot*0.05)

  inp_valid = input[:nvalid,:]
  lab_valid = label[:nvalid,:]
  inp_train = input[nvalid:ntrain+nvalid,:]
  lab_train = label[nvalid:ntrain+nvalid,:]
 
  # print(inp_valid, lab_valid)
  # print(ntot, ntrain,nvalid)

  print(f'training started')  
  start = time.time()

  for ep in range(epoch):
    for step in range(nstep):

      tr_err = trainModel(model, loss_func, optim, inp_train, lab_train)        
      vl_err = evalModel(model, loss_func, inp_valid, lab_valid )
      print(f'ep:{ep}, step:{step}, train error = {tr_err:3.3}, validation error = {vl_err:3.3}, min val error = {min_vl:3.3}')

      if min_vl > vl_err:
        min_vl = vl_err
        torch.save({
          'model_state_dict': model.state_dict(),
          'optimizer_state_dict': optim.state_dict(),
          'loss': min_vl
          }, tor_name)
      else: 
        torch.save({
          'model_state_dict': model.state_dict(),
          'optimizer_state_dict': optim.state_dict(),
          'loss': min_vl
          }, tor_name.split('.')[0]+'_bk.'+tor_name.split('.')[1])

  end = time.time()

  print(f'time taken for the training is {end - start}')

  #   for tr in train_data:
  #     out = trainModel(model, tr)

def test():
  sqrf = 'sqr_data.csv'
  df = pd.read_csv(sqrf)
  # print(df)

  # sd, vib = sd_vib([1,1,1,8,1],df)
  # print(sd,vib)  
  input,lab = format_data(df)

  # print(input[:10])

if __name__ == "__main__":
  main()
  # test()

  
