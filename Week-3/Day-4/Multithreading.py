import requests
from concurrent.futures import ThreadPoolExecutor
import time

# declareing the function to download the file 

def download_file(url):
    urls, filename = url  #here urls tuple are formatted in arguments
    response  = requests.get(urls) 
    with open (filename, 'wb') as file:
        file.write(response.content)
        print(f'Downloaded: {filename}')



urls = [
    ('https://example.com/file1.txt', 'file1.txt'),
    ('https://example.com/file2.txt','file2.txt'),
    ('https://example.com/file3.txt', 'file3.txt'),
    ]


# now using threadpoolexecutor to download files concurrently

def downloadfiles_concurently(urls):
    with ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(download_file, urls)


if __name__ == "__main__":
    start_time = time.time()
    downloadfiles_concurently(urls)
    end_time = time.time()

    execution_time = end_time - start_time

    print(f'execution time: {execution_time} seconds')
