#!/usr/bin/env python

import rospy
import random
from std_msgs.msg import Bool

def talker():
    pub = rospy.Publisher('cv_bottle', Bool, queue_size=10)
    rospy.init_node('cv_bottle_pub', anonymous=True)
    rate = rospy.Rate(1)
    while not rospy.is_shutdown():
        found = random.randint(0,1)
        if(found == 1):
            pub.publish(True)
        else:
            pub.publish(False)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass