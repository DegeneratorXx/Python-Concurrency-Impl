# Python Concurrency Tutorial 



## Threading-

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

##  Key Examples

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

