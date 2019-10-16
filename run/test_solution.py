import argparse
from subprocess import run, CalledProcessError, TimeoutExpired
from generate.generators import generators
from run.results import TestResults
from tqdm import tqdm
from time import time

parser = argparse.ArgumentParser()
parser.add_argument('problem_sheet')
parser.add_argument('problem_name')
parser.add_argument('solution_path')
parser.add_argument('-num_random_instances', default=60, type=int)

args = parser.parse_args()

TIMEOUT = 1


# TODO capture more exceptions here
def run_instance(instance):
    instance_in, instance_out = instance

    data = dict(instance_in=instance_in,
                instance_out=instance_out)

    try:
        start_time = time()
        run_result = run(args=['runenv/python', args.solution_path],
                         timeout=TIMEOUT,
                         input=instance_in,
                         check=True,
                         text=True,
                         capture_output=True)
        duration = time() - start_time
        if run_result.returncode != 0:
            data['error'] = 'execution failed'
            data['success'] = False
    except TimeoutExpired as e:
        data['stdout'] = e.stdout
        data['stderr'] = e.stderr
        data['error'] = 'timeout'
        data['success'] = False
        data['duration'] = TIMEOUT
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

# do special instances first
num_special_instances = sum(1 for _ in generator.special_instances())
results = TestResults(args.problem_sheet, args.problem_name)

for instance in tqdm(generator.special_instances(),
                     desc='special instances',
                     total=num_special_instances):
    r = run_instance(instance)
    results.add_result(special=True, **r)

for _ in tqdm(range(args.num_random_instances),
              desc='random instances'):
    instance = generator.get_random_instance()
    r = run_instance(instance)
    results.add_result(special=False, **r)

print(flush=True)
results.print_summary()
results.save_report('reports')
