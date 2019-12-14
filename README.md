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
pytest -v -s -n3 --cov=tests/ --html=report.html
```
-v means verbose, so you can get a clear understanding of which tests passed or failed

-s refers to system outputs, so you can see what gets outputted from your tests, if anything

-n# refers to the number of tests you would like to run at a time (Ideally this would be done automatically in GCP but for the purposes of this project, this will do)

To view the test report, copy and paste the generated html report into your browser