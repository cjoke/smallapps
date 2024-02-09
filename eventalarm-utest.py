import unittest
import os
from eventalarm import Alarm


class TestAlarm(unittest.TestCase):
    def setUp(self):
        self.alarm = Alarm()

    def test_add_alarm(self):
        self.alarm.add_alarm("01.01.22 00.00.00", "sound.wav")
        self.assertEqual(len(self.alarm.alarms), 1)

    def test_delete_alarm(self):
        self.alarm.add_alarm("01.01.22 00.00.00", "sound.wav")
        self.alarm.delete_alarm(0)
        self.assertEqual(len(self.alarm.alarms), 0)

    def tearDown(self):
        if os.path.exists("alarms.json"):
            os.remove("alarms.json")


if __name__ == "__main__":
    unittest.main()
