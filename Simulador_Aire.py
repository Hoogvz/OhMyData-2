

import datetime
import time
import random
import requests

i=0
#idays= 30
while i < 20 :  
           

           url = "http://localhost:7896/iot/d?i="


           date=datetime.datetime.now() 
           ahora = date.strftime("%Y-%m-%dT%H:%M:%SZ")
           
           NO2_1 = random.uniform(50, 300)
           SO2_1 = random.uniform(190, 420)
           CO_1 = random.uniform(0, 20)
           O3_1 = random.uniform(120, 300)
           H2S_1 = random.uniform(120, 300)
           DB_1 = random.randint(0, 130) 

           NO2_2 = random.uniform(50, 300)
           SO2_2 = random.uniform(190, 420)
           CO_2 = random.uniform(0, 20)
           O3_2 = random.uniform(120, 300)
           H2S_2 = random.uniform(120, 300)
           DB_2 = random.randint(0, 130) 

           NO2_3 = random.uniform(50, 300)
           SO2_3 = random.uniform(190, 420)
           CO_3 = random.uniform(0, 20)
           O3_3 = random.uniform(120, 300)
           H2S_3 = random.uniform(120, 300)
           DB_3 = random.randint(0, 130) 

           NO2_4 = random.uniform(50, 300)
           SO2_4 = random.uniform(190, 420)
           CO_4 = random.uniform(0, 20)
           O3_4 = random.uniform(120, 300)
           H2S_4 = random.uniform(120, 300)
           DB_4 = random.randint(0, 130) 

           NO2_5 = random.uniform(50, 300)
           SO2_5 = random.uniform(190, 420)
           CO_5 = random.uniform(0, 20)
           O3_5 = random.uniform(120, 300)
           H2S_5 = random.uniform(120, 300)
           DB_5 = random.randint(0, 130) 

           devicename1 ="calidad01"  
           devicename2 ="calidad02"
           devicename3 ="calidad03"
           devicename4 ="calidad04"
           devicename5 ="calidad05"

           endpoint1 = url+devicename1+"&k=4jggokgpepnvsb2uv4s40d5911"
           payload1 = "n|"+devicename1+"|no2|"+str("{0:.2f}".format(NO2_1))+"|so2|"+str("{0:.2f}".format(SO2_1))+"|co|"+str("{0:.2f}".format(CO_1))+"|o3|"+str("{0:.2f}".format(O3_1))+"|h2s|"+str("{0:.2f}".format(H2S_1))+"|DB|"+str("{0:.2f}".format(DB_1))+"|d|"+str(ahora)
    
           endpoint2 = url+devicename2+"&k=4jggokgpepnvsb2uv4s40d5911"
           payload2 = "n|"+devicename2+"|no2|"+str("{0:.2f}".format(NO2_2))+"|so2|"+str("{0:.2f}".format(SO2_2))+"|co|"+str("{0:.2f}".format(CO_2))+"|o3|"+str("{0:.2f}".format(O3_2))+"|h2s|"+str("{0:.2f}".format(H2S_2))+"|db|"+str("{0:.2f}".format(DB_2))+"|d|"+str(ahora)

           endpoint3 = url+devicename3+"&k=4jggokgpepnvsb2uv4s40d5911"
           payload3 = "n|"+devicename3+"|no2|"+str("{0:.2f}".format(NO2_3))+"|so2|"+str("{0:.2f}".format(SO2_3))+"|co|"+str("{0:.2f}".format(CO_3))+"|o3|"+str("{0:.2f}".format(O3_3))+"|h2s|"+str("{0:.2f}".format(H2S_3))+"|db|"+str("{0:.2f}".format(DB_3))+"|d|"+str(ahora)

           endpoint4 = url+devicename4+"&k=4jggokgpepnvsb2uv4s40d5911"
           payload4 = "n|"+devicename4+"|no2|"+str("{0:.2f}".format(NO2_4))+"|so2|"+str("{0:.2f}".format(SO2_4))+"|co|"+str("{0:.2f}".format(CO_4))+"|o3|"+str("{0:.2f}".format(O3_4))+"|h2s|"+str("{0:.2f}".format(H2S_4))+"|db|"+str("{0:.2f}".format(DB_4))+"|d|"+str(ahora)

           endpoint5 = url+devicename5+"&k=4jggokgpepnvsb2uv4s40d5911"
           payload5 = "n|"+devicename5+"|no2|"+str("{0:.2f}".format(NO2_5))+"|so2|"+str("{0:.2f}".format(SO2_5))+"|co|"+str("{0:.2f}".format(CO_5))+"|o3|"+str("{0:.2f}".format(O3_5))+"|h2s|"+str("{0:.2f}".format(H2S_5))+"|db|"+str("{0:.2f}".format(DB_5))+"|d|"+str(ahora)

           header = {"ContentType":"text/plain"} 


           r1 = requests.post(url= endpoint1,headers=header, data=payload1)
           print("datos sensor {} {}".format(devicename1,payload1))
           time.sleep(0.5)
           r2 = requests.post(url= endpoint2,headers=header, data=payload2)
           print("datos sensor {} {}".format(devicename2,payload2))
           time.sleep(0.5)
           r3 = requests.post(url= endpoint3,headers=header, data=payload3)
           print("datos sensor {} {}".format(devicename3,payload3))
           time.sleep(0.5)
           r4 = requests.post(url= endpoint4,headers=header, data=payload4)
           print("datos sensor {} {}".format(devicename4,payload4))
           time.sleep(0.5)
           r5 = requests.post(url= endpoint5,headers=header, data=payload5)
           print("datos sensor {} {}".format(devicename5,payload5))
           time.sleep(0.5)

           i+=1

