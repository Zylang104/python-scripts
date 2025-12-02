# please be careful where you run this since you may not want to create a folder in some directories
import os
import time
os.mkdir("test")
time.sleep(10)
os.rmdir("test")