import rospy
from std_msgs.msg import Int64

class depthSub:
    
    def __init__(self):
        self.depth

    def setDepth(self, value):
        self.depth = int(value)
        

    def getDepth(self):
        return self.depth

    def callback(self, data):
        rospy.loginfo(rospy.get_caller_id() + ": I heard %d" %data.data)
        self.setDepth(data.data)        

    def depthListener(self):
        rospy.init_node('depthListener', anonymous =True)

        rospy.Subscriber('depthTalker', Int64, self.callback)
        rospy.spin()
    #    rospy.Subscriber('')

# if __name__ == '__main__':
#     depthSuber = depthSub()
#     depthSuber.depthListener()