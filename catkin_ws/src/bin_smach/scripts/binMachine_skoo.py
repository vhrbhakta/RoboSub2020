#!/usr/bin/env python

import rospy
import smach
import smach_ros

class Find_bin(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['found', 'not_found', 'failed_find_attempts'])
    
    def execute(self, userdata):
        pass

class Lift_lid(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['lid_lifted', 'not_lifted', 'failed_lift_attempts'])
    
    def execute(self, userdata):
        pass

class Drop_markers(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['markers_dropped', 'missed', 'failed_marker_attempts'])
    
    def execute(self, userdata):
        pass

class Drop_bottle(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['bottle_dropped', 'missed_bin', 'failed_bottle_attempts'])
    
    def execute(self, userdata):
        pass

def main():
    rospy.init_node('bin_state_machine')

    sm = smach.StateMachine(outcomes=['failed', 'passed'])

    with sm:
        smach.StateMachine.add('FIND_BIN', Find_bin(), transitions={'found':'LIFT_LID', 'not found':'FIND_BIN', 'failed_find_attempts':'failed'})
        smach.StateMachine.add('LIFT_LID', Lift_lid(), transitions={'lid_lifted':'DROP_MARKERS', 'not_lifted':'LIFT_LID', 'failed_lift_attempts':'failed'})
        smach.StateMachine.add('DROP_MARKERS', Drop_markers(), transitions={'markers_dropped':'DROP_BOTTLE', 'missed':'DROP_MARKERS','failed_marker_attempts': 'failed'})
        smach.StateMachine.add('DROP_BOTTLE', Drop_bottle(), transitions={'bottle_dropped':'passed', 'missed_bin':'DROP_BOTTLE', 'failed_bottle_attempts':'failed'} )

    outcome = sm.execute()


if __name__=='__main__':
    main()