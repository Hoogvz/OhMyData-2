

import datetime
import time
import random
import requests

i=0
while i < 10 :     

      url = "http://localhost:7896/iot/d?i="
      idays = 30
      while idays >=1:
           date=datetime.datetime.now() + datetime.timedelta(days=idays*-1)
           ahora = date.strftime("%Y-%m-%dT%H:%M:%SZ")
           
           llenado_1 = random.uniform(0, 100)
           bateria_1 = random.uniform(0, 100)
           temperatura_1 = random.uniform(0, 50)
           zona =["Paris"]
           for location in zona:
                zona_1 = location

   
           llenado_2 = random.uniform(0, 100)
           bateria_2 = random.uniform(0, 100)
           temperatura_2 = random.uniform(0, 50)
           zona =["Frankfurt"]
           for location in zona:
               zona_2 = location

           llenado_3 = random.uniform(0, 100)
           bateria_3 = random.uniform(0, 100)
           temperatura_3 = random.uniform(0, 50)
           zona =["Bordeaux"]
           for location in zona:
               zona_3 = location

           llenado_4 = random.uniform(0, 100)
           bateria_4 = random.uniform(0, 100)
           temperatura_4 = random.uniform(0, 50)
           zona =["London"]
           for location in zona:
               zona_4 = location

           llenado_5 = random.uniform(0, 100)
           bateria_5 = random.uniform(0, 100)
           temperatura_5 = random.uniform(0, 50)
           zona =["Vienna"]
           for location in zona:
               zona_5 = location

           devicename1 ="residuos01"  
           devicename2 ="residuos02"
           devicename3 ="residuos03"
           devicename4 ="residuos04"
           devicename5 ="residuos05"

           endpoint1 = url+devicename1+"&k=4jggokgpepnvsb2uv4s40d5911"
           payload1 = "n|"+devicename1+"|l|"+str("{0:.2f}".format(llenado_1))+"|b|"+str("{0:.2f}".format(bateria_1))+"|t|"+str("{0:.2f}".format(temperatura_1))+"|z|"+ zona_1 +"|d|"+str(ahora)
    
           endpoint2 = url+devicename2+"&k=4jggokgpepnvsb2uv4s40d5911"
           payload2 = "n|"+devicename2+"|l|"+str("{0:.2f}".format(llenado_2))+"|b|"+str("{0:.2f}".format(bateria_2))+"|t|"+str("{0:.2f}".format(temperatura_2))+"|z|"+zona_2 +"|d|"+str(ahora)

           endpoint3 = url+devicename3+"&k=4jggokgpepnvsb2uv4s40d5911"
           payload3 = "n|"+devicename3+"|l|"+str("{0:.2f}".format(llenado_3))+"|b|"+str("{0:.2f}".format(bateria_3))+"|t|"+str("{0:.2f}".format(temperatura_3))+"|z|"+zona_3+"|d|"+str(ahora)

           endpoint4 = url+devicename4+"&k=4jggokgpepnvsb2uv4s40d5911"
           payload4 ="n|"+devicename4+ "|l|"+str("{0:.2f}".format(llenado_4))+"|b|"+str("{0:.2f}".format(bateria_4))+"|t|"+str("{0:.2f}".format(temperatura_4))+"|z|"+zona_4+"|d|"+str(ahora)

           endpoint5 = url+devicename5+"&k=4jggokgpepnvsb2uv4s40d5911"
           payload5 = "n|"+devicename5+"|l|"+str("{0:.2f}".format(llenado_5))+"|b|"+str("{0:.2f}".format(bateria_5))+"|t|"+str("{0:.2f}".format(temperatura_5))+"|z|"+zona_5+"|d|"+str(ahora)

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
           idays-=1
      i+=1
