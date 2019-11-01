import rospy
import random
from std_msgs.msg import Int64

def sonarPub():
    pub = rospy.Publisher('sonar', Int64, queue_size='10')
    rospy.init_node('sonarReadings', anonymous=True)
    rate = rospy.Rate(10)

    rd = random.randint(0,100)
    rospy.loginfo(rd%2)
    pub.publish(rd%2)
    
    rate.sleep()
    '''
    pub.publish()
   '''




if __name__ == '__main__':
    try:
        sonarPub()
    except rospy.ROSInterruptException:
        pass
