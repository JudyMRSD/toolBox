#from folder apc_40_prior 
import re
import os
import xml.etree.ElementTree as ET
import pdb

tree = ET.parse('tote301.xml')
root = tree.getroot()
print "start"

import glob, os
os.chdir("/childfolder")
for file in glob.glob("*.txt"):
    print(file)

    f = open(file+'.txt', 'w')
    for item in root.findall('object'):
        name = item.find('name').text
        print name 
        for bndbox in item.findall('bndbox'):
            xmin = bndbox.find('xmin').text
            ymin = bndbox.find('ymin').text
            xmax = bndbox.find('xmax').text
            ymax = bndbox.find('ymax').text
            print name
            print xmin
            s = str(name)+' '+str(xmin)+' '+ str(ymin)+' '+str(xmax)+' '+str(ymax)+' 1'+'\n'
            f.write(s)

    
#output: names, xmin, ymin, xmax, ymax, score