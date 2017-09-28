#!/usr/bin/env python

import rospy
import time, os
from cob_perception_msgs.msg import DetectionArray

timer = time.time()
alexTimer = time.time()-7
thomasTimer = time.time()-7
theoTimer = time.time()-7
chrisPTimer = time.time()-7
chrisATimer = time.time()-7
nasiaTimer = time.time()-7
nikosTimer = time.time()-7
primeMinisterTimer = time.time()-7
cdname = None
listings = []


def shoutAlexander(label):
    global cdname, alexTimer
    if cdname == label and time.time()-alexTimer > 10:
        os.system('rosrun sound_play play.py ~/catkin_ws/src/face_to_speech/sounds/alexander.wav')
        cdname = label
        alexTimer = time.time()
    elif cdname != label:
        os.system('rosrun sound_play play.py ~/catkin_ws/src/face_to_speech/sounds/alexander.wav')
        cdname = label
        alexTimer = time.time()

def shoutThomas(label):
    global cdname, thomasTimer
    if cdname == label and time.time()-thomasTimer > 10:
        os.system('rosrun sound_play play.py ~/catkin_ws/src/face_to_speech/sounds/thomas.wav')
        cdname = label
        thomasTimer = time.time()
    elif cdname != label:
        os.system('rosrun sound_play play.py ~/catkin_ws/src/face_to_speech/sounds/thomas.wav')
        cdname = label
        thomasTimer = time.time()

def shoutTheodore(label):
    global cdname, thomasTimer
    if cdname == label and time.time()-theoTimer > 10:
        os.system('rosrun sound_play play.py ~/catkin_ws/src/face_to_speech/sounds/theodore.wav')
        cdname = label
        theoTimer = time.time()
    elif cdname != label:
        os.system('rosrun sound_play play.py ~/catkin_ws/src/face_to_speech/sounds/theodore.wav')
        cdname = label
        theoTimer = time.time()

def shoutChrisA(label):
    global cdname, chrisATimer
    if cdname == label and time.time()-chrisATimer > 10:
        os.system('rosrun sound_play play.py ~/catkin_ws/src/face_to_speech/sounds/chris.wav')
        cdname = label
        chrisATimer = time.time()
    elif cdname != label:
        os.system('rosrun sound_play play.py ~/catkin_ws/src/face_to_speech/sounds/chris.wav')
        cdname = label
        chrisATimer = time.time()

def shoutChrisP(label):
    global cdname, chrisPTimer
    if cdname == label and time.time()-chrisPTimer > 10:
        os.system('rosrun sound_play play.py ~/catkin_ws/src/face_to_speech/sounds/chris.wav')
        cdname = label
        chrisPTimer = time.time()
    elif cdname != label:
        os.system('rosrun sound_play play.py ~/catkin_ws/src/face_to_speech/sounds/chris.wav')
        cdname = label
        chrisPTimer = time.time()

def shoutNasia(label):
    global cdname, nasiaTimer
    if cdname == label and time.time()-nasiaTimer > 10:
        os.system('rosrun sound_play play.py ~/catkin_ws/src/face_to_speech/sounds/nasia.wav')
        cdname = label
        nasiaTimer = time.time()
    elif cdname != label:
        os.system('rosrun sound_play play.py ~/catkin_ws/src/face_to_speech/sounds/nasia.wav')
        cdname = label
        nasiaTimer = time.time()

def shoutNikos(label):
    global cdname, nikosTimer
    if cdname == label and time.time()-nikosTimer > 10:
        os.system('rosrun sound_play play.py ~/catkin_ws/src/face_to_speech/sounds/nikos.wav')
        cdname = label
        nikosTimer = time.time()
    elif cdname != label:
        os.system('rosrun sound_play play.py ~/catkin_ws/src/face_to_speech/sounds/nikos.wav')
        cdname = label
        nikosTimer = time.time()

def shoutPrimeMinister(label):
    global cdname, primeMinisterTimer
    if cdname == label and time.time()-primeMinisterTimer > 10:
        os.system('rosrun sound_play play.py ~/catkin_ws/src/face_to_speech/sounds/primeMinister.wav')
        cdname = label
        primeMinisterTimer = time.time()
    elif cdname != label:
        os.system('rosrun sound_play play.py ~/catkin_ws/src/face_to_speech/sounds/primeMinister.wav')
        cdname = label
        primeMinisterTimer = time.time()

def appendToList(label):
    global listings
    listings.append(label)

def checkEqual(iterator):
    iterator = iter(iterator)
    try:
        first = next(iterator)
    except StopIteration:
        return True
    return all(first == rest for rest in iterator)

def callback(msg):
    global timer, list
    try:
        if time.time()-timer > 0.5:
            label = msg.detections[0].label
            appendToList(label)
            print (listings)
            timer = time.time()
            equal = checkEqual(listings)
            if not equal:
                del listings[:]
            if len(listings) == 6 and equal:
                if label == 'Thomas':
                    shoutThomas(label)
                    del listings[:]
                elif label == 'Alexander':
                    shoutAlexander(label)
                    del listings[:]
                elif label == 'Theodore':
                    shoutTheodore(label)
                    del listings[:]
                elif label == 'ChrisA':
                    shoutChrisA(label)
                    del listings[:]
                elif label == 'ChrisP':
                    shoutChrisP(label)
                    del listings[:]
                elif label == 'Nasia':
                    shoutNasia(label)
                    del listings[:]
                elif label == 'Nikos':
                    shoutNikos(label)
                    del listings[:]
                elif label == 'TsiprasA':
                    shoutPrimeMinister()
                    del listings[:]
            elif len(listings) == 6:
                del listings[:]
    except:
        pass

def listener():
    rospy.init_node('face_to_speech', anonymous=True)
    rospy.Subscriber('face_recognizer/face_recognitions', DetectionArray, callback)
    rospy.spin()

if __name__ == '__main__':
    listener()
