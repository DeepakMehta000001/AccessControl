import unittest
from controller import AccessControl
from data import create_data
from unittest import mock
from unittest.mock import MagicMock

class TestAccessControl(unittest.TestCase):

    currentResult = None # holds last result object passed to run method

    @classmethod
    def setResult(cls, amount, errors, failures, skipped):
        cls.amount, cls.errors, cls.failures, cls.skipped = \
            amount, errors, failures, skipped


    def tearDown(self):
        amount = self.currentResult.testsRun
        errors = self.currentResult.errors
        failures = self.currentResult.failures
        skipped = self.currentResult.skipped
        self.setResult(amount, errors, failures, skipped)

    @classmethod
    def tearDownClass(cls):
        print("Called at last")
        print("\ntests run: " + str(cls.amount))
        print("errors: " + str(len(cls.errors)))
        print("failures: " + str(len(cls.failures)))
        print("success: " + str(cls.amount - len(cls.errors) - len(cls.failures)))
        print("skipped: " + str(len(cls.skipped)))

    def run(self, result=None):
        self.currentResult = result # remember result for use in tearDown
        unittest.TestCase.run(self, result) # call superclass run method

    def setUp(self):
        self.access_control = AccessControl()
        create_data(self.access_control)

    @mock.patch('builtins.input', MagicMock(return_value=4))
    # @mock.patch('builtins.input', side_effect=[4])
    def test_admin_options(self):
        self.access_control.current_user='deepak'
        self.access_control.current_role=1
        test_response =self.access_control.show_options()
        self.assertEqual(test_response, 'admin_options')

    @mock.patch('builtins.input', MagicMock(return_value=4))
    def test_user_options(self):
        self.access_control.current_user='arun'
        self.access_control.current_role=2
        test_response =self.access_control.show_options()
        self.assertEqual(test_response, 'user_options')

    def test_add_user(self):
        self.access_control.add_user('test_user', ['admin'])
        self.assertEqual(True, 'test_user' in self.access_control.users)
        self.assertEqual([1], self.access_control.users['test_user']['roles'])

    @mock.patch('builtins.input',MagicMock(return_value='R5'))
    def test_access_resource_admin(self):
        self.access_control.current_user='deepak'
        self.access_control.current_role=1
        self.access_control.access_resources()
        self.assertEqual(self.access_control.users['deepak']['resources'], ['R5'])

    @mock.patch('builtins.input',MagicMock(return_value='R2'))
    def test_access_resource_user(self):
        self.access_control.current_user='arun'
        self.access_control.current_role=2
        self.access_control.access_resources()
        self.assertEqual(self.access_control.users['arun']['resources'], ['R2'])

if __name__ == '__main__':
    unittest.main()
