import torch
import numpy as np
import DebugFunction as df
from scipy.optimize import linear_sum_assignment

def evaluate_helper(gt_list, pred_list):
    sum_ = 0
    error_ = []
    num = len(gt_list)
    for i in range(num):
        pred_list - gt_list[i]
    #検出できたものベースで制度をだす
    for curr_gt in gt_list:
        error_.append(np.sum(pred_list - curr_gt, axis=1))
    #エラーから最小の組み合わせを見つける
    error = np.array(error_)
    mat = []
    for idx in range(len(error)):
        error[idx] = np.sqrt(error[idx]**2)
    #_error = torch.sqrt(error**2)
    row_ind, col_ind = linear_sum_assignment(error)
    #loss_ += _error**2
    #sum_ = torch.sqrt(loss_)
    '''
    error = torch.stack(error, dim=1)
    for (start, end) in seq_start_end:
        start = start.item()
        end = end.item()
        _error = error[start:end]
        _error = torch.sum(_error, dim=0)
        _error = torch.min(_error)
        sum_ += _error
    '''
    df.set_trace()
    return col_ind

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
    gt_path = ''
    pred_list = ''
    gt_data = read_file(gt_path, delim='\t')
    pred_data = read_file(pred_path, delim='\t')
    unique_frames = np.unique(pred_data[:, 0]).tolist()
    gt_list = np.array([[3.0, 5.0], [5.0, 7.0], [7.0, 9.0]])
    pred_list = np.array([[3.0, 5.0], [7.0, 9.0]])
    evaluate_helper(gt_list, pred_list)
