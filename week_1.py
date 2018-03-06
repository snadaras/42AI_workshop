# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    week_1.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: fbabin <fbabin@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/03/06 18:01:07 by fbabin            #+#    #+#              #
#    Updated: 2018/03/06 18:08:10 by fbabin           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#create a tuple
("fbabin", 25)

#dictionnary initialisation
dict = {"pdespres": 46, "pchoffe": 56}

#get info in dict
dict["pdespres"]

#adding enry to dict
dict["fbabin"]=25

#creating a list
A = [1,3,2,7,4,10,46]

#show first three elements
A[:3]

#show third to fifth element
B = A[3:6]

#concatenate lists
C = A + B

#add to list
C.append(5)
C.append(None)

#functions
def nconcat(lst, n):
    new = []
    while n != 0:
        new += lst
        n -= 1
    return new

result = nconcat(B, 2)
result

#optionnal arguments
def nconcat(lst, n=2):
    new = []
    while n != 0:
        new += lst
        n -= 1
    return new

result = nconcat(B)
result

#while loops
i = 0
while C[i] != None:
    print(str(C[i]))
    i += 1

#pair ints
n = 0
for elem in A:
    if (elem % 2 == 0):
        n += 1
print (str(n))

C = []
for elem in A:
    if (elem % 2 == 0):
        C.append(elem)
print (C)

#Numpy

import numpy as np

a = np.asarray(A)
b = np.asarray(B)
c = np.concatenate((a, b), axis=0)

c / 3
np.sum(c)
np.add(N, M)
np.dot(N, M)
