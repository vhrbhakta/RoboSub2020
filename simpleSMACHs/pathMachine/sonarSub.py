import rospy
from std_msgs.msg import Int64

class sonarSub:
    
    def __init__(self):
        self.ping

    def setPing(self, value):
        self.ping = value
        

    def getPing(self):
        return self.ping

    def callback(self, data):
        rospy.loginfo(rospy.get_caller_id() + ": I heard %d" %data.data)
        self.setPing(data.data)        

    def SonarListener(self):
        rospy.init_node('sonarListener', anonymous =True)

        rospy.Subscriber('sonarReadings', Int64, self.callback)
        rospy.spin()
