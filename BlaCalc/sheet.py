# export to excel file, yet to know whether we need it or not
from openpyxl import Workbook
from cent_tb import *


class sheet:
    def __init__(self):
        pass

    def save(self, cent: CentCut):
        if cent.name == 'P-Cut':
            print('P-Cut is saved')

        if cent.name == 'V-Cut':
            print('V-Cut is saved')
