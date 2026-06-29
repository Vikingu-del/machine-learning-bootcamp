import time


def ft_progress(lst):
    """Displays a progress bar for the given iterable."""
    start_time = time.time()
    total = len(lst)
    eta = 0
    for i, elem in enumerate(lst):
        percent = (i + 1) / total * 100
        remaining = total - (i + 1)
        bar_length = 42
        filled_length = int(bar_length * (i + 1) // total)
        current_time = time.time()
        elapsed_time = current_time - start_time
        i_per_second = i + 1 / elapsed_time
        eta = remaining / i_per_second
        bar = '=' * filled_length + '>' + ' ' * (bar_length - filled_length)
        look = f"\rETA: {eta:.2f}s [{percent:.2f}%] [{bar}] {i + 1}/{total} "
        look += f"| elapsed time: {elapsed_time:.2f}s"
        print(look, end='', flush=True)
        yield elem
