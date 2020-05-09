# Parse it to a CSV challenge

Oh no! Wanjing's dissertation is almost due and she doesn't have time to manually enter her experiment data into a spreadsheet. Can you help her by writing a program to put her data into a spreadsheet automatically?

## Problem definition

Wanjing is running a series of experiments, and outputting the raw results of them to a file. Each experiment result has the following structure. Each variable is denoted as `<variable_name>`.

```
from <table1> join <table2>
p1 <p1>
p2 <p2>
k (keywidth):  1
FPRAS ran in <runtime> seconds
```

Given this structure, your job is to produce a CSV that looks like the following:

```
table1,table2,p1,p2,runtime
gifts9,contributions5,0.06540697674418605,0.03347840642785403,78.0314
gifts7,contributions12,0.051622418879056046,0.06980990226613683,84.5057
gifts1,contributions13,0.007716049382716049,0.07477833564790086,75.7801
...
```

The CSV should contain a header row with the variable names and one row for each experiment result that you read.

## Provided files

You are provided with some files to get you started.

 - `simple_results`: This is the output of Wanjing's experiment.
 - `read_results.py`: This is a skeleton Python file for you to write your code in.
 - `expected_results.csv`: This is what your CSV file should look like in the end.
 - `is_my_solution_correct.py`: This file will test your solution and tell you if you have finished the challenge.

## Writing your solution

There are two functions defined in `read_results.py` - `parse_results(csvfilename)` and `read_single_result()`.

`parse_results` should open the results file, call `read_single_result()` until there are no more results, and write the output to the given `csvfilename`.

`read_single_result` should use the `input()` function to get enough lines to cover a single result. It should then return the variables from the result in the order (table1, table2, p1, p2, runtime).

## Useful code snippets

`input()` - gets a line of input from STDIN. Normally this means the user types it, but in our case, this is a line from a file.

`"a a".split(" ")` - `split` takes a string as an argument and splits another string on every instance of that argument. The example would produce `["a", "a"]`.

```python
mylist = [1, 2, 3]
mylist[0] == 1 # True
```

List indexing is done with square brackets.

`mytuple = (1, 2, 3)` - Tuples are just like lists, but are great for when you don't need to add or remove elements after creating them.

## Testing your solution

You can run your solution with the following command:

```
python3 read_results.py output.csv < simple_results
```

This will run the file `read_results.py` with the argument of `output.csv` and use `simple_results` as the STDIN. This means that when you call `input()` in your file, it will get a line from `simple_results`.

You can test if your solution is correct by running:

```
python3 is_my_solution_correct.py
```

Before your write your solution, the output will look like:

```
E
======================================================================
ERROR: test_simple_case (__main__.ReadResultsTest)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/usr/lib/python3.6/subprocess.py", line 425, in run
    stdout, stderr = process.communicate(input, timeout=timeout)
  File "/usr/lib/python3.6/subprocess.py", line 863, in communicate
    stdout, stderr = self._communicate(input, endtime, timeout)
  File "/usr/lib/python3.6/subprocess.py", line 1560, in _communicate
    self.wait(timeout=self._remaining_time(endtime))
  File "/usr/lib/python3.6/subprocess.py", line 1469, in wait
    raise TimeoutExpired(self.args, timeout)
subprocess.TimeoutExpired: Command '['python3', 'read_results.py', 'test.csv']' timed out after 0.9999311759602278 seconds

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "is_my_solution_correct.py", line 14, in test_simple_case
    subprocess.run(["python3", "read_results.py", self.TESTFILE], stdin=f, timeout=1)
  File "/usr/lib/python3.6/subprocess.py", line 430, in run
    stderr=stderr)
subprocess.TimeoutExpired: Command '['python3', 'read_results.py', 'test.csv']' timed out after 1 seconds

----------------------------------------------------------------------
Ran 1 test in 1.002s

FAILED (errors=1)
```

This is telling you that your script timed out. It timed out because you are not calling `input()` in `read_single_result()`. Can you think why?

When your solution is correct, this file will give output of the form:

```
.
----------------------------------------------------------------------
Ran 1 test in 0.066s

OK
```

This means that you've complete the challenge.
