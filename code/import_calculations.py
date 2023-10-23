import numpy as np
import obspy
from obspy.taup import TauPyModel
import matplotlib as plt
from obspy.taup import taup_create


model = TauPyModel(model="prem")

arrivals = model.get_travel_times(source_depth_in_km=55,
                                  distance_in_degree=67)


import pandas as pd

# Replace 'DWAK.bm' with the actual path to your .bm file
file_path = 'DWAK.csv'

# Read the .bm file into a DataFrame
df = pd.read_csv(file_path,header=None)
nd_model=df.values



# Call the build_taup_model method
DWAK = taup_create.build_taup_model(nd_model)
