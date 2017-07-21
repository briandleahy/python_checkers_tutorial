"""
I load in from test.py but create my own testclass on the fly:
"""

import os, sys

curdir = os.path.dirname(__file__)
sys.path.append(curdir)
sys.path.append(os.path.join(os.path.dirname(curdir), 'projects'))

import check_work

def create_testclass(ind):
    astr = 'from checkers_tk_problem{} import CheckersGUI as testclass'.format(ind)
    exec(astr)

    class CheckersTestClass(testclass):
        def _initialize(self, *args, **kwargs):
            pass
    return CheckersTestClass


if __name__ == '__main__':
    print 'Which problem:'
    ind = raw_input('->')
    cls = create_testclass(ind)
    check_work.check_work(cls)

