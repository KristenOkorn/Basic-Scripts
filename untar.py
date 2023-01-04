

import tarfile
import os
path = 'C:\\Users\\kokorn\\Documents\\LA Deployment\\AVIRIS'
filename = 'ang20161006t195245.tar.gz'
filepath = os.path.join(path, filename)
my_tar1 = tarfile.open(filepath)
my_tar1.extractall(path) # specify which folder to extract to
my_tar1.close()
