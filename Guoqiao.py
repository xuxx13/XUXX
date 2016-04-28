#coding=utf-8
#!/usr/bin/env python

import threading  
import time  

north = threading.Condition()
south = threading.Condition()
road = threading.Condition()
people = 2  

class North(threading.Thread):  
    def __init__(self):  
        threading.Thread.__init__(self)  

    def run(self):  
        global north, people, road  
        while True:  
            if road.acquire():
                if north.acquire():
                    if people < 2:  
                        people += 1;  
                        print "Nouth(%s):p one, now %s people." %(self.name, people)  
                        north.notify()  
                        road.notify()  
                    else:
                        print "Nouth(%s):already 2, stop pass, now %s people." %(self.name, people)  
                        north.wait()  
                        road.wait()  
                    north.release()  
                road.release()  

class South(threading.Thread):  
    def __init__(self):  
        threading.Thread.__init__(self)  

    def run(self):  
        global south, people, road  
        while True:  
            if road.acquire():
                if south.acquire():  
                    if people >= 1:  
                        people -= 1  
                        print "sorth(%s): pass one  now %s people." %(self.name, people)  
                        south.notify()  
                        road.notify()  
                    else:  
                        print "sorth(%s):  no one , stop consume now %s people." %(self.name, people)  
                        south.wait()  
                        road.wait() 
                    south.release()  
                road.release()

if __name__ == "__main__":  
    for p in range(0, 4):  
        p = South()  
        p.start()  

    for c in range(0, 4):  
        c = North()  
        c.start() 
