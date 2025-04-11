"""
Python Concurrency and Parallelism Demo

Covers:
1. threading (I/O-bound tasks)
2. multiprocessing (CPU-bound tasks)
3. asyncio (highly concurrent I/O)
4. concurrent.futures (high-level interface)
"""

import time
import threading

# import multiprocessing
import asyncio
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor


# Module-level function for multiprocessing
def cpu_bound_task(n):
    return sum(i * i for i in range(n))


# ========== THREADING (I/O-BOUND) ==========
def demonstrate_threading():
    """
    Shows threading for I/O-bound tasks.
    Note: Threads share memory but are limited by GIL for CPU-bound work.
    """
    print("\n=== THREADING DEMO (I/O-BOUND) ===")

    def io_bound_task(task_id, delay):
        print(f"Thread {task_id}: Starting I/O operation")
        time.sleep(delay)  # Simulate I/O wait
        print(f"Thread {task_id}: Finished after {delay} sec")

    threads = []
    start_time = time.time()

    for i in range(3):
        t = threading.Thread(target=io_bound_task, args=(i, 1))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print(f"Total time (threading): {time.time() - start_time:.2f} sec")


# ========== MULTIPROCESSING (CPU-BOUND) ==========
def demonstrate_multiprocessing():
    """
    Shows multiprocessing for CPU-bound tasks.
    Processes have separate memory and bypass GIL.
    """
    print("\n=== MULTIPROCESSING DEMO (CPU-BOUND) ===")

    start_time = time.time()

    with ProcessPoolExecutor() as executor:
        results = list(executor.map(cpu_bound_task, [1_000_000, 1_000_000, 1_000_000]))

    print(f"Results: {results}")
    print(f"Total time (multiprocessing): {time.time() - start_time:.2f} sec")


# ========== ASYNCIO (HIGH CONCURRENCY I/O) ==========
async def demonstrate_asyncio():
    """
    Shows asyncio for highly concurrent I/O-bound tasks.
    Uses cooperative multitasking with async/await.
    """
    print("\n=== ASYNCIO DEMO (HIGH CONCURRENCY I/O) ===")

    async def async_io_task(task_id, delay):
        print(f"Task {task_id}: Starting async I/O")
        await asyncio.sleep(delay)  # Non-blocking sleep
        print(f"Task {task_id}: Finished after {delay} sec")

    start_time = time.time()

    await asyncio.gather(async_io_task(1, 1), async_io_task(2, 1), async_io_task(3, 1))

    print(f"Total time (asyncio): {time.time() - start_time:.2f} sec")


# ========== CONCURRENT.FUTURES (HIGH-LEVEL) ==========
def demonstrate_futures():
    """
    Shows concurrent.futures high-level interface.
    Can use either threads or processes.
    """
    print("\n=== CONCURRENT.FUTURES DEMO ===")

    def task(n):
        time.sleep(1)  # Simulate work
        return n * n

    start_time = time.time()

    with ThreadPoolExecutor() as executor:
        futures = [executor.submit(task, i) for i in range(3)]
        results = [f.result() for f in futures]

    print(f"Thread results: {results}")
    print(f"Thread time: {time.time() - start_time:.2f} sec")


# ========== MAIN EXECUTION ==========
async def main():
    print("=== PYTHON CONCURRENCY & PARALLELISM DEMO ===")

    demonstrate_threading()
    demonstrate_multiprocessing()
    await demonstrate_asyncio()
    demonstrate_futures()

    print("\n=== DEMO COMPLETE ===")
    print("Key Takeaways:")
    print("- Use threading for I/O-bound tasks")
    print("- Use multiprocessing for CPU-bound tasks")
    print("- Use asyncio for high-concurrency I/O")
    print("- concurrent.futures provides high-level interface")


if __name__ == "__main__":
    asyncio.run(main())
