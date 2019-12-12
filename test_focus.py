import os
import time
from unittest import TestCase

from phillypywin32 import focus


class Test(TestCase):
    def test_bring_window_to_top(self):
        with self.assertRaises(focus.WindowNotFoundError) as e:
            focus.focus_on_window("TEST FAILED!!!!!!!!!!!")

        os.startfile(r"C:\WINDOWS\system32\notepad.exe")
        time.sleep(2)
        os.startfile(r"C:\WINDOWS\system32\cmd")
        time.sleep(2)
        focus.focus_on_window("Untitled - Notepad")
        time.sleep(2)
        focus.focus_on_window("C:\WINDOWS\system32\cmd.exe")
