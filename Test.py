from Energenie import *
import time

energenie = Energenie()

energenie.gpiosetup()
energenie.gpioon()
time.sleep(5)
energenie.gpiooff()
energenie.gpiocleanup()
