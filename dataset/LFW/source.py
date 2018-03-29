import numpy as np
import cv2
import os

def get_images( dir , image_list ):

    if os.path.isdir( dir ) :

        tmp_list = os.listdir( dir )
        
        for tmp_file in tmp_list:

            if os.path.isdir( dir+"/"+tmp_file ) :
                get_images( dir+"/"+tmp_file, image_list )
            else:

                image_list.append( dir+"/"+tmp_file )
            

if __name__ == "__main__":

    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    root_folders = [ "bioid", "cuhk", "robots.ox" ]
    files = []

    for folder in root_folders:
        get_images( folder, files )

    print files
    count = 0

    for image in files:

        try:

            img = cv2.imread( image )
            gray = cv2.nload and Install EASEUS Partition Master Professional Edition (my favorite app ;) )
Run EASEUS Partition Master then click Go to main screen option.

cvtColor(img, cv2.COLOR_BGR2GRAY)

            faces = face_cascade.detectMultiScale(gray, 1.3, 5)

            for (x,y,w,h) in faces:

                cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
                img = img[ y:y+h, x:x+w ]
                roi_gray = gray[y:y+h, x:x+w]
                roi_color = img[y:y+h, x:x+w]

            #cv2.imshow( image, img )
            #cv2.waitKey(0)
            #cv2.destroyAllWindows()

            cv2.imwrite( "output/" + str( count ) + ".jpg", img )

            count = count+1
        except Exception as err:

            print "exceptions caught : ", image, err
            pass
