import time
import asyncio
import requests
import concurrent.futures
import aiohttp

# === I/O-bound ===
def io_task(url):
    requests.get(url, timeout=5)

async def aio_task(session, url):
    async with session.get(url) as response:
        await response.text()

# === CPU-bound ===
def fib(n):
    return n if n <= 1 else fib(n-1) + fib(n-2)

def cpu_task(n):
    return fib(n)

# === Тесты ===
def test_sequential_io():
    urls = ["https://httpbin.org/delay/1"] * 3
    start = time.time()
    for url in urls:
        io_task(url)
    return time.time() - start

def test_threading_io():
    urls = ["https://httpbin.org/delay/1"] * 3
    start = time.time()
    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(io_task, urls)
    return time.time() - start

async def _test_asyncio_io():
    urls = ["https://httpbin.org/delay/1"] * 3
    async with aiohttp.ClientSession() as session:
        tasks = [aio_task(session, url) for url in urls]
        await asyncio.gather(*tasks)

def test_asyncio_io():
    start = time.time()
    asyncio.run(_test_asyncio_io())
    return time.time() - start

def test_sequential_cpu():
    tasks = [30] * 3
    start = time.time()
    for n in tasks:
        cpu_task(n)
    return time.time() - start

def test_multiprocessing_cpu():
    tasks = [30] * 3
    start = time.time()
    with concurrent.futures.ProcessPoolExecutor() as executor:
        list(executor.map(cpu_task, tasks))
    return time.time() - start

# === Запуск ===
if __name__ == "__main__":
    print("🚀 Тесты I/O-bound:")
    t1 = test_sequential_io()
    t2 = test_threading_io()
    t3 = test_asyncio_io()
    print(f"  Последовательно: {t1:.2f} с")
    print(f"  Многопоточность: {t2:.2f} с")
    print(f"  Асинхронность:   {t3:.2f} с")

    print("\n🔥 Тесты CPU-bound:")
    t4 = test_sequential_cpu()
    t5 = test_multiprocessing_cpu()
    print(f"  Последовательно: {t4:.2f} с")
    print(f"  Многопроцессорность: {t5:.2f} с")