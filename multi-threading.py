# Multi-threading: Used to perform multiple tasks concurrently (multitasking)
# Good for I/O bound tasks such as reading files or fetching data from APIs
# threading.Thread(target=my_function)

import threading
import time

def reading_file(file_name):
    time.sleep(8)
    print(f"Reading a file: {file_name}")
    
def fetching_via_api():
    time.sleep(4)
    print("Fetching data from APIs")

def computation():
    time.sleep(2)
    print("Computation")

# reading_file()
# fetching_via_api()
# computation()

chore1 = threading.Thread(target=reading_file, args=("README.md",))
chore1.start()

chore2 = threading.Thread(target=fetching_via_api)
chore2.start()

chore3 = threading.Thread(target=computation)
chore3.start()

chore1.join()
chore2.join()
chore3.join()

# With the join method, we wait for the threads to finish before continuing with the rest of the program

print("All tasks completed")