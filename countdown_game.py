import time
import random

def countdown_timer(seconds):
    print(f"\nCountdown starting from {seconds}...")
    print("Press Ctrl+C to stop early\n")
    
    try:
        for i in range(seconds, -1, -1):
            print(f"\rTime remaining: {i:3d} seconds", end="", flush=True)
            time.sleep(1)
        print("\n\nTime's up!")
    except KeyboardInterrupt:
        print("\n\nCountdown stopped early!")

def guess_countdown_game():
    target = random.randint(5, 15)
    print(f"\nGuess the Countdown Game!")
    print("I will countdown from a random number.")
    print("Try to guess when it will reach 0!\n")
    
    guess = input(f"Guess the starting number (between 5 and 15): ")
    
    try:
        user_guess = int(guess)
        print(f"\nStarting countdown from {target}...")
        
        for i in range(target, -1, -1):
            print(f"\r{i:3d}", end="", flush=True)
            time.sleep(0.5)
        
        print("\n\nCountdown finished!")
        
        if user_guess == target:
            print("Congratulations! You guessed correctly!")
        else:
            print(f"Wrong! The number was {target}, not {user_guess}.")
    except ValueError:
        print("Please enter a valid number!")

def stop_at_zero_game():
    print("\nStop at Zero Game!")
    print("Watch the countdown and try to press Enter when it hits 0!")
    print("Press Enter to start...")
    input()
    
    start = random.randint(10, 20)
    print(f"\nCountdown from {start}...")
    
    start_time = time.time()
    
    for i in range(start, -1, -1):
        print(f"\r{i:3d}", end="", flush=True)
        time.sleep(0.3)
    
    print("\n\nNOW! Press Enter as fast as you can!")
    
    try:
        input()
        end_time = time.time()
        reaction_time = end_time - start_time
        
        if reaction_time < 0.5:
            print(f"Amazing! Reaction time: {reaction_time:.3f} seconds")
        elif reaction_time < 1.0:
            print(f"Good! Reaction time: {reaction_time:.3f} seconds")
        else:
            print(f"Reaction time: {reaction_time:.3f} seconds")
    except:
        pass

def main():
    print("=" * 50)
    print("     SIMPLE COUNTDOWN GAME")
    print("=" * 50)
    
    while True:
        print("\nChoose a game:")
        print("1. Simple Countdown Timer")
        print("2. Guess the Countdown")
        print("3. Stop at Zero Challenge")
        print("4. Quit")
        
        choice = input("\nEnter your choice (1-4): ").strip()
        
        if choice == "1":
            try:
                seconds = int(input("Enter countdown seconds: "))
                if seconds > 0:
                    countdown_timer(seconds)
                else:
                    print("Please enter a positive number!")
            except ValueError:
                print("Please enter a valid number!")
        
        elif choice == "2":
            guess_countdown_game()
        
        elif choice == "3":
            stop_at_zero_game()
        
        elif choice == "4":
            print("\nThanks for playing!")
            break
        
        else:
            print("Invalid choice! Please enter 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()
