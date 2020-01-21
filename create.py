import numpy as np
from scipy import interpolate
import matplotlib.pyplot as plt
import DebugFunction as df

#interpld
def spline1(x,y,point):
    f = interpolate.interp1d(x, y,kind="quadratic") #kindの値は一次ならslinear、二次ならquadraticといった感じに
    X = np.linspace(x[0],x[-1],num=point,endpoint=True)
    Y = f(X)
    return X,Y

#Akima1DInterpolator
def spline2(x,y,point):
    f = interpolate.Akima1DInterpolator(x, y)
    X = np.linspace(x[0],x[-1],num=point,endpoint=True)
    Y = f(X)
    return X,Y

#splprep
def spline3(x,y,point,deg):
    tck,u = interpolate.splprep([x,y],k=deg,s=0) 
    u = np.linspace(0,1,num=point,endpoint=True) 
    spline = interpolate.splev(u,tck)
    return spline[0],spline[1]

def readfile(fpath):
    path = fpath

    with open(path) as fl:
        data = fl.readlines()
        data.append('end_of_file')
        curr_points = []
        num = []
        points = np.array([])
        for line in data:
            if 'Num of control' in line:
                curr_num_str = ''
                for i in range(4):
                    if line[i] == ' ':
                        break
                    else:
                        curr_num_str += line[i]
                curr_num = int(curr_num_str)
                num.append(curr_num)
                if not curr_points:
                    points = np.append(points, np.asarray(curr_points))
                    curr_points.clear()
            elif line == 'end_of_file':
                points = np.append(points, np.asarray(curr_points))
                curr_points.clear()
            else:
                curr_points.append(line)
        return num, points
        '''
        for curr_num in num:
            curr_all = points[:curr_num]
            points = points[:curr_num]
            curr_points = np.array([])
            for curr_data in curr_all:
                curr_points = np.append(curr_points, float(curr_data.split(' ')[0]))
                curr_points = np.append(curr_points, float(curr_data.split(' ')[1]))
                curr_points = np.append(curr_points, int(curr_data.split(' ')[2]))
            curr_points = curr_points.reshape([-1,3])
            fstart = curr_points[0,2]
            fend = curr_points[-1,2]
            all_frame = fend - fstart
            df.set_trace()
            print('test')
        '''
if __name__ == "__main__":
    num, points = readfile('/home/sakata/crowds_zara01.txt')
    wpath = '/home/sakata/true_zara01.txt'
    for curr_num in num:
        curr_all = points[:curr_num]
        points = points[curr_num:]
        curr_points = np.array([], dtype=int)
        for curr_data in curr_all:
            df.set_trace()
            curr_points = np.append(curr_points, np.round(float(curr_data.split(' ')[0])).astype('int64'))
            curr_points = np.append(curr_points, np.round(float(curr_data.split(' ')[1])).astype('int64'))
            curr_points = np.append(curr_points, np.round(float(curr_data.split(' ')[2])).astype('int64'))
        curr_points = curr_points.reshape([-1,3])
        fstart = curr_points[0,2]
        fend = curr_points[-1,2]
        all_frame = fend - fstart
        df.set_trace()
        print('test')

        #x座標に関して、重複、減少傾向を持つ座標群
        #x = [-5, -5, -3, 2, 3, 0, -2]
        #y = [6, 1, 6, 7, 1, -1, 0]

        #x方向に増加傾向である座標群
        #x = [-5, 0, 1,3,4,6]
        #y = [-4, 2, -2,-4,0,4]
        x = curr_points[:,0]
        y = curr_points[:,1]

        df.set_trace()

        #a1,b1 = spline1(x,y,all_frame) #interp1dメソッドを実行
        #a2,b2 = spline2(x,y,all_frame) #Akima1DInterpolatorメソッドを実行
        a3,b3 = spline3(x,y,all_frame,2) #splprepメソッドを実行

        df.set_trace()
        for cf, cx, cy in zip(range(fstart, fend, 1), x, y):
            with open(wpath, mode='a') as wtxt:
                df.set_trace()
                tf = str(cf)
                tx = str(cx)
                ty = str(cy)
                write_txt = tf + '\t' + tx + '\t' + ty + '\n'
                wtxt.write(write_txt)

        #グリッド線やラベルなどを付与しつつスプライン曲線をプロット
        plt.plot(x, y, 'ro',label="controlpoint")
        #plt.plot(a1,b1,label="interp1d")
        #plt.plot(a2,b2,label="Akima1DInterpolator")
        plt.plot(a3,b3,label="splprep")
        plt.title("spline")
        plt.xlim([-400, 400])
        plt.ylim([-400, 400])
        plt.legend(loc='lower right')
        plt.grid(which='major',color='black',linestyle='-')
        plt.grid(which='minor',color='black',linestyle='-')
        plt.xticks(list(filter(lambda x: x%1==0, np.arange(-10,10))))
        plt.yticks(list(filter(lambda x: x%1==0, np.arange(-10,10))))
        plt.show()
