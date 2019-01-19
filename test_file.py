#https://jeffknupp.com/blog/2016/03/07/python-with-context-managers/

import unittest
from file import File

files = []


class Test_My_Lambda(unittest.TestCase):

    def test_test_my_file(self):
        for _ in range(10000):
            with File('foo.txt', 'w') as infile:
                infile.write('flu')
                files.append(infile)   
        f= open("foo.txt","r")
        content =f.read()
        self.assertEqual(content, "flu")

