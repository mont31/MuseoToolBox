# -*- coding: utf-8 -*-
"""
Leave-P-SubGroup-Out (LPSGO)
======================================================

This example shows how to make a Leave-Percent-SubGroup-Out.

"""

##############################################################################
# Import librairies
# -------------------------------------------

from museotoolbox.cross_validation import LeavePSubGroupOut
from museotoolbox import datasets,raster_tools
import numpy as np

##############################################################################
# Load HistoricalMap dataset
# -------------------------------------------

raster,vector = datasets.getHistoricalMap()
field = 'Class'
group = 'uniquefid'

##############################################################################
# Create CV
# -------------------------------------------
valid_size = 0.5 # Means 50%
LPSGO = LeavePSubGroupOut(valid_size = valid_size,n_splits=10,
                          random_state=12,verbose=False)
    
###############################################################################
# Extract X,y and group.
# -------------------------------------------

X,y,g=raster_tools.getSamplesFromROI(raster,vector,field,group)

###############################################################################
# .. note::
#    Split is made to generate each fold

for tr,vl in LPSGO.split(X,y,g):
    print(tr.shape,vl.shape)

print('y label with number of samples')
print(np.unique(y[tr],return_counts=True))
##############################################################################
# Differences with scikit-learn
# -------------------------------------------
from sklearn.model_selection import LeavePGroupsOut
# You need to specify the number of groups
LPGO = LeavePGroupsOut(n_groups=2)
for tr,vl in LPGO.split(X,y,g):
    print(tr.shape,vl.shape)

##############################################################################
# With GroupShuffleSplit, won't keep the percentage per subgroup
# This generate unbalanced classes
    
from sklearn.model_selection import GroupShuffleSplit
GSS = GroupShuffleSplit(test_size=0.5,n_splits=5)
for tr,vl in GSS.split(X,y,g):
    print(tr.shape,vl.shape)

print('y label with number of samples')
print(np.unique(y[tr],return_counts=True))

###############################################################################
# Plot example in image
    
import numpy as np
from matplotlib import pyplot as plt
plt.scatter(np.random.randint(10,20,40),np.random.randint(10,30,40),s=100,color='#1f77b4')
plt.scatter(np.random.randint(0,10,40),np.random.randint(10,30,40),s=100,color='#1f77b4')
plt.scatter(np.random.randint(0,10,20),np.random.randint(0,10,20),s=100,color='#ff7f0e')
plt.scatter(np.random.randint(20,30,20),np.random.randint(10,30,20),s=100,color='#ff7f0e')
plt.axis('off')
plt.show()