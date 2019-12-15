[![asv](http://img.shields.io/badge/benchmarked%20by-asv-blue.svg?style=flat)](https://github.com/talianassi921/gm)


# Perception Tests for General Motors

General Motors Object Detection Assignment

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install [pytest](https://docs.pytest.org/en/latest/).

```bash
pip3 install pytest
```

Then install the following three packages.

```bash
pip3 install pytest-xdist
```
This allows you to run multiple tests at a time
```bash
pip3 install pytest-html
```
This allows you to generate an html report for each test run
```bash
pip3 install pytest-cov
```
This will print a coverage report with each test run

## Running the Tests

To run your tests, enter the follwing command:
```bash
./run_tests.sh
```

If you get a permissions error, enter ```chmod +x run_tests.sh``` and try again

## Test Reports

Each test run will generate a test report. To view the test report, copy and paste the generated html report into your browser.