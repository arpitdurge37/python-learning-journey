# from typing import List, Union, Tuple, Dict

# n : int = 5

# name : str = "harry"

# def sum(a: int, b: int) -> int:
#     return a+b
# sum(3)



from typing import List, Tuple, Dict, Union

# List of integers
number: List[int] = [1, 2, 3, 4, 5]

# TUPLE OF A STRING AND AN INTEGER
person: Tuple[str, int]= ("Alice", 30)

# Dictionary with string keys and integer values
scores: Dict[str, int] = {"Alice": 90, "Bob": 85}

# Union type for variables that can hold multiple types

identifier: Union[int, str] = "ID123"
idntifier = 12345 #Also valid 