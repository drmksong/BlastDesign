import os
import numpy as np
import pandas as pd
import torch 
from torch import nn as nn
from sklearn.preprocessing import MinMaxScaler
from torch.nn.modules import module
from SimpNN import SimpNN as SimpNN

scaler = MinMaxScaler()


# 4 x 4 x 4 x 8 = 512
# 4 x 4 x 12 x 8 = 1536
# 512 + 1536 = 2048
#

col_size = 5
out_size = 3

exp_dic = []
exp_dic.append('모든 화약')
exp_dic.append('에멀젼C')
exp_dic.append('정밀폭약')
exp_dic.append('함수폭약')

det_dic = []
det_dic.append('모든 뇌관')
det_dic.append('비전기')
det_dic.append('전기')
det_dic.append('전자')

rocktype_dic = []
rocktype_dic.append('모든 암석분류')
rocktype_dic.append('변성암')
rocktype_dic.append('퇴적암')
rocktype_dic.append('화성암')

rockname_dic = []
rockname_dic.append('모든 암종')
rockname_dic.append('규장암')
rockname_dic.append('사암')
rockname_dic.append('석회암')
rockname_dic.append('섬록암')
rockname_dic.append('셰일')
rockname_dic.append('안산암')
rockname_dic.append('응회암')
rockname_dic.append('편마암')
rockname_dic.append('편암')
rockname_dic.append('화강반암')
rockname_dic.append('화강암')

cen_dic = []
cen_dic.append('모든 심발')
cen_dic.append('Cylinder-cut')
cen_dic.append('TBM 선굴착')
cen_dic.append('V-CUT')
cen_dic.append('라인 드릴링')
cen_dic.append('분착식 다단발파')
cen_dic.append('선대구경')
cen_dic.append('수직구')

def format_data(data):

  data_norm = pd.DataFrame(scaler.fit_transform(data), columns = data.columns)
  input_np = data_norm.to_numpy()
  
  input = torch.FloatTensor(input_np[:,3:]) 
  lab = torch.FloatTensor(input_np[:,:3]) 
  
  return input,lab

def predict(key_in):

  model = load_model()
  reg_sqr = pd.read_csv('sqr_data.csv')  

  lst = np.array([0,0,0,0,0,0,0,0],dtype=float)
  K,n,s = (0,0,0)
  lst[0] = 0 # K
  lst[1] = 0 # s
  lst[2] = 0 # n

  ie  = lst[3] = key_in[0]
  id  = lst[4] = key_in[1]
  irt = lst[5] = key_in[2]  
  irn = lst[6] = key_in[3]  
  ic  = lst[7] = key_in[4]  

  case = pd.DataFrame([lst],columns=reg_sqr.columns)
  case_norm = pd.DataFrame(scaler.transform(case), columns = case.columns)
  case_np = case_norm.to_numpy()
  case_inp = case_np[:,3:]
  # print(case_inp)
  
  case_tc = torch.FloatTensor(case_inp).cuda()
  pred = model(case_tc)
  case_norm['K'] = pred[0,0].item()
  case_norm['n'] = pred[0,1].item()
  case_norm['s'] = pred[0,2].item()

  case_inv = pd.DataFrame(scaler.inverse_transform(case_norm), columns = case.columns)
  case_inv['exp'] = exp_dic[ie]
  case_inv['det'] = det_dic[id]
  case_inv['rot'] = rocktype_dic[irt]
  case_inv['roc'] = rockname_dic[irn]
  case_inv['cen'] = cen_dic[ic]

  K = case_norm['K']
  n = case_norm['n']
  s = case_norm['s']

  return K,n,s


def load_model():
  model = SimpNN()
  loss = nn.MSELoss()
  optim = torch.optim.SGD(model.parameters(), lr = 0.005)

  model = SimpNN()
  loss = nn.MSELoss()
  optim = torch.optim.SGD(model.parameters(), lr = 0.005)

  tor_name = 'sq_model_train_valid.pt'

  if os.path.isfile(tor_name) == True:
      print(tor_name,' exists loading is in progress')
      checkpoint = torch.load(tor_name)
      model.load_state_dict(checkpoint['model_state_dict'])
      optim.load_state_dict(checkpoint['optimizer_state_dict'])
      loss = checkpoint['loss']

  model.cuda()
  model.eval()


  return model

def evaluate():

  reg_sqr = pd.read_csv('sqr_data.csv')  
  reg_sqr.drop(['# of elem'], axis = 1, inplace = True)

  input, label = format_data(reg_sqr)

  # model = SimpNN()
  # loss = nn.MSELoss()
  # optim = torch.optim.SGD(model.parameters(), lr = 0.005)
  # tor_name = 'sq_model_train_valid.pt'

  model = load_model()

  case_all = pd.DataFrame(columns=reg_sqr.columns)
  

  for ie, exp in enumerate(exp_dic):
    lst = np.array([0,0,0,0,0,0,0,0],dtype=float)
    lst[0] = 0 # K
    
    lst[1] = 0 # s
    lst[2] = 0 # n

    # case['exp'] = ie
    lst[3] = ie
    for id, det in enumerate(det_dic):
      # case['det'] = id
      lst[4] = id

      for ic, cen in enumerate(cen_dic):
        # case['cen'] = ic
        lst[7] = ic

        irn = 0
        lst[6] = irn

        for irt, rt in enumerate(rocktype_dic):
          # case['rot'] = irt
          lst[5] = irt

          case = pd.DataFrame([lst],columns=reg_sqr.columns)
          case_norm = pd.DataFrame(scaler.transform(case), columns = case.columns)
          case_np = case_norm.to_numpy()
          case_inp = case_np[:,3:]
          # print(case_inp)
          
          case_tc = torch.FloatTensor(case_inp).cuda()
          pred = model(case_tc)

          case_norm['K'] = pred[0,0].item()
          case_norm['n'] = pred[0,1].item()
          case_norm['s'] = pred[0,2].item()
          # print(case_norm)
          case_inv = pd.DataFrame(scaler.inverse_transform(case_norm), columns = case.columns)
          case_inv['exp'] = ie # exp_dic[ie]
          case_inv['det'] = id # det_dic[id]
          case_inv['rot'] = irt # rocktype_dic[irt]
          case_inv['roc'] = irn # rockname_dic[irn]
          case_inv['cen'] = ic # cen_dic[ic]
          case_all = case_all.append(case_inv)
          # print(case_inv)

          # print(pred[0,1])
          # print(f'{pred.cpu().detach().numpy()} {exp} {det} {rt} {rn} {cen}')

        irt = 0
        lst[5] = irt        
        for irn, rn in enumerate(rockname_dic):
          # case['roc'] = irn
          lst[6] = irn

          case = pd.DataFrame([lst],columns=reg_sqr.columns)
          case_norm = pd.DataFrame(scaler.transform(case), columns = case.columns)
          case_np = case_norm.to_numpy()
          case_inp = case_np[:,3:]
          # print(case_inp)
          
          case_tc = torch.FloatTensor(case_inp).cuda()
          pred = model(case_tc)

          case_norm['K'] = pred[0,0].item()
          case_norm['n'] = pred[0,1].item()
          case_norm['s'] = pred[0,2].item()
          # print(case_norm)
          case_inv = pd.DataFrame(scaler.inverse_transform(case_norm), columns = case.columns)
          case_inv['exp'] = ie # exp_dic[ie]
          case_inv['det'] = id # det_dic[id]
          case_inv['rot'] = irt # rocktype_dic[irt]
          case_inv['roc'] = irn # rockname_dic[irn]
          case_inv['cen'] = ic # cen_dic[ic]
          case_all = case_all.append(case_inv)
          # print(case_inv)

          # print(pred[0,1])
          # print(f'{pred.cpu().detach().numpy()} {exp} {det} {rt} {rn} {cen}')


def main():

  reg_sqr = pd.read_csv('sqr_data.csv')  
  reg_sqr.drop(['# of elem'], axis = 1, inplace = True)

  input, label = format_data(reg_sqr)

  # model = SimpNN()
  # loss = nn.MSELoss()
  # optim = torch.optim.SGD(model.parameters(), lr = 0.005)
  # tor_name = 'sq_model_train_valid.pt'

  model = load_model()

  case_all = pd.DataFrame(columns=reg_sqr.columns)
  

  for ie, exp in enumerate(exp_dic):
    lst = np.array([0,0,0,0,0,0,0,0],dtype=float)
    lst[0] = 0 # K
    
    lst[1] = 0 # s
    lst[2] = 0 # n

    # case['exp'] = ie
    lst[3] = ie
    for id, det in enumerate(det_dic):
      # case['det'] = id
      lst[4] = id

      for ic, cen in enumerate(cen_dic):
        # case['cen'] = ic
        lst[7] = ic

        irn = 0
        lst[6] = irn

        for irt, rt in enumerate(rocktype_dic):
          # case['rot'] = irt
          lst[5] = irt

          case = pd.DataFrame([lst],columns=reg_sqr.columns)
          case_norm = pd.DataFrame(scaler.transform(case), columns = case.columns)
          case_np = case_norm.to_numpy()
          case_inp = case_np[:,3:]
          # print(case_inp)
          
          case_tc = torch.FloatTensor(case_inp).cuda()
          pred = model(case_tc)

          case_norm['K'] = pred[0,0].item()
          case_norm['n'] = pred[0,1].item()
          case_norm['s'] = pred[0,2].item()
          # print(case_norm)
          case_inv = pd.DataFrame(scaler.inverse_transform(case_norm), columns = case.columns)
          case_inv['exp'] = ie # exp_dic[ie]
          case_inv['det'] = id # det_dic[id]
          case_inv['rot'] = irt # rocktype_dic[irt]
          case_inv['roc'] = irn # rockname_dic[irn]
          case_inv['cen'] = ic # cen_dic[ic]
          case_all = case_all.append(case_inv)
          # print(case_inv)

          # print(pred[0,1])
          # print(f'{pred.cpu().detach().numpy()} {exp} {det} {rt} {rn} {cen}')

        irt = 0
        lst[5] = irt        
        for irn, rn in enumerate(rockname_dic):
          # case['roc'] = irn
          lst[6] = irn

          case = pd.DataFrame([lst],columns=reg_sqr.columns)
          case_norm = pd.DataFrame(scaler.transform(case), columns = case.columns)
          case_np = case_norm.to_numpy()
          case_inp = case_np[:,3:]
          # print(case_inp)
          
          case_tc = torch.FloatTensor(case_inp).cuda()
          pred = model(case_tc)

          case_norm['K'] = pred[0,0].item()
          case_norm['n'] = pred[0,1].item()
          case_norm['s'] = pred[0,2].item()
          # print(case_norm)
          case_inv = pd.DataFrame(scaler.inverse_transform(case_norm), columns = case.columns)
          case_inv['exp'] = ie # exp_dic[ie]
          case_inv['det'] = id # det_dic[id]
          case_inv['rot'] = irt # rocktype_dic[irt]
          case_inv['roc'] = irn # rockname_dic[irn]
          case_inv['cen'] = ic # cen_dic[ic]
          case_all = case_all.append(case_inv)
          # print(case_inv)

          # print(pred[0,1])
          # print(f'{pred.cpu().detach().numpy()} {exp} {det} {rt} {rn} {cen}')

  print(case_all)
  case_all.to_csv('case_all.csv',encoding="utf-8-sig")


if __name__ == '__main__':
  main()