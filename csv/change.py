import os
import pandas as pd
fpath = 'C:\\Users\\Tony\\Desktop\\git\\Data\\2019-08-16\\Audio\\Numeric\\1'
sorted_flist = sorted(os.listdir(fpath))
for i, file in enumerate(sorted_flist):
    with open('C:\\Users\\Tony\\Desktop\\git\\Data\\2019-08-16\\Audio\\1\\1_%d'%(i+1)+'.csv', 'r') as f:
        a_list = pd.read_csv(f, header=None)
        a_list.loc[:,0] = 10
        print(file)
        print(a_list.loc[:,0])

        #a_list.to_csv('C:\\Users\\Tony\\Desktop\\git\\Data\\2019-08-16\\Audio\\1\\1_%d'%(i+1)+'.csv', header=None, index=False)