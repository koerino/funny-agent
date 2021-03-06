'''
* Copyright (c) 2014, 2015 Entertainment Intelligence Lab, Georgia Institute of Technology.
* Originally developed by Mark Riedl.
* Last edited by Mark Riedl 05/2015
*
* Licensed under the Apache License, Version 2.0 (the "License");
* you may not use this file except in compliance with the License.
* You may obtain a copy of the License at
*
*     http://www.apache.org/licenses/LICENSE-2.0
*
* Unless required by applicable law or agreed to in writing, software
* distributed under the License is distributed on an "AS IS" BASIS,
* WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
* See the License for the specific language governing permissions and
* limitations under the License.
'''

import sys, pygame, math, numpy, random, time, copy, operator
from pygame.locals import *

from constants import *
from utils import *
from core import *

# Creates the pathnetwork as a list of lines between all pathnodes that are traversable by the agent.
def myBuildPathNetwork(pathnodes, world, agent = None):
    lines = []
    worldLines = world.getLinesWithoutBorders()
    corners = world.getPoints()

    for startNode in pathnodes:
        for endNode in pathnodes:
            # check if there's an intersection between the edge from start node to end node and every line of the obstacles (not including screen boundaries)
            if startNode != endNode and rayTraceWorld(startNode, endNode, worldLines) == None:
                # check if there's sufficient space between the edge and the obstacle corners for the agent to pass
                edge = (startNode, endNode)
                # record the distance from the edge to the closest corner
                closestDistance = float('inf')
                for corner in corners:
                    dis = minimumDistance(edge, corner)
                    if dis < closestDistance:
                        closestDistance = dis

                if agent.getRadius() * 2 < closestDistance:
                    lines.append(edge)

    return lines
