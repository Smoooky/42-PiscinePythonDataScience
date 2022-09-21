#!/usr/bin/env python3

import timeit
from random import randint
from collections import Counter


class CounterRandomTester:
    def __init__(self, list_size: int) -> None:
        self.random_list = [randint(0, 100) for _ in range(list_size)]
        self.cached_counts_loop = None
        self.cached_counts_counter = None

    def loop_approach(self) -> dict:
        counts = {}
        for value in self.random_list:
            if value in counts.keys():
                counts[value] += 1
            else:
                counts[value] = 1

        self.cached_counts_loop = counts
        return counts

    def get_top_ten_loop(self) -> dict:
        if self.cached_counts_loop is None:
            self.loop_approach()

        return dict(sorted(self.cached_counts_loop.items(),
                           key=lambda item: item[1], reverse=True)[:10])

    def counter_approach(self) -> dict:
        self.cached_counts_counter = Counter(self.random_list)
        return dict(self.cached_counts_counter)

    def get_top_ten_counter(self) -> dict:
        if self.cached_counts_counter is None:
            self.counter_approach()

        return self.cached_counts_counter.most_common(10)


def main():
    iters = 10000
    tester = CounterRandomTester(1000)

    time_results = {
        'my function': timeit.timeit(tester.loop_approach, number=iters),
        'Counter': timeit.timeit(tester.counter_approach, number=iters),
        'my top': timeit.timeit(tester.get_top_ten_loop, number=iters),
        "Counter's top": timeit.timeit(tester.get_top_ten_loop, number=iters),
    }

    for item in time_results:
        print(f'{item}: {time_results[item]}')


if __name__ == '__main__':
    main()