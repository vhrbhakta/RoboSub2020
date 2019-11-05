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

class SEARCHPATHDIRECTION(smach.state):
     def __init__(self):
         smach.State.__init__(self, outcomes=['Path Found']
         input_keys=['cv']
         output_keys=['cv_scan']
    self.cv = True
    self.foundpathpicture = False
    self.foundPathDistanceTravel = distance_traveled
    import random

    def exeute(self)
    #calculate direction of the path by using cv scan of the picture
    #line 54 - 60 is taking the picture that was scan by the cv and matching it with a 
    #photo gallery of direction pictures
    #from PIL import Image

    #filename = 'image.png'
    #with Image.open(filename) as image:
    #    width, height = image.size
    #foundPictureDirection = [i for i, value in enumerate(pictureDirectionGallery) if value == cv_scan_picture] 
    int pathCount = 0
        cv.position = 2
        random.choice([True, False])
        while(pathCount < 4)
            if( choice = True && pathCount < 2 )
                foundPathPicture = True
                print("Path found changing sub x direction: ")
            else if( choice = False && pathCount < 2)
                foundPathPicture = False
                print("Path not found retrying")
            else:
                print("path cant be found, now Im going 10 feet to find next") 
  
