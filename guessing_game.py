"""
Data Analysis Techdegree
Project 1 - A Number Guessing Game
--------------------------------
"""

# Import the random and statistics modules.
import random
import statistics

def start_game():
	"""
	Main game function that handles the entire game loop,
	user interaction, and data analysis.
	"""
	# List to store all game attempts for statistical analysis
	attempts_history = []
	# Game configuration
	MIN_NUMBER = 1
	MAX_NUMBER = 10
	
	# Display welcome message
	print("=" * 50)
	print("🎯 WELCOME TO THE NUMBER GUESSING GAME! 🎯")
	print("=" * 50)
	print(f"I'm thinking of a number between {MIN_NUMBER} and {MAX_NUMBER}.")
	print("Let's see how many tries it takes you to guess it!")
	print()
	
	# Main game loop - continues until player decides to quit
	while True:
		# Display high score if available
		if attempts_history:
			high_score = min(attempts_history)
			print(f"🏆 Current High Score: {high_score} attempts")
			print()
		
		# Generate random winning number for this round
		winning_number = random.randint(MIN_NUMBER, MAX_NUMBER)
		current_attempts = 0
		
		print("🎲 New game started! Make your first guess:")
		
		# Inner loop for individual game rounds
		while True:
			try:
				# Get player's guess with input validation
				guess_input = input(f"Enter a number between {MIN_NUMBER}-{MAX_NUMBER}: ")
				guess = int(guess_input)
				
				# Check if guess is within valid range (Extra Credit requirement)
				if guess < MIN_NUMBER or guess > MAX_NUMBER:
					print(f"⚠️  Please enter a number between {MIN_NUMBER} and {MAX_NUMBER}!")
					continue  # Don't increment attempts for out-of-range guesses
				
				# Only increment attempts for valid guesses within range
				current_attempts += 1
				
				# Check if guess is correct
				if guess == winning_number:
					print("🎉 Got it! Congratulations!")
					print(f"It took you {current_attempts} attempts.")
					attempts_history.append(current_attempts)
					break
				# Provide feedback for incorrect guesses
				elif guess > winning_number:
					print("📉 It's lower! Try again.")
				else:
					print("📈 It's higher! Try again.")
					
			except ValueError:
				# Handle non-integer input errors - don't count as an attempt
				print("❌ Please enter a valid whole number!")
				continue
		
		# Display statistical analysis after each game
		print("\n" + "=" * 30)
		print("📊 GAME STATISTICS")
		print("=" * 30)
		print(f"Attempts this game: {current_attempts}")
		print(f"Games played: {len(attempts_history)}")
		print(f"Average attempts: {statistics.mean(attempts_history):.2f}")
		print(f"Median attempts: {statistics.median(attempts_history)}")
		
		# Handle mode calculation (can have multiple modes or no mode)
		try:
			mode_value = statistics.mode(attempts_history)
			print(f"Mode of attempts: {mode_value}")
		except statistics.StatisticsError:
			print("Mode of attempts: No single mode found")
		
		# Prompt player to continue or quit
		print("\n" + "-" * 30)
		while True:
			try:
				play_again = input("Would you like to play again? (yes/no): ").lower().strip()
				if play_again in ['yes', 'y']:
					print("\n" + "🔄 Starting new game...")
					print("-" * 30)
					break
				elif play_again in ['no', 'n']:
					# Display goodbye message and final statistics
					print("\n" + "=" * 40)
					print("👋 Thanks for playing!")
					print("=" * 40)
					if len(attempts_history) > 1:
						print("📈 Final Statistics:")
						print(f"   Total games played: {len(attempts_history)}")
						print(f"   Best score: {min(attempts_history)} attempts")
						print(f"   Average score: {statistics.mean(attempts_history):.2f} attempts")
					print("See you next time! 🎮")
					return
				else:
					print("Please enter 'yes' or 'no'.")
			except KeyboardInterrupt:
				print("\n\nGoodbye! Thanks for playing! 👋")
				return

# Kick off the program by calling the start_game function.
if __name__ == "__main__":
	start_game()
