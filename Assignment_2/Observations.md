# Assignment 2

## FrozenLake-v1 : Random Agent Baseline

The random agent selects actions uniformly at random and does not learn from past experience. Because FrozenLake is a stochastic and slippery environment, random movement frequently leads the agent into holes, causing episodes to terminate early. As a result, the random agent demonstrates a very low success rate of **1.400%** and an average episode length of **7.898 steps**, indicating that it fails quickly and rarely reaches the goal.

---

## FrozenLake-v1 : Q-Learning Agent

In contrast, the Q-learning agent gradually learns an optimal policy using the Bellman equation and updates its Q-values through repeated interaction with the environment. Over **20,000 training episodes**, the agent steadily improves its policy, ultimately achieving a **training success rate of 40.11%** with an average of **29.598 steps per episode**.

After training, the policy is evaluated separately without exploration, where the agent demonstrates strong generalization, achieving an **evaluation success rate of 71.0%** and an average of **45.14 steps per episode**.

Compared to the random agent— which fails almost all the time and ends episodes quickly due to falling into holes — the Q-learning agent not only survives longer but also navigates intentionally toward the goal. The longer episode duration reflects meaningful decision-making rather than random drifting, highlighting the effectiveness of learned behavior.

---

## FrozenLake-v1 : Hyperparameter Sensitivity Analysis

To understand how learning performance changes with different configurations, we systematically varied the Q-learning agent’s key hyperparameters: **learning rate (α)**, **discount factor (γ)**, and **exploration rate (ε)**. For each hyperparameter combination, the agent was trained over multiple runs, and we compared the average episode length and success rate.

### Key Observations

- **Learning rate (α):**
  - Very low values (e.g., 0.01) caused extremely slow learning.
  - Very high values (α = 1.0) caused unstable updates on the slippery surface.
  - Moderate values (α ≈ 0.1–0.5) gave smoother and faster convergence.

- **Discount factor (γ):**
  - Small γ led to short-sighted behavior.
  - Larger γ values (0.9–0.99) significantly improved performance by encouraging long-term planning.

- **Exploration rate (ε):**
  - Very high ε caused excessive randomness.
  - Very low ε prevented the agent from exploring enough.
  - A moderate ε = 0.1 provided the best balance.

Overall, the analysis shows that FrozenLake is highly sensitive to hyperparameter choices. Optimal performance emerges only when **α**, **γ**, and **ε** are tuned together rather than adjusted independently.

---

## **Table 1: Comparing Random Agent and Q-Learning Agent for the Frozen Lake Problem**

| **Metric**                                | **Random Agent** | **Q-Learning Agent** |
|-------------------------------------------|------------------|-----------------------|
| Training Success Rate                     | 1.40%            | 40.11%                |
| Evaluation Success Rate                   | 0.299%           | 71.0%                 |
| Avg. Steps per Episode (Training)         | 7.898            | 29.598                |
| Avg. Steps per Episode (Evaluation)       | 6.34             | 45.14                 |

---

## **Table 2: Best Hyperparameters**

| **Hyperparameter**         | **Best Value** |
|----------------------------|----------------|
| α (Learning Rate)          | 1.0            |
| γ (Discount Factor)        | 0.99           |
| ε (Exploration Rate)       | 0.1            |

---


