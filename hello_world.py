# coding=utf-8

from simpleai.search import SearchProblem, breadth_first, depth_first, astar, greedy
from simpleai.search.viewers import WebViewer

GOAL = 'HELLO'
my_viewer = WebViewer()

"""
breadth first = 0
depth first = 1
astar = 2
greedy = 3
"""

print("For breadth first algorithm = 0")
print("For depth first algorithm = 1")
print("For astar algorithm = 2")
print("For greedy algorithm = 3")

algorithm = int(input("Which search algorithm? Please enter a number.\n"))

while algorithm<0 or 3<algorithm:
    algorithm = int(input(" Which search algorithm?"))

class HelloProblem(SearchProblem):
    def actions(self, state):
        if algorithm == 0 or algorithm == 1:#breadth first and depth first
            if len(state) < len(GOAL):
                return list('EHLO')
            else:
                return []
        if algorithm == 2 or algorithm == 3:#astar and greedy
            if len(state) < len(GOAL):
                return list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
            else:
                return []
            
    def result(self, state, action):
        return state + action

    def is_goal(self, state):
        return state == GOAL

    def heuristic(self, state):
        # how far are we from the goal?
        wrong = sum([1 if state[i] != GOAL[i] else 0
                    for i in range(len(state))])
        missing = len(GOAL) - len(state)
        return wrong + missing

problem = HelloProblem(initial_state='')

if algorithm == 0:
    print("Result of according to breadth first")
    result = breadth_first(problem,viewer=my_viewer)
    
elif algorithm == 1:
    print("Result of according to depth first")
    result = depth_first(problem,viewer=my_viewer)

elif algorithm == 2:
    print("Result of according to astar")
    result = astar(problem,viewer=my_viewer)

else:
    print("Result of according to greedy")
    result = greedy(problem,viewer=my_viewer)

print(result.state)
print(result.path())

print('Stats: ')
print(my_viewer.stats)