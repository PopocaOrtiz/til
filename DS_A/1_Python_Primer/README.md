# 1 Python primer
- classes form the basis for all data types
- identifier implicitly associated with the memory address
- an identifier has no declared type but the value(object) has a definite type
- if an object support behaviors that affect its state, changes will be reflected in other references to the same object
- subsequent assignment statement breaks the alias
- literal form to create new instances of a class
- `data.sort()`  # order a list
- **accessors** returns information about the state but don't affect that state
- **mutator** or **update methods** do change the state of an object
- `int(value, 16)`  # conversion from a different base
- **float** like a double in java rather than languages' float type
    - 2.0 equivalent to 2.
    - 6.02e23 scientific notation, represents the mathematical value 6.02 * 10^23
- **sequence** types, in which the order is significant
- a list is a **referential** structure, it stores a sequence of references
- a **set** is based on a hash table
    - only allows **immutable** types like tupes but not list or sets, frozensets are allowed
    - {} represents an empty dict not a set
- **dict**
    - dictionary or mapping
    - [(key, value)]
    - doesn't support operators such as
- **compound expressions** two or more operations
- use `is` or `is not` only when is necessary to detect true aliasing (or with None)
- `n/m, q = n // m, r = n % m then q * m + = n`
    - when the divisor is positive `0 ≤ r < m`
    - when the divisor is negative `m < r ≤ 0`
- `~` bitwise complement
- `^` bitwise exclusive or
- **open interval** an interval that doesn't contains its end points
- sequences can be compared with the greater, less operands
- **sets**
    - s1 ≤ s2, s1 is a subset of s2
    - s1 < s2, s1 is a proper subset of s2
    - s1 | s2, union
    - s1 & s2, intersection
    - s1 - s2, elements in s1 but not in s2
    - s1 ^ s2, elements in s1 or s2
    - **lexicographic** = **alphabetical order**
    - **disjoint sets** sets that doesn't have any element in common
- unary operators and exponentiation are evaluated from right to left
- **functions** vs **methods**
- each time a function is called python creates an activation record
- **formal parameters** vs **actual parameters**
- **polymorphic** support for more than one calling signature
- **collections.Iterable** used by all Python's iterable container types, guarantee support for the for-loop syntaxis
- **try-except-raise**
    - except (Exception1, Exception2)
    - raise (without any subsequent argument)
    - except (without any identified error types) catch any other exceptions that ocurred
    - **finally** executes even with an uncaught or a re-raised exception
- 1.8 iterators and generators
    - iterator i, returns an element when calling next(i)
    - iterable i, returns an iterator when calling iter(i)
    - `iter([]) -> list_iterator`  # that iterator doesn't store its own copy of the list but the current index, so it can report an update version of an specific index
    - return(without a value) can be used to stop a generator
    - k * k < n => k < sqrt(n)
    - searching factors can avoid the half of the series cause if n % k \== m then n % m \== n and after sqrt(n) the couples star to repeat but this way will produce an unordered sequence
    - there are not comprehension for tuples, the sintaxys is used for generators
    - unpack in a for loop: `for x,y in [(x1,y1),(x2,y2),...]`
- 1.10 Scopes an namespaces
    - `dir()` return the names in the current scope
    - `vars()` return local variables in the current scope
**random**
- next number in a pseudo-random generator is determined by the previous number(s)
- independent instances of the Random class but also a global single generator instance

## Exercises of Creativity

- **[C-1.18](C_1_18.py):** Reproduce a list with a comprehension
- **[C-1.20](C_1_20.py):** Custom random.shuffle function using random.randint
- **[C-1.21](C_1_21.py):** Read lines until EOF, then prints them in reverse order 
- **[C-1.22](C_1_22.py):** Dot product of two arrays 
- **[C-1.23](C_1_23.py):** In a list add an element that may be out of bounds
- **[C-1.24](C_1_24.py):** Count number of vowels in a string
- **[C-1.25](C_1_25.py):** Remove punctuations from a string
- **[C-1.26](C_1_26.py):** Determine if numbers form a valid formula
- **[C-1.27](C_1_27.py):** Return factors of a number in incremental order
- **[C-1.28](C_1_28.py):** Calculate the p-norm of a vector

## Projects

- **[P-1.29](C_1_29.py):** All posible strings formed by a group of characters
- **[P-1.30](C_1_30.py):** Times a number can be repeatedly divided by 2
- **[P-1.31](C_1_31.py):** Calculate the amount of bills and coins for a given
- **[P-1.32](C_1_32.py):** Calculator that receives an operator or a number at
  a time
- **[P-1.33](C_1_33.py):** Calculator that receives many operations in a single
  input
change

