import os
import sys
sys.path.append("D:/bigdata_github/Lipstick")
import getcolor
from os.path import join as pjoin
from scipy import misc
os.chdir("D:/bigdata_github/Lipstick")

def load_color(color_dir,list): 
    count = 0
    for dir in os.listdir(color_dir):  
        img_dir = pjoin(color_dir, dir)  
        image = getcolor.Image.open(img_dir)
        image = image.convert('RGB')
        get=getcolor.get_dominant_color(image)
        list.append(get)
        count = count+1
        #print(person_dir)
    #print(count)
    return count

def Mean_color(count,list):
     Mean_R=Mean_G=Mean_B=0
     for i in range(count):
        tuple=list[i]
        Mean_R+=tuple[0]
        Mean_G+=tuple[1]
        Mean_B+=tuple[2]
     MeanC=((int)(Mean_R/count),(int)(Mean_G/count),(int)(Mean_B/count))
     return MeanC

#if __name__ == '__main__':
#     result = load_color(('sample'),[])
#     MeanC = Mean_color(result[0],result[1])
#     print(MeanC)
