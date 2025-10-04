![thumbnail.png](https://github.com/aldr4GO/SnakeGameAI/blob/main/thumbnail.png)

# 🐍 Reinforcement Learning Snake Game AI

Welcome to my Reinforcement Learning project! This repository demonstrates my hands-on journey with RL concepts by building an AI agent that learns to play the classic Snake game using Deep Q-Learning. 🚀

---

## 📚 What I Learned
- **Agent & Environment**: How an agent interacts with its environment and learns from feedback.
- **State, Action, Reward**: Defining the state space, possible actions, and designing a reward system.
- **Learning Parameters**: Tuning learning rate, discount factor, and exploration vs. exploitation.
- **Deep Q-Learning**: Implementing a neural network to approximate Q-values.
- **Training & Evaluation**: Visualizing training progress and evaluating the agent's performance.

---

## 🖥️ Project Structure
```
agent.py      # RL agent logic
model.py      # Neural network and Q-learning trainer
helper.py     # Plotting and visualization
summary.py    # Model summary and weights loading
game.py       # Snake game environment (Pygame)
arial.ttf     # Font for game display
```

---

## 📊 Results
- The agent learns to play Snake from scratch, improving its score over time.
- Training progress and scores are visualized live.
- Model weights are saved for future evaluation.

---

## 🚀 Run Locally

### 1. Clone the repository
```powershell
git clone https://github.com/aldr4GO/SnakeGameAI.git
cd "SnakeGameAI"
```

### 2. Install dependencies
Make sure you have Python 3.7+ installed. Then run:
```powershell
pip install torch pygame matplotlib torchinfo
```

### 3. Run the training
```powershell
python agent.py
```

### 4. Visualize the results
- Training plots will appear automatically.
- To see the model summary, run:
```powershell
python summary.py
```

---

## ✨ Screenshots
![ss1](https://github.com/user-attachments/assets/1b6c44cc-e9c0-4e3b-9192-349435594f78)


---

## 🤝 Contributing
Pull requests and suggestions are welcome! Feel free to fork and improve the project.

---

## 📬 Contact
For questions or feedback, open an issue or reach out via [LinkedIn](https://www.linkedin.com/in/tanishverma007/).

---

> **Made with ❤️ for learning Reinforcement Learning!**
