import json
from time import strftime
import os


class TestResults:
    def __init__(self, problem_sheet, problem_name):
        self.timestamp = strftime("%Y%m%d_%H%M%S")
        self.problem_sheet = problem_sheet
        self.problem_name = problem_name
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
        path = os.path.join(dir, f"{self.problem_sheet}_{self.problem_name}_{self.timestamp}")
        res_obj = {'timestamp': self.timestamp,
                   'problem_sheet': self.problem_sheet,
                   'problem_name': self.problem_name,
                   'results': self.results}
        with open(path, 'x') as file:
            json.dump(res_obj, file, indent=2)

    def print_summary(self):
        total_time = sum(r['duration'] for r in self.results)
        avg_time = total_time / len(self.results)
        print(f"Ran {len(self.results)} instances in {total_time:.1f}s (~{avg_time:.2f}s/instance)")

        num_special = sum(1 for r in self.results if r['special'])
        hit_special = sum(1 for r in self.results if r['special'] and r['success'])
        num_random = len(self.results) - num_special
        hit_random = sum(1 for r in self.results if not r['special'] and r['success'])

        print(f"- {hit_random}/{num_random} random instances correct")
        print(f"- {hit_special}/{num_special} special instances correct")

        print()
        if hit_special == num_special and hit_random == num_random:
            print("SUCCESS!")
        else:
            print("FAILED!")
