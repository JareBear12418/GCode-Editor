# from gcodeparser import GcodeParser
# from pprint import pprint as print
# # open gcode file and store contents as variable
# with open('heptagon-circle-50mm.nc', 'r') as f:
#   gcode = f.read()

# print(GcodeParser(gcode).lines)    # get parsed gcode lines

from matplotlib import pyplot as plt # import libraries
import pandas as pd # import libraries
import netCDF4 # import libraries
fp='heptagon-circle-50mm.nc' # your file name with the eventual path
nc = netCDF4.Dataset(fp) # reading the nc file and creating Dataset
""" in this dataset each component will be 
in the form nt,nz,ny,nx i.e. all the variables will be flipped. """
plt.imshow(nc['Temp'][1,:,0,:]) 
""" imshow is a 2D plot function
according to what I have said before this will plot the second
iteration of the vertical slize with y = 0, one of the vertical
boundaries of your model. """
plt.show() # this shows the plot