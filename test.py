import unittest
import datetime
from main import should_send, get_hour_to_send_today, RUN_HOURS
from collections import defaultdict
import logging

logging.basicConfig()
logging.getLogger().setLevel(logging.WARN)


class TestMain(unittest.TestCase):

    JAN_2022 = datetime.datetime(2022, 1, 1, 0, 0)
    JAN_2023 = datetime.datetime(2023, 1, 1, 0, 0)

    @staticmethod
    def hourly_datetimes(start: datetime.datetime, end: datetime.datetime):
        while start < end:
            yield start
            start = start + datetime.timedelta(hours=1)
    
    def test_should_send_is_true_once_a_day(self):
        results = defaultdict(int)
        for time in self.hourly_datetimes(self.JAN_2022, self.JAN_2023):
            is_should_send = should_send(time)
            key = (time.month, time.day)
            results[key] += int(is_should_send)

        assert len([v for v in results.values() if v != 1]) == 0

    def test_get_hour_to_send_today_returns_each_run_hour_eventually(self):
        results = defaultdict(int)
        for time in self.hourly_datetimes(self.JAN_2022, self.JAN_2023):
            hour_to_send = get_hour_to_send_today(time)
            results[hour_to_send] += 1

        print(results)
        assert len([k for k in RUN_HOURS if k not in results]) == 0

if __name__ == '__main__':
    unittest.main()
