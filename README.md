# Perception Tests for General Motors

General Motors Object Detection Assignment

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install [pytest](https://docs.pytest.org/en/latest/).

```bash
pip3 install pytest
```

Then install the following two packages.

```bash
pip3 install pytest-html
```
This allows you to generate an html report for each test run
```bash
pip3 install pytest-benchmark
```
This will print benchmarking of run time per test

## Running the Tests

To run your tests, enter the follwing command:
```bash
./run_tests.sh
```

If you get a permissions error, enter ```chmod +x run_tests.sh``` and try again

## Test Reports

Each test run will generate a test report. To view the test report, copy and paste the generated html report into your browser.