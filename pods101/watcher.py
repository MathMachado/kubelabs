import requests
import time
r = requests.get("http://127.0.0.1").text
while True:
    num = r.count("n")
    print(f"There are {num} occurrences of 'n'")
