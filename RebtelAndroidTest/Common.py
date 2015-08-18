import os
import time
import traceback
import unittest
import xmlrunner
from datetime import datetime


def writeInfo(text):
    ''''Printing timestamped activity message.'''
    print('\n' + datetime.now().strftime("%Y-%m-%d %H:%M:%S") + ' - ' + text)