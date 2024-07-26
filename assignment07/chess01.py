import time

def synchronous_chess_exhibition():
    num_opponents = 24
    judit_move_time = 5 # seconds
    opponent_move_time = 55 # seconds
    num_moves = 30 # pair-moves (60 moves total)
    
    total_time_per_game = (judit_move_time + opponent_move_time) * num_moves
    total_time_exhibition = total_time_per_game * num_opponents
    
    print(f"Total time for each game: {total_time_per_game / 60} minutes")
    print(f"Total time for the entire exhibition: {total_time_exhibition / 3600} hours")

# เรียกใช้ฟังก์ชัน
synchronous_chess_exhibition()
