import unittest
from company.employee import Developer, Tester, Manager

class TestEmployee(unittest.TestCase):

    def test_developer_payment(self):
        dev = Developer(101, "Aro", 80000, 5000, 2000, False)
        self.assertEqual(dev.get_total_payment(), 87000)

    def test_tester_payment(self):
        tester = Tester(102, "Barath", 75000, True, False, True, 3000)
        self.assertEqual(tester.get_total_payment(), 78000)

    def test_manager_payment(self):
        manager = Manager(103, "Chandru", 120000, 60000, 5)
        self.assertEqual(manager.get_total_payment(), 180000)

if __name__ == '__main__':
    unittest.main()
