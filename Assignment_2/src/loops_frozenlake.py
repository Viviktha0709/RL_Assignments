import numpy as np
import random
from tqdm import tqdm

def train(agent, env, n_episodes, epsilon):
    timesteps_per_episode = []
    success_per_episode = []

    for ep in tqdm(range(n_episodes)):
        state, info = env.reset()
        done = False
        steps = 0
        reward = 0

        while not done:
            # epsilon greedy strategy
            if random.uniform(0, 1) < epsilon:
                action = env.action_space.sample()
            else:
                action = agent.get_action(state)

            next_state, reward, terminated, truncated, info = env.step(action)
            done = terminated or truncated

            agent.update_parameters(state, action, reward, next_state)

            state = next_state
            steps += 1

        timesteps_per_episode.append(steps)
        success_per_episode.append(1 if reward == 1 else 0)

    return timesteps_per_episode, success_per_episode


def train_many_runs(agent_class, env, alpha, gamma, n_episodes, epsilon, n_runs):
    all_timesteps = np.zeros((n_runs, n_episodes))
    all_success = np.zeros((n_runs, n_episodes))

    for run in range(n_runs):
        agent = agent_class(env, alpha, gamma)
        timesteps, success = train(agent, env, n_episodes, epsilon)

        all_timesteps[run] = timesteps
        all_success[run]  = success

    return all_timesteps.mean(axis=0), all_success.mean(axis=0)
