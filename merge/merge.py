import os
import pandas as pd
#fpath = 'C:\\Users\\Tony\\Desktop\\git\\Data\\2019-08-16\\Dual\\1'
for i in range(0,50):
    with open('C:\\Users\\Tony\\Desktop\\git\\Data\\2019-08-16\\Dual\\acc_pasted\\1\\1_%d'%(i+1)+'.csv', 'r') as f1:
        with open('C:\\Users\\Tony\\Desktop\\git\\Data\\2019-08-16\\Audio\\csv\\win15000\\freq6\\1.csv','r') as f2:
            a_list = pd.read_csv(f1, header=None)
            b_list = pd.read_csv(f2, header=None)
            add_col = b_list[i:i+1].T
            merge = pd.DataFrame()
            merge[5] = add_col[i]
            merge[0] = a_list[0]
            merge[1] = a_list[1]
            merge[2] = a_list[2]
            merge[3] = a_list[3]
            merge[4] = a_list[4]
            merge = pd.DataFrame(merge, columns=[0,1,2,3,4,5])
            print(merge[:])

            #merge.to_csv('C:\\Users\\Tony\\Desktop\\git\\Data\\2019-08-16\\Dual\\csv\\a\\a_%d'%(i+1)+'.csv', header=None, index=False)
