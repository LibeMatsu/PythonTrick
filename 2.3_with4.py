import time

class Timer:
    def __enter__(self):
        self.start = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end = time.time()
        self.interval = self.end - self.start
        print(f"実行時間: {self.interval:.4f} 秒")




with Timer():

    # 測定したいコード。例。
    for i in range(1000000):
        pass
