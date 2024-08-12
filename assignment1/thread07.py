# Using a ThreadPoolExecutor
import concurrent.futures
import logging
import time


def thread_function(name) :
    logging.info("Thread %s: sstarting", name)
    time.sleep(2)
    logging.info("Thread %s: finishing", name)


if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")

    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:#สร้าง ThreadPoolExecutor กำหนดจำนวนสูงสุดThreads ที่ทำงานพร้อมกัน
        executor.map(thread_function, range(3))

# โปรแกรมนี้จะสร้าง ThreadPoolExecutor ที่สามารถรัน Threads พร้อมกันได้สูงสุด 3 ตัว
# ฟังก์ชัน thread_function จะถูกเรียกใช้พร้อมกันด้วยค่า 0, 1, และ 2 โดยแต่ละการเรียกจะรันใน Thread แยกกัน
# โปรแกรมจะบันทึกข้อมูลว่าแต่ละ Thread เริ่มทำงานและเสร็จสิ้นการทำงานผ่าน logging
# การทำงานทั้งหมดจะถูกจัดการโดย ThreadPoolExecutor ซึ่งทำให้การจัดการหลาย Threads