Number Guessing Game 🎯
A Python-based interactive number guessing game with statistical analysis and data tracking features.

🎮 Overview
This is an enhanced number guessing game where players attempt to guess a randomly generated number between 1 and 10. The game provides intelligent feedback and tracks detailed statistics using Python's statistics module to analyze player performance over multiple games.
✨ Features
Core Features

Interactive Gameplay: Continuous guessing with helpful feedback
Smart Feedback System: "Higher" or "Lower" hints for incorrect guesses
Statistical Analysis: Real-time calculation of mean, median, and mode
Multi-Game Sessions: Play multiple rounds with cumulative statistics
High Score Tracking: Display best performance across all games

Extra Features

Input Validation: Robust error handling for invalid inputs
Range Validation: Ensures guesses are within the valid 1-10 range
User-Friendly Interface: Clean formatting with emojis and clear sections
Graceful Exit: Proper handling of game termination

🔧 Requirements

Python 3.6+ (for f-string support)
Built-in modules:
random (for number generation)
statistics (for data analysis)

No external dependencies required!
📥 Installation

Clone or download the repository:
git clone <repository-url>
cd number-guessing-game

Ensure Python 3.6+ is installed:
python --version

Run the game:
python guessing_game.py

🎯 How to Play

Start the game by running the Python script
Read the welcome message and game instructions
Make your guess by entering a number between 1 and 10
Follow the feedback:
"It's higher!" - Your guess was too low
"It's lower!" - Your guess was too high

Continue guessing until you find the correct number
View your statistics after each game
Choose to play again or exit

Example Gameplay
🎯 WELCOME TO THE NUMBER GUESSING GAME! 🎯
I'm thinking of a number between 1 and 10.
Let's see how many tries it takes you to guess it!

🎲 New game started! Make your first guess:
Enter a number between 1-10: 5
📈 It's higher! Try again.
Enter a number between 1-10: 8
📉 It's lower! Try again.
Enter a number between 1-10: 7
🎉 Got it! Congratulations!
It took you 3 attempts.
🚀 Game Features
Input Validation

Non-numeric inputs: Handled with try/except blocks
Out-of-range numbers: Validates 1-10 range requirement
Invalid attempts: Don't count toward your score

Statistical Analysis
After each game, view:

Current game attempts
Total games played
Average attempts across all games
Median attempts (middle value)
Mode attempts (most common score)

High Score System

Tracks your best performance (fewest attempts)
Displays current high score at the start of each new game
Motivates improvement across multiple sessions

⚠️ Error Handling
The game handles various error conditions:

Error Type
Handling Method
User Impact

Non-numeric input
ValueError exception
Friendly error message, retry

Out-of-range guess
Conditional validation
Range reminder, retry

Statistics calculation
StatisticsError exception
Graceful mode handling

Keyboard interrupt
KeyboardInterrupt
Clean exit message

📊 Statistics Tracking
The game uses Python's statistics module to provide:

Mean: Average number of attempts across all games
Median: Middle value when attempts are sorted
Mode: Most frequently occurring number of attempts
High Score: Best (lowest) attempt count

Example Statistics Output
📊 GAME STATISTICS
==============================
Attempts this game: 4
Games played: 5
Average attempts: 3.60
Median attempts: 4.0
Mode of attempts: 3
🎨 Customization
Easy modifications you can make:

# Change number range

MIN_NUMBER = 1 # Lower bound
MAX_NUMBER = 100 # Upper bound

# Modify difficulty

winning_number = random.randint(MIN_NUMBER, MAX_NUMBER)
🤝 Contributing
Contributions are welcome! Here are some ideas for enhancements:

Difficulty levels (different number ranges)
Hint system (show remaining possible numbers)
Timer functionality (speed challenges)
Save game history to file
Multiplayer mode
GUI interface with tkinter

📄 License
This project is open source and available under the MIT License.
🏆 Project Requirements Met
✅ Core Requirements

Random number generation
Continuous guess prompting  
Higher/lower feedback
Statistics calculation (mean, median, mode)
Play again functionality
Error handling

✅ Extra Credit

Out-of-range feedback
High score display
f-string formatting throughout

Happy Gaming! 🎮
Built with Python 3.6+ • No external dependencies • Beginner-friendly
