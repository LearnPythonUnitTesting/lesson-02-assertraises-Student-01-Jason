# Lesson-02-AssertRaises
### 1. Assert Methods
| Method                    | Checks that          | New in |
| ------------------------- | -------------------- | ------ |
| assertEqual(a, b)         | a == b               | \-     |
| assertNotEqual(a, b)      | a != b               | \-     |
| assertTrue(x)             | bool(x) is True      | \-     |
| assertFalse(x)            | bool(x) is False     | \-     |
| assertIs(a, b)            | a is b               | 3.1    |
| assertIsNot(a, b)         | a is not b           | 3.1    |
| assertIsNone(x)           | x is None            | 3.1    |
| assertIsNotNone(x)        | x is not None        | 3.1    |
| assertIn(a, b)            | a in b               | 3.1    |
| assertNotIn(a, b)         | a not in b           | 3.1    |
| assertIsInstance(a, b)    | isinstance(a, b)     | 3.2    |
| assertNotIsInstance(a, b) | not isinstance(a, b) | 3.2    |
- 
| Method                                           | Checks that                                                       | New in |
| ------------------------------------------------ | ----------------------------------------------------------------- | ------ |
| assertRaises(exc, fun, \*args, \*\*kwds)         | fun(\*args, \*\*kwds) raises exc                                  | \-     |
| assertRaisesRegex(exc, r, fun, \*args, \*\*kwds) | fun(\*args, \*\*kwds) raises exc and the message matches regex r  | 3.1    |
| assertWarns(warn, fun, \*args, \*\*kwds)         | fun(\*args, \*\*kwds) raises warn                                 | 3.2    |
| assertWarnsRegex(warn, r, fun, \*args, \*\*kwds) | fun(\*args, \*\*kwds) raises warn and the message matches regex r | 3.2    |
| assertLogs(logger, level)                        | The with block logs on logger with minimum level                  | 3.4    |

### 2. Basic Example
```
def divide(a, b):
    if b == 0:
        raise ValueError('Can not divide by zero.')
    return a / b
```
When defining the method 'divide(a,b)', we have to raise ValueError if divisor is 0. 

```
def test_divide(self):
    self.assertEqual(calculate.divide(10, 5), 2)

    # assertRaises
    self.assertRaises(ValueError, calculate.divide, 10, 0)
```
A call to assertEqual() to check for an expected result, and assertRaises() to verify that a specific exception gets raised.

### 3. Exercise
1. Complete 'test_calculate.py' to test four methods in 'calculate.py'.