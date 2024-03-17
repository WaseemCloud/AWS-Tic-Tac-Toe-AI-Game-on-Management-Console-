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

- Give a name to your function, select your runtime as "python 3.12", and click on "":

![Screen Shot 2024-03-17 at 3 36 32 PM](https://github.com/WaseemCloud/Tic-Tac-Toe-AI-Game-on-AWS-Management-Console-/assets/157589909/41907d80-2717-43c5-a168-e85e5b4ad4c6)

![Screen Shot 2024-03-17 at 3 39 08 PM](https://github.com/WaseemCloud/Tic-Tac-Toe-AI-Game-on-AWS-Management-Console-/assets/157589909/752bb16f-2851-40df-8671-f8ce2e7b9661)

- Scroll down to your code section, and replace the existing default code with your "Lambda_function.py" code:

![Screen Shot 2024-03-17 at 3 40 35 PM](https://github.com/WaseemCloud/Tic-Tac-Toe-AI-Game-on-AWS-Management-Console-/assets/157589909/b1115763-4a12-4ad4-a254-1f5c577e92a6)

- Once you have successfully placed your code, click on "Deploy", so the Lambda Function gets deployed:

![Screen Shot 2024-03-17 at 3 43 29 PM](https://github.com/WaseemCloud/Tic-Tac-Toe-AI-Game-on-AWS-Management-Console-/assets/157589909/37484fbc-7fe6-4463-bab9-745c35ed936f)

Now, before we carry on with our deployment, we have to test our Lambda function to make sure that its logic works fine and most importantly, it is returning something. To illustrate this, the game logic will be going as the following, our javascript, will pass the current state of the board to the lambda function through an API Call. Lambda function, will evaluate the received state, check the availabilities, and determine the best move to be made. The best AI move will be returned as the index of the empty cell, which will be filled with the letter "O" by javascript to represent the AI turn. 

To test this, we will need to pass a JSON body to our lambda function, and you will need to click on "Test":

![Screen Shot 2024-03-17 at 3 50 14 PM](https://github.com/WaseemCloud/Tic-Tac-Toe-AI-Game-on-AWS-Management-Console-/assets/157589909/3ff2f28d-1577-407d-aa4e-ca2c2b6c27e1)

Clear the following JSON Body:

![Screen Shot 2024-03-17 at 3 52 15 PM](https://github.com/WaseemCloud/Tic-Tac-Toe-AI-Game-on-AWS-Management-Console-/assets/157589909/ede8ac3c-1fbe-4ad9-a81f-d835be09374b)

Place the following JSON body instead, which represents a dummy state for the game board:

           {
           "body": "{\"board\": [\"O\", \"X\", \" \", \" \", \"X\", \" \", \" \", \" \", \"O\"]}"
           }
  
Click on "Invoke":

![Screen Shot 2024-03-17 at 3 57 58 PM](https://github.com/WaseemCloud/Tic-Tac-Toe-AI-Game-on-AWS-Management-Console-/assets/157589909/10d02556-6434-40aa-86b6-dad6e88354c2)

From the following response, we can tell that the test was successful, and our lambda function did indeed return the desired next move which is represented by cell index no: "7":

![Screen Shot 2024-03-17 at 3 59 12 PM](https://github.com/WaseemCloud/Tic-Tac-Toe-AI-Game-on-AWS-Management-Console-/assets/157589909/100b06f5-91bf-453e-a9a1-f75d5eb5e2b1)

--------------------------------------------------
# 2) API Gateway:
--------------------------------------------------

Let's move on to our next component and create our API Gateway. Go to your search bar, and find "API Gateway":

![Screen Shot 2024-03-17 at 4 02 41 PM](https://github.com/WaseemCloud/Tic-Tac-Toe-AI-Game-on-AWS-Management-Console-/assets/157589909/74c8fc34-9d5d-40ac-9f02-5a5468363c06)

Scroll down and select "REST API":

![Screen Shot 2024-03-17 at 4 06 03 PM](https://github.com/WaseemCloud/Tic-Tac-Toe-AI-Game-on-AWS-Management-Console-/assets/157589909/c76557fd-6ba8-42df-9c1d-844da9d1a18a)

Give your API a name, and click on "Create API":

![Screen Shot 2024-03-17 at 4 07 34 PM](https://github.com/WaseemCloud/Tic-Tac-Toe-AI-Game-on-AWS-Management-Console-/assets/157589909/95ed0f65-51e4-4d64-b797-8a67babb2bc4)


























