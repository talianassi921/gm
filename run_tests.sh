#!/bin/bash

python3 -m pytest -v -s -n6 tests/ --cov=tests/ --html=report.html