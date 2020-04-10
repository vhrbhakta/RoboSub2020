#!/usr/bin/env python
import rospy
import random
from std_msgs.msg import String

def talker():
    pub = rospy.Publisher('CV_role_finder', String, queue_size=10)
    rospy.init_node('CV_role_finder', anonymous=True)
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        role = random.randint(0,1)
        if(role == 1):
            pub.publish('Bootlegger')
        else:
            pub.publish('G-man')
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass