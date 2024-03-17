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

- Give a name to your function, select your runtime as "python 3.12", and click on "Create function":

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

We will need to create a "POST" method, to allow our front-end to pass the board state to the Lambda function when this API is invoked:

![Screen Shot 2024-03-17 at 4 09 22 PM](https://github.com/WaseemCloud/Tic-Tac-Toe-AI-Game-on-AWS-Management-Console-/assets/157589909/58e62586-0314-498e-8bd1-5d615439f8f1)

Select "POST" as a method type, make sure the integration type is "Lambda function", and ensure to link the proper lambda function from the dropdown box:

![Screen Shot 2024-03-17 at 4 11 19 PM](https://github.com/WaseemCloud/Tic-Tac-Toe-AI-Game-on-AWS-Management-Console-/assets/157589909/6d248d77-80f7-4a28-9c14-5091dc9d486f)

Click on the root resource directory, and make sure to enable "CORS":

![Screen Shot 2024-03-17 at 4 14 58 PM](https://github.com/WaseemCloud/Tic-Tac-Toe-AI-Game-on-AWS-Management-Console-/assets/157589909/40c26f41-74a7-4393-bb1e-0b023d8f5b66)

Make sure that "POST" is checked:

![Screen Shot 2024-03-17 at 4 18 56 PM](https://github.com/WaseemCloud/Tic-Tac-Toe-AI-Game-on-AWS-Management-Console-/assets/157589909/522eb218-6bc9-457e-8121-5849e9ba3943)

Click on "Deploy API":

![Screen Shot 2024-03-17 at 4 20 11 PM](https://github.com/WaseemCloud/Tic-Tac-Toe-AI-Game-on-AWS-Management-Console-/assets/157589909/14538b12-1c8d-4e50-b665-d49cd42fb04a)

Create a new Deployment Stage, and hit on "Deploy":

![Screen Shot 2024-03-17 at 4 21 52 PM](https://github.com/WaseemCloud/Tic-Tac-Toe-AI-Game-on-AWS-Management-Console-/assets/157589909/8ca093f5-1d09-4705-87e8-51d6eb87145e)

Now, your API should be ready to be invoked from your front-end app using the following Invoke link. Make sure you copy it somewhere safe, becaue you will need to update your Javascript code with it:

![Screen Shot 2024-03-17 at 4 24 01 PM](https://github.com/WaseemCloud/Tic-Tac-Toe-AI-Game-on-AWS-Management-Console-/assets/157589909/eece6f32-0cd4-411d-b814-a1795c74b861)

Before, we move on to our front-end, let's test our API exactly the same way we have tested our lambda function, to make sure that it is successfully communicating with our lambda function, and returning a response:

![Screen Shot 2024-03-17 at 4 28 34 PM](https://github.com/WaseemCloud/Tic-Tac-Toe-AI-Game-on-AWS-Management-Console-/assets/157589909/ff90cc7a-7df2-4da9-8deb-e1fc1008c702)

Pass the following JSON body, and hit on "Test":


           {
           "body": "{\"board\": [\"O\", \"X\", \" \", \" \", \"X\", \" \", \" \", \" \", \"O\"]}"
           }


![Screen Shot 2024-03-17 at 4 31 13 PM](https://github.com/WaseemCloud/Tic-Tac-Toe-AI-Game-on-AWS-Management-Console-/assets/157589909/84b19580-ea6f-418b-acbb-9981da78a3e1)

Sweet! It is working 😉 !

![Screen Shot 2024-03-17 at 4 32 23 PM](https://github.com/WaseemCloud/Tic-Tac-Toe-AI-Game-on-AWS-Management-Console-/assets/157589909/f2f45c26-e904-466c-abf3-d8b18bace398)

NOTE:
----
Make sure you update your javascript with your API Key before proceeding with the next step...


--------------------------------------------------
# 3) Hosting our front-end on S3 Bucket:
--------------------------------------------------

Let's create our S3 bucket, which will be hosting all our website files (index, css, js).

Search for "S3" in the search box:

![Screen Shot 2024-03-17 at 4 36 50 PM](https://github.com/WaseemCloud/Tic-Tac-Toe-AI-Game-on-AWS-Management-Console-/assets/157589909/0ab1c9b5-bb93-4ed4-8009-02f4c9deb16b)

Click on "Create bucket":

![Screen Shot 2024-03-17 at 4 38 58 PM](https://github.com/WaseemCloud/Tic-Tac-Toe-AI-Game-on-AWS-Management-Console-/assets/157589909/08c86125-f8b6-4218-a7a9-9b51771fef5b)

Give your bucket a name and make sure it is unique:

![Screen Shot 2024-03-17 at 4 40 19 PM](https://github.com/WaseemCloud/Tic-Tac-Toe-AI-Game-on-AWS-Management-Console-/assets/157589909/5f100800-65bd-4458-8492-f0ac5e05db98)

Since we want our lovely game to be publicly accessible, make sure to uncheck the "Block all public access" option:

![Screen Shot 2024-03-17 at 4 41 27 PM](https://github.com/WaseemCloud/Tic-Tac-Toe-AI-Game-on-AWS-Management-Console-/assets/157589909/e08c8a7d-442e-4d00-be89-ac2d0ca582eb)

leave everything as default, and click on "Create bucket":

![Screen Shot 2024-03-17 at 4 43 44 PM](https://github.com/WaseemCloud/Tic-Tac-Toe-AI-Game-on-AWS-Management-Console-/assets/157589909/0eb330d1-0880-4fd4-89a6-122aca3f118d)

Browse to your created bucket, and click on "Upload" to upload all our website files:

![Screen Shot 2024-03-17 at 4 45 13 PM](https://github.com/WaseemCloud/Tic-Tac-Toe-AI-Game-on-AWS-Management-Console-/assets/157589909/be9b563a-f88a-4ae0-bde1-3d35b02aa51f)


![Screen Shot 2024-03-17 at 4 47 22 PM](https://github.com/WaseemCloud/Tic-Tac-Toe-AI-Game-on-AWS-Management-Console-/assets/157589909/3f09108b-dc01-4357-ac86-838aad7a0082)

Click on "Upload":

![Screen Shot 2024-03-17 at 4 48 13 PM](https://github.com/WaseemCloud/Tic-Tac-Toe-AI-Game-on-AWS-Management-Console-/assets/157589909/557117fb-ca4e-44e1-b49d-21e5f52f8a86)

As soon as the upload is successful, click on "Properties" to enable the "Static website hosting" option:

![Screen Shot 2024-03-17 at 4 49 05 PM](https://github.com/WaseemCloud/Tic-Tac-Toe-AI-Game-on-AWS-Management-Console-/assets/157589909/dd9f9154-cac5-498d-bbfe-9ad5b5ca03ab)

Scroll to the very bottom, and click on "Edit":

![Screen Shot 2024-03-17 at 4 50 24 PM](https://github.com/WaseemCloud/Tic-Tac-Toe-AI-Game-on-AWS-Management-Console-/assets/157589909/e167d757-b112-4fbe-9092-e200282828bb)

Enable the option, and specify the name of your index file:

![Screen Shot 2024-03-17 at 4 51 52 PM](https://github.com/WaseemCloud/Tic-Tac-Toe-AI-Game-on-AWS-Management-Console-/assets/157589909/485b13e2-1e00-4c15-b7be-9091ef95e6ca)

Then, click on "Save changes":

![Screen Shot 2024-03-17 at 4 53 57 PM](https://github.com/WaseemCloud/Tic-Tac-Toe-AI-Game-on-AWS-Management-Console-/assets/157589909/1b6a9005-0fb0-4768-a753-06bc4dde0ecf)

Finally, we will need to attach an IAM Policy to this bucket, to allow access to it. Click on "Permissions" tab:

![Screen Shot 2024-03-17 at 4 55 10 PM](https://github.com/WaseemCloud/Tic-Tac-Toe-AI-Game-on-AWS-Management-Console-/assets/157589909/37fb0db7-c823-4dea-94aa-d6c2cad9b593)

Click on "Edit", to add your policy:

![Screen Shot 2024-03-17 at 4 56 56 PM](https://github.com/WaseemCloud/Tic-Tac-Toe-AI-Game-on-AWS-Management-Console-/assets/157589909/34858fe6-2767-4c5f-84b3-e46a7b31b158)

Copy, the following policy and paste it in the box, but make sure to replace the "BUCKET-ARN" with your correct ARN:


    {
    "Version":"2012-10-17",
    "Statement": [
        {
            "Sid":"AddPerm",
            "Effect":"Allow",
            "Principal":"*",
            "Action":"s3:GetObject",
            "Resource":"BUCKET-ARN/*"
        }
    ]
    }



![Screen Shot 2024-03-17 at 4 58 37 PM](https://github.com/WaseemCloud/Tic-Tac-Toe-AI-Game-on-AWS-Management-Console-/assets/157589909/215ea90f-546e-4065-8293-e6ee022c77e3)

Go back to your Bucket's properties, and find your web link !

![Screen Shot 2024-03-17 at 5 05 35 PM](https://github.com/WaseemCloud/Tic-Tac-Toe-AI-Game-on-AWS-Management-Console-/assets/157589909/be854592-8874-4365-892f-50a275285013)


![Screen Shot 2024-03-17 at 5 07 18 PM](https://github.com/WaseemCloud/Tic-Tac-Toe-AI-Game-on-AWS-Management-Console-/assets/157589909/8141f244-06a0-4e69-8ec4-c96ce6a2fbc4)

--------------------------------------------------

Now, it's time to play the GAME...!!

🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥



https://github.com/WaseemCloud/Tic-Tac-Toe-AI-Game-on-AWS-Management-Console-/assets/157589909/4437b303-9aef-4268-8772-d22b20665b7b


# Enjoy ... 😉


























