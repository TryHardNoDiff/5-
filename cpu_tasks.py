import time

def fib(n):
    return n if n <= 1 else fib(n - 1) + fib(n - 2)

def cpu_task(n):
    start = time.time()
    result = fib(n)
    print(f"Fib({n}) = {result} | Time: {time.time() - start:.2f}s")
    return result

def run_cpu_sequential():
    tasks = [30, 30, 30]
    start = time.time()
    for n in tasks:
        cpu_task(n)
    print(f"✅ Sequential CPU time: {time.time() - start:.2f}s\n")