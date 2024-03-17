import json
from random import choice


def minimax(board, depth, is_maximizing):
    # Minimax algorithm for determining the AI move
    scores = {
        'X': -1,  # Human player's score
        'O': 1,  # AI player's score
        'tie': 0  # Score for a tie game
    }

    result = determine_winner(board)  # Call determine_winner to find out if there's a winner

    if result != None:  # Check if there's a win or tie
        return scores[result]

    if is_maximizing:
        best_score = -1000  # Initialize the best score for the maximizing player
        for move in get_available_moves(board):  # Iterate through available moves
            board[move] = 'O'  # The AI will make a move by setting one of the boxes to "O"
            score = minimax(board, depth + 1, False)  # Recursively call minimax for the next depth
            board[move] = ' '  # Undo the move, so it can try other moves and evaluate them
            best_score = max(score, best_score)  # Update the best score
        return best_score
    else:
        best_score = 1000  # Initialize the best score for the minimizing player
        for move in get_available_moves(board):  # Iterate through available moves
            board[move] = 'X'  # Make a move for the human player
            score = minimax(board, depth + 1, True)  # Recursively call minimax for the next depth
            board[move] = ' '  # Undo the move
            best_score = min(score, best_score)  # Update the best score
        return best_score

def get_available_moves(board):
    # Function to get available moves (empty cells) on the board
    return [i for i in range(9) if board[i] == ' ']

def determine_winner(board):
    # Function to determine the winner of the game
     # Function to determine the winner of the game
    winning_patterns = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
        [0, 4, 8], [2, 4, 6]  # diagonals
    ]

    for pattern in winning_patterns:
        if board[pattern[0]] == board[pattern[1]] == board[pattern[2]] != ' ':
            return board[pattern[0]]

    if ' ' not in board:
        return 'tie'

    return None


def get_ai_move(board):
    # Function to get the AI's move using the Minimax algorithm
    best_score = float('-inf')
    best_move = None

    for move in get_available_moves(board):
        board[move] = 'O'
        score = minimax(board, 0, False)
        board[move] = ' '

        if score > best_score:
            best_score = score
            best_move = move

    return best_move

def lambda_handler(event, context):
    # Handler function for Lambda
    request_body = json.loads(event['body'])
    board = request_body.get('board', [' '] * 9)

    ai_move = get_ai_move(board)

    response_body = {
        'ai_move': ai_move
    }

    response = {
        'statusCode': 200,
        'body': json.dumps(response_body)
    }

    return response