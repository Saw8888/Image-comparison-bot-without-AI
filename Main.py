import cv2

lib = 'Map1.png'
lib2 = 'Map2.png'
lib3 = []

Read = list(cv2.imread(lib).astype("int"))
Read2 = list(cv2.imread(lib2).astype("int"))

counter = 0

for i in range(len(Read)):#y coords
    for j in range(len(Read[i])):#x coords
        blue = list(Read[i][j])[0]
        green = list(Read[i][j])[1]
        red = list(Read[i][j])[2]
        blue2 = list(Read2[i][j])[0]
        green2 = list(Read2[i][j])[1]
        red2 = list(Read2[i][j])[2]
        difference = (blue+green+red)-(blue2+green2+red2)
        lib3.append(difference)
        if difference <= 10 and difference >= -10:
            counter+=1
            print(counter)

if counter >= (i*j)*0.75:
    print('They are similar images')
    print('They are different by:', str((counter / (i * j)) * 100), '%')
else:
    print('They are different')
    print('They are different by:', str((counter / (i * j)) * 100), '%')


