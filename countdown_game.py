import time
import random
import sys


best_reaction = None


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
    print("\nGuess the Countdown Game!")
    print("I will pick a starting number — try to guess it!\n")
    target = random.randint(5, 25)  # slightly expanded range
    guess = input(f"Guess the starting number (between 5 and 25): ")
    try:
        user_guess = int(guess)
        print(f"\nStarting countdown from {target}...\n")
        for i in range(target, -1, -1):
            print(f"\r{i:3d}", end="", flush=True)
            time.sleep(0.5)
        print("\n\nCountdown finished!")
        if user_guess == target:
            print("🎉 Correct! Nice guess!")
        else:
            print(f"❌ Wrong — I counted from {target}, not {user_guess}.")
    except ValueError:
        print("⚠️ Invalid number entered!")


def stop_at_zero_game():
    global best_reaction

    print("\nStop at Zero Game!")
    print("Try to press Enter exactly as it hits 0!")
    input("Press Enter to start...")

    start = random.randint(10, 30)  # slightly extended range
    print(f"\nCountdown from {start}...\n")
    start_time = time.time()
    for i in range(start, -1, -1):
        print(f"\r{i:3d}", end="", flush=True)
        time.sleep(0.3)
    print()

    input("NOW! Press Enter!")
    end_time = time.time()

    reaction_time = end_time - start_time
    print(f"\n⏱ Reaction time: {reaction_time:.3f} seconds")

    # Update high score
    if best_reaction is None or reaction_time < best_reaction:
        best_reaction = reaction_time
        print("🔥 New high score!")

    if best_reaction is not None:
        print(f"🏆 Best reaction time: {best_reaction:.3f}s")


def main():
    while True:
        print("\n" + "=" * 40)
        print("     SIMPLE COUNTDOWN GAME MENU")
        print("=" * 40)
        print("1. Simple Countdown Timer")
        print("2. Guess the Countdown")
        print("3. Stop at Zero Challenge")
        print("4. Quit")

        choice = input("\nEnter your choice (1-4): ").strip()
        print()

        if choice == "1":
            try:
                seconds = int(input("Enter countdown seconds: "))
                if seconds > 0:
                    countdown_timer(seconds)
                else:
                    print("⚠️ Enter a positive number!")
            except ValueError:
                print("⚠️ Enter a valid number!")
        elif choice == "2":
            guess_countdown_game()
        elif choice == "3":
            stop_at_zero_game()
        elif choice == "4":
            print("\nThanks for playing! 👋")
            sys.exit(0)
        else:
            print("❌ Invalid choice — choose 1 to 4!")
        input("\nPress Enter to continue...")  # allow replay


if __name__ == "__main__":
    main()
