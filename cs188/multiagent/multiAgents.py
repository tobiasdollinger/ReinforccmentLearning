# multiAgents.py
# --------------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


from util import manhattanDistance
from game import Directions
import random, util

from game import Agent

class ReflexAgent(Agent):
    """
      A reflex agent chooses an action at each choice point by examining
      its alternatives via a state evaluation function.

      The code below is provided as a guide.  You are welcome to change
      it in any way you see fit, so long as you don't touch our method
      headers.
    """


    def getAction(self, gameState):
        """
        You do not need to change this method, but you're welcome to.

        getAction chooses among the best options according to the evaluation function.

        Just like in the previous project, getAction takes a GameState and returns
        some Directions.X for some X in the set {North, South, West, East, Stop}
        """
        # Collect legal moves and successor states
        legalMoves = gameState.getLegalActions()

        # Choose one of the best actions
        scores = [self.evaluationFunction(gameState, action) for action in legalMoves]
        bestScore = max(scores)
        bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
        chosenIndex = random.choice(bestIndices) # Pick randomly among the best

        "Add more of your code here if you want to"

        return legalMoves[chosenIndex]

    def evaluationFunction(self, currentGameState, action):
        """
        Design a better evaluation function here.

        The evaluation function takes in the current and proposed successor
        GameStates (pacman.py) and returns a number, where higher numbers are better.

        The code below extracts some useful information from the state, like the
        remaining food (newFood) and Pacman position after moving (newPos).
        newScaredTimes holds the number of moves that each ghost will remain
        scared because of Pacman having eaten a power pellet.

        Print out these variables to see what you're getting, then combine them
        to create a masterful evaluation function.
        """
        # Useful information you can extract from a GameState (pacman.py)
        "*** YOUR CODE HERE ***"
        successorGameState = currentGameState.generatePacmanSuccessor(action)
        newPos = successorGameState.getPacmanPosition()
        newFood = successorGameState.getFood()
        newGhostStates = successorGameState.getGhostStates()
        newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]
        numFoodLeft = len(newFood.asList())
        try:
            minDistanceFromFood = min([util.manhattanDistance((x,y), newPos) for x,y in newFood.asList()])
            minDistanceFromGhosts = min([util.manhattanDistance(newPos,(x,y)) for x,y in  successorGameState.getGhostPositions()])
        except ValueError:
            minDistanceFromFood = 0
            minDistanceFromGhosts = 0 
        runFromGhost = 0 if minDistanceFromGhosts > 1 or numFoodLeft == 0 else -5000
        return -numFoodLeft*100-(minDistanceFromFood+1)+runFromGhost

def scoreEvaluationFunction(currentGameState):
    """
      This default evaluation function just returns the score of the state.
      The score is the same one displayed in the Pacman GUI.

      This evaluation function is meant for use with adversarial search agents
      (not reflex agents).
    """
    return currentGameState.getScore()

class MultiAgentSearchAgent(Agent):
    """
      This class provides some common elements to all of your
      multi-agent searchers.  Any methods defined here will be available
      to the MinimaxPacmanAgent, AlphaBetaPacmanAgent & ExpectimaxPacmanAgent.

      You *do not* need to make any changes here, but you can if you want to
      add functionality to all your adversarial search agents.  Please do not
      remove anything, however.

      Note: this is an abstract class: one that should not be instantiated.  It's
      only partially specified, and designed to be extended.  Agent (game.py)
      is another abstract class.
    """

    def __init__(self, evalFn = 'scoreEvaluationFunction', depth = '2'):
        self.index = 0 # Pacman is always agent index 0
        self.evaluationFunction = util.lookup(evalFn, globals())
        self.depth = int(depth)

class MinimaxAgent(MultiAgentSearchAgent):
    """
      Your minimax agent (question 2)
    """

    def getAction(self, gameState):
        """
          Returns the minimax action from the current gameState using self.depth
          and self.evaluationFunction.

          Here are some method calls that might be useful when implementing minimax.

          gameState.getLegalActions(agentIndex):
            Returns a list of legal actions for an agent
            agentIndex=0 means Pacman, ghosts are >= 1

          gameState.generateSuccessor(agentIndex, action):
            Returns the successor game state after an agent takes an action

          gameState.getNumAgents():
            Returns the total number of agents in the game
        """
        "*** YOUR CODE HERE ***"
        def minimax(gameState):
            bestAction = ''
            bestScore = float("-inf")
            for curAction in gameState.getLegalActions(0):
                curScore = value(gameState.generateSuccessor(0, curAction), 0, 1)
                if curScore > bestScore:
                    bestScore = curScore
                    bestAction = curAction
            print '\n\n\n\n'
            print bestScore
            return bestAction 
                
        def value(gameState, curDepth, curAgent):
            if curAgent ==  gameState.getNumAgents():
                curAgent = 0
                curDepth +=1
            print 'curDepth', curDepth
            print 'curAgent', curAgent              
            if curDepth == self.depth or gameState.isWin() or gameState.isLose():
                return self.evaluationFunction(gameState)
            if curAgent == 0:
                return maxValue(gameState, curDepth, curAgent)
            else:
                return minValue(gameState, curDepth, curAgent)
         
        def maxValue(gameState, curDepth, curAgent):
            v = float("-inf")
            for curAction in gameState.getLegalActions(curAgent):
                v = max(v, value(gameState.generateSuccessor(curAgent, curAction), curDepth, curAgent+1))
            return v
        
        def minValue(gameState, curDepth, curAgent):
            v = float("inf")
            for curAction in gameState.getLegalActions(curAgent):
                v = min(v, value(gameState.generateSuccessor(curAgent, curAction), curDepth, curAgent+1))
            return v
        
        return minimax(gameState)
        util.raiseNotDefined()

class AlphaBetaAgent(MultiAgentSearchAgent):
    """
      Your minimax agent with alpha-beta pruning (question 3)
    """

    def getAction(self, gameState):
        """
          Returns the minimax action using self.depth and self.evaluationFunction
        """
        "*** YOUR CODE HERE ***"
        def alphaBeta(gameState):
            bestAction = ''
            bestScore = float("-inf")
            alpha = float('-inf')
            beta = float('inf')
            for curAction in gameState.getLegalActions(0):
                curScore = value(gameState.generateSuccessor(0, curAction), 0, 1, alpha, beta)
                if curScore > bestScore:
                    bestScore = curScore
                    bestAction = curAction
                    alpha = curScore
            return bestAction
                
        def value(gameState, curDepth, curAgent, alpha, beta):
            if curAgent ==  gameState.getNumAgents():
                curAgent = 0
                curDepth +=1
 
            if curDepth == self.depth or gameState.isWin() or gameState.isLose():
                return self.evaluationFunction(gameState)
            if curAgent == 0:
                return maxValue(gameState, curDepth, curAgent, alpha, beta)
            else:
                return minValue(gameState, curDepth, curAgent, alpha, beta)
         
        def maxValue(gameState, curDepth, curAgent, alpha, beta):
            v = float("-inf")
            for curAction in gameState.getLegalActions(curAgent):
                v = max(v, value(gameState.generateSuccessor(curAgent, curAction), curDepth, curAgent+1, alpha, beta))
                if v > beta:
                    return v
                alpha = max(v, alpha)
            return v
        
        def minValue(gameState, curDepth, curAgent, alpha, beta):
            v = float("inf")
            for curAction in gameState.getLegalActions(curAgent):
                v = min(v, value(gameState.generateSuccessor(curAgent, curAction), curDepth, curAgent+1, alpha, beta))
                if v < alpha: 
                    return v
                beta = min(v, beta)
            return v
        return alphaBeta(gameState)
        util.raiseNotDefined()

class ExpectimaxAgent(MultiAgentSearchAgent):
    """
      Your expectimax agent (question 4)
    """

    def getAction(self, gameState):
        """
          Returns the expectimax action using self.depth and self.evaluationFunction

          All ghosts should be modeled as choosing uniformly at random from their
          legal moves.
        """
        "*** YOUR CODE HERE ***"
        def expectimax(gameState):
            bestAction = ''
            bestScore = float("-inf")
            for curAction in gameState.getLegalActions(0):
                curScore = value(gameState.generateSuccessor(0, curAction), 0, 1)
                if curScore > bestScore:
                    bestScore = curScore
                    bestAction = curAction
            return bestAction 

        def value(gameState, curDepth, curAgent):
            if curAgent ==  gameState.getNumAgents():
                curAgent = 0
                curDepth += 1
            if curDepth == self.depth or gameState.isWin() or gameState.isLose():
                return self.evaluationFunction(gameState)
            if curAgent == 0:
                return maxValue(gameState, curDepth, curAgent)
            else:
                return minValue(gameState, curDepth, curAgent)

        def maxValue(gameState, curDepth, curAgent):
            v = float("-inf")
            for curAction in gameState.getLegalActions(curAgent):
                v = max(v, value(gameState.generateSuccessor(curAgent, curAction), curDepth, curAgent+1))
            return v

        def minValue(gameState, curDepth, curAgent):
            v = 0
            listLegalActions = gameState.getLegalActions(curAgent)
            p = 1.0/len(listLegalActions)
            for curAction in listLegalActions:
                v += p*value(gameState.generateSuccessor(curAgent, curAction), curDepth, curAgent+1)
            return v
        
        return expectimax(gameState)
        util.raiseNotDefined()

def betterEvaluationFunction(currentGameState):
    """
      Your extreme ghost-hunting, pellet-nabbing, food-gobbling, unstoppable
      evaluation function (question 5).

      DESCRIPTION: <write something here so we know what you did>
    """
    "*** YOUR CODE HERE ***"
                     
    newPos = currentGameState.getPacmanPosition()
    newFood = currentGameState.getFood()
    
#     newGhostStates = currentGameState.getGhostStates()
#     newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]
    numFoodLeft = len(newFood.asList())
    manhattDistancesFood = [util.manhattanDistance((x,y), newPos) for x,y in newFood.asList()]
    secondMinFromFood = 0
    try:
        minDistanceFromFood = min(manhattDistancesFood)
        try:
            secondMinFromFood = min(manhattDistancesFood.remove(minDistanceFromFood)) 
        except:
            pass
        minDistanceFromGhosts = min([util.manhattanDistance(newPos,(x,y)) for x,y in  currentGameState.getGhostPositions()])
    except ValueError:
        minDistanceFromFood = 0 
        minDistanceFromGhosts = 0 
    runFromGhost = 0 if minDistanceFromGhosts > 1 or numFoodLeft == 0 else -5000
    return -numFoodLeft*100-(minDistanceFromFood+1)-(secondMinFromFood+1)+runFromGhost
    util.raiseNotDefined()

# Abbreviation
better = betterEvaluationFunction

