import pandas as pd
import numpy as np
import os
from sklearn.linear_model import LinearRegression

# global variable
sub = './separated/'

def get_flist():
  flist = os.listdir(sub)
  return flist


def remove_empty(flist):
  for fl in flist:
    # print(sub+fl)
    df = pd.read_csv(sub+fl)
    if df.size == 0:
      print(sub+fl+ ' will be removed')
      os.remove(sub+fl)


def lin_reg(fl):
  df = pd.read_csv(sub+fl)
  x = df['SR SD'].to_numpy().reshape(-1,1)
  y = df['최대입자속도'].to_numpy().reshape(-1,1)
  x = np.log(x)
  y = np.log(y)
  # print(x,y)

  lin_fit = LinearRegression()
  lin_fit.fit(x,y)
  print(f'b = {np.exp(lin_fit.intercept_)}, a = {lin_fit.coef_}') 
  return np.exp(lin_fit.intercept_), lin_fit.coef_
  

def synthesis(flist):
  sqrf = 'sqr_data.csv'
  df = pd.read_csv(sqrf)

  print(df)

  for fl in flist[:1]:
    code = fl.split('_')
    code[5] = code[5].split('.')[0]
    exp = 0 if code[1]=='a' else int(code[1])+1
    det = 0 if code[2]=='a' else int(code[2])+1
    rot = 0 if code[3]=='a' else int(code[3])+1
    roc = 0 if code[4]=='a' else int(code[4])+1
    cen = 0 if code[5]=='a' else int(code[5])+1
    
    print(f'화약 {exp} 뇌관 {det} 암종{rot} 암석{roc} 심발{cen}')

    cond = (df['exp'] == exp) & (df['det'] == det) & (df['rot'] == rot)
    cond = cond & (df['roc'] == roc) & (df['cen'] == cen)
    loc = df.loc[cond]
    
    K = loc.iloc[0]['K']
    n = loc.iloc[0]['n']
    s = loc.iloc[0]['s']

    print(f'K = {K:3.3}, n = {n:3.3}, s = {s:3.3}')
    
    b, a = lin_reg(fl)

  return df


def main():
  flist = get_flist()
  remove_empty(flist)
  synthesis(flist)


if __name__ == '__main__':
  main()
