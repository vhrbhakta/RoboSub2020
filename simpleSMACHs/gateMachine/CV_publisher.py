import rospy
import random
from std_msgs.msg import Bool

def talker():
    pub = rospy.Publisher('CV_gate_spotter', Bool, queue_size=10)
    rospy.init_node('CV_gate_spotter', anonymous=True)
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        cv_found = random.randint(0,1)
        if(cv_found == 1):
            pub.publish(True)
        else:
            pub.publish(False)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass