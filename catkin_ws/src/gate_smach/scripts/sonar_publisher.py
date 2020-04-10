#!/usr/bin/env python
import rospy
import random
from std_msgs.msg import Bool

def talker():
    pub = rospy.Publisher('sonar', Bool, queue_size=10)
    rospy.init_node('sonar', anonymous=True)
    rate = rospy.Rate(30)
    while not rospy.is_shutdown():
        interference = random.randint(0,1)
        if(interference == 1):
            pub.publish(True)
        else:
            pub.publish(False)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass