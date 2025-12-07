import time
import requests

def fetch_url(url):
    start = time.time()
    try:
        response = requests.get(url, timeout=5)
        print(f"Fetched {url} in {time.time() - start:.2f}s | Status: {response.status_code}")
    except Exception as e:
        print(f"Error: {e}")

def run_io_sequential():
    urls = ["https://httpbin.org/delay/1"] * 3
    start = time.time()
    for url in urls:
        fetch_url(url)
    print(f"✅ Sequential I/O time: {time.time() - start:.2f}s\n")