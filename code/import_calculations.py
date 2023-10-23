import numpy as np
import obspy
from obspy.taup import TauPyModel
import matplotlib
matplotlib.use('TkAgg')  # Use the TkAgg backend
import matplotlib.pyplot as plt
from obspy.taup.slowness_model import SlownessModel
from obspy.taup.tau_model import TauModel
from obspy.taup.velocity_model import VelocityModel
from obspy.taup.taup_create import build_taup_model

##Import PREM model for arrival times calculations

model_prem = TauPyModel(model="prem")

arrivals = model_prem.get_travel_times(source_depth_in_km=105,
                                  distance_in_degree=107)
arrivals=model_prem.get_ray_paths(source_depth_in_km=500,
                               distance_in_degree=130,
                               phase_list=["Pdiff", "Sdiff",
                                           "pPdiff", "sSdiff"])
#ax = arrivals.plot_rays()

import pandas as pd
#build new model based on Mars predicted seismic data

#rearrange data set
file_path='DWAK.csv'
df = pd.read_csv (file_path,header=None)
df = df.drop(df.columns[[4, 5, 6,7,8,9]], axis=1)

if 1 in df.columns:
    col0 = df.pop(1)
    df.insert(len(df.columns), '0', col0)
else:
    # Handle the case when the column doesn't exist
    # You can raise an error, display a message, or perform other actions.
    print("Column '1' does not exist in the DataFrame.")
print(df)
######save modified file as nd

file_path_in_nd='DWAK.nd'
#file structure of DWAK.nd : NAME DWAK - COLUMNS radius rho vpv vsv qka qmu vsh vph eta
model_DWAK=build_taup_model(file_path_in_nd, output_folder=None, verbose=True)

print(model_DWAK)