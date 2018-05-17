import numpy as np
import pylab as pl
import numpy
import os, sys
from matplotlib import pyplot as plt
from matplotlib import colors
from mpl_toolkits.axes_grid1 import make_axes_locatable
plt.rcParams.update({'font.size': 30})
magic_num_N=[2,8,20,28,50,82,126,184]
magic_num_Z=[2,8,20,28,50,82]
array=numpy.empty((105,220,))
array[:]=numpy.NaN
st=numpy.empty((105,220,))
st[:]=numpy.NaN
Data1 = np.loadtxt('Stable_Nuclides.txt')
num_lines1 = sum(1 for line in open('Stable_Nuclides.txt'))
for i in range (0,num_lines1-1):
	x=int(Data1[i][0])
	y=int(Data1[i][1])
	print x
	print y
	x=x-y
	st[y][x]= 1
cmap = colors.ListedColormap(['white', 'black'])
bounds=[0,0.5,1]
norm = colors.BoundaryNorm(bounds, cmap.N)

Data = np.loadtxt('path.dat')
num_lines = sum(1 for line in open('path.dat'))
for i in range (0,num_lines-1):
	x=int(Data[i][0])
	y=int(Data[i][1])
	print x
	print y
	array[y][x]= Data[i][2]
fig, ax1 = plt.subplots(nrows=1, ncols=1, figsize=(45,30))
plt.title('Something of importance', color='b')
plt.xlabel('Neutron Number (N)', color='k')
plt.ylabel('Atomic Number (Z)', color='k')
plt.imshow(st, interpolation='nearest', origin='upper',
                    cmap=cmap, norm=norm)
im=plt.imshow(array, interpolation="nearest", origin="upper")
for s in magic_num_N:
	for el in range (0,104):
		if np.isnan(st[el][s])!=True:
			el_ind=el
	for el in range (0,104):
		if np.isnan(array[el][s])!=True:
			mg=float(s)
			ax1.vlines(mg+0.5, el-1, el_ind+1, color="k")
			ax1.vlines(mg-0.5, el-1, el_ind+1, color="k")
for s in magic_num_Z:
	N_ind=0
	for N in range (0,219):
		if np.isnan(st[s][N])!=True:
			N_ind=N
	for N in range (0,219):
		if np.isnan(array[s][N])!=True:
			if N_ind!=0:
				mg=float(s)
				ax1.hlines(mg+0.5, N_ind-1, N+1, color="k")
				ax1.hlines(mg-0.5, N_ind-1, N+1, color="k")
			else:
				mg=float(s)
				ax1.hlines(mg+0.5, N-1, N+1, color="k")
				ax1.hlines(mg-0.5, N-1, N+1, color="k")
plt.gca().invert_yaxis()
divider = make_axes_locatable(ax1)
cax = divider.append_axes("right", size="5%", pad=0.05)
plt.colorbar(im, cax=cax)
plt.tight_layout()
plt.savefig("Your_plot.svg", transparent=True)
