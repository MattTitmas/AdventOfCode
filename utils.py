import time


class Timer():
    def __init__(self, tag: str = "") -> None:
        self.tag = tag

    def __enter__(self):
        self.start = time.time()
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        print(f"Timer {self.tag}: {self.get_time():.4f}s")

    def get_time(self) -> float:
        return time.time() - self.start
