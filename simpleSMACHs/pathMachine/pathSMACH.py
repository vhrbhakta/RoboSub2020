import rospy
import smach

class SEARCHPATH(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['Path Found', 'Path not Found']
        input_keys=['cv', 'floorDistance']
        output_keys=['cv_scan'])
    self.pathAttempt = 0
    self.pathFound = False
    self.cv = True
    self.floorDistance = sonar.ping
    self.depth = barometer.scan
    self.distance_traveled = 0

    def exeute(self):
        #Find path using cv
        cv.position = 2
        while floorDistance > 6
            depth += 1
        while pathAttempt < 3
            while distance_traveled < 10
                distance_traveled += 1
                if self.pathScan()
                    pathFound = True
                    return 'Path Found'
                else
                    while distance_traveled > -1
                        distance_traveled -= 1
        pathAttempt += 1
        if pathAttempt = 2
            return 'Path Not Found'
            self.surface()

    def pathScan(self):
        if(cv.detectPath)
            return True
        return False

    def surface(self):
        depth = 0
