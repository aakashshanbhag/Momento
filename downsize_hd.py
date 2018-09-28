
from glob import glob
import os
import cv2

# path to the root folder for splitting into test and train folders
files = glob(r"C:\\Users\\ashanbhag\\Desktop\\Momento\\Chinmay\\2DP\\*.jpg")
files = files[:]


# output folder directories for test train and validation
filename_train = "C:\\Users\\ashanbhag\\Desktop\\Momento\\Chinmay\\cc\\"
count=0

# Split the data and store into specific folders specific to training, validation and test
for path2 in files:
    c1=os.path.split(path2)
    print(c1[1])
    img1=cv2.imread(path2)
    img1 = cv2.resize (img1, (1920, 1080), interpolation=cv2.INTER_CUBIC)
    cv2.imwrite(filename_train+c1[1],img1)
    count+=1
print("Done! "+str(count))









