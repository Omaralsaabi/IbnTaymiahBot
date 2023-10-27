import requests
import json
import time
import threading

def download_page(i):
    global fullText, error_flag
    print(f"Page {i}")
    url = f"https://api.turath.io/page?book_id={book_id}&pg={i}&ver=3"
    response = requests.get(url, headers=headers, data=payload)

    if response.status_code != 200:
        error_flag = True
        print(f"Error on page {i}. Status code: {response.status_code}")
        return

    text = response.text
    json_data = json.loads(text)
    text = json_data['text']

    fullText += text

start_time = time.time()
payload = {}
headers = {
    'Cookie': '__cfduid=d0b2a5a6c4a4e1e9b3f2d9b8b9a6b9c6c1617158574; _ga=GA1.2.1253656535.1617158577; _gid=GA1.2.175145893.1617158577; _gat_gtag_UA_153738851_1=1'
}
fullText = ''
error_flag = False  # Flag to check for errors
book_id = 735

# Number of threads to use
num_threads = 4  # You can adjust this as needed

threads = []

for i in range(3, 16874):
    if not error_flag:
        while len(threads) >= num_threads:
            # Wait for a thread to finish
            for t in threads:
                if not t.is_alive():
                    threads.remove(t)
                    break

        if not error_flag:
            thread = threading.Thread(target=download_page, args=(i,))
            thread.start()
            threads.append(thread)

# Wait for all threads to finish
for thread in threads:
    thread.join()

# Save the full text to a file
book_name = 'البخاري'
with open(f'{book_name}.txt', 'w', encoding='utf-8') as f:
    f.write(fullText)

# Measure the time of the script
print("--- %s seconds ---" % (time.time() - start_time))

if error_flag:
    print("Script stopped due to an error.")
else:
    print("Script completed successfully.")
