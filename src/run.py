#!/usr/bin/env python

import rospy
import time, os
from cob_perception_msgs.msg import DetectionArray

timer = time.time()
alexTimer = time.time()-7
thomasTimer = time.time()-7
theoTimer = time.time()-7
cdname = None

def shoutAlexander(label):
    global cdname, alexTimer
    if cdname == label and time.time()-alexTimer > 10:
        #os.system('rosrun sound_play play.py /home/quelotic/catkin_ws/src/face_to_speech/sounds/alexander.wav')
        os.system('rosrun sound_play say.py "Hello, ' + label + '!"')
        cdname = label
        alexTimer = time.time()
    elif cdname != label:
        #os.system('rosrun sound_play play.py /home/quelotic/catkin_ws/src/face_to_speech/sounds/alexander.wav')
        os.system('rosrun sound_play say.py "Hello, ' + label + '!"')
        cdname = label
        alexTimer = time.time()

def shoutThomas(label):
    global cdname, thomasTimer
    if cdname == label and time.time()-thomasTimer > 10:
        #os.system('rosrun sound_play play.py /home/quelotic/catkin_ws/src/face_to_speech/sounds/thomas.wav')
        os.system('rosrun sound_play say.py "Hello, ' + label + '!"')
        cdname = label
        thomasTimer = time.time()
    elif cdname != label:
        #os.system('rosrun sound_play play.py /home/quelotic/catkin_ws/src/face_to_speech/sounds/thomas.wav')
        os.system('rosrun sound_play say.py "Hello, ' + label + '!"')
        cdname = label
        thomasTimer = time.time()

def shoutTheodore(label):
    global cdname, thomasTimer
    if cdname == label and time.time()-theoTimer > 10:
        #os.system('rosrun sound_play play.py /home/quelotic/catkin_ws/src/face_to_speech/sounds/theodore.wav')
        os.system('rosrun sound_play say.py "Hello, ' + label + '!"')
        cdname = label
        theoTimer = time.time()
    elif cdname != label:
        #os.system('rosrun sound_play play.py /home/quelotic/catkin_ws/src/face_to_speech/sounds/theodore.wav')
        os.system('rosrun sound_play say.py "Hello, ' + label + '!"')
        cdname = label
        theoTimer = time.time()

def callback(msg):
    global timer
    try:
        if time.time()-timer > 2:
            label = msg.detections[0].label
            print (label)
            timer = time.time()
            if label == 'Thomas':
                shoutThomas(label)
            elif label == 'Alexander':
                shoutAlexander(label)
            elif label == 'Theodore':
                shoutTheodore(label)
            else:
                pass
    except:
        pass

def listener():
    rospy.init_node('face_to_speech', anonymous=True)
    rospy.Subscriber('face_recognizer/face_recognitions', DetectionArray, callback)
    rospy.spin()

if __name__ == '__main__':
    listener()
