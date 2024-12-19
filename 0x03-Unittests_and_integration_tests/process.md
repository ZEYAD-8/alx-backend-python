access_nested_map

    This is the function from the `utils` module that we are going to test. This function retrieves a value from a nested dictionary based on a given path (a sequence of keys).

@parameterized.expand Decorator

    >>Decorates the test_access_nested_map method to run it with different sets of inputs.
    >>The decorator takes a list of tuples, each containing the parameters for one test case (nested_map, path, expected).

**@parameterized.expand**:

    This decorator allows the `test_access_nested_map` method to be run multiple times with different sets of parameters. Each tuple in the list passed to `expand` represents a set of parameters for one test case:
    - `({"a": 1}, ("a",), 1)`: Tests that accessing the key `"a"` in the dictionary `{"a": 1}` returns `1`.
    - `({"a": {"b": 2}}, ("a",), {"b": 2})`: Tests that accessing the key `"a"` in the dictionary `{"a": {"b": 2}}` returns the nested dictionary `{"b": 2}`.
    - `({"a": {"b": 2}}, ("a", "b"), 2)`: Tests that accessing the path `("a", "b")` in the dictionary `{"a": {"b": 2}}` returns `2`.

def test_access_nested_map(self, nested_map, path, result):
    self.assertEqual(access_nested_map(nested_map, path), result)

    >> Calls access_nested_map with nested_map and path
    >> Asserts that the result is equal to the expected value using self.assertEqual.


     **test_access_nested_map**: This is the actual test method that will be run with the different sets of parameters. It takes three arguments:
    - `nested_map`: The nested dictionary to be accessed.
    - `path`: The sequence of keys to follow in the nested dictionary.
    - `expected`: The expected result of accessing the nested dictionary with the given path.

=============================
task 1

    -- It describes the TestAccessNestedMap
        class, explaining that it tests the
        access_nested_map function to ensure
        it correctly retrieves values from nested
        dictionaries or raises the expected exceptions.

    @parameterized.expand([
            ({}, ('a',)),
            ({'a': 1}, ('a', 'b')),
        ])
        def test_access_nested_map_exception(self, nested_map, path):
            with self.assertRaises(KeyError) as error:
                access_nested_map(nested_map, path)
            self.assertEqual(error.exception.args[0], path[-1])

    Example inputs tested:
    - `{}`, ('a',): Test accessing key 'a' in an empty dictionary should raise a KeyError.
    - `{'a': 1}, ('a', 'b'): Test accessing key 'b' in {'a': 1} should raise a KeyError.


    chatgpt:

    ### Explanation

    In the `test_access_nested_map_exception` method, we use `assertRaises` as a context manager to check if calling `access_nested_map(nested_map, path)` raises a `KeyError`. The `with self.assertRaises(KeyError) as error` block captures the raised `KeyError` and stores it in the `error` variable.

    ```python
    with self.assertRaises(KeyError) as error:
        access_nested_map(nested_map, path)
    ```

    After capturing the exception, we then verify the content of the exception message using `self.assertEqual`.

    ```python
    self.assertEqual(error.exception.args[0], path[-1])
    ```

    #### Details:

    - **`error.exception`**: This gives us the actual exception object that was raised (`KeyError` in this case).
    - **`error.exception.args[0]`**: This accesses the first argument of the exception, which is the error message associated with the exception.
    - **`path[-1]`**: This retrieves the last element of the `path` tuple, which is the key that caused the `KeyError`.


    

   
