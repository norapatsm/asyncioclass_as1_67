import asyncio
import time

judit_move_time = 0.1  # Judit's move time in seconds
opponent_move_time = 0.5  # Opponent's move time in seconds
opponents = 24  # Number of opponents
move_pairs = 30  # Number of pair-moves (60 moves total)

async def game(game_number):
    for move in range(1, move_pairs + 1):
        # Judit's move
        print(f"Game {game_number}, Move {move * 2 - 1}: Judit")
        time.sleep(judit_move_time)
        
        # Opponent's move
        print(f"Game {game_number}, Move {move * 2}: Opponent")
        await asyncio.sleep(opponent_move_time)

async def async_io():
    start_time = time.perf_counter()

    # Create a task for each game
    tasks = [game(i) for i in range(1, opponents + 1)]
    await asyncio.gather(*tasks)

    total_time = round(time.perf_counter() - start_time, 2)
    print(f"Board exhibition finished in {total_time} secs.")

if __name__ == "__main__":
    asyncio.run(async_io())
