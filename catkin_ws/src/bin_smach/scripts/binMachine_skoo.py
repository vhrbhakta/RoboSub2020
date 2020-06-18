#!/usr/bin/env python

import rospy
import smach
import smach_ros
import time
from std_msgs.msg import Bool

class Find_bin(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['found', 'not_found', 'failed_find_attempts'])
        self.waypoint = None
        self.detected = None
        self.cv_bin = None
        self.attempt = 0
        rospy.Subscriber('sonar', Bool, self.sonar_callback)
        rospy.Subscriber('cv_bin', Bool, self.cv_bin_cb)
    
    def execute(self, userdata):
        if self.attempt >= 5:
            return 'failed_find_attempts'
        #set waypoint if waypoint == none
        if self.waypoint == None:
            self.waypoint = [1,1,1]
            rospy.loginfo('set waypoint')
        
        #go forward 15 m
        rospy.loginfo('moving forward 15 meters')
        #if sonar senses something use CV to see what it is
        for i in range(30):
            time.sleep(1)
            if self.detected == True:
                for j in range(30):
                    time.sleep(1)
                    if self.cv_bin == True:
                        return 'found'
                    elif self.cv_bin == False:
                        self.attempt += 1
                        rospy.loginfo('Bin not found. Returning to waypoint')
                        return 'not_found'
            elif self.detected == False:
                self.attempt += 1
                rospy.loginfo('Bin not found. Returning to waypoint')
                return 'not_found'
        if self.detected == None or self.cv_bin == None:
            self.attempt += 1
            rospy.loginfo('Bin not found. Returning to waypoint')
            return 'not_found'
        #if nothing found or CV did not find bin go back to waypoint, attempt++, return not_found
        

    def sonar_callback(self, data):
        self.detected = data.data
    
    def cv_bin_cb(self, data):
        self.cv_bin = data.data

class Lift_lid(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['lid_lifted', 'not_lifted', 'failed_lift_attempts'])

        self.attempts = 0
        self.cv_lid = None
        rospy.Subscriber('cv_lid', Bool, self.cv_lib_cb)
    
    def execute(self, userdata):
        if self.attempts >= 5:
            return 'failed_lift_attempts'
        
        #use CV to find lid
        for i in range(30):
            time.sleep(1)
            if self.cv_lid == True:
                #move lid off bin
                rospy.loginfo('moving lid off of bin')
                return 'lid_lifted'
            elif self.cv_lid ==False:
                self.attempts += 1
                rospy.loginfo('did not find lid')
                return 'not_lifted'
        if self.cv_lid == None:
            self.attempts += 1
            rospy.loginfo('did not find lid')
            return 'not_lifted'
        
        
        

    def cv_lib_cb(self, data):
        self.cv_lid = data.data

class Drop_markers(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['markers_dropped', 'missed', 'failed_marker_attempts'])
        self.attempts = 0
        self.cv_top = None
        rospy.Subscriber('cv_top', Bool, self.cv_top_cb)
    
    def execute(self, userdata):
        if self.attempts >= 5:
            return 'failed_marker_attempts'
        self.attempts += 1
        #use CV to find top of bin
        for i in range(30):
            time.sleep(1)
            if self.cv_top == True:
                rospy.loginfo('dropping markers')
                return 'markers_dropped'
            elif self.cv_top == False:
                
                
                return 'missed'
        if self.cv_top == None:
            rospy.loginfo('top of bin not found')
            return 'missed'
        #if CV not find bin attempt++, return missed
        #move to over bin
        # drop markers
    
    def cv_top_cb(self, data):
        self.cv_top = data.data

class Drop_bottle(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['bottle_dropped', 'missed_bin', 'failed_bottle_attempts'])
        self.waypoint = None
        self.cv_bottle = None
        self.cv_top = None
        self.attempts = 0
        rospy.Subscriber('cv_bottle', Bool, self.cv_bottle_cb)
        rospy.Subscriber('cv_top', Bool, self.cv_top_cb)
    
    def execute(self, userdata):
        if self.attempts >= 5:
            return 'failed_bottle_attempts'
        self.attempts += 1
        #set waypoint if not set
        if self.waypoint == None:
            self.waypoint = [1,1,1]
            rospy.loginfo('setting waypoint')

        #Use CV to find bottle
        for i in range(30):
            time.sleep(1)
            if(self.cv_bottle == True):
                #go to bottle
                #grab bottle
                rospy.loginfo('picked up bottle moving to bin')
                for j in range(30):
                    time.sleep(1)
                    if self.cv_top == True:
                        #go back to waypoint
                        #drop bottle in bin
                        rospy.loginfo('dropping bottle into bin')
                        return 'bottle_dropped'
                    #if CV not find bottle, return missed_bin
                    elif self.cv_top == False:
                        rospy.loginfo('did not find bin')
                        return 'missed_bin'
            elif(self.cv_bottle==False):
                rospy.loginfo('did not find bottle')
                return 'missed_bin'
        if self.cv_bottle == None or self.cv_top == None:
            return 'missed_bin'
                        
    def cv_bottle_cb(self, data):
        self.cv_bottle = data.data

    def cv_top_cb(self, data):
        self.cv_top = data.data

def main():
    rospy.init_node('bin_state_machine')

    sm = smach.StateMachine(outcomes=['failed', 'passed'])

    with sm:
        smach.StateMachine.add('FIND_BIN', Find_bin(), transitions={'found':'LIFT_LID', 'not_found':'FIND_BIN', 'failed_find_attempts':'failed'})
        smach.StateMachine.add('LIFT_LID', Lift_lid(), transitions={'lid_lifted':'DROP_MARKERS', 'not_lifted':'LIFT_LID', 'failed_lift_attempts':'failed'})
        smach.StateMachine.add('DROP_MARKERS', Drop_markers(), transitions={'markers_dropped':'DROP_BOTTLE', 'missed':'DROP_MARKERS','failed_marker_attempts': 'failed'})
        smach.StateMachine.add('DROP_BOTTLE', Drop_bottle(), transitions={'bottle_dropped':'passed', 'missed_bin':'DROP_BOTTLE', 'failed_bottle_attempts':'failed'} )

    outcome = sm.execute()


if __name__=='__main__':
    main()