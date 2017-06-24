#tr = "this is string example....wow!!!:wq!"
#print str.lstrip()
#str = "88888888this is string example....wow!!!8888888"
#print str.lstrip('8')
import os
import csv
import numpy as np

from matplotlib.ticker import MultipleLocator, FormatStrFormatter

import matplotlib.pyplot as plt


loss = []
#number iterations per epoch
num_iter = 100000

#s1 = "I0317 20:16:44.186024 15597 solver.cpp:229] Iteration 80, loss = 1.47939";
#s2 = "loss ="
#s3 = s1[s1.index(s2) + len(s2):]
#print s3
#loss_number = float(s3)
#print loss_number

interest_word = ", loss = "
print "---"
with open("./test.txt", "r") as file:
#with open("./pretrain.txt", "r") as ins:
    for line in file:
        if interest_word in line:
            print interest_word
            print line 
            loss_string = line[line.index(interest_word) + len(interest_word):]
            loss_number = float(loss_string)
            loss.append(loss_number)
n = len(loss)
print loss
