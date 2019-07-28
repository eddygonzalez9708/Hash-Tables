'''
Basic hash table key/value pair
'''

class Pair:
  def __init__(self, key, value):
    self.key = key
    self.value = value

# Basic hash table

# Fill this in.
# All storage values should be initialized to None.

class BasicHashTable:
  def __init__(self, capacity):
    self.storage = [None] * capacity

# Fill this in.
# Research and implement the djb2 hash function

def hash(string, max):
  hash = 5381
  
  for character in string:
    hash = ((hash << 5) + hash) + ord(character)
   
  return hash % max

# Fill this in.
# If you are overwriting a value with a different key, print a warning.
  
def hash_table_insert(hash_table, key, value):
  # Receive generated index from hash function for key.
  index = hash(key, len(hash_table.storage))

  # If index is None, then memory location at index is available.
  # Else print warning
  if hash_table.storage[index] is None:
    hash_table.storage[index] = Pair(key, value)
  else:
    print('Warning: You cannot overwrite this location in memory with a different key and value pair.')

# Fill this in.
# If you try to remove a value that isn't there, print a warning.

def hash_table_remove(hash_table, key):
  # Receive generated index from hash function for key.
  index = hash(key, len(hash_table.storage))

  # Check if there is a value at the current index position
  if hash_table.storage[index] is not None:
    hash_table.storage[index] = None
  else:
    print(f'Warning: Key "{key}" cannot be removed because it does not exist.')

# Fill this in.
# Should return None if the key is not found.

def hash_table_retrieve(hash_table, key):
  # Receive generated index from hash function for key.
  index = hash(key, len(hash_table.storage))

  # Retrieve value at the current index position
  if hash_table.storage[index] is not None:
    return hash_table.storage[index].value
  else:
    print(f'Warning: Key "{key}" cannot be retrieved because it does not exist.')

def Testing():
  ht = BasicHashTable(16)

  hash_table_insert(ht, "line", "Here today...\n")

  hash_table_remove(ht, "line")

  if hash_table_retrieve(ht, "line") is None:
    print("...gone tomorrow (success!)")
  else:
    print("ERROR:  STILL HERE")

Testing()