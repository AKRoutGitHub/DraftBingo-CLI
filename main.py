import random
import time

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
start_ultimate_bingo()