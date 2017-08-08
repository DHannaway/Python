import numpy as np
import matplotlib.pyplot as plt
import random
import os

#Path to the executable file:
codepath='C:\\Users\\Dan\\Documents\\GitHub\\Python\\'
filename='CMacIonize.exe --params test_dustsimulation.param --dusty-radiative-transfer --threads 4'

#Enter new values for the parameters
B_T=input("Enter the value of B_over_T: ")	# B_over_T
h_stars=input("Enter the value of h_stars (kpc): ")	# h_stars
r_stars=input("Enter the value of r_stars (kpc): ")	# r_stars
h_ISM=input("Enter the value of h_ISM (kpc): ")	# h_ISM
r_ISM=input("Enter the value of r_ISM (kpc): ")	# r_ISM
n_0=input("Enter the value of n_0 (cm^-3): ")	# n_0

nphotons=600000

#Replace the old .param file with a new one with the entered values
with open('test_dustsimulation_original.param') as g:
	lines=list(g)

h=open('test_dustsimulation.param','w')
for i in range(0,len(lines)):
	if i==12:
		h.write('  B_over_T: '+B_T+'\n')
	elif i==13:
		h.write( '  h_stars: '+h_stars+' kpc\n' )
	elif i==14:
		h.write('  r_stars: '+r_stars+' kpc\n'  )
	elif i==16:
		h.write('  h_ISM: '+h_ISM+' kpc\n'  )
	elif i==18:
		h.write('  r_ISM: '+r_ISM+' kpc\n'  )
	elif i==17:
		h.write('  n_0: '+n_0+' cm^-3\n' )
	elif i==28:
		h.write('number of photons: '+str(nphotons)+'\n'  )
	else:
		h.write(lines[i])
h.close()

#Input this new file into the testDustSimulation program and compile
os.system(codepath+filename)  

#Input the created binary file, and plot as an image
image = np.fromfile("test_dustsimulation_output.dat", dtype = np.float64)
image = image.reshape((200, 200))
fig, ax = plt.subplots()
ax.matshow(np.transpose(image), cmap='Greys_r')
plt.text(5,60,"B_T ="+str(B_T)+'\n'+"h_stars ="+str(h_stars)+'\n'+"r_stars ="+str(r_stars)+'\n'+"h_ISM ="+str(h_ISM)+'\n'+"r_ISM ="+str(r_ISM)+'\n'+"n0 ="+str(n_0),color='w')
plt.show()

