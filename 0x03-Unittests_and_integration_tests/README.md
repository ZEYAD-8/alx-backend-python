A tool that developers can use from the command line to select and run specific tests

### Step 1: Setting Up Your Environment

Ensure you have Python installed on your system. This tool will be designed to run with Python 3.x.

### Step 2: Organize Your Tests

Organize your tests in a structured directory. For example, all your tests are inside `0x03-Unittests_and_integration_tests` as per your provided structure. Each test can be a separate Python file or organized logically within files.

### Step 3: Create a Command Line Tool

Create a new Python script named `run_tests.py` in the root of your project directory. This script will use `argparse` to parse command line arguments.

#### `run_tests.py`

```python
import argparse
import unittest
import sys
from pathlib import Path

def load_tests(loader, tests, pattern):
    suite = unittest.TestSuite()
    for test in tests:
        suite.addTests(loader.loadTestsFromTestCase(test))
    return suite

def run_specific_test(test_name):
    loader = unittest.TestLoader()
    start_dir = '0x03-Unittests_and_integration_tests'
    suite = loader.discover(start_dir, pattern='test_*.py')

    specific_tests = {
        "access_nested_map": "TestAccessNestedMap",
        "access_nested_map_exception": "TestAccessNestedMap",
        "mock_http_calls": "TestGetJson",
        "memoize": "TestMemoize",
        "github_org_client": "TestGithubOrgClient",
        "public_repos_url": "TestGithubOrgClient",
        "public_repos": "TestGithubOrgClient",
        "has_license": "TestGithubOrgClient",
        "integration": "TestIntegrationGithubOrgClient"
    }

    if test_name in specific_tests:
        tests = [cls for cls in unittest.defaultTestLoader.loadTestsFromName(f"{start_dir}.{specific_tests[test_name]}") if cls.__class__.__name__ == specific_tests[test_name]]
        unittest.TextTestRunner().run(load_tests(loader, tests, None))
    else:
        print("Invalid test name. Please check the available tests.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run specific unittests for the ALX Backend Python project.")
    parser.add_argument("test_name", help="The name of the test to run.")
    args = parser.parse_args()

    run_specific_test(args.test_name)
```

### Step 4: Usage Instructions

To use this tool, developers will navigate to the terminal or command prompt, navigate to the project directory, and then run the script with the desired test as an argument. For example:

```bash
python run_tests.py access_nested_map
```

This command would run the `TestAccessNestedMap` tests.

### Step 5: Extend and Customize

- You can extend the `run_specific_test` function to include more specific tests or test cases by modifying the `specific_tests` dictionary.
- Ensure all test files follow the naming pattern `test_*.py` for the discover mechanism to work correctly.
- Update the `start_dir` variable if you decide to change the structure of your test directories.

### Conclusion

This script serves as a starting point for creating a customizable testing tool for developers. It can be further enhanced by adding more command line options, such as verbosity levels, running all tests within a specific file, or even integrating with CI/CD pipelines for automated testing environments.

[Blog Post:](https://shazaali.substack.com/p/0x03-unittests-and-integration-tests)