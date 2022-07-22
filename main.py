import os
import time
from numpy.random import choice

class TriviaMdp(object):
    def __init__(self, N):
        self.N = N
    def startState(self):
        return 1
    def inEnd (self, state):
        return state == self.N
    def actions(self, state):
        result = []
        if state+1<=self.N:
            result.append("stay")
            result.append("quit")
        return result
    def succProbReward (self, state, action):
        # return list of (newState, prob, reward) triples
        # state = s, action = a, newState = s'
        # prob = T(s, a, s'), reward = Reward(s, a, s')
        result = []
        if action == "stay":
            if state == 1:
                result.append((state + 1, 0.99, 1.))
                result.append((self.N, 0.01, 0.))
            elif state == 2:
                result.append((state + 1, 0.9, 5.))
                result.append((self.N, 0.1, -1.))
            elif state == 3:
                result.append((state + 1, 0.8, 10.))
                result.append((self.N, 0.2, -6.))
            elif state == 4:
                result.append((state + 1, 0.7, 50.))
                result.append((self.N, 0.3, -16.))
            elif state == 5:
                result.append((state + 1, 0.6, 100.))
                result.append((self.N, 0.4, -66.))
            elif state == 6:
                result.append((state + 1, 0.5, 500))
                result.append((self.N, 0.5, -166.))
            elif state == 7:
                result.append((state + 1, 0.4, 1000))
                result.append((self.N, 0.6, -666.))
            elif state == 8:
                result.append((state + 1, 0.3, 5000))
                result.append((self.N, 0.7, -1666.))
            elif state == 9:
                result.append((state + 1, 0.2, 10000))
                result.append((self.N, 0.8, -6666.))
            elif state == 10:
                result.append((state + 1, 0.1, 15000))
                result.append((self.N, 0.9, -16666.))

        elif action == "quit":
            if state == 1:
                result.append((self.N, 1., 0.))
            elif state == 2:
                result.append((self.N, 1., 1.))
            elif state == 3:
                result.append((self.N, 1., 6.))
            elif state == 4:
                result.append((self.N, 1., 16.))
            elif state == 5:
                result.append((self.N, 1., 66.))
            elif state == 6:
                result.append((self.N, 1, 166.))
            elif state == 7:
                result.append((self.N, 1, 666.))
            elif state == 8:
                result.append((self.N, 1, 1666.))
            elif state == 9:
                result.append((self.N, 1, 6666.))
            elif state == 10:
                result.append((self.N, 1, 16666.))
        return result

    def discount (self):
        return 1.

    def states(self):
        return range(1, self.N+1)

def valueIteration(mdp):
    # initialize
    V = {} # state  -> Vopt[state]

    for state in mdp.states():
        V[state] = 0.

    def Q(state, action):
        return sum(prob*(reward + mdp.discount() * V[newState]) \
                   for newState, prob, reward in mdp.succProbReward(state, action))
    while True:
        # compute the new values (newV) given the old values
        newV = {}
        pi =[]
        for state in mdp.states():
            if mdp.inEnd(state):
                newV[state]=0.
                pi.append("End State")
            else:
                pi.append(max((Q(state, action), action) for action in mdp.actions(state))[1])
                newV[state]=max(Q(state, action) for action in mdp.actions(state))
        #check for convergence
        if max(abs(V[state]-newV[state]) for state in mdp.states()) < 1e-10:
            break
        V = newV

        # print stuff out
        print('{:15} {:15} {:15}'.format('s', 'V(s)', 'pi(s)'))
        for state in mdp.states():
            print('{:} {:>17.2f} {:>15}'.format(state, V[state], pi[state-1]))
        print()
    return pi,V












def agentQuiz(pi):
    print("welcome to the trivia quiz!")
    #time.sleep(1)
    pairs, correctAnswers, probs = getQuestionsAndAnswersAndProbs()
    arange_probs = reArangeProbs(correctAnswers, probs)
    potentialRewards =(1, 5, 10, 50, 100, 500, 1000, 5000, 10000, 15000)
    reward=0


    for i in range(len(pairs)):
        printQuestionsAndAnswers(pairs[i][0], pairs[i][1])
        chosenAnswer = choice(pairs[i][1], 1, p=arange_probs[i])
        #time.sleep(4)
        print("the chosen answer is: "+chosenAnswer[0])
        #time.sleep(3)
        if(chosenAnswer[0]==pairs[i][1][int(correctAnswers[i])-1]):#the agent was right
            reward += potentialRewards[i]
            print("you are correct !!!")
            print("Your score is : " + str(reward))
         #   time.sleep(4)
            print("\nDo you want to keep playing ?")
            #time.sleep(4)
            if(pi[i] == 'stay'):
                print("Yes, i want to keep playing\n")
          #      time.sleep(4)
            else:
                print("No, I want to quit")
           #     time.sleep(4)
                print("Congratulation You win:  " + str(reward) + "$")
                break
        else:

            print("You Wrong !\nGame Over!")
            break







def printQuestionsAndAnswers(question, answers):
    print("\n\n"+question)
    print("1.{}\n2.{}\n3.{}".format(answers[0],answers[1],answers[2]))
    print("choose 1-3\n")



def getQuestionsAndAnswersAndProbs():
    pairs = []
    correctAnswers = []
    probs = [0.99, 0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1]
    #1
    question ="What does www stand for in a website browser?"
    answeres=("World Wide Web", "world war wide", "wide world web")
    correctAnswers.append("1")
    pairs.append((question,answeres))
    #2
    question = "How long is an Olympic swimming pool (in meters)?"
    answeres = ("30", "50", "60")
    correctAnswers.append("2")
    pairs.append((question, answeres))
    #3
    question = "What geometric shape is generally used for stop signs?"
    answeres = ("triangle", "Octagon", "circle")
    correctAnswers.append("2")
    pairs.append((question, answeres))
    #4
    question = "How many languages are written from right to left?"
    answeres = ("12", "30", "5")
    correctAnswers.append("1")
    pairs.append((question, answeres))
    #5
    question = "What does the 'from ____ import' command do?"
    answeres = ("Import an image", "Import text", "Import a module")
    correctAnswers.append("3")
    pairs.append((question, answeres))
    #6
    question = "What is the name of the biggest technology company in South Korea?"
    answeres = ("Sony", "Lg", "Samsung")
    correctAnswers.append("3")
    pairs.append((question, answeres))
    #7
    question = "Which animal can be seen on the Porsche logo?"
    answeres = ("Bull", "Elephant", "Horse")
    correctAnswers.append("3")
    pairs.append((question, answeres))
    #8
    question = "Who was the first woman to win a Nobel Prize (in 1903)?"
    answeres = ("Marie Curie", "Toni Morrison", "Shirin Ebadi")
    correctAnswers.append("1")
    pairs.append((question, answeres))
    #9
    question = "What is cynophobia ?"
    answeres = ("Fear of dogs", "Fear of falling", "Fear of spiders")
    correctAnswers.append("1")
    pairs.append((question, answeres))
    #10
    question = "Who was the first woman pilot to fly solo across the Atlantic?"
    answeres = ("Toni Morrison", "Amelia Earhart", "Harriet Quimby")
    correctAnswers.append("2")
    pairs.append((question, answeres))



    return pairs, correctAnswers, probs




def reArangeProbs(correctAnswers, probs):
    newProbs=[]
    for i in range(len(correctAnswers)):
        if correctAnswers[i] == '1':
            newProbs.append((probs[i], (1-probs[i])/2, (1-probs[i])/2))
        elif correctAnswers[i] == '2':
            newProbs.append((((1-probs[i])/2), probs[i], (1-probs[i])/2))
        elif correctAnswers[i] == '3':
            newProbs.append((((1-probs[i])/2), (1-probs[i])/2, probs[i]))
    return newProbs


mdp = TriviaMdp (N=11)
pi, V = valueIteration(mdp)
count =0
while(1):
   count+=1
   agentQuiz(pi)
print()