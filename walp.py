import datetime
import time
import os

def todayAt(hr, min, sec=0, micros=0):
    now = datetime.datetime.now()
    return(now.replace(hour=hr, minute=min, second=sec, microsecond=micros))

def timeNow():
    now = datetime.datetime.now()
    return(now.replace(second=0, microsecond=0))

# The time requires to be set without the leading zero, for example 06:09 AM should be todayAt(6, 9)

data = [
["deepnight", lambda: todayAt(1, 41), lambda: todayAt(5, 10), "/home/ari/Images/Wallpapers/energy-aurora.jpg"],
["dawn" , lambda: todayAt(5, 11), lambda: todayAt(5, 59), "/home/ari/Images/Wallpapers/river-china-landscape.jpg"],
["earlymorning", lambda: todayAt(6, 0), lambda: todayAt(7, 12), "/home/ari/Images/Wallpapers/altai-mountains-lake-scenic-reflection-clouds-dark-gloomy-fog.jpeg"],
["morning", lambda: todayAt(7, 13), lambda: todayAt(8, 42), "/home/ari/Images/Wallpapers/altai-republic.jpg"],
["middlemorning", lambda: todayAt(8, 43), lambda: todayAt(10, 7), "/home/ari/Images/Wallpapers/justrees.jpg"],
["latemorning", lambda: todayAt(10, 8), lambda: todayAt(10, 35), "/home/ari/Images/Wallpapers/cool-sunny-ice-antartica.jpg"],
["latermorning", lambda: todayAt(10, 36), lambda: todayAt(11, 27), "/home/ari/Images/Wallpapers/russia-summer-paysage.jpg"],
["noon", lambda: todayAt(11, 28), lambda: todayAt(13, 39), "/home/ari/Images/Wallpapers/birch-trail.jpg"],
["latenoon", lambda: todayAt(13, 40), lambda: todayAt(14, 17), "/home/ari/Images/Wallpapers/altai-mountains-valley-hills-river-landscape-19372.jpg"],
["afternoon", lambda: todayAt(14, 18), lambda: todayAt(15, 10), "/home/ari/Images/Wallpapers/mountain-full-of-pines.jpg"],
["earlyevening", lambda: todayAt(15, 11), lambda: todayAt(17, 0), "/home/ari/Images/Wallpapers/spring-in-antarctica.jpg"],
["evening", lambda: todayAt(17, 1), lambda: todayAt(17, 25), "/home/ari/Images/Wallpapers/a-la-moon-base.jpg"],
["lateevening", lambda: todayAt(17, 26), lambda: todayAt(19, 15), "/home/ari/Images/Wallpapers/mountain-aurora.jpg"],
["dusk", lambda: todayAt(19, 16), lambda: todayAt(20, 55), "/home/ari/Images/Wallpapers/sunsethorizon.jpg"],
["night", lambda: todayAt(20, 56), lambda: todayAt(21, 58), "/home/ari/Images/Wallpapers/iss-aurora.jpg"],
["latenight_with_midnight_quick_fix", lambda: todayAt(21, 59), lambda: todayAt(23, 59, 59), "/home/ari/Images/Wallpapers/late-night-aurora.jpg"],
["latenight_with_midnight_quick_fix", lambda: todayAt(0, 0), lambda: todayAt(1, 41, 59), "/home/ari/Images/Wallpapers/late-night-aurora.jpg"]
]

now = timeNow()
for item in data:
    if item[1]() < now < item[2]():
        os.system("xwallpaper --zoom " + item[3])
        print("Success")
        print(item[3])
        continue
    else:
        continue

while True:
    now = timeNow()
    time.sleep(15)
    for item in data:
        if item[1]() < now < item[2]():
            os.system("xwallpaper --zoom " + item[3])
            print("Success")
            print(item[3])
            continue
        else:
            continue
