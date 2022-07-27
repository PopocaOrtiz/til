# Data Structures & Algorithms by Goodrich, Tamasia & Goldwasser
- part of the curriculum of computer science engineering degrees
- design, analysis and implementation of algorithms
- beginning level data structures
- intermediate level introduction to algorithms
- ADT: abstract data type, list, bag, collection...
- ADT rather than collection of bytes and addresses
- differente implementation strategies for a particular ADT
- object oriented design patterns to organize those implementations into reusable components
- DS: data structure
- algorithm strategies for efficient realizations of common DS
- algorithm performance, common trade offs between competing strategies
- use existing DS and algorithms found in libraries
- many example aplications
    - file systems
    - matching tags in structured formats(HTML)
    - simple cryptography
    - text frequency analysis
    - automated geometric layout
    - Huffman coding
    - DNA sequence alignment
    - search engine indexing
- differences with other books of those authors
    - code redesigned to use python features like generators
    - ADT consistent interface with python's data types and python's collections module
    - dynamic matrix fundamentals for lists, tuples and str
- online help
    - hints to all excersises
    - solutions to excersises
- contents and organization
    - fundational techniques like algorithm analysis and recursion
    - memory management
    - seven most important functions for algorithm analysis, sections that don't use those functions are optional and indicated with a star (⋆)

## Python overview
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

# Further reading
https://bcs.wiley.com/he-bcs/Books?action=index&itemId=1118290275&bcsId=8029
https://stackoverflow.com/questions/10267084/what-is-adt-abstract-data-type#:~:text=Commonly%20used%20ADT'S%20include%3A%20Linked,Hash%20Tables%20and%20many%20others.


page 11