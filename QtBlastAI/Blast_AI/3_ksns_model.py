import os
import numpy as np
import pandas as pd
import torch 
from torch import nn as nn
from sklearn.preprocessing import MinMaxScaler
from SimpNN import SimpNN as SimpNN
import matplotlib.pyplot as plt
# from matplotlib import font_manager, rc
import pyformulas as pf

ksns_eval = __import__('4_ksns_eval')


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
  lab_k = torch.FloatTensor(input_np[:,0]) 
  lab_n = torch.FloatTensor(input_np[:,1]) 
  lab_s = torch.FloatTensor(input_np[:,2])   

  lab_ks = torch.cat((lab_k.view(-1,1),lab_n.view(-1,1),lab_s.view(-1,1)),dim=1)
  lab_ns = torch.FloatTensor(input_np[:,:2]) 
  
  # print(lab_ks.size(), lab_ns.size())
  # assert lab_ks.size() == lab_ns.size()
  return input,lab_ks,lab_ns


def case_plot(X,Y,x,y):
  # X = case_all['K']
  # Y = case_all['n']
 
  fig = plt.figure()

  canvas = np.zeros((480,640))
  screen = pf.screen(canvas,'test')
     
  plt.scatter(X,Y)
  plt.scatter(x,y)

  fig.canvas.draw()

  image = np.frombuffer(fig.canvas.tostring_rgb(), dtype=np.uint8)
  image = image.reshape(fig.canvas.get_width_height()[::-1] + (3,))

  screen.update(image)
   
  return

def main():

  hist = []
  
  min_error = 1e4
  min_err_val = 1e4
  step_size = 200000000
  one_step = 10000
    
  print (torch.cuda.current_device())
  print (torch.cuda.device_count())
  
  reg_sqr = pd.read_csv('sqr_data_sort.csv')  
  reg_sqr.drop(['# of elem'], axis = 1, inplace = True)

 
  input, label_ks, label_ns = format_data(reg_sqr)

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
  lab_ks_valid = label_ks[:len_valid,:]
  # lab_ns_valid = label_ns[:len_valid,:]

  inp_train = input[len_valid:len_train+len_valid,:]
  lab_ks_train = label_ks[len_valid:len_train+len_valid,:]
  # lab_ns_train = label_ns[len_valid:len_train+len_valid,:]
   
  inp_test = input[len_train+len_valid:,:]
  lab_ks_test = label_ks[len_train+len_valid:,:]
  # lab_ns_test = label_ns[len_train+len_valid:,:]

  print(f'input{inp_train.shape} = ', inp_train)
  print(f'output{lab_ks_train.shape} = ', lab_ks_train)
  # print(f'output{lab_ns_train.shape} = ', lab_ns_train)

  model_ks = SimpNN(5,300,3)
  # model_ns = SimpNN(5,300,2)

  model_ks.cuda()
  # model_ns.cuda()

  loss_ks = nn.MSELoss()
  # loss_ns = nn.MSELoss()

  optim_ks = torch.optim.SGD(model_ks.parameters(), lr = 0.005)
  # optim_ns = torch.optim.SGD(model_ns.parameters(), lr = 0.005)

  tor_name = 'sq_model_ks_ns.pt'

  if os.path.isfile(tor_name) == True:
      print(tor_name,' exists loading is in progress')
      checkpoint = torch.load(tor_name)
      model_ks.load_state_dict(checkpoint['model_ks_state_dict'])
      optim_ks.load_state_dict(checkpoint['optimizer_ks_state_dict'])
      loss_ks = checkpoint['loss_ks']
      # model_ns.load_state_dict(checkpoint['model_ns_state_dict'])
      # optim_ns.load_state_dict(checkpoint['optimizer_ns_state_dict'])
      # loss_ns = checkpoint['loss_ns']

  print(model_ks)
  # print(model_ns)

  # print(reg_sqr)
  inp_train = inp_train.cuda()
  lab_ks_train = lab_ks_train.cuda()
  # lab_ns_train = lab_ns_train.cuda()

  inp_valid = inp_valid.cuda()
  lab_ks_valid = lab_ks_valid.cuda()
  # lab_ns_valid = lab_ns_valid.cuda()

  inp_test = inp_test.cuda()
  lab_ks_test = lab_ks_test.cuda()
  # lab_ns_test = lab_ns_test.cuda()

  for step in range(step_size):

    model_ks.train()
    optim_ks.zero_grad()

    # model_ns.train()
    # optim_ns.zero_grad()

    pred_ks = model_ks(inp_train)
    # pred_ns = model_ns(inp_train)

    error_ks = loss_ks(pred_ks[:,0],lab_ks_train[:,0]) + loss_ks(pred_ks[:,1],lab_ks_train[:,1]) + loss_ks(pred_ks[:,2],lab_ks_train[:,2]) 
    # error_ns = loss_ns(pred_ns[:,0],lab_ns_train[:,0]) + loss_ns(pred_ns[:,1],lab_ns_train[:,1]) 

    if error_ks != error_ks:
      print(pred_ks[pred_ks!=pred_ks])
      print(pred_ks[pred_ks==pred_ks])
      print (f'step is {step}, error is {error_ks}')
      exit()

    # if error_ns != error_ns:
    #   print(pred_ns[pred_ns!=pred_ns])
    #   print(pred_ns[pred_ns==pred_ns])
    #   print (f'step is {step}, error is {error_ns}')
    #   exit()

    K = pred_ks[:,0]
    n = pred_ks[:,1]
    # n = pred_ns[:,0]

    # if K[K2].size()[0] > 0 and step % 10 == 0:
    #   logK = torch.log(K[K2])
    #   # D = torch.abs(0.1345*logK+n[K2])/np.sqrt(0.1345*0.1345+1)
    #   D = torch.abs(0.1*logK+n[K2])/np.sqrt(0.1*0.1+1)

    # err = np.nan
    # if K[K2].size()[0] > 0 and step % 10 == 0:
    #   err = loss(D,torch.zeros(D.size()).cuda())

    if error_ks != error_ks:
      print(f'second place error is {error_ks}')
      exit()
    
    # if K[K2].size()[0] > 0 and err != err:
    #   print(D)
    #   exit()

    error = error_ks #+ error_ns

    error_ks.backward(retain_graph=True)
    # error_ns.backward(retain_graph=True)

    optim_ks.step()
    # optim_ns.step()

    if step % one_step == 0:
      with torch.no_grad():
        model_ks.eval()
        # model_ns.eval()

        val_ks = model_ks(inp_valid)
        # val_ns = model_ns(inp_valid)
        # print(f'max K is {torch.max(val_ks[:,0])}, min K is {torch.min(val_ks[:,0])}')
        # print(f'max n is {torch.max(val_ns[:,0])}, min n is {torch.min(val_ns[:,0])}')
        # print(f'max true K is {torch.max(lab_ks_train[:,0])}, min true K is {torch.min(lab_ks_train[:,0])}')
        # print(f'max true n is {torch.max(lab_ns_train[:,1])}, min true n is {torch.min(lab_ns_train[:,1])}')

        K = val_ks[:,0]
        n = val_ks[:,1]
        # n = val_ns[:,0]

        er_ks_val = loss_ks(val_ks[:,0],lab_ks_valid[:,0]) + loss_ks(val_ks[:,1],lab_ks_valid[:,1]) + loss_ks(val_ks[:,2],lab_ks_valid[:,2]) 
        # er_ns_val = loss_ns(val_ns[:,0],lab_ns_valid[:,0]) + loss_ns(val_ns[:,1],lab_ns_valid[:,1]) 

        if er_ks_val != er_ks_val:
          print('er_ks_val is nan\n')
          exit()

        # if er_ns_val != er_ns_val:
        #   print('er_ns_val is nan\n')
        #   exit()

      er_val = er_ks_val # + er_ns_val
      print(f'{int(step/one_step)} training K loss = {error_ks.item()}, validation K los = {er_ks_val.item()}, min loss = {min_err_val}')
      # print(f'{int(step/one_step)} training n loss = {error_ns.item()}, validation n los = {er_ns_val.item()}, min loss = {min_err_val}')
      
      hist.append([step % one_step, error.item(), er_val.item()])

      if min_err_val > er_val.item():
        min_err_val = er_val.item()
        torch.save({
          'model_ks_state_dict': model_ks.state_dict(),
          'optimizer_ks_state_dict': optim_ks.state_dict(),
          'loss_ks': loss_ks,
          # 'model_ns_state_dict': model_ns.state_dict(),
          # 'optimizer_ns_state_dict': optim_ns.state_dict(),
          # 'loss_ns': loss_ns

          }, tor_name)
 
      if min_error > error.item(): 
        min_error = error.item()
        torch.save({
          'model_ks_state_dict': model_ks.state_dict(),
          'optimizer_ks_state_dict': optim_ks.state_dict(),
          'loss_ks': loss_ks,
          # 'model_ns_state_dict': model_ns.state_dict(),
          # 'optimizer_ns_state_dict': optim_ns.state_dict(),
          # 'loss_ns': loss_ns
          }, tor_name.split('.')[0]+'_tr.'+tor_name.split('.')[1])


      df_hist = pd.DataFrame(hist)
      df_hist.to_csv('sq_hist.csv')
      

      case_all = ksns_eval.evaluate(reg_sqr, model_ks)#, model_ns)

      # case_plot(case_all['K'], case_all['n'])
      # case_plot(K.cpu().detach().numpy(),n.cpu().detach().numpy())
      lab_ks = lab_ks_train.detach().cpu().numpy()
      # lab_ns = lab_ns_train.detach().cpu().numpy()
      # case_plot(lab_ks[:,0],lab_ks[:,1],K.cpu().detach().numpy(),n.cpu().detach().numpy() )
      
   
if __name__ == '__main__':
  main()