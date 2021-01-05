import os
import subprocess 
import time
     
result = "Some String"
while True: 
     result = subprocess.call(
               'echo pass | sudo hwclock -r', shell=True)
     print(result)
     
     time.sleep(1)
     
 
 


