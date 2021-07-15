# pip install psutil
import psutil
import pync
import os 

battery = psutil.sensors_battery()
plugged = battery.power_plugged
percent = battery.percent

sym = '%'
if percent <= 30:
    pync.notify(f"{percent} {sym} Battery remain! Charge your computer.", title="Battery", group=os.getpid(), execute='say "Carrega primo"')   
else:
    pync.notify(f"{percent} {sym} Battery remain. Calm down bro :)", title="Battery", group=os.getpid()) 