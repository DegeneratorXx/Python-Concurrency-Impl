# Python Concurrency Tutorial 



## Threading

### 1. Basic Threading Concepts
- **Single Thread Creation**: Creating and starting individual threads
- **Daemon Threads**: Understanding daemon vs non-daemon threads
- **Multiple Threads**: Managing multiple threads manually
- **Thread Joining**: Waiting for threads to complete

### 2. ThreadPoolExecutor (Recommended Approach)
- **Basic Usage**: Using `concurrent.futures.ThreadPoolExecutor`
- **Submit Method**: Individual task submission with `executor.submit()`
- **Map Method**: Batch processing with `executor.map()`
- **Context Management**: Using `with` statements for automatic cleanup

### 3. Performance Comparisons
- **Sequential vs Concurrent**: Clear timing comparisons
- **Real-world Benchmarks**: Actual performance measurements
- **Threading Benefits**: Understanding when threading helps

### 4. Practical Real-World Example
- **Image Downloads**: Downloading multiple images concurrently
- **Network I/O**: Demonstrating threading benefits for I/O-bound tasks
- **Error Handling**: Proper exception handling in threaded code

## Key Examples

### Basic Threading
```python
import threading
import time

def worker_function(name):
    print(f"Thread {name}: starting")
    time.sleep(2)
    print(f"Thread {name}: finishing")

# Create and start thread
thread = threading.Thread(target=worker_function, args=(1,))
thread.start()
thread.join()  # Wait for completion
```

### ThreadPoolExecutor (Modern Approach)
```python
import concurrent.futures

with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
    # Method 1: Submit individual tasks
    future1 = executor.submit(worker_function, 1)
    future2 = executor.submit(worker_function, 2)
    
    # Method 2: Map over multiple inputs (cleaner)
    results = executor.map(worker_function, range(3))
```

### Performance Comparison Results
| Approach | Time (10 tasks, 1.5s each) |
|----------|----------------------------|
| Sequential | ~15 seconds |
| Threaded | ~1.5 seconds |
| **Speed Up** | **~10x faster!** |

## Project Structure

```
Thread.ipynb
├── Basic Threading Concepts
│   ├── Single Thread
│   ├── Daemon Threads
│   └── Multiple Threads
├── ThreadPoolExecutor Examples
│   ├── Submit Method
│   ├── Map Method
│   └── As Completed
├── Performance Benchmarks
│   ├── Sequential vs Threaded
│   └── Timing Comparisons
└── Real-World Example
    ├── Image Downloads
    ├── Sequential Downloads
    ├── Threaded Downloads
    └── Performance Analysis
```

## 🛠️ Prerequisites

### Required Packages
```bash
pip install requests  # For image download examples
```

### Python Version
- Python 3.7+ (tested with Python 3.10.13)

##  Key Learning Outcomes

After working through this notebook, you'll understand:

1. **When to use threading**: I/O-bound tasks (file downloads, API calls, database queries)
2. **When NOT to use threading**: CPU-bound tasks (due to Python's GIL)
3. **Modern threading patterns**: Using `ThreadPoolExecutor` over manual thread management
4. **Performance benefits**: Real timing comparisons showing 3-10x speed improvements
5. **Best practices**: Context managers, error handling, and resource cleanup


## 📊 Performance Highlights

### Image Download Comparison
- **Sequential**: Downloads images one by one
  - 10 images: ~20-30 seconds
- **Threaded**: Downloads images concurrently  
  - 10 images: ~5-8 seconds
  - **Result**: 3-5x speed improvement!

### Threading vs Sequential (10 tasks, 1 second each)
```
Sequential: 10.0 seconds  ████████████████████
Threaded:    1.0 seconds  ██
```

##  Advanced Concepts Covered

- **Context Managers**: Using `with` statements for resource management
- **Future Objects**: Understanding asynchronous result handling
- **Exception Handling**: Proper error handling in concurrent code
- **Resource Cleanup**: Automatic thread pool shutdown
- **Performance Measurement**: Using `time.perf_counter()` for accurate timing

##  Best Practices Demonstrated

1. **Use ThreadPoolExecutor** over manual thread management
2. **Context managers** (`with` statements) for automatic cleanup
3. **Proper exception handling** in threaded code
4. **Performance measurement** for quantifying improvements
5. **Real-world examples** over toy problems


##  Notes

- Threading is perfect for **I/O-bound tasks** (network requests, file operations)
- **Not ideal for CPU-bound tasks** due to Python's Global Interpreter Lock (GIL)
- Always use **context managers** (`with` statements) for resource management
- **ThreadPoolExecutor** is the modern, recommended approach over manual threading

## Asyncio

### 1. Basic Asyncio Concepts
- **Async Functions**: Defining functions with `async def`
- **Await Keyword**: Waiting for asynchronous operations
- **Coroutines**: Working with coroutine objects

### 2. Asyncio Execution Patterns
- **Sequential Async**: Running async functions one after another
- **Tasks**: Creating and managing tasks with `asyncio.create_task()`
- **Gather**: Using `asyncio.gather()` for concurrent execution
- **Task Groups**: Modern approach with built-in exception handling

### 3. Synchronization Primitives
- **Locks**: Preventing race conditions with `asyncio.Lock()`
- **Semaphores**: Controlling access to limited resources
- **Events**: Coordination between coroutines
- **Futures**: Low-level result objects

### 4. Advanced Concepts
- **Race Conditions**: Understanding and preventing concurrent access issues
- **Resource Management**: Proper cleanup and error handling

## Threading vs Asyncio Comparison

| Aspect | Threading | Asyncio |
|--------|-----------|---------|
| **Best For** | I/O-bound tasks with blocking calls | I/O-bound tasks with async libraries |
| **Memory Usage** | Higher (each thread ~8MB) | Lower (single thread) |
| **Debugging** | More complex (race conditions) | Easier (single-threaded) |
| **Learning Curve** | Moderate | Steeper (async/await syntax) |

## Project Structure

```
Threading & Asyncio Examples
├── Threading Examples
│   ├── Basic Threading Concepts
│   ├── ThreadPoolExecutor Examples
│   ├── Performance Benchmarks
│   └── Real-World Examples
└── Asyncio Basics
    ├── 1_await_n_async.py - Basic async/await
    ├── 2.py - Sequential async execution
    ├── 3_tasks.py - Creating and managing tasks
    ├── 4_gather.py - Concurrent execution with gather
    ├── 5_task_groups.py - Modern task groups
    ├── 6_futures.py - Low-level future objects
    ├── 7_lock.py - Preventing race conditions
    ├── 8_raceCondition.py - Demonstrating race conditions
    ├── 9_semaphores.py - Resource throttling
    └── 10_event.py - Coroutine coordination
```

## 🛠️ Prerequisites

### Required Packages
```bash
pip install requests      # For threading examples
# No additional packages needed for asyncio basics
```

### Python Version
- Python 3.7+ (tested with Python 3.10.13)
- asyncio is built into Python 3.7+

## Key Learning Outcomes

After working through these examples, you'll understand:

1. **Threading vs Asyncio**: When to use each approach
2. **Async/await syntax**: Modern Python asynchronous programming
3. **Concurrency patterns**: Tasks, gather, and task groups
4. **Synchronization**: Locks, semaphores, and events
5. **Race conditions**: How to identify and prevent them
6. **Performance benefits**: Real timing comparisons for both approaches

## 📊 Performance Highlights

### API Calls Comparison (10 requests, 1s delay each)
- **Sequential Sync**: Makes requests one by one
  - 10 requests: ~10 seconds
- **Threading**: Uses thread pool for concurrent requests
  - 10 requests: ~1 second
- **Asyncio**: Single-threaded concurrent execution
  - 10 requests: ~1 second
  - **Bonus**: Lower memory usage than threading!

### Memory Usage Comparison
```
Sequential:   ~20MB   ████
Threading:    ~100MB  ████████████████████
Asyncio:      ~25MB   █████
```

## When to Use What?

### Use Asyncio When:
- Building new applications with I/O-bound tasks
- Need to handle many concurrent operations
- Memory usage is a concern
- Want easier debugging (single-threaded)

### Use Threading When:
- Working with existing synchronous libraries
- Need to integrate with legacy code
- Blocking operations that can't be made async

## Notes

- **Asyncio is ideal for I/O-bound tasks** when using async libraries
- **Threading works with any library** but uses more memory
- **Both are ineffective for CPU-bound tasks** due to Python's GIL
- **Asyncio requires learning async/await syntax** but offers better scalability
- **Proper synchronization is crucial** for both approaches to avoid race conditions

## Key Learning Outcomes

After working through these notebooks, you'll understand:

1. **Threading vs Asyncio**: When to use each approach
2. **Async/await syntax**: Modern Python asynchronous programming
3. **Event loops**: How asyncio manages concurrent operations
4. **Performance benefits**: Real timing comparisons for both approaches
5. **Library ecosystem**: Threading works with any library, asyncio needs async libraries

## 📊 Performance Highlights

### API Calls Comparison (10 requests, 1s delay each)
- **Sequential Sync**: Makes requests one by one
  - 10 requests: ~10 seconds
- **Threading**: Uses thread pool for concurrent requests
  - 10 requests: ~1 second
- **Asyncio**: Single-threaded concurrent execution
  - 10 requests: ~1 second
  - **Bonus**: Lower memory usage than threading!

### Memory Usage Comparison
```
Sequential:   ~20MB   ████
Threading:    ~100MB  ████████████████████
Asyncio:      ~25MB   █████
```

## When to Use What?

### Use Asyncio When:
- Building new applications with I/O-bound tasks
- Working with async libraries (aiohttp, etc.)
- Memory usage is a concern

### Use Threading When:
- Working with existing synchronous libraries
- Need to integrate with legacy code
- Blocking operations that can't be made async

## Notes

- **Asyncio is ideal for I/O-bound tasks** with async library support
- **Threading works with any library** but uses more memory
- **Both are ineffective for CPU-bound tasks** due to Python's GIL
- **Always use async libraries** (aiohttp) with asyncio, not sync ones
- **Context managers are crucial** for both approaches
Asyncio:      ~25MB   █████
```

## Advanced Concepts Covered

### Threading Advanced Topics
- **Context Managers**: Using `with` statements for resource management
- **Future Objects**: Understanding asynchronous result handling
- **Exception Handling**: Proper error handling in concurrent code

### Asyncio Advanced Topics
- **Event Loop Management**: Custom event loops and policies
- **Async Context Managers**: Using `async with` statements
- **Semaphores**: Limiting concurrent operations
- **Queue Operations**: Producer-consumer patterns with asyncio queues
- **Exception Groups**: Handling multiple exceptions in concurrent code

## Best Practices Demonstrated

1. **Choose the right tool**:
   - Use **asyncio** for new projects with I/O-bound tasks
   - Use **threading** when working with existing sync libraries
2. **Resource management**: Always use context managers
3. **Error handling**: Proper exception handling in concurrent code
4. **Performance measurement**: Quantify improvements with timing
5. **Memory awareness**: Understand resource usage differences

## When to Use What?

### Use Asyncio When:
- Building new applications
- Working with async libraries (aiohttp, asyncpg, etc.)
- Need to handle thousands of concurrent operations
- Memory usage is a concern
- Debugging simplicity is important

### Use Threading When:
- Working with existing synchronous libraries
- Need to integrate with legacy code
- Blocking operations that can't be made async
- CPU-bound tasks (with ProcessPoolExecutor)

## Notes

- **Asyncio is ideal for I/O-bound tasks** with async library support
- **Threading works with any library** but uses more memory
- **Both are ineffective for CPU-bound tasks** due to Python's GIL
- **Asyncio has a steeper learning curve** but offers better scalability
- **Always use async libraries** (aiohttp, asyncpg) with asyncio, not sync ones
- **Context managers are crucial** for both approaches

