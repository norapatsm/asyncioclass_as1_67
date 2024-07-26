import asyncio
import time

async def judit_move():
    await asyncio.sleep(0.05) # Judit takes 5 seconds per move

async def opponent_move():
    await asyncio.sleep(0.55) # Opponent takes 55 seconds per move

async def play_game(game_id):
    num_moves = 30
    for move in range(num_moves):
        await judit_move()
        await opponent_move()
    print(f"Game {game_id} finished")

async def asynchronous_chess_exhibition_with_asyncio():
    num_opponents = 24
    tasks = []
    
    for i in range(1, num_opponents + 1):
        tasks.append(play_game(i))
    
    await asyncio.gather(*tasks)

# เรียกใช้ฟังก์ชัน
start_time = time.time()
asyncio.run(asynchronous_chess_exhibition_with_asyncio())
end_time = time.time()

print(f"Total time for the entire exhibition: {(end_time - start_time) / 3600} hours")
