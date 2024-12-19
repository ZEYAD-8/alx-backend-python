unittesting ?

    -- is a software testing method where individual units or components of the software are tested in isolation from the rest of the application.

    we need to undertand some concepts before we start in testing:
        -- Test Case : The smallest unit of testing. It checks for a specific response to a particular set of inputs.
        -- Test Suite: A collection of test cases, test suites, or both.
        -- Test Runner: A component that orchestrates the execution of tests and provides the outcome to the user.

    - Focuses on a single function, method, or class.
    - Generally fast because they test small pieces of code.
    - Easier to diagnose failures since the scope is limited to a small unit.


    -Example: Testing a single function in a module to ensure it returns the correct result given a set of inputs.

Integration Testing ?

    -- Integration testing involves combining individual units and testing them together as a group. The goal is to identify issues that occur when units interact with each other.
    Example: Testing the interaction between a database module and an API module to ensure they work together as expected.

Common Testing Patterns
    Mocking:

    -is a library used to replace parts of your system under test and make assertions about how they have been used. It allows you to mock and stub out dependencies in your code during testing.

    Mocking is the practice of replacing real objects in your code with mock objects to isolate the code being tested and focus on its behavior.

    Mocking is useful when testing functions that interact with external systems (e.g., databases, APIs).

    Mock Object Library (unittest.mock) ?


    some concepts  :
        -- Mock Objects: Simulated objects that mimic the behavior of real objects.
        -- Patching: Temporarily replacing a part of your application with a mock during a test.
        -- Assertions: Checks to see how mock objects have been used, such as verifying that a method was called with specific parameters.

        from unittest import TestCase
        from unittest.mock import PropertyMock, patch

        class MyClass:
            @property
            def my_property(self):
                return "original value"

        class TestMyClass(TestCase):
            @patch.object(MyClass, 'my_property', new_callable=PropertyMock)
            def test_my_property(self, mock_my_property):
                mock_my_property.return_value = "mocked value"
                obj = MyClass()
                self.assertEqual(obj.my_property, "mocked value")

        if __name__ == '__main__':
            unittest.main()



Parameterized Testing ?

    -- Parameterized testing involves running the same test multiple times with different sets of inputs.
    -- Useful for testing functions with multiple input scenarios.
    -- It allows you to run the same test logic with different inputs. This helps in reducing code duplication and making your tests more comprehensive.

    import unittest
    from ddt import ddt, data, unpack

    @ddt
    class TestMath(unittest.TestCase):
        
        @data((1, 1, 2), (2, 3, 5), (3, 5, 8))
        @unpack
        def test_add(self, a, b, expected):
            self.assertEqual(a + b, expected)

    if __name__ == '__main__':
        unittest.main()

Fixtures ?

    Fixtures are setup/teardown code that runs before and after tests. They prepare the necessary context or state for the tests.

    Useful for initializing objects or states that are shared across multiple tests.

    import unittest

class TestExample(unittest.TestCase):
    
    def setUp(self):
        self.test_data = [1, 2, 3, 4, 5]
    
    def tearDown(self):
        self.test_data = None

    def test_sum(self):
        self.assertEqual(sum(self.test_data), 15)

    if __name__ == '__main__':
        unittest.main()

Memoization ?

    -- is an optimization technique used to speed up function calls by caching the results of expensive function calls and returning the cached result when the same inputs occur again.

    Memoization is an optimization technique that involves storing the results of expensive function calls and returning the cached result when the same inputs occur again.
    Useful for functions with expensive or time-consuming computations that are called multiple times with the same inputs.

    def memoize(func):
    cache = {}
    
    def memoized_func(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    
    return memoized_func

    @memoize
    def fibonacci(n):
        if n in (0, 1):
            return n
        return fibonacci(n-1) + fibonacci(n-2)

    # Test
    print(fibonacci(10))  # Outputs 55


Difference Between Unit and Integration Tests ?

    -- Unit Tests: Test individual units of code in isolation from the rest of the system. They are fast, simple, and focus on a small piece of functionality.
    Integration Tests: Test how different parts of the system work together. They ensure that components interact correctly but are more complex and slower than unit tests.

Common Testing Patterns ?

    Mocking: Used to simulate the behavior of real objects in testing. This helps in isolating the unit of work being tested and ensuring it interacts as expected with its dependencies.
    Parameterized Testing: Running the same test with different sets of data. This improves test coverage and reduces redundancy.
    Fixtures: Predefined state or context used to run tests. They provide a fixed baseline for running tests, ensuring consistency and reliability.

