import time
time1 = time.time()

from PIL import Image,ImageFilter
import pytesseract as ocr 
import cv2 
import numpy as np 


###########二元化
def binarizing(img,threshold):
    pixdata = img.load()
    w, h = img.size
    for y in range(h):
        for x in range(w):
            if pixdata[x, y] < threshold:
                pixdata[x, y] = 0
            else:
                pixdata[x, y] = 255
    return img

###########去除干擾線
# def depoint(img):   #input: gray image
#     pixdata = img.load()
#     w,h = img.size
#     for y in range(1,h-1):
#         for x in range(1,w-1):
#             count = 0
#             if pixdata[x,y-1] > 245:
#                 count = count + 1
#             if pixdata[x,y+1] > 245:
#                 count = count + 1
#             if pixdata[x-1,y] > 245:
#                 count = count + 1
#             if pixdata[x+1,y] > 245:
#                 count = count + 1
#             if count > 2:
#                 pixdata[x,y] = 255
#     return img

########識別全部
def all_OCR(pic_path):
    #####截圖
    img1=Image.open(pic_path)
    w,h=img1.size
    ##圖片放大3倍
    out=img1.resize((w*3,h*3),Image.ANTIALIAS)

    # 轉成灰階圖
    img= out.convert('L')
    # 模糊
    blurred_image = img.filter(ImageFilter.BLUR)
    # 轉成binary圖片
    img1=binarizing(blurred_image,100)
    #img2=depoint(img1)
    img1.show()
    code = ocr.image_to_string(img1,lang="eng")
    return code.split('\n')
    # print(code.split('\n'))

if __name__ == '__main__':
    ident_list = []
    for i in range(1,12):
        pic_path="./images/"+str(i)+".gif"
        ident_list.append(all_OCR(pic_path))
    time2 = time.time()
    print("結果",ident_list)
    print ('總共耗時：' + str(time2 - time1) + 's')