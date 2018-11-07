import numpy as np
import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt
import os
import holoviews as hv
hv.notebook_extension('matplotlib')

dirList = os.listdir("dataFiles_few/")
a = len(dirList)

