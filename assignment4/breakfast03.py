import asyncio
from time import time

# functionทำกาเเฟ
async def make_coffee():
    print("coffee: prepare ingredients")
    await asyncio.sleep(1)  # ใช้ asyncio.sleep เพื่อไม่ให้บล็อก event loop
    print("coffee: waiting...")
    await asyncio.sleep(5)
    print("coffee: ready")

#functionทำใข่
async def fry_eggs():
    print("eggs: prepare ingredients")
    await asyncio.sleep(1)  # ใช้ asyncio.sleep เพื่อไม่ให้บล็อก event loop
    print("eggs: frying...")
    await asyncio.sleep(3)
    print("eggs: ready")

# ประกาศให้ main เป็น async เพื่อให้สามารถใช้ await ได้
async def main():
    start = time()
    # ใช้ asyncio.gather เพื่อรันทั้งสองฟังก์ชันพร้อมกัน
    await asyncio.gather(
    make_coffee(),
    fry_eggs()
)
    print(f"breakfast is ready in {time() - start} seconds")

asyncio.run(main())