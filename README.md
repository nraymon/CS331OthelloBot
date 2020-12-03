# CS331 4x4 Othello bot

### Description

The core logic of the Othello game was written by Erich Kramer and supplied to us by our instructor, but all the minimax logic was written by me.

This program uses the minimax algroithm with no alpha-beta pruning to play the game Othello on a 4x4 board. There is no limit on how far it iterates down a tree, so it keeps going until it finds an end state of that tree.

The AI can be either the min or max player depending on the order of the parameters given. Once the application has started running, a board will be presented on the screen asking for the next player's turn. The minimax bot will read the state of the board once it is its turn and since there is not iteration limit, it will go through every next move that can be made from the currently read in state and iterate through every possibility base on that move and so on and so forth until it has reached an end state. When that end state is reached, it will rank the move based on how many pieces each player has on the board. Those ranks being a 1 which is good for the max player and bad for the min player. A 0 which means it is a tie which is ok for either player and a -1 which is good for the min plaher and bad for the max player. Based on that ranking and the type of player it is, the bot will choose of the possible next moves from the board it originally read in.
