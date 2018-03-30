
import os
from shutil import copyfile

root_dir = "/media/test/WorkSpace/Codes/PROJECT_ES/project_es/dataset/"
out_path = "/media/test/WorkSpace/Codes/PROJECT_ES/ESD/img/"
count = 0
files = []

for dr in os.listdir( root_dir ):

    path = root_dir+dr+"/img/"
    images = os.listdir( path )

    for img in images:

        os.system( " cp "+path+img + " " + out_path+str( count )+".jpg" )
        count += 1
    
    print path+" \t COMPLETED"