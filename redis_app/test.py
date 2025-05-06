import requests
import time

url = 'http://127.0.0.1:8000/animals/'

start_time = time.time()
response = requests.get(url)
duration = time.time() - start_time
print(f"Response time: {duration} seconds")