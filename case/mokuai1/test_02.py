import unittest

#用例执行顺序，先执行setUpClass>setUp>testAdd>tearDown>setUp>testAdd>tearDown>testMultiply

def login():
    print("先登陆")
class IntegerArithmeticTestCase(unittest.TestCase):

    u'''测试用例集合'''
    @classmethod
    def setUpClass(cls):
        print("前置只执行一次")
        login()
    @classmethod
    def tearDownClass(cls):
        print("所有用例执行完毕后最后执行这个")

    def setUp(self):#每个用例都会先执行这个
        print("前置")

    def tearDown(self):
        print("后置")

    def testAdd(self):  # test method names begin with 'test'
        u'''测试用例1'''
        self.assertEqual((1 + 2), 3)
        self.assertEqual(0 + 1, 1)

    def testMultiply(self):
        u'''测试用例2'''
        self.assertEqual((0 * 10), 0)
        self.assertEqual((5 * 8), 41)


if __name__ == '__main__':
    unittest.main()