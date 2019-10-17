import argparse
from subprocess import run, TimeoutExpired
from generate.generators import generators
from run.results import TestResults
from tqdm import tqdm
from time import time
from difflib import Differ
import json
import sys
import os

parser = argparse.ArgumentParser()
parser.add_argument('problem_sheet')
parser.add_argument('problem_name')
parser.add_argument('-num_random_instances', default=60, type=int)
parser.add_argument('-verbose', default=None)
parser.add_argument('-pedantic', action='store_true')

args = parser.parse_args()

TIMEOUT = 1
solution_path = os.path.join('..','solutions',args.problem_sheet, args.problem_name+'.py')


# TODO capture more exceptions here
def run_instance(instance):
    instance_in, instance_out = instance

    data = dict(instance_in=instance_in,
                instance_out=instance_out)

    try:
        start_time = time()
        run_result = run(args=['runenv/python', solution_path],
                         timeout=TIMEOUT,
                         input=instance_in,
                         text=True,
                         capture_output=True)
    except TimeoutExpired as e:
        data['stdout'] = e.stdout
        data['stderr'] = e.stderr
        data['error'] = 'timeout'
        data['success'] = False
        data['duration'] = TIMEOUT

    else:
        duration = time() - start_time

        if run_result.returncode != 0 or run_result.stderr.startswith('Traceback'):
            data['error'] = 'execution failed'
            data['success'] = False
        else:
            if run_result.stdout == instance_out:
                data['success'] = True
            else:
                data['success'] = False
                data['error'] = 'incorrect result'

        data['duration'] = duration
        data['stdout'] = run_result.stdout
        data['stderr'] = run_result.stderr

    return data


generator = generators[args.problem_sheet][args.problem_name]
results = TestResults(args.problem_sheet, args.problem_name)


def run_instances(instances, desc, total, special):
    for instance in tqdm(instances,
                         desc=desc,
                         total=total,
                         disable=args.verbose == "all"):
        r = run_instance(instance)

        if args.verbose is not None:
            if args.verbose == 'all' or args.verbose == 'error' and not r['success']:
                print(json.dumps(r, indent=2))

                if not r['success'] and r['error'] == 'incorrect result':
                    print("Diff of the results:")
                    print("-")
                    diff = Differ().compare(r['stdout'].splitlines(), r['instance_out'].splitlines())
                    print('\n'.join(diff))
                    print("-")

        results.add_result(special=special, **r)

        if args.pedantic and not r['success']:
            print("Aborting run.", flush=True)
            print(r['stderr'], file=sys.stderr, flush=True)
            break


if args.verbose == 'all':
    print("verbosity level is 'all', omitting progress bars.")

# do special instances first
num_special_instances = sum(1 for _ in generator.special_instances())

run_instances(generator.special_instances(),
              desc='special instances',
              total=num_special_instances,
              special=True)
run_instances((generator.get_random_instance() for _ in range(args.num_random_instances)),
              desc='random instances',
              total=args.num_random_instances,
              special=False)

print(flush=True)
results.print_summary()
results.save_report('reports')
