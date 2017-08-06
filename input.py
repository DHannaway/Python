import numpy as np
import matplotlib.pyplot as plt
import random
import os

#Path to the executable file:
codepath='C:\\Users\\Dan\\Desktop\\"Summer_Project"\\testDustSimulation.exe'

#Enter new values for the four parameters
param1=input("Enter the value of B_over_T (Original value: 0.2): ")	# B_over_T
param2=input("Enter the value of h_stars (Original value: 0.6 kpc): ")	# h_stars
param3=input("Enter the value of r_stars (Original value: 5. kpc): ")	# r_stars
param4=input("Enter the value of h_ISM (Original value: 0.22 kpc): ")	# h_ISM
nphotons=input("Enter the number of photons to simulate (Original value 50,000): ")

#Replace the old .param file with a new one with the entered values
with open('test_dustsimulation_original.param') as g:
	lines=list(g)

h=open('test_dustsimulation.param','w')
for i in range(0,len(lines)):
	if i==12:
		h.write('  B_over_T: '+param1+'\n')
	elif i==13:
		h.write( '  h_stars: '+param2+' kpc\n' )
	elif i==14:
		h.write('  r_stars: '+param3+' kpc\n'  )
	elif i==16:
		h.write('  h_ISM: '+param4+' kpc\n'  )
	elif i==28:
		h.write('number of photons: '+nphotons+'\n'  )
	else:
		h.write(lines[i])
h.close()

#Input this new file into the testDustSimulation program and compile
os.system(codepath)  

#Input the created binary file, and plot as an image
image = np.fromfile("test_dustsimulation_output.dat", dtype = np.float64)
image = image.reshape((200, 200))
fig, ax = plt.subplots()
ax.matshow(np.transpose(image), cmap='Greys')
plt.text(5,40,"B_T ="+str(param1)+'\n'+"h_stars ="+str(param2)+'\n'+"r_stars ="+str(param3)+'\n'+"h_ISM ="+str(param4))
plt.show()

