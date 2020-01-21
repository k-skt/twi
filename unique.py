import torch
import numpy as np
import DebugFunction as df
from scipy.optimize import linear_sum_assignment

def read_file(_path, delim='\t'):
    data = []
    if delim == 'tab':
        delim = '\t'
    elif delim == 'space':
        delim = ' '
    with open(_path, 'r') as f:
        for line in f:
            line = line.strip().split(delim)
            line = [float(i) for i in line]
            data.append(line)
    return np.asarray(data)

if __name__ == '__main__':
    #_path = ''
    #data = read_file(gt_path, delim='\t')
    data = np.array([[10.0, 1.0, 2.0, 2.0], [20.0, 1.0, 2.1, 2.1], [20.0, 1.0, 100.0, 100.0], [30.0, 1.0, 2.1, 2.1], [30.0, 1.0, 100.0, 100.0]])
    unique_ped_id = np.unique(data[:, 1]).tolist()
    new_d = []
    for ped in unique_ped_id:
        curr_data = data[data[:,1]==ped,:]
        udata, counts = np.unique(curr_data[:,0], return_counts=True)
        if len(udata) == len(curr_data):
            continue
        reduce_d, reduce_d_ = [], []
        unique_d, unique_d_ = [], []
        for idx in udata[counts!=1]:
            reduce_d_.append(curr_data[curr_data[:,0]==idx, :])
        #reduce_d = curr_data[curr_data[:,0]==counts != 1, :]
        reduce_d = np.asarray(reduce_d_).reshape(-1,4)
        for idx in udata[counts==1]:
            unique_d_.append(curr_data[curr_data[:,0]==idx, :])
        #reduce_d = curr_data[curr_data[:,0]==counts != 1, :]
        unique_d = np.asarray(unique_d_).reshape(-1,4)
        #unique_d = curr_data[counts == 1, :]
        if len(reduce_d) > 0:
            for r_d in reduce_d_:
                if len(curr_data[curr_data[:,0]==r_d[0][0]-10.0]) == 1:
                    bf_data = curr_data[curr_data[:,0]==r_d[0][0]-10.0,:].copy()
                    df.set_trace()
                    reduces_data = curr_data[curr_data[:,0]==r_d-10.0,:].copy()
                    diffs = [np.linalg.norm(xx) for xx in reduces_data[:,2:4]-bf_data[2:4]]
                    min_idx = np.argmin(diffs)
