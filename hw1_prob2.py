"""
import numpy as np


array1 = np.array([[1, 2], [4, 5], [6,7], [8,9]])
array2 = np.array([[2, 2], [3, 3], [4,4], [5,5]])

def calc_k_nearest_neighbors(data_NF,query_QF,K):
   neighb_QKF = np.zeros((len(query_QF),K,query_QF.ndim))
   print(neighb_QKF)
   print(neighb_QKF.shape)

   for i in data_NF:
          for j in query_QF:
              distance = np.sqrt(np.sum((i - j )** 2))
              neighb_QKF[i] = np.array([1,2])
              print(neighb_QKF)
   return distance

"""



import numpy as np


array1 = np.array([[1, 2], [4, 5], [6,7], [8,9]])
array2 = np.array([[2, 2], [3, 3], [4,4], [5,5]])

def calc_k_nearest_neighbors(data_NF,query_QF,K):
    distance = np.eye(len(data_NF))
    for i in range(len(data_NF)):
        for j in range(len(query_QF)):
            distance[i,j] = np.sqrt(np.sum((data_NF[i] - query_QF[j]) ** 2))
            NF, QF, Dist = data_NF[i], query_QF[j], distance[i,j]
            return NF, QF, Dist
    neighb_QKF = np.sort(distance[i,j][:,:K])
    neighb_QKF = np.hstack((query_QF,neighb_QKF, data_NF))[:K]
    return neighb_QKF


knn = np.array(calc_k_nearest_neighbors(array1,array2,K=3),dtype=object)
print(knn)
"""
   for i in data_NF:
       distance = np.sqrt(np.sum((data_NF - query_QF) ** 2)) 

   print(distances)
    
   
    neighb_QKF = np.zeros((len(query_QF),K,query_QF.ndim))
   print(neighb_QKF)
   print(neighb_QKF.shape)

   for i in data_NF:
          for j in query_QF:
              distance = np.sqrt(np.sum((i - j )** 2))
              neighb_QKF[i] = np.array([1,2])
              print(neighb_QKF)
   return distance


"""