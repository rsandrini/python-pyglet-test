


class behaviours():

    circleRadius = 6  #the radius of the circle
    wanderAngle = 0   #the change to the current direction. Produces sustained turned, keeps it from being jerky. Makes it smooth
    wanderChange = 1  #the amount to change the angle each frame.

    #Those numbers can be changed to get other movement patterns. Those are
    #the defaults used in the demo
    def wander(velocity):
        circleMidde = velocity.cloneVector().normalize().multiply(circleRadius); #circle middle is the the velocity pushed out to the radius.
        wanderForce.length = 3  #/force length, can be changed to get a different motion
        wanderForce.angle = wanderAngle #set the angle to move
        wanderAngle += Math.random() * wanderChange - wanderChange * .5 #change the angle randomly to make it wander
        return circleMidde.add(wanderForce)  #apply the force

