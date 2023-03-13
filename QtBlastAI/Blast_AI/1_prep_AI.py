import os
import numpy as np
from numpy.lib.function_base import average
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

# import tensorflow as tf
# from tensorflow.keras.models import Sequential
# from tensorflow.keras.layers import Dense, Dropout
from line_reg_model import Reg
from sklearn.linear_model import LinearRegression 


# '변성암' 
#   '편마암' # 변성암
#   '편암' # 변성암

# '퇴적암'
#   '사암' # 퇴적암
#   '석회암' # 퇴적암
#   '셰일' # 퇴적암
#   '응회암' # 퇴적암

# '화성암'
#   '규장암' # 화성암
#   '섬록암' # 화성암
#   '안산암' # 화성암
#   '화강반암' # 화성암
#   '화강암' # 화성암


# global variable definition
sub = './tun/'

rock_dic = {} # convert rockname to rocktype, e.g. 사암 -> 퇴적암 

exp_set = set([])
det_set = set([])
rocktype_set = set([])
rockname_set = set([])
cen_set = set([])

reg2 = Reg()
reg3 = Reg()

def fill_set(df):
  global exp_set, det_set, rocktype_set, rockname_set, cen_set

  print(df.columns)
  # print(df['화약'].size)
  for i in range(df['화약'].size):
    exp_set.add(df['화약'][i])
  exp_set = sorted(exp_set)    
  print('화약 : ',exp_set)  
  
  for i in range(df['뇌관'].size):
    det_set.add(df['뇌관'][i])
  det_set = sorted(det_set)        
  print('뇌관 : ',det_set)  

  for i in range(df['암석분류'].size):
    rocktype_set.add(df['암석분류'][i])
  rocktype_set = sorted(rocktype_set)    
  print('암석분류 : ', rocktype_set)  

  for i in range(df['암종'].size):
    rockname_set.add(df['암종'][i])
  rockname_set = {x for x in rockname_set if pd.notna(x)}
  rockname_set = sorted(rockname_set)    
  print('암종 : ', rockname_set)  
  
  for i in range(df['심발'].size):
    cen_set.add(df['심발'][i])
  cen_set = sorted(cen_set)    
  print('심발 : ', cen_set)  

  return


def filter(df,en=-1, dn=-1, rtn=-1, rnn=-1, cn=-1):
  
  gdf = df.copy()
  gdf = gdf.drop(columns = ['지발당장약량'])
  gdf = gdf.drop(columns = ['이격거리'])

  if en==-1:
    gdf = gdf.drop(columns = ['화약'])
  if dn==-1:
    gdf = gdf.drop(columns = ['뇌관'])
  if rtn==-1:
    gdf = gdf.drop(columns = ['암석분류'])
  if rnn==-1:
    gdf = gdf.drop(columns = ['암종'])
  if cn==-1:
    gdf = gdf.drop(columns = ['심발'])

  if en>=0:
    cond = ( gdf['화약']  == gdf['화약'] ) # 초기화
  elif dn>=0:
    cond = ( gdf['뇌관']  == gdf['뇌관'] ) # 초기화
  elif rtn>=0:
    cond = ( gdf['암석분류']  == gdf['암석분류'] ) # 초기화
  elif rnn>=0:
    cond = ( gdf['암종']  == gdf['암종'] ) # 초기화
  elif cn>=0:
    cond = ( gdf['심발']  == gdf['심발'] ) # 초기화
  # else:
  #   cond = ''

  if int(en) >= 0:
    cond = cond & ( gdf['화약']  == list(exp_set)[en] )

  if dn>= 0:
    cond = cond & ( gdf['뇌관'] == list(det_set)[dn] )

  if rtn >= 0:
    cond = cond & ( gdf['암석분류'] == list(rocktype_set)[rtn] )

  if rnn >= 0:
    cond = cond & ( gdf['암종'] == list(rockname_set)[rnn] )

  if cn >= 0:
    cond = cond & ( gdf['심발'] == list(cen_set)[cn] )
   
  print('condition is \n',cond)
  gdf = gdf[cond]
  print(gdf)

  return gdf


def gen_data():

  tun_AI_csv = './터널_AI data_V5.csv'
  df = pd.read_csv(tun_AI_csv,encoding='utf-8') # ,encoding='ANSI'

  fill_set(df)

  A = 'a'

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
  rockname_dic[0] = '규장암' # 화성암  2
  rockname_dic[1] = '사암' # 퇴적암 1
  rockname_dic[2] = '석회암' # 퇴적암 1
  rockname_dic[3] = '섬록암' # 화성암 2
  rockname_dic[4] = '셰일' # 퇴적암 1
  rockname_dic[5] = '안산암' # 화성암 2
  rockname_dic[6] = '응회암' # 퇴적암 1
  rockname_dic[7] = '편마암' # 변성암 0
  rockname_dic[8] = '편암' # 변성암 0
  rockname_dic[9] = '화강반암' # 화성암 2
  rockname_dic[10] = '화강암' # 화성암 2

  rock_dic['편마암'] = '변성암'
  rock_dic['편암'] = '변성암'

  rock_dic['사암'] = '퇴적암'
  rock_dic['석회암'] = '퇴적암'
  rock_dic['셰일'] = '퇴적암'
  rock_dic['응회암'] = '퇴적암'

  rock_dic['규장암'] = '화성암'
  rock_dic['섬록암'] = '화성암'
  rock_dic['안산암'] = '화성암'
  rock_dic['화강반암'] = '화성암'
  rock_dic['화강암'] = '화성암'

  def conv(irn):
    rn = rockname_dic[irn]
    rt = rock_dic[rn]
    for key, value in rocktype_dic.items():
      if rt == value:
        return key
    print(f'    error in gen_data::conv() {rt} {value}')
    exit() 

  cen_dic = {}
  cen_dic[0] = 'Cylinder-cut'
  cen_dic[1] = 'TBM 선굴착'
  cen_dic[2] = 'V-CUT'
  cen_dic[3] = '라인 드릴링'
  cen_dic[4] = '분착식 다단발파'
  cen_dic[5] = '선대구경'
  cen_dic[6] = '수직구'

  for ie in range(len(exp_set)):  # ie
    fname = f'{sub}tun_{exp_dic[ie]}.csv'
    fname = f'{sub}tun_{ie}_{A}_{A}_{A}_{A}.csv'
    gdf = filter(df,en=ie, dn=-1, rtn=-1, rnn=-1, cn=-1)  # -1 : all data drop column, number : given number only with column name
    gdf.to_csv(fname,index=False)

    for id in range(len(det_set)): # ie-id
      fname = f'{sub}tun_{exp_dic[ie]}_{det_dic[id]}.csv'
      fname = f'{sub}tun_{ie}_{id}_{A}_{A}_{A}.csv'
      gdf = filter(df,en=ie, dn=id, rtn=-1, rnn=-1, cn=-1)  # -1 : all data drop column, number : given number only with column name
      gdf.to_csv(fname,index=False)

      for irt in range(len(rocktype_set)): # ie-id-irt
        fname = f'{sub}tun_{exp_dic[ie]}_{det_dic[id]}_{rocktype_dic[irt]}.csv'
        fname = f'{sub}tun_{ie}_{id}_{irt}_{A}_{A}.csv'
        gdf = filter(df,en=ie, dn=id, rtn=irt, rnn=-1, cn=-1)  # -1 : all data drop column, number : given number only with column name
        gdf.to_csv(fname,index=False)

        for ic in range(len(cen_set)): # ie-id-irt-ic
          fname = f'{sub}tun_{exp_dic[ie]}_{det_dic[id]}_{rocktype_dic[irt]}_{cen_dic[ic]}.csv'
          fname = f'{sub}tun_{ie}_{id}_{irt}_{A}_{ic}.csv'
          gdf = filter(df,en=ie, dn=id, rtn=irt, rnn=-1, cn=ic)  # -1 : all data drop column, number : given number only with column name
          gdf.to_csv(fname,index=False)

      for irn in range(len(rockname_set)): # ie-id-irn
        fname = f'{sub}tun_{exp_dic[ie]}_{det_dic[id]}_{rockname_dic[irn]}.csv'
        fname = f'{sub}tun_{ie}_{id}_{A}_{irn}_{A}.csv'
        gdf = filter(df,en=ie, dn=id, rtn=-1, rnn=irn, cn=-1)  # -1 : all data drop column, number : given number only with column name
        gdf.to_csv(fname,index=False)

        # convert irn -> irt
        _irt = conv(irn)
        fname = f'{sub}tun_{ie}_{id}_{_irt}_{irn}_{A}.csv'
        gdf = filter(df,en=ie, dn=id, rtn=_irt, rnn=irn, cn=-1)  # -1 : all data drop column, number : given number only with column name
        gdf.to_csv(fname,index=False)


        for ic in range(len(cen_set)): # ie-id-irn-ic
          fname = f'{sub}tun_{exp_dic[ie]}_{det_dic[id]}_{rockname_dic[irn]}_{cen_dic[ic]}.csv'
          fname = f'{sub}tun_{ie}_{id}_{A}_{irn}_{ic}.csv'
          gdf = filter(df,en=ie, dn=id, rtn=-1, rnn=irn, cn=ic)  # -1 : all data drop column, number : given number only with column name
          gdf.to_csv(fname,index=False)

          # convert irn -> irt
          _irt = conv(irn)
          fname = f'{sub}tun_{ie}_{id}_{_irt}_{irn}_{ic}.csv'
          gdf = filter(df,en=ie, dn=id, rtn=_irt, rnn=irn, cn=ic)  # -1 : all data drop column, number : given number only with column name
          gdf.to_csv(fname,index=False)

      for ic in range(len(cen_set)): # ie-id-ic
        fname = f'{sub}tun_{exp_dic[ie]}_{det_dic[id]}_{cen_dic[ic]}.csv'
        fname = f'{sub}tun_{ie}_{id}_{A}_{A}_{ic}.csv'
        gdf = filter(df,en=ie, dn=id, rtn=-1, rnn=-1, cn=ic)  # -1 : all data drop column, number : given number only with column name
        gdf.to_csv(fname,index=False)

    for irt in range(len(rocktype_set)): # ie-irt
      fname = f'{sub}tun_{exp_dic[ie]}_{rocktype_dic[irt]}.csv'
      fname = f'{sub}tun_{ie}_{A}_{irt}_{A}_{A}.csv'
      gdf = filter(df,en=ie, dn=-1, rtn=irt, rnn=-1, cn=-1)  # -1 : all data drop column, number : given number only with column name
      gdf.to_csv(fname,index=False)

      for ic in range(len(cen_set)): # ie-irt-ic
        fname = f'{sub}tun_{exp_dic[ie]}_{rocktype_dic[irt]}_{cen_dic[ic]}.csv'
        fname = f'{sub}tun_{ie}_{A}_{irt}_{A}_{ic}.csv'
        gdf = filter(df,en=ie, dn=-1, rtn=irt, rnn=-1, cn=ic)  # -1 : all data drop column, number : given number only with column name
        gdf.to_csv(fname,index=False)

    for irn in range(len(rockname_set)): # ie-irn
      fname = f'{sub}tun_{exp_dic[ie]}_{rockname_dic[irn]}.csv'
      fname = f'{sub}tun_{ie}_{A}_{A}_{irn}_{A}.csv'
      gdf = filter(df,en=ie, dn=-1, rtn=-1, rnn=irn, cn=-1)  # -1 : all data drop column, number : given number only with column name
      gdf.to_csv(fname,index=False)

      # convert irn -> irt
      _irt = conv(irn)
      fname = f'{sub}tun_{ie}_{A}_{_irt}_{irn}_{A}.csv'
      gdf = filter(df,en=ie, dn=-1, rtn=_irt, rnn=irn, cn=-1)  # -1 : all data drop column, number : given number only with column name
      gdf.to_csv(fname,index=False)


      for ic in range(len(cen_set)): # ie-irn-ic
        fname = f'{sub}tun_{exp_dic[ie]}_{rockname_dic[irn]}_{cen_dic[ic]}.csv'
        fname = f'{sub}tun_{ie}_{A}_{A}_{irn}_{ic}.csv'
        gdf = filter(df,en=ie, dn=-1, rtn=-1, rnn=irn, cn=ic)  # -1 : all data drop column, number : given number only with column name
        gdf.to_csv(fname,index=False)
  
        # convert irn -> irt
        _irt = conv(irn)
        fname = f'{sub}tun_{ie}_{A}_{_irt}_{irn}_{ic}.csv'
        gdf = filter(df,en=ie, dn=-1, rtn=_irt, rnn=irn, cn=ic)  # -1 : all data drop column, number : given number only with column name
        gdf.to_csv(fname,index=False)

    for ic in range(len(cen_set)): # ie-ic
      fname = f'{sub}tun_{exp_dic[ie]}_{cen_dic[ic]}.csv'
      fname = f'{sub}tun_{ie}_{A}_{A}_{A}_{ic}.csv'
      gdf = filter(df,en=ie, dn=-1, rtn=-1, rnn=-1, cn=ic)  # -1 : all data drop column, number : given number only with column name
      gdf.to_csv(fname,index=False)

#--------------------------------------------------------------------------

  for id in range(len(det_set)): # id
    fname = f'{sub}tun_{det_dic[id]}.csv'
    fname = f'{sub}tun_{A}_{id}_{A}_{A}_{A}.csv'
    gdf = filter(df,en=-1, dn=id, rtn=-1, rnn=-1, cn=-1)  # -1 : all data drop column, number : given number only with column name
    gdf.to_csv(fname,index=False)

    for irt in range(len(rocktype_set)): # id-irt
      fname = f'{sub}tun_{det_dic[id]}_{rocktype_dic[irt]}.csv'
      fname = f'{sub}tun_{A}_{id}_{irt}_{A}_{A}.csv'
      gdf = filter(df,en=-1, dn=id, rtn=irt, rnn=-1, cn=-1)  # -1 : all data drop column, number : given number only with column name
      gdf.to_csv(fname,index=False)

      for ic in range(len(cen_set)): # id-irt-ic
        fname = f'{sub}tun_{det_dic[id]}_{rocktype_dic[irt]}_{cen_dic[ic]}.csv'
        fname = f'{sub}tun_{A}_{id}_{irt}_{A}_{ic}.csv'
        gdf = filter(df,en=-1, dn=id, rtn=irt, rnn=-1, cn=ic)  # -1 : all data drop column, number : given number only with column name
        gdf.to_csv(fname,index=False)

    for irn in range(len(rockname_set)): # id-irn
      fname = f'{sub}tun_{det_dic[id]}_{rockname_dic[irn]}.csv'
      fname = f'{sub}tun_{A}_{id}_{A}_{irn}_{A}.csv'
      gdf = filter(df,en=-1, dn=id, rtn=-1, rnn=irn, cn=-1)  # -1 : all data drop column, number : given number only with column name
      gdf.to_csv(fname,index=False)

      # convert irn -> irt
      _irt = conv(irn)
      fname = f'{sub}tun_{A}_{id}_{_irt}_{irn}_{A}.csv'
      gdf = filter(df,en=-1, dn=id, rtn=_irt, rnn=irn, cn=-1)  # -1 : all data drop column, number : given number only with column name
      gdf.to_csv(fname,index=False)


      for ic in range(len(cen_set)): # id-irn-ic
        fname = f'{sub}tun_{det_dic[id]}_{rockname_dic[irn]}_{cen_dic[ic]}.csv'
        fname = f'{sub}tun_{A}_{id}_{A}_{irn}_{ic}.csv'
        gdf = filter(df,en=-1, dn=id, rtn=-1, rnn=irn, cn=ic)  # -1 : all data drop column, number : given number only with column name
        gdf.to_csv(fname,index=False)

        # convert irn -> irt
        _irt = conv(irn)
        fname = f'{sub}tun_{A}_{id}_{_irt}_{irn}_{ic}.csv'
        gdf = filter(df,en=-1, dn=id, rtn=_irt, rnn=irn, cn=ic)  # -1 : all data drop column, number : given number only with column name
        gdf.to_csv(fname,index=False)

    for ic in range(len(cen_set)): # id-ic
      fname = f'{sub}tun_{det_dic[id]}_{cen_dic[ic]}.csv'
      fname = f'{sub}tun_{A}_{id}_{A}_{A}_{ic}.csv'
      gdf = filter(df,en=-1, dn=id, rtn=-1, rnn=-1, cn=ic)  # -1 : all data drop column, number : given number only with column name
      gdf.to_csv(fname,index=False)

#--------------------------------------------------------------------------

  for irt in range(len(rocktype_set)): # irt
    fname = f'{sub}tun_{rocktype_dic[irt]}.csv'
    fname = f'{sub}tun_{A}_{A}_{irt}_{A}_{A}.csv'
    gdf = filter(df,en=-1, dn=-1, rtn=irt, rnn=-1, cn=-1)  # -1 : all data drop column, number : given number only with column name
    gdf.to_csv(fname,index=False)

    for ic in range(len(cen_set)): # irt-ic
      fname = f'{sub}tun_{rocktype_dic[irt]}_{cen_dic[ic]}.csv'
      fname = f'{sub}tun_{A}_{A}_{irt}_{A}_{ic}.csv'
      gdf = filter(df,en=-1, dn=-1, rtn=irt, rnn=-1, cn=ic)  # -1 : all data drop column, number : given number only with column name
      gdf.to_csv(fname,index=False)

#--------------------------------------------------------------------------

  for irn in range(len(rockname_set)): # irn
    fname = f'{sub}tun_{rockname_dic[irn]}.csv'
    fname = f'{sub}tun_{A}_{A}_{A}_{irn}_{A}.csv'
    gdf = filter(df,en=-1, dn=-1, rtn=-1, rnn=irn, cn=-1)  # -1 : all data drop column, number : given number only with column name
    gdf.to_csv(fname,index=False)

    # convert irn -> irt
    _irt = conv(irn)
    fname = f'{sub}tun_{A}_{A}_{_irt}_{irn}_{A}.csv'
    gdf = filter(df,en=-1, dn=-1, rtn=_irt, rnn=irn, cn=-1)  # -1 : all data drop column, number : given number only with column name
    gdf.to_csv(fname,index=False)
    

    for ic in range(len(cen_set)): # irn-ic
      fname = f'{sub}tun_{rockname_dic[irn]}_{cen_dic[ic]}.csv'
      fname = f'{sub}tun_{A}_{A}_{A}_{irn}_{ic}.csv'      
      gdf = filter(df,en=-1, dn=-1, rtn=-1, rnn=irn, cn=ic)  # -1 : all data drop column, number : given number only with column name
      gdf.to_csv(fname,index=False)

      # convert irn -> irt
      _irt = conv(irn)
      fname = f'{sub}tun_{A}_{A}_{_irt}_{irn}_{ic}.csv'      
      gdf = filter(df,en=-1, dn=-1, rtn=_irt, rnn=irn, cn=ic)  # -1 : all data drop column, number : given number only with column name
      gdf.to_csv(fname,index=False)

#--------------------------------------------------------------------------

  for ic in range(len(cen_set)): # ic
    fname = f'{sub}tun_{cen_dic[ic]}.csv'
    fname = f'{sub}tun_{A}_{A}_{A}_{A}_{ic}.csv'
    gdf = filter(df,en=-1, dn=-1, rtn=-1, rnn=-1, cn=ic)  # -1 : all data drop column, number : given number only with column name
    gdf.to_csv(fname,index=False)

  return


def lin_reg(gdf,fl,which):  # sklearn module
  # df = pd.read_csv(sub+fl)

  if which == 'reg2':
    gdf = gdf.sort_values(by=['SR SD'], axis=0)
    x = gdf['SR SD'].to_numpy().reshape(-1,1)    

  elif which == 'reg3':
    gdf = gdf.sort_values(by=['CR SD'], axis=0)
    x = gdf['CR SD'].to_numpy().reshape(-1,1)

  # x = gdf['SR SD'].to_numpy().reshape(-1,1)
  y = gdf['최대입자속도'].to_numpy().reshape(-1,1)
  x = np.log(x)
  y = np.log(y)
  # print(x,y)

  lin_fit = LinearRegression()
  lin_fit.fit(x,y)
  print(f'b = {np.exp(lin_fit.intercept_)}, a = {lin_fit.coef_}') 

  a = lin_fit.coef_
  b = lin_fit.intercept_
  sqr = np.sqrt(a*a+1)

  D = (a*x-y+b)/sqr # distances to the log-log regression line of every log-log points

  Ave = np.mean(D)
  STD = np.std(D)

  return np.exp(lin_fit.intercept_[0]), lin_fit.coef_[0,0], STD


def reg_ana(gdf,title,which): # ANN regression

  global reg2
  global reg3

  K = []
  n = []
  s = []

  if len(gdf) <= 0:
    print('empty in file')
    return K,n,s

  if which == 'reg2':
    gdf = gdf.sort_values(by=['SR SD'], axis=0)
    X = gdf['SR SD']    
    reg = reg2

  if which == 'reg3':
    gdf = gdf.sort_values(by=['CR SD'], axis=0)
    X = gdf['CR SD']    
    reg = reg3

  Y = gdf['최대입자속도']

  X = np.log(X)
  Y = np.log(Y)

  # print(X)
  # print(Y)
  
  reg.setXY(X,Y)

  pred = reg.train()

  # plt.plot(X,Y,'ro',X,pred)#,'bo')
  # plt.title(title)
  # plt.xlabel('Logarithmic Scaled Distance')
  # plt.ylabel('Logarithmic PPV')
  # plt.show()

  a = reg.W.numpy()
  b = reg.b.numpy()
  sqr = np.sqrt(a*a+1)

  D = (a*X-Y+b)/sqr # distance to the regression line of every point

  Ave = np.mean(D)
  STD = np.std(D)

  # print(f'Ave Dist to line is {Ave}, and std is {STD}')

  K = np.exp(reg.b.numpy())
  n = reg.W.numpy()
  s = STD
  return K, n, s

def get_flist():
  flist = os.listdir(sub)

  return flist

def plt_setting():
  font_path = "C:/Windows/Fonts/malgunsl.ttf"
  font = font_manager.FontProperties(fname=font_path).get_name()
  rc('font', family=font)  


def main():

  plt_setting()


  reg_df = pd.DataFrame(columns=('File Name','K','n','s','# of elem'))

  gen_data() # split data case by case and save it to file when it has some records

  flist = get_flist()

  for idx,fl in enumerate(flist): # redo
    if fl[0:4] == 'tun_': 
      print(f'loading file {sub+fl}...')
      df = pd.read_csv(sub+fl)
      if len(df) > 0:
        print(f'file name is {fl} and its length is {len(df)}') 
        K, n, s = lin_reg(df,fl,'reg2') 
        print(f'K = {K}, n = {n}, s = {s} ')
        reg_df.loc[idx] = [fl,K,n,s,len(df)]
        print(reg_df)
  reg_df.to_csv('reg_res_sqr.csv')

  # for idx,fl in enumerate(flist): # Done
  #   if fl[0:4] == 'tun_': 
  #     print(f'loading file {fl}...')
  #     df = pd.read_csv(fl)
  #     if len(df) > 0:
  #       print(f'file name is {fl} and its length is {len(df)}') 
  #       K, n, s = reg_ana(df,fl,'reg3')
  #       print(f'K = {K}, n = {n}, s = {s} ')
  #       reg_df.loc[idx] = [fl,K,n,s]
  #       print(reg_df)
  # reg_df.to_csv('reg_res_cbr.csv')

  return


if __name__ == "__main__":
  main()
