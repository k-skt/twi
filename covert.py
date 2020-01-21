import DebugFunction as df
import numpy as np

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
    path = '/home/sakata/testtxt.txt'
    data = read_file(path, delim='\t')
    peds = np.unique(data[:, 1]).tolist()
    ped_id = 1.0
    for curr_ped in peds:
        with open('ped_id.txt',mode='w') as f:
            f.write(str(ped_id))
        #現在の人が出る最初のフレーム
        tmp = np.argwhere(data[:,1]==curr_ped)
        sframe = int(float(data[tmp[0], 0]))
        eframe = int(float(data[tmp[-1], 0]))
        next_frame = sframe+16
        #idx_data = data[sframe:last_frame, 1] == curr_ped
        #idx = data.index(idx_data)
        data[np.where((data[:,0]>=sframe) & (data[:,0]<sframe+16.0) & (data[:,1]==curr_ped))[0],1] = ped_id
        
        #data[[[, 1] == curr_ped], 1] = ped_id
        ped_id += 1.0
        for cframe in range(next_frame, eframe, 8):
            data[np.where((data[:,0]>=cframe) & (data[:,0]<cframe+8.0) & (data[:,1]==curr_ped))[0],1] = ped_id
            #data[[cframe:cframe+8.0, 1] == curr_ped, 1] = ped_id
            ped_id += 1.0
        with open('ped_id.txt', mode='w') as f:
            f.write(',' + str(ped_id) + '\n')
        ped_id += 1.0
    wdata = []

    for line in data:
        line = [str(i) for i in line]
        wdata.append(line)

    df.set_trace()

    wdata[:, 0] += '\t'
    wdata[:, 1] += '\t'
    wdata[:, 2] += '\t'
    wdata[:, 3] += '\n'

    with open(path_w, mode='w') as f:
        for curr_data in wdata:
            f.write(curr_data)

