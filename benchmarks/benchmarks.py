import os
from tests.test_busy_freeway import BusyFreewayTests

class TimeSuite:

    def time_test_road_recognition(self):
        os.system("python3 -m pytest -v -n6 tests/")
        busy_freeway_test = BusyFreewayTests()
        busy_freeway_test.setup_method()
        busy_freeway_test.test_road_recognition()
 