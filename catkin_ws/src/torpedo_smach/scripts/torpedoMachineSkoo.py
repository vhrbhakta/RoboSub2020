#!/usr/bin/env python

import rospy
import smach
import smach_ros
import time
import threading
from std_msgs.msg import Bool

class Find_board(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['found_board', 'retry', 'failed'])

    def execute(self, userdata):
        pass

class Chosen_side(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['moved', 'retry', 'failed'])

    def execute(self, userdata):
        pass

class Shoot(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['shot', 'retry', 'failed'])

    def execute(self, userdata):
        pass


def main():
    rospy.init_node('torpedo_state_machine')

    sm = smach.StateMachine(outcomes = ['pass', 'fail'])
    
    with sm:
        smach.StateMachine.add('FIND_BOARD', Find_board(), transitions={'found_board':'CHOSEN_SIDE', 'retry': 'FIND_BOARD', 'failed':'fail'})
        smach.StateMachine.add('CHOSEN_SIDE', Chosen_side(), transitions=['moved':'SHOOT', 'retry':'CHOSEN_SIDE', 'failed':'FIND_BOARD'])
        smach.StateMachine.add('SHOOT', Shoot(), transitions=['shot':'pass', 'retry':'SHOOT', 'failed':'fail'])

    outcome = sm.execute()

if __name__ == '__main__':
    main()
