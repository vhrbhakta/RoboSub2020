import roslib; roslib.load_manifest('smach_tutorials')
import rospy
import smach
import smach_ros
import random
from std_msgs.msg import Bool
from std_msgs.msg import String

class SCANGATE(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['Found_gate','Retry', 'Failed_attempts'])
        self.attempts = 0
        self.max_attemps = 5
        self.starting_point = None
        self.interference = None

    def execute(self):
        if self.attempts == 5:
            return 'Failed_attempts'

        if self.starting_point == None:
            self.set_starting_point()
        
        #change heading by 22.5 degrees away from wall (api call to change heading)
        #heading = heading + (22.5 * self.attempts)
        # rospy.loginfo('Heading: x degrees')

        #attempt++
        self.attempts = self.attempts +1

        #Move forward 15 meters (api call to move forward)
        rospy.loginfo('Moving forward 15 meters')
        
        rospy.Subscriber('sonar', Bool,self.sonar_callback)
        
        #if found something return found_gate else retry until attempt == 5
        if self.interference:
            return 'Found_gate'
        else:
            #if nothing found go back to waypoint (ros sub call to Sonar topic)
            rospy.loginfo('Heading back to waypoint')
            
            return 'Retry'

    def sonar_callback(self, data):
        self.interference = data.data

    def set_starting_point(self):
        #set waypoint (ros sub to DVL coordinates topic)
        pass

class FINDGATE(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['Found', 'Not_Found'])
        self.found = None
    
    def execute(self):
        #turn on CV (api call to turn on CV)
        rospy.Subscriber('CV_gate_spotter', Bool, self.cv_gate_spotter_callback)
        if(self.found):
            #position sub to be in center of gate (api calls to move sub; ros sub to CV topic)
            #return found
            rospy.loginfo('Moving to center of gate')

            return 'Found'
        else:
            #if not gate return not_found
            return 'Not_Found'


    def cv_gate_spotter_callback(self, data):
        self.found = data.data

class PASSGATE(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes = ['Passed_Gate', 'Not_Passed', 'Failed_gate'])
        self.pass_attempt=0
        self.max_pass_attempt = 5
        self.role = None
        self.pic_found = None
    
    def execute(self):
        if(self.pass_attempt >= self.max_pass_attempt):
            return 'Failed_gate'

        self.pass_attempt = self.pass_attempt +1
        #choose bootlegger or g-man (50/50 chance)
        coinflip = random.randint(0,1)
        if coinflip == 0:
            self.role = 'Bootlegger'
        else:
            self.role = 'G-man'
        
        #position to selected side (api calls to move and ros sub to CV topic)
        rospy.Subscriber('CV_role_finder', String, self.cv_role_finder_callback)
        if self.pic_found == self.role:
            rospy.loginfo('Passing gate')
            return 'Passed_Gate'
        else:
            
            return 'Not_Passed'

    def cv_role_finder_callback(self, data):
        self.pic_found = data.data

def main():
    rospy.init_node('gate_task')
    
    

    sm = smach.StateMachine(outcomes=['Passed', 'Failed'])
    
    with sm:
        smach.StateMachine.add('SCANGATE', SCANGATE(), transitions={'Found_gate':'FINDGATE', 'Retry':'SCANGATE', 'Failed_attempts':'Failed'})
        smach.StateMachine.add('FINDGATE', FINDGATE(), transitions={'Found':'PASSGATE', 'Not_Found':'SCANGATE'})
        smach.StateMachine.add('PASSGATE', PASSGATE(), transitions={'Passed_Gate': 'Passed', 'Not_Passed':'PASSGATE', 'Failed_gate':'Failed'})

    outcome = sm.execute()



if __name__ == '__main__':
    main()

