import unittest

import bxuimodel
import sys
from io import StringIO


class MyTestCase(unittest.TestCase):
    def test_something(self):
        strio = StringIO(u"-User;author[y,l15,w36,a1]:i;title(f14,cw);id[x,y](ch):l;url(cwa):b;mobile:f;bgView(cwa):v")
        sys.stdin = strio
        bxuimodel.main()


if __name__ == '__main__':
    unittest.main()