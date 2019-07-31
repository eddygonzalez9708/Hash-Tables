## DAY 1

- [X] Your assignment is to implement a basic hash table in the `basic_hash_table` directory. You should be able to insert, read, and delete elements from the hash table. You do not need to handle collisions but should print a warning when you are overwriting an existing value.

- [X] Run your code by typing navigating to the directory then typing `python3 b_hashtables.py` in the terminal.

- [X] Run tests by typing `python3 b_hashtables_tests.py`.

## DAY 2

- [X] Your assignment is to upgrade your basic hash table to handle collisions with linked list chaining. You should be able to insert an arbitrary amount of elements into your hash table, regardless of table size, and read them back without any data loss. You should also implement a resizing function that doubles the size of your hash table and copies all elements into the new data structure.

- [X] Run your code by typing navigating to the directory then typing `python3 r_hashtables.py` in the terminal.

- [X] Run tests by typing `python3 r_hashtables_tests.py`.

### test`

## STRETCH GOALS

- [ ] Update your HashTable to automatically double in size when it grows past a load factor of 0.7.

- [ ] Update your HashTable to automatically halve in size when it shrinks past a load factor of 0.2. This should only occur if the HashTable has been resized past the initial size.

- [ ] Refactor tests to pass with your resizing HashTable.
