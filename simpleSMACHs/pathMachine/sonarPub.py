import rospy
from std_msgs.msg import Int64

def sonarPub():
    pub = rospy.Publisher('sonar', Int64, queue_size='10')
    rospy.init_node('sonarReadings', anonymous=True)
    rate = rospy.Rate(10)
    '''
    pub.publish()
   '''


if __name__ == '__main__':
    try:
        sonarPub()
    except rospy.ROSInterruptException:
        pass
