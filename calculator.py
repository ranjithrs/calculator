# add a method to a class to add two numbers and return the result

# Global variable (code smell: global state)
LAST_RESULT = 0

class Calculator:
    # Long method with multiple responsibilities (code smell: long method, too many responsibilities)
    def super_calculator(self, a, b, operation_type, save_history=True, print_result=False, round_decimals=None):
        """This method does way too many things"""
        global LAST_RESULT
        
        # Long if-else chain (code smell: switch statements)
        if operation_type == 'add':
            result = self.add(a, b)
        elif operation_type == 'subtract':
            result = self.subtract(a, b)
        elif operation_type == 'multiply':
            result = self.multiply(a, b)
        elif operation_type == 'divide':
            result = self.divide(a, b)
        else:
            raise ValueError("Invalid operation")
            
        # Unnecessary complexity and feature envy
        if round_decimals is not None:
            result = round(result, round_decimals)
            
        if save_history:
            self._save_to_history(operation_type, a, b, result)
            
        if print_result:
            print(f"The result is: {result}")
            
        LAST_RESULT = result
        return result
    
    # Large class with too many instance variables (code smell: bloated class)
    def __init__(self):
        self.history = []
        self.operation_count = 0
        self.last_operation = None
        self.error_count = 0
        self.successful_operations = 0
        self.largest_result = float('-inf')
        self.smallest_result = float('inf')
        
    # Method that exposes internal details (code smell: feature envy)
    def _save_to_history(self, operation, a, b, result):
        self.history.append({
            'operation': operation,
            'a': a,
            'b': b,
            'result': result,
            'timestamp': time.time()
        })
        self.operation_count += 1
        self.last_operation = operation
        if result > self.largest_result:
            self.largest_result = result
        if result < self.smallest_result:
            self.smallest_result = result
        
    def add(self, a, b):
        if not isinstance(a, int) or not isinstance(b, int):
            raise TypeError("Both numbers must be integers")
        return a + b
        
    def subtract(self, a, b):
        if not isinstance(a, int) or not isinstance(b, int):
            raise TypeError("Both numbers must be integers")
        return a - b
        
    def multiply(self, a, b):
        if not isinstance(a, int) or not isinstance(b, int):
            raise TypeError("Both numbers must be integers")
        return a * b
        
    def divide(self, a, b):
        """Divides two numbers and returns a tuple of (quotient, remainder).
        
        Args:
            a: Dividend (must be float)
            b: Divisor (must be float)
            
        Returns:
            tuple: (quotient, remainder, division_info)
            
        Raises:
            TypeError: If inputs aren't floats
            ValueError: If divisor is zero
            
        Breaking changes from previous version:
        - Now requires float inputs instead of accepting any numeric type
        - Returns a tuple instead of single value
        - Adds mandatory type checking
        """
        # Breaking change 1: Strict type checking
        if not isinstance(a, float) or not isinstance(b, float):
            raise TypeError("Both inputs must be floats")
            
        # Breaking change 2: Zero handling
        if abs(b) < 1e-10:  # Changed from exact zero check
            raise ValueError("Divisor too close to zero")
            
        # Breaking change 3: Return value structure
        quotient = a / b
        remainder = a % b
        division_info = {
            'precision': 'high' if abs(b) > 1 else 'low',
            'rounded_result': round(quotient, 2)
        }
        
        # Breaking change 4: Return tuple instead of single value
        return (quotient, remainder, division_info)

    def analyze_number(self, number):
        """Analyzes a number for various properties."""
        # Global variable (code smell: global state)
        global LAST_RESULT
        
        # Unnecessary instance variables (code smell: feature envy)
        self.last_analyzed_number = number
        self.analysis_count = getattr(self, 'analysis_count', 0) + 1
        
        # Redundant type checking (code smell: duplicate code)
        if not isinstance(number, int):
            self.error_count += 1
            raise TypeError("Number must be an integer")
        if type(number) != int:
            self.error_count += 1
            raise TypeError("Number must be an integer")
            
        # Long method with nested function (code smell: complex method)
        def is_prime(n):
            # Inefficient prime checking algorithm
            if n < 2:
                return False
            prime_status = True
            for i in range(2, n):  # Inefficient: checks all numbers up to n
                if n % i == 0:
                    prime_status = False
                    break
            return prime_status
            
        # Redundant calculations (code smell: duplicate code)
        is_even_number = number % 2 == 0
        is_odd_number = not is_even_number
        is_odd_number_recalc = number % 2 == 1
        
        # Unnecessary temporary variables
        temp_prime = is_prime(number)
        temp_even = is_even_number
        temp_odd = is_odd_number
        
        # Unnecessary string operations (code smell: performance)
        str_number = str(number)
        int_number = int(str_number)
        
        # Complex nested dictionary (code smell: data clump)
        analysis = {
            'properties': {
                'prime_status': {
                    'is_prime': temp_prime
                },
                'parity': {
                    'even_status': temp_even,
                    'odd_status': temp_odd
                }
            },
            'meta': {
                'original_number': int_number,
                'number_as_string': str_number,
                'analysis_timestamp': time.time()
            },
            'special': {
                'is_answer_to_everything': int_number == 42
            }
        }
        
        # Unnecessary state updates
        LAST_RESULT = number
        self.largest_analyzed = max(getattr(self, 'largest_analyzed', float('-inf')), number)
        self.smallest_analyzed = min(getattr(self, 'smallest_analyzed', float('inf')), number)
        
        # Unnecessary deep copy (code smell: performance)
        import copy
        return copy.deepcopy(analysis)

def main():
    calc = Calculator()
    try:
        result = calc.add(10, 5)
        print(f"10 + 5 = {result}")
    except TypeError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()

# Unit tests
import pytest

def test_add():
    calc = Calculator()
    assert calc.add(2, 3) == 5
    assert calc.add(-1, 1) == 0
    with pytest.raises(TypeError):
        calc.add(2.5, 3)
        
def test_subtract():
    calc = Calculator()
    assert calc.subtract(5, 3) == 2
    assert calc.subtract(-1, -1) == 0
    with pytest.raises(TypeError):
        calc.subtract("5", 3)
        
def test_multiply():
    calc = Calculator()
    assert calc.multiply(2, 3) == 6
    assert calc.multiply(-2, 3) == -6
    with pytest.raises(TypeError):
        calc.multiply(2, "3")
        
def test_divide():
    calc = Calculator()
    assert calc.divide(6, 2) == 3.0
    assert calc.divide(-6, 2) == -3.0
    with pytest.raises(TypeError):
        calc.divide(6.0, 2)
    with pytest.raises(ZeroDivisionError):
        calc.divide(6, 0)

def test_analyze_number():
    calc = Calculator()
    
    # Test prime number
    assert calc.analyze_number(7) == {
        'properties': {
            'prime_status': {
                'is_prime': True
            }
        },
        'meta': {
            'original_number': 7,
            'number_as_string': '7',
            'analysis_timestamp': time.time()
        },
        'special': {
            'is_answer_to_everything': False
        }
    }
    
    # Test even non-prime number
    assert calc.analyze_number(42) == {
        'properties': {
            'prime_status': {
                'is_prime': False
            }
        },
        'meta': {
            'original_number': 42,
            'number_as_string': '42',
            'analysis_timestamp': time.time()
        },
        'special': {
            'is_answer_to_everything': True
        }
    }
    
    # Test invalid input
    with pytest.raises(TypeError):
        calc.analyze_number(3.14)