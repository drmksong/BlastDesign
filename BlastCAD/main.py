import os
import math
import pyautocad
from pyautocad import APoint
from ctypes import *
# from comtypes import automation 
# from comtypes.automation import tagVARIANT as VARIANT
# import win32com.client
# import pythoncom

# def aVariant(obj):
#   return win32com.client.VARIANT(pythoncom.VT_ARRAY | pythoncom.VT_DISPATCH,(obj))
#   # return win32com.client.VARIANT(pythoncom.VT_ARRAY | pythoncom.VT_VARIANT,(obj))


def test():
  acad = pyautocad.Autocad()

  cen = APoint(0,0)
  pnt = APoint(10,10)
  cir1 = acad.model.AddCircle(cen, 100)
  cir1.Move(cen,pnt)
  cir2 = acad.model.AddCircle(cen, 100)

  cir1.ScaleEntity(cen,1.1)

  l1 = acad.model.AddLine(cen,pnt)

  l1.ScaleEntity(cen,10)
  l1.move(cen, pnt)

  try:
    sset = acad.doc.SelectionSets.Add('SS1')
    print('SS1 added')
  except:  
    sset = acad.doc.SelectionSets('SS1')
    print('Existing SS1 used')


  sset.Select(5)  # acSelectionSetAll = 5

  # sset.Erase()
  sset.Delete()

Arcs = []
acad = pyautocad.Autocad()

def sel():

  cen = APoint(0,0)
  pnt = APoint(-10,-10)

  try:
    sset = acad.doc.SelectionSets.Add('SS1')
    print('SS1 added')
  except:  
    sset = acad.doc.SelectionSets('SS1')
    print('Existing SS1 used')

  sset.SelectOnScreen()

  Arcs.clear()

  for ent in sset:
    print(ent.EntityName)

    if ent.EntityName ==  "AcDbArc":
      Ent = [ent.EntityName,ent.Center, ent.Radius, ent.StartAngle, ent.EndAngle]
      Arcs.append(Ent)
    elif ent.EntityName == "AcDbLine":
      Ent = [ent.EntityName, ent.StartPoint, ent.EndPoint]
      Arcs.append(Ent)

  sset.Erase()
  sset.Delete()

def draw():
  
  cen = APoint(0,0)
  pnt = APoint(10,10)

  for arc in Arcs:
    if arc[0]=="AcDbArc":
      print(arc[1]+cen, arc[2], arc[3], arc[4])
      acad.model.AddArc(arc[1]+pnt, arc[2], arc[3], arc[4])
    elif arc[0]=="AcDbLine":
      print(arc[1]+pnt, arc[1]+pnt)
      acad.model.AddLine(arc[1]+pnt, arc[2]+pnt)

  acad.doc.Regen(1)

def drill():
  cen = APoint(0,0)

  dr = []
  for i in range(10):
    for j in range(10):
      cen = APoint(i*2,j*2)
      cir = acad.model.AddCircle(cen, 0.5)
      dr.append(cir)

  acad.doc.Regen(1)

def selclr():
  cen = APoint(0,0)
  pnt = APoint(-10,-10)

  try:
    sset = acad.doc.SelectionSets.Add('SS2')
    print('SS2 added')
  except:  
    sset = acad.doc.SelectionSets('SS2')
    print('Existing SS2 used')

  sset.Select(5)
  
  for ent in sset:
    print(ent.EntityName)

    if ent.EntityName ==  "AcDbCircle" \
      or ent.EntityName ==  "AcDbHatch" \
      or ent.EntityName == "AcDbLine" \
      or ent.EntityName == "AcDbAlignedDimension" \
      or ent.EntityName == "AcDbRotatedDimension":
      ent.Delete()

  sset.Delete()
  acad.doc.Regen(1)

def PCut(In):

  acad.doc.ActiveDimStyle = acad.doc.DimStyles('standard')

  print(acad.doc.Linetypes.Item('ACAD_ISO02W100'))
  linetypeName = 'ACAD_ISO02W100'
  # if linetypeName not in acad.doc.Linetypes:
  #   acad.doc.Linetypes.Load( linetypeName, "acad.lin")

  cen = []
  bp1 = []
  bp2 = []
  bp3 = []
  bp4 = []

  bc1 = []
  bc2 = []
  bc3 = []
  bc4 = []

  bl1 = []
  bl2 = []
  bl3 = []
  bl4 = []

  dims = []  

  phi = In['Phi']
  cphi = phi*math.sqrt(In['NCH'])

  dia = In['Dia']
  a = int((1.5*cphi)/100)*100

  print(f'phi: {phi}, cphi: {cphi}, a: {a}')  

  av = cphi*(In['NCH']-1)/math.pow(In['NCH'],2)
  ah = 0 #cphi*(In['NCH']-1)/math.pow(In['NCH'],2)

  print(a,av,ah)

  nch = (In['NCH']*2) - 1
  print(nch)
  
  iphi = phi/1.0
  for i in range(nch):
    cen.append(APoint(0,i*iphi-(nch-1)*iphi/2))
    if i==nch-1:# and nch != 1:
      av = i*iphi-(nch-1)*iphi/2 - a + iphi*1.7
    if i%2==0:
      cenhole = acad.model.AddCircle(cen[i],phi/2)

  W1 = round((1.5*cphi)*math.sqrt(2)/100)*100

  # carr = []
  
  # cenhole = (acad.model.AddCircle(cen,dia/2))
  # carr.append(cenhole)
  
  # carr = VARIANT(carr)
  # carr = aVariant(carr)
  # carr = automation.VARIANT(carr)

  # patternName = "SOLID"
  # PatternType = 0
  # bAssociativity = True
  # hatchObj = acad.model.AddHatch(PatternType, patternName, bAssociativity)

  # hatchObj.AppendOuterLoop(carr)
  # hatchObj.AppendOuterLoop(carr)
  # hatchObj.Evaluate()

  bp1.append(APoint(0,a+av))
  bp1.append(APoint(a-ah,0))
  bp1.append(APoint(0,-a-av))
  bp1.append(APoint(-a+ah,0))

  bc1.append(acad.model.AddCircle(bp1[0],dia/2))
  bc1.append(acad.model.AddCircle(bp1[1],dia/2))
  bc1.append(acad.model.AddCircle(bp1[2],dia/2))
  bc1.append(acad.model.AddCircle(bp1[3],dia/2))
  
  bl1.append(acad.model.AddLine(bp1[0],bp1[1]))
  bl1.append(acad.model.AddLine(bp1[1],bp1[2]))
  bl1.append(acad.model.AddLine(bp1[2],bp1[3]))
  bl1.append(acad.model.AddLine(bp1[3],bp1[0]))

  for l in bl1:
    l.LineType = linetypeName
    l.LinetypeScale = 1
    # l.LineWeight = 1000

  W2 = round(1.5*W1*math.sqrt(2)*100)/100

  bp2.append(APoint(W1,W1))
  bp2.append(APoint(W1,-W1))
  bp2.append(APoint(-W1,-W1))
  bp2.append(APoint(-W1,W1))

  bc2.append(acad.model.AddCircle(bp2[0],dia/2))
  bc2.append(acad.model.AddCircle(bp2[1],dia/2))
  bc2.append(acad.model.AddCircle(bp2[2],dia/2))
  bc2.append(acad.model.AddCircle(bp2[3],dia/2))

  bl2.append(acad.model.AddLine(bp2[0],bp2[1]))
  bl2.append(acad.model.AddLine(bp2[1],bp2[2]))
  bl2.append(acad.model.AddLine(bp2[2],bp2[3]))
  bl2.append(acad.model.AddLine(bp2[3],bp2[0]))

  for l in bl2:
    l.LineType = linetypeName
    l.LinetypeScale = 1
    # l.LineWeight = 1000

  W3 = round(W2/100+.5)*100#*math.sqrt(2) 

  bp3.append(APoint(0,W2))
  bp3.append(APoint(W2,0))
  bp3.append(APoint(0,-W2))
  bp3.append(APoint(-W2,0))

  bc3.append(acad.model.AddCircle(bp3[0],dia/2))
  bc3.append(acad.model.AddCircle(bp3[1],dia/2))
  bc3.append(acad.model.AddCircle(bp3[2],dia/2))
  bc3.append(acad.model.AddCircle(bp3[3],dia/2))

  bl3.append(acad.model.AddLine(bp3[0],bp3[1]))
  bl3.append(acad.model.AddLine(bp3[1],bp3[2]))
  bl3.append(acad.model.AddLine(bp3[2],bp3[3]))
  bl3.append(acad.model.AddLine(bp3[3],bp3[0]))

  for l in bl3:
    l.LineType = linetypeName
    l.LinetypeScale = 1
    # l.LineWeight = 1000

  W4 = W3#*math.sqrt(2)

  bp4.append(APoint(W3,W3))
  bp4.append(APoint(W3,-W3))
  bp4.append(APoint(-W3,-W3))
  bp4.append(APoint(-W3,W3))

  bc4.append(acad.model.AddCircle(bp4[0],dia/2))
  bc4.append(acad.model.AddCircle(bp4[1],dia/2))
  bc4.append(acad.model.AddCircle(bp4[2],dia/2))
  bc4.append(acad.model.AddCircle(bp4[3],dia/2))

  bl4.append(acad.model.AddLine(bp4[0],bp4[1]))
  bl4.append(acad.model.AddLine(bp4[1],bp4[2]))
  bl4.append(acad.model.AddLine(bp4[2],bp4[3]))
  bl4.append(acad.model.AddLine(bp4[3],bp4[0]))

  for l in bl4:
    l.LineType = linetypeName
    l.LinetypeScale = 1
    # l.LineWeight = 1000

  print(f'W1:{W1},W2:{W2},W3:{W3}, W4:{W4}')

  ###################

  dims.append(acad.model.AddDimAligned(bp1[1],bp1[3],bp4[1]+APoint(0.,-200)))
  dims.append(acad.model.AddDimRotated(bp2[2],bp1[3],bp4[1]+APoint(0.,-200),0))
  dims.append(acad.model.AddDimRotated(bp1[1],bp2[1],bp4[1]+APoint(0.,-200),0))
  dims.append(acad.model.AddDimRotated(bp4[2],bp2[2],bp4[1]+APoint(0.,-200),0))
  dims.append(acad.model.AddDimRotated(bp2[1],bp4[1],bp4[1]+APoint(0.,-200),0))
  dims.append(acad.model.AddDimAligned(bp4[1],bp4[2],bp4[1]+APoint(0.,-400)))

  ##################

  dims.append(acad.model.AddDimRotated(bp4[2],bp2[2],bp4[2]+APoint(-200.,0),3.14/2))
  dims.append(acad.model.AddDimRotated(bp2[3],bp4[3],bp4[2]+APoint(-200.,0),3.14/2))
  dims.append(acad.model.AddDimRotated(bp2[2],bp3[3],bp4[2]+APoint(-200.,0),3.14/2))
  dims.append(acad.model.AddDimRotated(bp3[3],bp2[3],bp4[2]+APoint(-200.,0),3.14/2))
  dims.append(acad.model.AddDimAligned(bp4[2],bp4[3],bp4[2]+APoint(-400.,0)))

  #################

  # dim1.Style = 'standard'


  # dr = []
  # for i in range(10):
  #   for j in range(10):
  #     cen = APoint(i*2,j*2)
  #     cir = acad.model.AddCircle(cen, phi/2)
  #     dr.append(cir)

  acad.doc.Regen(1)
  
def VCut(param):
  acad.doc.ActiveDimStyle = acad.doc.DimStyles('standard')

  linetypeName = 'ACAD_ISO02W100'
  # if linetypeName not in acad.doc.Linetypes:
  #   acad.doc.Linetypes.Load( linetypeName, "acad.lin")

  print(acad.doc.Linetypes.Item('ACAD_ISO02W100'))

  dia = param['Dia']
  ADV = param['ADV']
  B1 = param['B1']
  B2 = param['B2']
  H1 = param['H1']
  H2 = param['H2']
  H3 = param['H3']

  cen = []
  bp1 = []
  bp2 = []
  bp3 = []
  
  bc1 = []
  bc2 = []
  bc3 = []
  
  bl1 = []
  bl2 = []
  bl3 = []
  
  dims = []  

  L1 = round(math.sqrt((H1)*(H1)-(B1)*(B1))/10)*10

  print(f'L1 = {L1}')

  cen.append(APoint(0,-B1))
  cen.append(APoint(0,0))
  cen.append(APoint(0,B1))

  bp1.append(APoint(-L1,-B1))
  bp1.append(APoint(-L1,0))
  bp1.append(APoint(-L1,B1))

  bp1.append(APoint(L1,-B1))
  bp1.append(APoint(L1,0))
  bp1.append(APoint(L1,B1))

  bc1.append(acad.model.AddCircle(bp1[0],dia/2))
  bc1.append(acad.model.AddCircle(bp1[1],dia/2))
  bc1.append(acad.model.AddCircle(bp1[2],dia/2))

  bc1.append(acad.model.AddCircle(bp1[3],dia/2))
  bc1.append(acad.model.AddCircle(bp1[4],dia/2))
  bc1.append(acad.model.AddCircle(bp1[5],dia/2))
  
  bl1.append(acad.model.AddLine(bp1[0],bp1[1]))
  bl1.append(acad.model.AddLine(bp1[1],bp1[2]))

  bl1.append(acad.model.AddLine(bp1[3],bp1[4]))
  bl1.append(acad.model.AddLine(bp1[4],bp1[5]))

  for l in bl1:
    l.LineType = linetypeName
    l.LinetypeScale = 1
    # l.LineWeight = 1000


  L2 = round(math.sqrt((H2)*(H2)-(B1+B2)*(B1+B2))/10)*10

  print(f'L2 = {L2}')

  bp2.append(APoint(-L2,-B1))
  bp2.append(APoint(-L2,0))
  bp2.append(APoint(-L2,B1))

  bp2.append(APoint(L2,-B1))
  bp2.append(APoint(L2,0))
  bp2.append(APoint(L2,B1))

  bc2.append(acad.model.AddCircle(bp2[0],dia/2))
  bc2.append(acad.model.AddCircle(bp2[1],dia/2))
  bc2.append(acad.model.AddCircle(bp2[2],dia/2))

  bc2.append(acad.model.AddCircle(bp2[3],dia/2))
  bc2.append(acad.model.AddCircle(bp2[4],dia/2))
  bc2.append(acad.model.AddCircle(bp2[5],dia/2))

  bl2.append(acad.model.AddLine(bp2[0],bp2[1]))
  bl2.append(acad.model.AddLine(bp2[1],bp2[2]))

  bl2.append(acad.model.AddLine(bp2[3],bp2[4]))
  bl2.append(acad.model.AddLine(bp2[4],bp2[5]))

  for l in bl2:
    l.LineType = linetypeName
    l.LinetypeScale = 1
    # l.LineWeight = 1000

  L3 = round(math.sqrt((H3)*(H3)-(B1+B2)*(B1+B2))/10)*10 + L2

  print(f'L3 = {L3}')

  bp3.append(APoint(-L3,-B1))
  bp3.append(APoint(-L3,0))
  bp3.append(APoint(-L3,B1))
  bp3.append(APoint( L3,-B1))
  bp3.append(APoint( L3,0))
  bp3.append(APoint( L3,B1))

  bc3.append(acad.model.AddCircle(bp3[0],dia/2))
  bc3.append(acad.model.AddCircle(bp3[1],dia/2))
  bc3.append(acad.model.AddCircle(bp3[2],dia/2))
  bc3.append(acad.model.AddCircle(bp3[3],dia/2))
  bc3.append(acad.model.AddCircle(bp3[4],dia/2))
  bc3.append(acad.model.AddCircle(bp3[5],dia/2))

  bl3.append(acad.model.AddLine(bp3[0],bp3[1]))
  bl3.append(acad.model.AddLine(bp3[1],bp3[2]))
  bl3.append(acad.model.AddLine(bp3[3],bp3[4]))
  bl3.append(acad.model.AddLine(bp3[4],bp3[5]))

  for l in bl3:
    l.LineType = linetypeName
    l.LinetypeScale = 1
    # l.LineWeight = 1000


  ###################

  dims.append(acad.model.AddDimAligned(bp1[0],cen[0],cen[0]+APoint(0.,-200)))
  dims.append(acad.model.AddDimAligned(bp1[3],cen[0],cen[0]+APoint(0.,-200)))  
  dims.append(acad.model.AddDimAligned(bp2[0],bp1[0],bp1[0]+APoint(0.,-200)))
  dims.append(acad.model.AddDimAligned(bp2[3],bp1[3],bp1[0]+APoint(0.,-200)))  
  dims.append(acad.model.AddDimAligned(bp3[0],bp2[0],bp2[0]+APoint(0.,-200)))
  dims.append(acad.model.AddDimAligned(bp3[3],bp2[3],bp2[0]+APoint(0.,-200)))  
  dims.append(acad.model.AddDimAligned(bp3[0],cen[0],bp3[0]+APoint(0.,-400)))
  dims.append(acad.model.AddDimAligned(bp3[3],cen[0],bp3[3]+APoint(0.,-400)))

  ##################

  dims.append(acad.model.AddDimAligned(bp3[3],bp3[4],bp3[4]+APoint(200.,0)))
  dims.append(acad.model.AddDimAligned(bp3[4],bp3[5],bp3[5]+APoint(200.,0)))
  dims.append(acad.model.AddDimAligned(bp3[3],bp3[5],bp3[5]+APoint(400.,0)))

  #################



  acad.doc.Regen(1)


def Box(param):

  Dia = param['Dia']
  S = param['S']
  B = param['B']

  pnts = []
  pnts.append(APoint(1000,1000))
  pnts.append(APoint(-1000,1000))
  pnts.append(APoint(-1000,0))
  pnts.append(APoint(1000,0))

  lines = []
  lines.append(acad.model.AddArc(APoint(0,1000),1000,0,3.14159))
  lines.append(acad.model.AddLine(pnts[1],pnts[2]))
  lines.append(acad.model.AddLine(pnts[2],pnts[3]))
  lines.append(acad.model.AddLine(pnts[3],pnts[0]))


  # try:
  #   sset = acad.doc.SelectionSets.Add('SS3')
  #   print('SS3 added')
  # except:  
  #   sset = acad.doc.SelectionSets('SS3')
  #   print('Existing SS3 used')

  # sset.SelectOnScreen()

  bl = []

  dps = []





  acad.doc.Regen(1)
  
  


def main():
  
  param = {}

  # sel()
  # print('erase all')
  # draw()
  # print('redraw all')
  # drill()
  # selcir()

  # param['Phi'] = 0.102
  # param['NCH'] = 2
  # CenCut(param)
  # os.system('pause')

  selclr()

  ########################################################
  # selclr()
  # param['NCH'] = 3  # number of uncharged center holes 
  # param['Phi'] = 102 # diameter of uncharged center holes
  # param['Dia'] = 45 # diameter of charged drill holes
  # PCut(param)

  #####################################################
  # selclr()  
  # param['Dia'] = 45 # diameter of charged drill holes
  # param['ADV'] = 1650 # drill length
  # param['B1'] = 850
  # param['B2'] = 850
  # param['H1'] = 1050
  # param['H2'] = 2000
  # param['H3'] = 1870
  # VCut(param)
  #########################################################

  param['Dia'] = 45
  param['B'] = 110
  param['S'] = 100
  Box(param)

  # os.system('pause')
  # selcir()

  # param['Phi'] = 0.076
  # param['NCH'] = 4
  # CenCut(param)
  # os.system('pause')
  # selcir()


if __name__ == '__main__':
  main()