import copy
import random
# Consider using the modules imported above.

class Hat:

    #build contents array
    def __init__(self, **kwargs):
        self.contents = []
        for key, value in kwargs.items():
            for i in range(value):
                self.contents.append(key)

    #draw balls out of contents array at random
    def draw(self, num):
        
        #return all balls in hat and clear contents array if num balls drawn >= num balls in hat
        if num >= len(self.contents):
            self.balls_drawn = copy.copy(self.contents)
            self.contents.clear()
        
        #draw balls from contents at random and place them in balls_drawn array
        else:
            self.balls_drawn = []
            for i in range(num):
                rng = random.randint(0, len(self.contents) - 1)
                self.balls_drawn.append(self.contents.pop(rng))

        #print("balls drawn:", self.balls_drawn)
        #print("balls not drawn:", self.contents)
        return self.balls_drawn

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    #initialize number of successful experiments
    count_success = 0

    #run experiment the number of times indicated
    for i in range(num_experiments):
        hat_copy = copy.deepcopy(hat) #make a deep copy of the hat object so that the hat "resets" with each iteration
        actual_balls = hat_copy.draw(num_balls_drawn) #draw balls from the hat and store them in actual_balls array
        expected_balls_arr = []
        drawn_balls = []
        
        #convert expected_balls from dict to array
        for key, value in expected_balls.items():
            for j in range(value):
                expected_balls_arr.append(key)

        #loop through expected_balls_arr and remove those balls from actual_balls array
        for ball in expected_balls_arr:

            #try to pull an expected ball out of the actual_balls array. If ball doesn't exist, mark the current experiment as failure (break inner loop) and restart experiment (outer-most loop)
            try:
                drawn_balls.append(actual_balls.pop(actual_balls.index(ball))) #adds balls that were expected and drawn
            except:
                break

        #add to successful experiments count
        if expected_balls_arr == drawn_balls:
            count_success += 1

        #print("run:", i)
        #print(actual_balls, "\n")
    return count_success / num_experiments
