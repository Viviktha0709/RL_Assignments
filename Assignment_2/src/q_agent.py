import numpy as np

class QAgent:
    def __init__(self, env, alpha, gamma):
        self.env = env
        self.q_table = np.zeros((env.observation_space.n, env.action_space.n))
        self.alpha = alpha
        self.gamma = gamma
        
    def get_action(self, state):
        return np.argmax(self.q_table[state])
    
    def update_parameters(self, state, action, reward, next_state):
        old_value = self.q_table[state, action]
        next_max = np.max(self.q_table[next_state])
        new_value = old_value + self.alpha * (reward + self.gamma * next_max - old_value)
        self.q_table[state, action] = new_value
