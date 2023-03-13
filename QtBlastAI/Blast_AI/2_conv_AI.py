import pandas as pd
import os

def extract(fname,idx):
  sp = fname.split('_')
  sp = sp[idx+1].split('.')
  if (sp[0]=='a'):
    return 0
  else:
    return int(sp[0])+1 # a -> 0, 0 -> 1, n -> n+1


def main():
  df = pd.read_csv('reg_res_sqr.csv', index_col=False)
  df['exp'] = 0  
  df['det'] = 0
  df['rot'] = 0
  df['roc'] = 0
  df['cen'] = 0
  df.drop(['Unnamed: 0'], axis = 1, inplace = True)

  df['exp']  = df['File Name'].map(lambda x : extract(x,0))
  df['det']  = df['File Name'].map(lambda x : extract(x,1))
  df['rot']  = df['File Name'].map(lambda x : extract(x,2))
  df['roc']  = df['File Name'].map(lambda x : extract(x,3))
  df['cen']  = df['File Name'].map(lambda x : extract(x,4))
  df.drop(['File Name'], axis = 1, inplace = True)

  print(df)
  df.to_csv('sqr_data.csv',index=False)

  # df = pd.read_csv('reg_res_cbr.csv', index_col=False)
  # df['exp'] = 0  
  # df['det'] = 0
  # df['rot'] = 0
  # df['roc'] = 0
  # df['cen'] = 0
  # df.drop(['Unnamed: 0'], axis = 1, inplace = True)

  # df['exp']  = df['File Name'].map(lambda x : extract(x,0))
  # df['det']  = df['File Name'].map(lambda x : extract(x,1))
  # df['rot']  = df['File Name'].map(lambda x : extract(x,2))
  # df['roc']  = df['File Name'].map(lambda x : extract(x,3))
  # df['cen']  = df['File Name'].map(lambda x : extract(x,4))
  # df.drop(['File Name'], axis = 1, inplace = True)

  # print(df)
  # df.to_csv('cbr_data.csv', index=False)


if __name__ == "__main__":
  main()
