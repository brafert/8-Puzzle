# 8-Puzzle
Finds and displays the minimum number of moves required to reach the goal state of any solvable 8-Puzzle. 

## 8-Puzzle.py
This file contains code to solve valid 8-Puzzles using a choice of two heuristics.
On completion, it outputs the moves taken to reach a user-provided goal state from a user-provided start state.

### Requirements:
The PriorityQueue class from Python's [queue module](https://docs.python.org/3/library/queue.html).
No installation is required, the queue module is part of Python's standard library.

### How to run:
 1. Open a terminal.
 2. Navigate to the directory 8-Puzzle.py is located.
 3. Execute the Python file.
 
      On Windows:
	   `./8-Puzzle.py`
     
      On Mac:
	   `python3 ./8-Puzzle.py`

 4. Enter a start state. This must be an 8-Puzzle, at the moment, no other size will work. Any configuration can be used, as long as the state contains an even number of [inversions](https://www.cs.bham.ac.uk/~mdr/teaching/modules04/java2/TilesSolvability.html). The file `puzzle-config.txt` contains two start and goal states that can be copy and pasted into the terminal. Use the second pair for a quicker response time. If you wish to enter your own, follow the format of the states in the `puzzle-config.txt` file by leaving a space between the first and second, and second and third tiles in each row. Seperate the rows onto their own lines and use an underscore '_' to represent the blank space/tile. Please note, the more complex the start and goal states, the longer the program may take to run.
 5. Enter a goal state. Follow the format for entering a start state. 
 6. Choose a heuristic. Into the terminal, type '1' to use the sum of Manhattan distances of the tiles or '2' for the Hamming distance. You can only use one heuristic at a time. To use a different heuristic, rerun the program. Both are admissable heuristics, so both will return the same moves taken to solve the puzzle (Manhattan tends to be faster for complex puzzles). 
