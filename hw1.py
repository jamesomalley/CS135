'''
hw1.py
Author: James O'Malley

Tufts CS 135 Intro ML

'''

import numpy as np

def split_into_train_and_test(x_all_LF,frac_test,random_state):
   #randomizing the data
   random_state = np.random.default_rng(seed=42)
   L = len(x_all_LF)
  # rng.shuffle(x_all_LF) 
   #x_all_LF = x_all_LF

   #training data
   M = L - np.round(frac_test * L)
   M = M.astype(int)
   x_train_MF =  np.array(x_all_LF[0:M])   
   
    #testing data
   N =  np.round(frac_test * L)
   N = N.astype(int)
   x_test_NF =  np.array(x_all_LF[M:len(x_all_LF)])
   x_test_NF = x_test_NF
    
   if random_state is None:
       random_state = np.random
   return x_train_MF,  x_test_NF

"""
#Run function
x_test_NF, x_train_MF = split_into_train_and_test(x_all_LF, frac_test,random_state=None)



#Print results
print (np.allclose(x_all_LF, xcopy_LF))
print("X Test NF: ", np.shape(x_test_NF), x_test_NF)
print("X Train MF: ", np.shape(x_train_MF), x_train_MF)
"""