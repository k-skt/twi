import numpy as np
import DebugFunction as df

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
    path = '/home/sakata/sgan/datasets/eth/test/test.txt'
    wpath = '/home/sakata/sgan/datasets/eth/sort.txt'
    delim='\t'
    data = read_file(path, delim)
    data = sorted(data, key=lambda x:(x[0], x[1]))
    for curr_data in data:
        frame_txt = str(curr_data[0])
        ped_txt = str(curr_data[1])
        x_txt = str(curr_data[2])
        y_txt = str(curr_data[3])
        with open(wpath, mode='a') as sgantxt:
            sgan_write_txt = str(frame_txt) + '\t' + str(ped_txt) + '\t' + str(x_txt) + '\t' + str(y_txt) + '\n'
            sgantxt.write(sgan_write_txt)
    print(data)
