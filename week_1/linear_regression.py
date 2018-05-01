#!/usr/bin/python

##################
#   LIBRAIRIES   #
##################

import numpy as np
import math
####################
#   INSTRUCTIONS   #
####################

#   READ FILE
################

file_in = open("data/ex1data1.txt")

A=[]
B=[]

for lines in file_in:
	lines.rstrip(" \n")
	A.append(float(lines.split(",")[0]))
	B.append(float(lines.split(",")[1]))

X=np.asmatrix(A)
Y=np.asmatrix(B)

#   model
############

Theta = [0, 0]

def	costFunction(x_values, y_values, theta):
	hypothesis = np.dot(theta[0], x_values) + theta[1]
	loss = hypothesis - y_values
	cost = np.sum(np.dot(loss, np.transpose(loss)))
	return(cost / (2*len(np.transpose(x_values))))

print(costFunction(X, Y, Theta))

def gradientDescent(x_values, y_values, theta, alpha, num_iters):
	m = len(np.transpose(x_values))
	J_history = [0]*num_iters
	for i in range(0, num_iters):
		J_theta_zero = np.sum(np.dot(((np.dot(theta[0], x_values) + theta[1]) - y_values), x_values))
		J_theta_one = np.sum((np.dot(theta[0], x_values) + theta[1]) - y_values)
		theta_zero = theta[0] - alpha * (1/m) * J_theta_zero
		theta_one  = theta[1] - alpha * (1/m) * J_theta_one
		theta = [theta_zero, theta_one]
		J_history[i] = costFunction(x_values, y_values, theta)
	return(min(J_history))

print(gradientDescent(A, B, Theta, 0.024, 1000))
