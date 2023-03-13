
import os
import numpy as np
import pandas as pd
import torch 
from torch import nn as nn
from sklearn.preprocessing import MinMaxScaler
from SimpNN import SimpNN as SimpNN


scaler = MinMaxScaler()
tr_K = 0
tr_n = 0


exp_dic = {}
exp_dic[0] =  '에멀젼C'
exp_dic[1] =  '정밀폭약'
exp_dic[2] =  '함수폭약'

det_dic = { }
det_dic[0] = '비전기'
det_dic[1] = '전기'
det_dic[2] = '전자'

rocktype_dic = {}
rocktype_dic[0] = '변성암'
rocktype_dic[1] = '퇴적암'
rocktype_dic[2] = '화성암'

rockname_dic = {}
rockname_dic[0] = '규장암'
rockname_dic[1] = '사암'
rockname_dic[2] = '석회암'
rockname_dic[3] = '섬록암'
rockname_dic[4] = '셰일'
rockname_dic[5] = '안산암'
rockname_dic[6] = '응회암'
rockname_dic[7] = '편마암'
rockname_dic[8] = '편암'
rockname_dic[9] = '화강반암'
rockname_dic[10] = '화강암'

cen_dic = {}
cen_dic[0] = 'Cylinder-cut'
cen_dic[1] = 'TBM 선굴착'
cen_dic[2] = 'V-CUT'
cen_dic[3] = '라인 드릴링'
cen_dic[4] = '분착식 다단발파'
cen_dic[5] = '선대구경'
cen_dic[6] = '수직구'

col_size = 5
out_size = 3


def format_data(data):
  data_norm = pd.DataFrame(scaler.fit_transform(data), columns = data.columns)
  input_np = data_norm.to_numpy()
  
  input = torch.FloatTensor(input_np[:,3:]) 
  lab = torch.FloatTensor(input_np[:,:3]) 
  
  return input,lab


def main():
  hist = []
  
  min_err_val = 1e4
  step_size = 200000000
  one_step = 10000
    
  print (torch.cuda.current_device())
  print (torch.cuda.device_count())
  
  reg_sqr = pd.read_csv('sqr_data.csv')  
  reg_sqr.drop(['# of elem'], axis = 1, inplace = True)
  
  input, label = format_data(reg_sqr)

  len = input.size()[0]
  len_train = int(len*0.90)
  len_valid = int(len*0.10)

  # train - validation
  # inp_train = input[:len_train,:]
  # lab_train = label[:len_train,:]
  # inp_valid = input[len_train:len_train+len_valid,:]
  # lab_valid = label[len_train:len_train+len_valid,:]
  # inp_test = input[len_train+len_valid:,:]
  # lab_test = label[len_train+len_valid:,:]

  # validation - train
  inp_valid = input[:len_valid,:]
  lab_valid = label[:len_valid,:]
  inp_train = input[len_valid:len_train+len_valid,:]
  lab_train = label[len_valid:len_train+len_valid,:]
  inp_test = input[len_train+len_valid:,:]
  lab_test = label[len_train+len_valid:,:]

  print(f'input{inp_train.shape} = ', inp_train)
  print(f'output{lab_train.shape} = ', lab_train)

  model = SimpNN()

  model.cuda()
  loss = nn.MSELoss()
  optim = torch.optim.SGD(model.parameters(), lr = 0.005)

  tor_name = 'sq_model_train_valid.pt'

  if os.path.isfile(tor_name) == True:
      print(tor_name,' exists loading is in progress')
      checkpoint = torch.load(tor_name)
      model.load_state_dict(checkpoint['model_state_dict'])
      optim.load_state_dict(checkpoint['optimizer_state_dict'])
      loss = checkpoint['loss']

  print(model)
  # print(reg_sqr)
  inp_train = inp_train.cuda()
  lab_train = lab_train.cuda()
  inp_valid = inp_valid.cuda()
  lab_valid = lab_valid.cuda()
  inp_test = inp_test.cuda()
  lab_test = lab_test.cuda()

  if os.path.isfile(tor_name) == True:
      print(tor_name,' exists loading is in progress')
      checkpoint = torch.load(tor_name)
      model.load_state_dict(checkpoint['model_state_dict'])
      optim.load_state_dict(checkpoint['optimizer_state_dict'])
      loss = checkpoint['loss']


  for step in range(step_size):

    model.train()
    optim.zero_grad()

    pred = model(inp_train)
    
    error = loss(pred[:,0],lab_train[:,0]) + loss(pred[:,1],lab_train[:,1]) + loss(pred[:,2],lab_train[:,2])

    if error != error:
      print(pred[pred!=pred])
      print(pred[pred==pred])
      print (f'step is {step}, error is {error}, err is {err}')
      exit()


    K = pred[:,0]
    n = pred[:,1]

    K1 = K < 0
    K2 = K > 0 
    n1 = n > 1

    # print (n[n1].size())
    # err = torch.autograd.Variable(torch.zeros(1),requires_grad=True).cuda()

    if K[K2].size()[0] > 0 and step % 10 == 0:
      logK = torch.log(K[K2])
      # D = torch.abs(0.1345*logK+n[K2])/np.sqrt(0.1345*0.1345+1)
      D = torch.abs(0.1*logK+n[K2])/np.sqrt(0.1*0.1+1)

    # print (pred[:,0])
    # print (label[:,0])

    # print(pred.shape, label.shape)
    # error = loss(pred,label)
    err = np.nan
    if K[K2].size()[0] > 0 and step % 10 == 0:
      # err = err + torch.sum(torch.pow(D,0.5))/pred.size()[0]
      err = loss(D,torch.zeros(D.size()).cuda())


    # if n[n1].size()[0] > 0:
    #   error = error+ torch.sum(torch.pow(n[n1]-1,2))
    # if K[K1].size()[0] > 0:
    #   error = error+ torch.sum(torch.pow(K[K1],2))

    # if K[K2].size()[0] > 0 and err == err:
    #   error = error + err

    if error != error:
      print(f'second place error is {error}, err is {err}')
    
    # if K[K2].size()[0] > 0 and err != err:
    #   print(D)
    #   exit()



    error.backward(retain_graph=True)
    if err == err:
      err.backward()
    
    optim.step()

    if step % one_step == 0:
      with torch.no_grad():
        model.eval()
        val = model(inp_valid)
        print(f'max K is {torch.max(pred[:,0])}, min K is {torch.min(pred[:,0])}')
        print(f'max n is {torch.max(pred[:,1])}, min n is {torch.min(pred[:,1])}')
        print(f'max true K is {torch.max(lab_train[:,0])}, min true K is {torch.min(lab_train[:,0])}')
        print(f'max true n is {torch.max(lab_train[:,1])}, min true n is {torch.min(lab_train[:,1])}')

        K = val[:,0]
        n = val[:,1]
        K1 = K < 0        
        K2 = K > 0
        n1 = n > 1

        if K[K2].size()[0] > 0:
          logK = torch.log(K[K2])
          # D = torch.abs(0.1345*logK+n[K2])/np.sqrt(0.1345*0.1345+1)
          D = torch.abs(0.1*logK+n[K2])/np.sqrt(0.1*0.1+1)

        er_val = loss(val[:,0],lab_valid[:,0]) + loss(val[:,1],lab_valid[:,1]) + loss(val[:,2],lab_valid[:,2])
        er_v = np.nan
        if K[K2].size()[0]>0:
          er_v = er_v + loss(D,torch.zeros(D.size()).cuda())

        if er_val != er_val:
          print('er_val is nan\n')
          print(f'size of K[K2] is {K[K2].size()[0]}')
          print(f'size of D is {D.size()[0]}')
          exit()

        # if n[n1].size()[0] > 0:
        #   er_val = er_val + torch.sum(torch.pow(n[n1]-1,2))
        # if K[K1].size()[0] > 0:
        #   er_val = er_val + torch.sum(torch.pow(K[K1],2))

      print(f'{int(step/one_step)} training loss = {error.item()}, validation los = {er_val.item()}, min loss = {min_err_val}')
      if err == err:
        print(f'  training D loss = {err.item()}')
      if er_v == er_v:
        print(f'  validation D los = {er_v.item()}')
      # for i, _ in enumerate(pred[:5]):
      #   print('val = ',val[i], 'lab_valid = ',lab_valid[i]) 
      
      
      hist.append([step % one_step, error.item(), er_val.item()])
      if min_err_val > er_val.item():
        min_err_val = er_val.item()
        torch.save({
          'model_state_dict': model.state_dict(),
          'optimizer_state_dict': optim.state_dict(),
          'loss': loss
          }, tor_name)
      else: 
        torch.save({
          'model_state_dict': model.state_dict(),
          'optimizer_state_dict': optim.state_dict(),
          'loss': loss
          }, tor_name.split('.')[0]+'_bk.'+tor_name.split('.')[1])

      df_hist = pd.DataFrame(hist)
      df_hist.to_csv('sq_hist.csv')
      
   
if __name__ == '__main__':
  main()