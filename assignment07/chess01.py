import time

my_computer_time = 0.1  # Judit's move time in seconds
opponent_computer_time = 0.5  # Opponent's move time in seconds
move_pairs = 30  # Number of pair-moves (60 moves total)

def game():
    total_time = 0
    for move in range(1, move_pairs + 1):
        # Judit's move
        start_move_time = time.perf_counter()
        print(f"Move {move * 2 - 1}: Judit")
        time.sleep(my_computer_time)
        total_time += (time.perf_counter() - start_move_time)
        
        # Opponent's move
        start_move_time = time.perf_counter()
        print(f"Move {move * 2}: Opponent")
        time.sleep(opponent_computer_time)
        total_time += (time.perf_counter() - start_move_time)
    
    return total_time

if __name__ == "__main__":
    start_time = time.perf_counter()
    
    # Simulate one game
    game_time = game()
    
    total_game_time = game_time
    
    print(f"One game finished in {total_game_time:.2f} secs.")
    print(f"Estimated total time for all games: {total_game_time * 24:.2f} secs.")
