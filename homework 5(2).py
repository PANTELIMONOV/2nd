
import unittest


# Distance between two points
def distance (x1,y1,x2,y2):

    return 0.5**((x1-x2)**2+(y1-y2)**2)

# Is the year a leap year?
def is_year_leap (y):
    if y % 4 == 0 and y % 100 != 0:
        return True
    elif y % 400 == 0:
        return True
    else:
        return False

# Is this a Triangle?
def triangle (a,b,c):
    if a+b>c and b+c>a and a+c>b:
        return True
    else:
        return False



class Test (unittest.TestCase):

    def test_distance(self):
        self.assertEqual(distance(1,2,3,4), 0.00390625)
    def test_is_year_leap(self):
        self.assertFalse(is_year_leap(2017),'False')
        self.assertTrue(is_year_leap(2000), 'True')
        self.assertTrue(is_year_leap(2016),'True')
    def test_triangle(self):
        self.assertFalse(triangle(4,1,5), 'False')
        self.assertFalse(triangle(1, 1, 5), 'False')
        self.assertTrue(triangle(2,2,2), 'True')
        self.assertTrue(triangle(2,3,2), 'True')


if __name__ == '__main__':
    unittest.main()