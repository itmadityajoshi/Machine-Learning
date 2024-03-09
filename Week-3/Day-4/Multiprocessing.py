import requests
import multiprocessing
import time

def collect(urls):
    response = requests.get(urls)
    print(f'content of : {urls}: {response.text[:50]}')


urls = [
    'https://example.com/page1',
    'https://example.com/page2',
    'https://example.com/page3',
]


def collect_parallel(urls):
    with multiprocessing.Pool() as pool:
        pool.map(collect,urls)


if __name__ == "__main__":
    start_time = time.time()
    collect_parallel(urls)
    end_time = time.time()

    execution_time = end_time - start_time

    print(f'execution time: {execution_time} seconds')

        

