import webbrowser
import time

total_breaks = 3;
breaks_count = 0;

print ('Program started running on' + time.ctime())
while breaks_count < total_breaks:
    breaks_count = breaks_count +1
    webbrowser.open_new("https://youtu.be/x2rQzv8OWEY")
    time.sleep (10)
else:
    print 'Program ended'
