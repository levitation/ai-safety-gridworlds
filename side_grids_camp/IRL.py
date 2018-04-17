#Thanks to:
@misc{alger16,
  author       = {Matthew Alger},
  title        = {Inverse Reinforcement Learning},
  year         = 2016,
  doi          = {10.5281/zenodo.555999},
  url          = {https://doi.org/10.5281/zenodo.555999}
}

import numpy as np

"""
# trajectories =  array of demonstration trajectories, each trajectory is an array of state action pairs
# Trajectories must all be same length?


# feature_matrix = array of feature vectors, each feature vector is associated with the state at that index


# transition_probabilities = probability of moving from one state to another given action, 1 for legal moves, 0 for illegal moves


# feature_expectations = sum feature vectors of every state visited in every demo trajectory, divide result by the number of trajectories, to get feature expectation (over all states) for an average demo trajectory?

# policy = 

"""


N_ACTIONS = 4
N_STATES = # TODO
LEARNING_RATE = 0.01
EPOCHS = 200
DISCOUNT = 0.01

irl = maxEntIRL(feature_matrix, trans_probs, trajectories)


# TODO methods to map from state to state index and back
# How are states represented here - location of agent and box? Hard to apply in complex envs. Feature array? Greyscale images?

def stateToInt(state):
    # TODO
    # Return int


def getExampleTrajectories():

    trajectories = []
    # TODO
    # (each state in traj is state action pair (state, action)
    # Could generate (take num, len, policy)or do by hand here
    return trajectories

def getFeatureMatrix(states, feature_vectors):

    feature_matrix = []
    # TODO
    # Each state has associated feature vector
    # for n in range (number of possible states)
        # append feature vector
    return feature_matrix


def getTransitionProbabilities(gridworld_environment):

    trans_probs = []
    # for each state
        # for each possible action
            # get state

    return trans_probs


def getFeatureExpectations(feature_matrix, trajectories):

    # feature_expectations = sum feature vectors of every state visited in every demo trajectory, divide result by the number of trajectories, to get feature expectation (over all states) for an average demo trajectory?

    feature_expectations = np.zeros(feature_matrix.shape[1])

    for trajectory in trajectories:
        for state, _, _ in trajectory:
            feature_expectations += feature_matrix[state]

    feature_expectations /= trajectories.shape[0]

    return feature_expectations


def getSVF(trajectories):
    # State visitiation frequencies

    svf = np.zeros(n_states)

        for trajectory in trajectories:
            for state, _, _ in trajectory:
                svf[state] += 1

        svf /= trajectories.shape[0]

    return svf


def getExpectedSVF(rewards, transition_probability, trajectories):
    # expected state visitation frequencies
    # policy = findPolicy(transition_probability, rewards)

    # Get initial state frequencies
    
    # initial_state_frequencies = np.zeros(N_STATES)
    # for each trajectory
        # get initial state of trajectory (trajectory[0][0], 1st element in 1st state in trajectory)
        # +1 to initial_state_frequencies at index of that state (so we get an array of frequencies of each state being the initial state)  
        
    # initial_state_probabilities = initial_state_frequencies/number of trajectories
    
    # (I guess initial_state_probabilities would look like this: [0,1,0,0,0,0...] because our agent always starts in same place? - BUT in dynamic envs with more objects could not be.
    
    # expected_svf = np.tile(initial_state_probabilities, (trajectories.shape[1], 1)).T
    
    # and then... 
    # for t in range(1, trajectories.shape[1])
        # set all except initial svf to 0
        # expected_svf[:,t] = 0
        # for each state1, action, state2 (3-loop)
           
            # the expected state vis freq for each state in each trajectory is the previous state vis freq * the probability of taking that action in that state * the probability of taking that action in the previous state leading to this state....??
            
            # expected_svf[state2, t] += expected_svf[state1, t-1] * policy[state1, action] * transition_probabilities[state1, action, state2]
            
            
    return expected_svf.sum(axis=1) # and return sum over all trajectories?



def findPolicy(transition_probabilities, rewards):

    # TODO

    # Find optimal policy

    # pull this out to irl method?
    value_function = getOptimalValueFunction(transition_probabilities,
                                             reward,
                                             discount_factor,
                                             conv_threshold)



def getOptimalValueFunction(transition_probabilities, reward, discount_factor,
                            conv_threshold):
    """Iterates over states s performing policy evaluation with the standard
    Bellman backup equation for current policy \pi:

    V(s) <- \sum_{a} \pi(a|s) * \sum_{s', r} p(s', r|s, a)[r + \gamma V(s')]

    where a is action, s is current state, s' is the next state, p is the
    transition measure and \gamma is the discount factor (see Sutton & Barto v2,
    page 75).

    Currently this code assumes deterministic transitions and a greedy policy,
    this could be relaxed by implementing other policy choices.

    Args:
        transition_probabilities: (n_states, n_actions, n_states) array
        reward: (n_states) array containing rewards for each state
        discount_factor: float in [0,1]
        conv_threshold: float setting convergence threshold

    Returns a vector of values of length n_states. The following code was used
    as a reference:
    https://github.com/krasheninnikov/max-causal-ent-irl/blob/master/value_iter_and_policy.py
    https://github.com/MatthewJA/Inverse-Reinforcement-Learning/blob/master/irl/maxent.py
    """

    n_states, n_actions, _ = transition_probabilities.shape
    val_func = np.copy(rewards) # initialise value at rewards

    diff = float("inf")
    while diff > threshold:
        V_prev = np.copy(V)

        Q = reward + gamma * np.dot(transition_probabilities, V_prev)
        V = np.amax(Q, axis=1)

        diff = np.amax(abs(V_prev - V))

    return V

def maxEntIRL(feature_matrix, trans_probs, trajectories):

    # TODO

    # Initialise weights = numpy.random.uniform(size=(num_of_states,))

    # Get feature matrix using all states and feature vectors

    # Get expert demo trajectories

    # Get feature expectations


    # for i in range EPOCHS
        # rewards = feature_matrix.dot(weights)

        # get expected svfs (state visitation frequencies)

        # rewards += learning_rate * (feature_expectations - (feature_matrix * expectedsvf))

    # return feature_matrix * rewards





    return rewards
