import unittest
import languageprocess.sqlizer

class TestSql(unittest.TestCase):
    '''
    generated query testing class
    '''

    def test_sql(self):
        res = languageprocess.sqlizer.sqlize('get all the student with score more than 90')
        self.assertEqual(res, 'SELECT * FROM student WHERE score >=  90')


if __name__ == '__main__':
    unittest.main()
