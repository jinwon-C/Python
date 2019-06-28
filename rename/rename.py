import os
from os.path import join

#fpath = '\\Users\\Tony\\Desktop\\paper\\Data_file\\without_noise\\raw_data\\nothing' #폴더 이름
fpath = '\\Users\\Tony\\Desktop\\depth_classification\\low-high'
sorted_flist = sorted(os.listdir(fpath))
for i,file in enumerate(sorted_flist):
    print(file)
    #new_file = file.replace('note8_20K_','') #'기존 이름', '바꿀 이름'
    new_file = "low-high%d"%(i+1)+".wav"
    print(new_file)
    os.rename(join(fpath,file), join(fpath,new_file))