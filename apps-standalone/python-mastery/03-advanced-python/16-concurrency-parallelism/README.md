# Python Concurrency and Parallelism Demo

This comprehensive demonstration covers:

1. `threading` for I/O-bound tasks
2. `multiprocessing` for CPU-bound tasks
3. `asyncio` for highly concurrent I/O
4. `concurrent.futures` high-level interface

## Key Features Demonstrated

### Threading

- I/O-bound task handling
- Global Interpreter Lock (GIL) implications
- Shared memory model

### Multiprocessing

- CPU-bound task handling
- Separate memory spaces
- Bypassing the GIL

### Asyncio

- Async/await syntax
- Cooperative multitasking
- High-concurrency I/O

### Concurrent.futures

- Thread/process pool executors
- Future objects
- High-level abstraction

## How to Run

1. Execute the demo script:
   ```bash
   python main.py
   ```
2. Observe the output demonstrating:
   - Threading for I/O operations
   - Multiprocessing for CPU work
   - Asyncio for concurrent I/O
   - Futures interface
3. Experiment by modifying:
   - Task durations
   - Number of workers
   - Task types

## Troubleshooting

- For multiprocessing, ensure functions are defined at module level (not nested)
- Reduce input sizes if multiprocessing takes too long (demo uses 1M instead of 10M)

## Sample Output

```
=== PYTHON CONCURRENCY & PARALLELISM DEMO ===

=== THREADING DEMO (I/O-BOUND) ===
Thread 0: Starting I/O operation
Thread 1: Starting I/O operation
Thread 2: Starting I/O operation
Thread 1: Finished after 1 sec
Thread 0: Finished after 1 sec
Thread 2: Finished after 1 sec
Total time (threading): 1.01 sec

=== MULTIPROCESSING DEMO (CPU-BOUND) ===
Results: [333332833333500000, 333332833333500000, 333332833333500000]
Total time (multiprocessing): 0.13 sec

=== ASYNCIO DEMO (HIGH CONCURRENCY I/O) ===
Task 1: Starting async I/O
Task 2: Starting async I/O
Task 3: Starting async I/O
Task 1: Finished after 1 sec
Task 2: Finished after 1 sec
Task 3: Finished after 1 sec
Total time (asyncio): 1.00 sec

=== CONCURRENT.FUTURES DEMO ===
Thread results: [0, 1, 4]
Thread time: 1.01 sec
```

## Learning Outcomes

After completing this demo, you will understand:

- When to use each concurrency approach
- GIL implications and workarounds
- Performance characteristics
- Best practices for each method
