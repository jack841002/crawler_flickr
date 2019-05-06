#%%
import requests
import numpy as np  
from bs4 import BeautifulSoup
import re #抓圖片
from urllib.request import urlretrieve #存照片
import os #為了建立資料夾
import sys #控制抓取文章頁數 system的縮寫

with open('train_img.txt','r') as fp:
    img = fp.read().splitlines()

errf = open("error_img.txt", "a")

error=[] #len(img)
for i in range(len(img)):
    print("process {} urls ".format(i+1))
    # errf.writelines(str(i)+'\n')
    url = img[i]
    try:
        res = requests.get(url)
        soup = BeautifulSoup(res.text,"html.parser")
        if soup.find('div').find('img') != None:
            image = soup.find('div').find('img')['src']
            f = image.split('/')[-1]
            f = f.split('_')[0]
            local = os.path.abspath('./image/{}.jpg'.format(f))
            try:
                urlretrieve(image,local) #link是下載的網址 local是儲存圖片的檔案位址
            except Exception as e:
                print(url)
                errf.writelines(str(url) + "\n")                
                error.append(url)
                print(e)
        else:
            print(url)
            errf.writelines(str(url) + "\n")
            error.append(url)
    except Exception as e:
        print(url)
        errf.writelines(str(url) + "\n")
        error.append(url)
#%%