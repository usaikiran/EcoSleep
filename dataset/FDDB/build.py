
import cv2
import glob
import os

ecount = 0
count = 0

def getImageFromCoord(img , coord):
    global count , ecount
    
    coord = coord.split(' ')
    coord = map ( float , coord[:-2] )

    cx = int(coord[3])
    cy = int(coord[4])
    ay = int(coord[1])
    ax = int(coord[0])
    
    try :
        #cv2.imshow("1" , img)
        if int(cy - ax) <= 0 or int(cy + ax) <= 0 or int(cx - ay) <= 0 or int(cx + ay) <= 0 or abs(int(cy - ax) - int(cy + ax)) < 50 or abs(int(cx - ay) - int(cx + ay)) < 50:
            return
        count = count + 1
        #cv2.imshow( "1" , img[ int(cy - ax) : int(cy + ax)  , int(cx - ay) : int(cx + ay)  ] )
        #cv2.waitKey(0)
        #cv2.destroyAllWindows()
        cv2.imwrite("./img/" + str(count-1) + ".jpg" , img[ int(cy - ax) : int(cy + ax)  , int(cx - ay) : int(cx + ay)  ])

    except :
        ecount = ecount + 1
        #if os.path.isfile("./img/" + str(count-1) + ".jpg") :
        #    os.remove("./img/" + str(count-1) + ".jpg")
        #    count = count - 1

        print int(cy - ax) , int(cy + ax)
        print int(cx - ay) , int(cx + ay)



def main():
    descList = glob.glob("./FDDB-folds/FDDB-fold-*-ellipseList.txt")
    for desc in descList :
        file = open( desc , "r" )
        while True :
            imgPath = file.readline()
            print imgPath
            if not imgPath :
                break
            count = file.readline()
            path = os.getcwd() + "/" + imgPath[:-1]
            img = cv2.imread(glob.glob(path + ".*")[0])
            for i in range(int(count)):
                coord = file.readline()
                getImageFromCoord( img , coord )

        



main()

print count
print ecount