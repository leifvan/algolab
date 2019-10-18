import json
from time import strftime
import os
from argparse import Namespace
from collections import Counter


class TestResults:
    def __init__(self, problem_sheet, problem_name, timeout, lang):
        self.timestamp = strftime("%Y%m%d_%H%M%S")
        self.problem_sheet = problem_sheet
        self.problem_name = problem_name
        self.timeout = timeout
        self.lang = lang
        self.results = []

    def add_result(self, instance_in, instance_out, success, stdout, stderr, duration, error=None, special=False):
        r = {'input': instance_in,
             'expected_output': instance_out,
             'stdout': stdout,
             'stderr': stderr,
             'success': success,
             'duration': duration,
             'special': special}
        if error is not None:
            assert not success
            r['error'] = error
        self.results.append(r)

    def save_report(self, dir):
        path = os.path.join(dir, f"{self.problem_sheet}_{self.problem_name}_{self.lang}_{self.timestamp}")
        res_obj = {'timestamp': self.timestamp,
                   'problem_sheet': self.problem_sheet,
                   'problem_name': self.problem_name,
                   'timeout': self.timeout,
                   'lang': self.lang,
                   **self.get_summary_stats().__dict__,
                   'results': self.results}
        with open(path, 'x') as file:
            json.dump(res_obj, file, indent=2)

    def get_summary_stats(self):
        total_time = sum(r['duration'] for r in self.results)
        avg_time = total_time / len(self.results)
        num_special = sum(1 for r in self.results if r['special'])
        hit_special = sum(1 for r in self.results if r['special'] and r['success'])
        num_random = len(self.results) - num_special
        hit_random = sum(1 for r in self.results if not r['special'] and r['success'])

        num_errors = Counter([r['error'] for r in self.results if 'error' in r])

        return Namespace(total_time=total_time,
                         avg_time=avg_time,
                         num_special=num_special,
                         hit_special=hit_special,
                         num_random=num_random,
                         hit_random=hit_random,
                         num_errors=num_errors)

    def print_summary(self):
        s = self.get_summary_stats()

        print(f"Ran {len(self.results)} instances in {s.total_time:.1f}s (~{s.avg_time:.2f}s/instance)")
        print(f"- {s.hit_random}/{s.num_random} random instances correct")
        print(f"- {s.hit_special}/{s.num_special} special instances correct")

        print()
        if s.hit_special == s.num_special and s.hit_random == s.num_random:
            print("SUCCESS!")
        else:
            print("FAILED!")
            print()
            for err, count in s.num_errors.most_common():
                print(f"- {count}x {err}")
