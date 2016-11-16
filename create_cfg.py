from sys import argv
import commands
import time
import re
import os
import string
from os import listdir

import sys
sys.path.append('./')

spin = ['GluGluSpin0ToBBbar_W_1p0_M_X_TuneCUEP8M1_13TeV_pythia8',
        'RSGravitonToBBbar_kMpl01_M_X_TuneCUEP8M1_13TeV_pythia8',
        'BstarToGJ_M_X_f1p0_TuneCUETP8M1_13TeV_pythia8',
        'ZprimeToBBbar_M_X_TuneCUETP8M1_13TeV_pythia8']

debug = True




##################

def create(sample, mass=750 , width=0.01):

    fin = open( sample+'_cfi.py' , 'r')
    fout = open( sample.replace('_X_', '_'+str(mass)+'_')+'_cfi.py', 'w')

    for line in fin:
        if 'm0' in line:
            fout.write(line.rstrip('\',\n')+("%.0f" % mass)+'\', \n')
        elif 'mWidth' in line:
            fout.write(line.rstrip('\',\n')+("%.1f" % (mass*width))+'\', \n')
        else:
            fout.write(line)

    fout.close()
    fin.close()
    
##################


for sample in spin:
    for mass in [500,1000,2000,3000,4000,5000,6000,7000,8000,9000]:
        create(sample, mass)
