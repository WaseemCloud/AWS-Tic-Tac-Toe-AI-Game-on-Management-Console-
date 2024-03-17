# Tic-Tac-Toe AI Game on AWS 🚀☁️

In this tutorial, I will be deploying a Tic-Tac-Toe board game and host it on AWS. This game will be 100% serverless, benefiting from all the serverless services that are available on AWS such as Lambda Function, API Gateway. The game logic will be implemented using the popular AI Algorithm "MiniMax Algorithm" which is widely used in developing games.

--------------------------------------------------
# MiniMax Algorithm: 🧠
--------------------------------------------------
The MiniMax algorithm is a decision-making algorithm commonly used in two-player zero-sum games, such as chess, checkers, or tic-tac-toe. Its main objective is to determine the optimal move for a player by considering all possible moves and their potential outcomes.

Here's a brief explanation of how the MiniMax algorithm works:

1) Tree Representation: The algorithm constructs a game tree where each level represents a player's turn, and each node represents a possible game state after a player's move.

2) Evaluation Function: At the leaf nodes (terminal states) of the tree, the algorithm evaluates the game state using an evaluation function. This function assigns a score to the state, indicating how favorable it is for the player whose turn it is.

3) Minimization and Maximization: The algorithm alternates between two types of nodes:

- Max Nodes: Represent the player's turn to maximize their score. The algorithm selects the move with the highest score.
- Min Nodes: Represent the opponent's turn to minimize the player's score. The algorithm selects the move with the lowest score.

4) Backtracking: The algorithm recursively explores the game tree until a certain depth or until reaching terminal states. Then, it backtracks, propagating the scores upward from the leaf nodes to the root of the tree.

5) Optimal Move Selection: Once the entire tree is evaluated, the algorithm selects the move that leads to the best outcome for the player, assuming the opponent also plays optimally.


--------------------------------------------------
# AWS Architecture:
--------------------------------------------------
![arch](https://github.com/WaseemCloud/Tic-Tac-Toe-AI-Game-on-AWS-Management-Console-/assets/157589909/f3f55289-9319-4f9e-91ee-d78f229fd114)

--------------------------------------------------
# Description:
--------------------------------------------------
We will be hosting our static webpage, which represents our game board, on S3 Bucket. We will also create an API Gateway which will be invoking and allowing the communication between the game board and Lambda function, which will be the brain of our game, as the MiniMax logic will be laying in it.

--------------------------------------------------
# Repository Structure:
--------------------------------------------------
In the repository, you can find the following files:
- lambda_function.py file: This python code needs to be configured in lambda function, as it contains the MiniMax logic for the game play.
- ./webappfile/index.html: This is our front-end web page which represents the board game and all the actions will be reflected on it on realtime.
- ./webappfile/styles.css: Adding some styling to the front-end.
- ./webappfile/script.js: Javascript file which will be handling the game scenarios and will be communicating with the API Gateway back and forth in order to update the state of the game board.


--------------------------------------------------
# Deoployment:
--------------------------------------------------
# 1) Lambda Function:
--------------------------------------------------
Let's start first with our lambda function.

- Go to your Management Console, and search for "Lambda":
![Screen Shot 2024-03-17 at 3 29 02 PM](https://github.com/WaseemCloud/Tic-Tac-Toe-AI-Game-on-AWS-Management-Console-/assets/157589909/cf16dee3-c0b1-4a34-92d6-92a160d9c3c8)

- Click on "Create a function":
![Screen Shot 2024-03-17 at 3 33 27 PM](https://github.com/WaseemCloud/Tic-Tac-Toe-AI-Game-on-AWS-Management-Console-/assets/157589909/4aae0333-cdf0-4988-a708-605c8a51253d)














