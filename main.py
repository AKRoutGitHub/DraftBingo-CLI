import random
import time

def get_valid_int(prompt, min_val=None, choices=None):
    """Ensures the user enters a valid integer within specific constraints."""
    while True:
        try:
            value = int(input(prompt))
            if min_val is not None and value < min_val:
                print(f"  ⚠️ Error: Value must be at least {min_val}.")
                continue
            if choices is not None and value not in choices:
                print("  ⚠️ Error: That number is not in the available pool!")
                continue
            return value
        except ValueError:
            print("  ⚠️ Error: Please enter a whole number (digits only).")


def start_ultimate_bingo():
    # 1. Setup Phase
    try:
        num_players = int(input("Enter number of players: "))
        if num_players <= 0: return
        
        num_to_pick = int(input("How many numbers should each player pick? (Minimum 2): "))
        if num_to_pick < 2:
            print("Setting to minimum of 2.")
            num_to_pick = 2
    except ValueError:
        print("Invalid input. Please enter numbers only.")
        return

    # 2. Generate the Master Pool
    total_needed = num_players * num_to_pick
    # We create a pool slightly larger than the total picks to give options
    pool_size = total_needed + 5 
    master_pool = list(range(1, pool_size + 1))
    random.shuffle(master_pool)
    
    # Track which numbers are still available to be picked
    available_choices = master_pool.copy()
    players_data = {}

    # 3. Interactive & Unique Selection
    for i in range(num_players):
        name = input(f"\nEnter name for Player {i+1}: ")
        chosen_numbers = []
        
        print(f"--- {name}, it's your turn! ---")
        print(f"Available Numbers: {sorted(available_choices)}")
        
        while len(chosen_numbers) < num_to_pick:
            try:
                pick = int(input(f"Pick number ({len(chosen_numbers)+1}/{num_to_pick}): "))
                
                # Check if it's in the pool AND hasn't been taken by ANYONE yet
                if pick in available_choices:
                    chosen_numbers.append(pick)
                    available_choices.remove(pick) # Remove so others can't pick it
                    print(f"  Confirmed! {pick} is yours.")
                else:
                    print("  ❌ That number is either not in the pool or already taken by another player!")
            except ValueError:
                print("  Please enter a valid digit.")
        
        players_data[name] = {"ticket": chosen_numbers, "matches": 0}

    # 4. Final Review Before Drawing
    print("\n" + "="*40)
    print("FINAL TICKETS (No overlaps!)")
    for name, info in players_data.items():
        print(f"{name}: {info['ticket']}")
    print("="*40)
    input("\nPress Enter to begin the drawing...")

    # 5. The Drawing Loop
    draw_pile = master_pool.copy()
    random.shuffle(draw_pile)
    
    winner = None
    for drawn_num in draw_pile:
        print(f"\n>>> COMPUTER DRAWS: {drawn_num} <<<")
        print("Check your numbers... (3 seconds)")
        time.sleep(3)
        
        match_found = False
        for name, info in players_data.items():
            if drawn_num in info["ticket"]:
                info["matches"] += 1
                match_found = True
                #     print(f"  🎯 MATCH! {name} hit {drawn_num} (Score: {info['matches']}/2)")
                # ... inside the drawing loop after matches are checked ...
        
                print("-" * 20)
                print("  CURRENT STANDINGS  ")
                for p_name, p_info in players_data.items():
                    print(f"  {p_name}: {p_info['matches']}/2")
                print("-" * 20)
                
                # Win Condition: First to 2 matches
                if info["matches"] == 2:
                    winner = name

        if winner:
            break

    # 6. Game End
    print("\n" + "#"*30)
    input("Game Over! See winner of the game? (Press Enter)")
    print("#"*30)
    print(f"🏆 THE WINNER IS: {winner.upper()}! 🏆")

# Run the game
if __name__ == "__main__":
    start_ultimate_bingo()
# start_ultimate_bingo()

# import random
# import time

# # --- CONTRIBUTION 2: ROBUST VALIDATION FUNCTION ---
# def get_valid_int(prompt, min_val=None, choices=None):
#     """Ensures the user enters a valid integer within specific constraints."""
#     while True:
#         try:
#             value = int(input(prompt))
#             if min_val is not None and value < min_val:
#                 print(f"  ⚠️ Error: Value must be at least {min_val}.")
#                 continue
#             if choices is not None and value not in choices:
#                 print("  ⚠️ Error: That number is not in the available pool!")
#                 continue
#             return value
#         except ValueError:
#             print("  ⚠️ Error: Please enter a whole number (digits only).")

# def start_ultimate_bingo():
#     # 1. Setup Phase (Using Contribution 2)
#     print("--- Welcome to Ultimate Bingo Race ---")
#     num_players = get_valid_int("Enter number of players: ", min_val=1)
#     num_to_pick = get_valid_int("How many numbers should each player pick? (Min 2): ", min_val=2)

#     # 2. Generate the Master Pool
#     total_needed = num_players * num_to_pick
#     pool_size = total_needed + 5 
#     master_pool = list(range(1, pool_size + 1))
#     random.shuffle(master_pool)
    
#     available_choices = master_pool.copy()
#     players_data = {}

#     # 3. Interactive Selection (Using Contribution 2)
#     for i in range(num_players):
#         name = input(f"\nEnter name for Player {i+1}: ")
#         chosen_numbers = []
        
#         print(f"--- {name}, it's your turn! ---")
        
#         while len(chosen_numbers) < num_to_pick:
#             print(f"Available Numbers: {sorted(available_choices)}")
#             # We pass available_choices to ensure the player picks a valid, unique number
#             pick = get_valid_int(f"Pick number ({len(chosen_numbers)+1}/{num_to_pick}): ", choices=available_choices)
            
#             chosen_numbers.append(pick)
#             available_choices.remove(pick) 
#             print(f"  ✅ Confirmed! {pick} is yours.")
        
#         players_data[name] = {"ticket": chosen_numbers, "matches": 0}

#     # 4. Final Review
#     print("\n" + "="*40)
#     print("FINAL TICKETS (No overlaps!)")
#     for name, info in players_data.items():
#         print(f"{name}: {info['ticket']}")
#     print("="*40)
#     input("\nPress Enter to begin the drawing...")

#     # 5. The Drawing Loop (With Contribution 1: Standings)
#     draw_pile = master_pool.copy()
#     random.shuffle(draw_pile)
    
#     winner = None
#     for drawn_num in draw_pile:
#         print(f"\n>>> COMPUTER DRAWS: {drawn_num} <<<")
#         print("Check your numbers... (3 seconds)")
#         time.sleep(3)
        
#         match_found = False
#         for name, info in players_data.items():
#             if drawn_num in info["ticket"]:
#                 info["matches"] += 1
#                 match_found = True
#                 print(f"  🎯 MATCH! {name} hit {drawn_num}!")

#                 # Win Condition
#                 if info["matches"] == 2:
#                     winner = name

#         # Show standings after the check
#         print("-" * 25)
#         print("    CURRENT STANDINGS    ")
#         for p_name, p_info in players_data.items():
#             print(f"    {p_name}: {p_info['matches']}/2")
#         print("-" * 25)

#         if winner:
#             break

#     # 6. Game End
#     print("\n" + "#"*30)
#     input("Game Over! See winner of the game? (Press Enter)")
#     print("#"*30)
#     print(f"🏆 THE WINNER IS: {winner.upper()}! 🏆")

# if __name__ == "__main__":
#     start_ultimate_bingo()