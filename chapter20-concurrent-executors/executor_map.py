import sys
from time import sleep, strftime
from concurrent import futures

def display(*args):
    print(strftime('[%H:%M:%S]'), end=' ')
    print(*args)

def loiter(n):
    msg = '{}loiter({}): doing nothing for {}s...'
    display(msg.format('\t'*n, n, n))
    sleep(n)
    msg = '{}loiter({}): done.'
    display(msg.format('\t'*n, n))
    return n * 10

def main():
    max_workers = 3
    num_loiters = 5
    if len(sys.argv) == 2:
        max_workers = int(sys.argv[1])
    elif len(sys.argv) == 3:
        max_workers = int(sys.argv[1])
        num_loiters = int(sys.argv[2])
    display(f'Script starting with {max_workers}.')
    executor = futures.ThreadPoolExecutor(max_workers=max_workers)
    results = executor.map(loiter, range(num_loiters))
    display('results:', results)
    display('Waiting for individual results:')

    """
    enumerate calls next(results) which in turn will invoke
    _f.result() on the (internal) _f future representing the
    first call, loiter(0). The result method will block until
    the future is done, therefore each iteration in this loop
    will have to wait for the next result to be ready. This is
    how ordered is preserved
    DOWNSIDE: We are not taking advantage on those threads that
    have already finished the computation! If we want to do that,
    we need to use both executor.submit + futures.as_completed

    You can check the implementation of map here:
    https://github.com/python/cpython/blob/main/Lib/concurrent/futures/_base.py#L575
    """
    for i , result in enumerate(results):
        display(f'result {i}: {result}')

if __name__ == '__main__':
    main()
