#!python

import sys
import unittest

sys.path.append('../')
from irlib.superlist import SuperList
from irlib.matrix import Matrix
 
class TestSuperList(unittest.TestCase):

    def setUp(self):
        self.x = SuperList([0,1,2,3])
        self.y = SuperList([0,1,2,3])

    def test_unique_append(self):
        new_item = 1
        i = self.x.unique_append(new_item)
        self.assertEqual(i, new_item)
        self.assertEqual(self.x, self.y)
        new_item = 4
        i = self.x.unique_append(new_item)
        self.assertEqual(i, new_item)
        self.assertNotEqual(self.x, self.y)

    def test_insert_after_padding(self):
        self.x.insert_after_padding(7,99)
        self.assertEqual(self.x[7],99)
        self.x.insert_after_padding(1,99)
        self.assertEqual(self.x[1],99)

    def test_increment_after_padding(self):
        self.x.increment_after_padding(7,99)
        self.assertEqual(self.x[7],99)
        self.x.increment_after_padding(1,99)
        self.assertEqual(self.x[1],100)

class TestMatrix(unittest.TestCase):

    def setUp(self):
        self.m = Matrix()

    def test_add_doc(self):
        # Try without frequency
        doc1_terms = ['buy', 'now', 'or', 'buy', 'later']
        self.m.add_doc( doc_id = 'file_spam.txt', 
                        doc_class='Spam', 
                        doc_terms= doc1_terms,
                        frequency=False)
        self.assertEqual(self.m.terms, ['buy', 'now', 'or', 'later'])
        self.assertEqual(self.m.docs[0]['terms'], [1,1,1,1])
        # Now try with frequency
        doc2_terms = ['buy', 'today', 'or', 'buy', 'later']
        self.m.add_doc( doc_id = 'file_spam.txt', 
                        doc_class='Spam', 
                        doc_terms= doc2_terms,
                        frequency=True)
        self.assertEqual(self.m.terms, ['buy', 'now', 'or', 'later', 'today'])
        self.assertEqual(self.m.docs[1]['terms'], [2,0,1,1,1])
        # Now let's see if padding is working
        doc2_terms = ['buy', 'now']
        self.m.add_doc( doc_id = 'file_spam.txt', 
                        doc_class='Spam', 
                        doc_terms= doc2_terms,
                        frequency=True,
                        do_padding=True)
        self.assertEqual(len(self.m.terms), len(self.m.docs[0]['terms']))     

if __name__ == '__main__':
    unittest.main()