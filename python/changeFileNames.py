


import os
import glob

path2imgs="./datasets/abstract/"
glob_pattern = os.path.join(path2imgs, '*.jpg')
image_filenames = sorted(glob.glob(glob_pattern))
for i,imp in enumerate(image_filenames):
    print(i,imp)
    bn=os.path.basename(imp)
    istr=str(i+1).rjust(5,"0")+".jpg"
    impNew=imp.replace(bn,istr)
    print(impNew)
    os.rename(imp, impNew)
    
    


    