import pandas as pd
import numpy as np
import os


def compute_energy_per_prompt(path_to_csv):
    # csv is extracted with 'watch -n 0.1 "rocm-smi -P --csv >> gpu_data.csv'
    data = pd.read_csv(path_to_csv,names=['col1','col2'])
    data = data[data['col1']!='device']
    data.dropna()
    data_gpu1 = data[data['col1']=='card0']
    data_gpu2 = data[data['col1']=='card1']
    data_gpu1['col2'] = data_gpu1['col2'].astype(float)
    data_gpu2['col2'] = data_gpu2['col2'].astype(float)

    data_prompt_gpu1 = data_gpu1.iloc[np.where(np.diff(data_gpu1.col2) != 0)[0]]
    data_prompt_gpu2 = data_gpu2.iloc[np.where(np.diff(data_gpu2.col2) != 0)[0]]
    
    energy_gpu1 = np.sum(data_prompt_gpu1.col2 * 0.1) # [W*s] = [J]
    energy_gpu1_uJ = energy_gpu1 * 10**6
    energy_gpu1_kWh = energy_gpu1_uJ * 2.77777778 * 10**(-13)

    energy_gpu2 = np.sum(data_prompt_gpu2.col2 * 0.1) # [W*s] = [J]
    energy_gpu2_uJ = energy_gpu2 * 10**6
    energy_gpu2_kWh = energy_gpu2_uJ * 2.77777778 * 10**(-13)

    os.remove(path_to_csv) #remove bcs next measurements append to existing file otherwise

    return energy_gpu1_kWh, energy_gpu2_kWh