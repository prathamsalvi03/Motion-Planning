#!/usr/bin/env python
import sys
import matplotlib.pyplot as plt
import pathlib
sys.path.append(str(pathlib.Path(__file__).parent.parent))



#show animation = True



def main():
        



        class Parent def: 
                planQRRTStar < planRRTStar

                properties
                ParentDepthSearch
                ParentDepthRewire
                properties(Access = protected)
                ParentNodeIds

        class methods:

                def __init__(self,stateSpace,stateVlidator):
                        class  super(): __init__(stateSpace, stateValidator)
                        self.ParentDepthSearch = 2;
                        self.ParentDepthRewire = 1;
                        self.ParentNodeIds = containers.Map('KeyType', 'double', 'ValueType', 'double');



        def [newNodeId, statusCode, treeInternal] = extend(self, randState, treeInternal)
        statusCode = self.InProgress;
        newNodeId = nan; 
        idx = treeInternal.nearestNeighbor(randState);
        nearestNode = treeInternal.getNodeState(idx);
        costNN = treeInternal.getNodeCostFromRoot(idx);
            
        d = self.StateSpace.distance(nearestNode, randState);


def planning(self,animation = True):

        self.node_list = [self.start]
        if d < 1e-10 :
                statusCode = self.ExistingState;
                return;
            
        newState = randState;

        if d > self.MaxConnectionDistance:
                newState = self.StateSpace.interpolate(nearestNode, newState, self.MaxConnectionDistance/d);
                d = self.MaxConnectionDistance;
            
        costNew = costNN + d;
            
        if self.StateValidator.isMotionValid(nearestNode, newState):
                statusCode = self.MotionInCollision;
                return;
            
        def choose_parent(self , new_node , near_node):
                if not nearIndices:
                return None
        nearIndices = treeInternal.near(newState);
        costMin = costNew;
        idMin = -1;
        
        for j in nearIndices : 1:length(nearIndices)
        near_node = self.node_list[i]
        idNear = nearIndices(j);
        stateNear = treeInternal.getNodeState(idNear);
        costNear = treeInternal.getNodeCostFromRoot(idNear);

        costTentative = costNear + self.StateSpace.distance(stateNear, newState);

        if costMin > costTentative & self.StateValidator.isMotionValid(stateNear, newState):
                    costMin = costTentative;
                    idMin = idNear;
            
        
            
        if idMin >= 0:
                nearIndices = nearIndices(nearIndices ~= idMin);
        else:
                idMin = idx;

            
            
        for n in ParentDepthSearch : 
            if self.ParentNodeIds.isKey(idMin):
                idParent = self.ParentNodeIds(idMin);
                stateParent = self.treeInternal.getNodeState(idParent);
                costParent = self.treeInternal.getNodeCostFromRoot(idParent);
             #return       
                costTentativeParent = costParent + self.StateSpace.distance(stateParent, newState);
            if costMin > costTentativeParent & self.StateValidator.isMotionValid(stateParent, newState):
        
                costMin = costTentativeParent;
                idMin = idParent;
            #return

        idNew = treeInternal.insertNode(newState, idMin);
        self.ParentNodeIds(idNew) = idMin;
        newNodeId = idNew;

        for k in nearIndices :
                idNear = self.nearIndices(k);
                stateNear = self.treeInternal.getNodeState(idNear);
                costNear = self.treeInternal.getNodeCostFromRoot(idNear);
                
                idNew = newNodeId;

                if costNear > costNew + self.StateSpace.distance(stateNear, newState) & self.StateValidator.isMotionValid(stateNear, newState):
                    for l in ParentDepthRewire:
                       if self.ParentNodeIds.isKey(idNew):
                             idParentRewire = self.ParentNodeIds(idNew);
                             stateParentRewire = treeInternal.getNodeState(idParentRewire);
                             costParentRewire = treeInternal.getNodeCostFromRoot(idParentRewire);
 
                             costTentativeParentRewire = costParentRewire + self.StateSpace.distance(stateNear, stateParentRewire);
 
                             if costNear > costTentativeParentRewire & self.StateValidator.isMotionValid(stateNear, stateParentRewire):
                                 costNear = costTentativeParentRewire;
                                 idNew = idParentRewire;
                            #return 
                    
                    rewireStatus = treeInternal.rewire(idNear, idNew);
                    self.ParentNodeIds(idNear) = idNew;

                
        if self.GoalReachedFcn(self, self.CurrentGoalState, newState):
                if self.ContinueAfterGoalReached:
                    statusCode = self.GoalReachedButContinue;
                else:
                    statusCode = self.GoalReached;
                
                return;
            
            
        if newNodeId == self.MaxNumTreeNodes:
                statusCode = self.MaxNumTreeNodesReached;
                return;


                    


                    







                
            
            
