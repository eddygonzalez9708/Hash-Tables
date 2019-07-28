# Do not use any of the built in array functions for this exercise

class Array:
  def __init__(self, capacity):
    self.elements = [None] * (capacity * 2)
    self.capacity = capacity * 2 
    self.count = 0

# Double the size of the given array

def resize_array(array):
  array.capacity *= 2
  new_array = [None] * array.capacity

  for i in range(array.count):
    new_array[i] = array.elements[i]
  
  array.elements = new_array[:]

# Return an element of a given array at a given index

def array_read(array, index):
  if index > -array.count and index < array.count:
    return array.elements[index]
  else:
    # Throw an error if array is out of the current count
    print(f"Error: Index {index} out of range.")

# Insert an element in a given array at a given index

def array_insert(array, value, index):
  # Resize the array if the number of elements is over capacity
  if array.count == len(array.elements):
    resize_array(array)
  
  # If index is greater than or equal to the current count.
  # Then, append the value at the end of the array.
  if index > array.count:
    array.elements[array.count] = value
    array.count += 1
    return
  elif index < 0 and index > -array.count:
    index = array.count - index
  elif index <= -array.count:
    index = 0

  # Move the elements to create a space at 'index'
  for i in range(array.count, index, -1):
    array.elements[i] = array.elements[i - 1]

  # Add the new element to the array and update the count
  array.elements[index] = value
  array.count += 1

# Add an element to the end of the given array

def array_append(array, value):
  # Hint, this can be done with one line of code.
  # (Without using a built in function)
  array_insert(array, value, array.count)

# Remove the first occurence of the given element from the array
# Throw an error if the value is not found

def array_remove(array, value):
  found = None

  for i in range(array.count):
    if array.elements[i] == value:
      found = i
      break
  
  if found is not None:
    return array_pop(array, i)
  else:
    print(f"Error: {value} not in list.")
 
# Remove the element in a given position and return it
# Then shift every element after that occurrance to fill the gap

def array_pop(array, index = None):
  if index == None:
    index = array.count - 1
  # Throw an error if array is out of the current count
  elif index <= -array.count or index >= array.count:
    print(f"Error: Index {index} out of range.")
    return
  elif index < 0:
    index = array.count - index

  value_removed = array.elements[index]

  for i in range(index, array.count):
    array.elements[i] = array.elements[i + 1]

  array.count -= 1
  return value_removed

# Utility to print an array

def array_print(array):
  string = "["
  for i in range(array.count):
    string += str(array.elements[i])
    if i < array.count - 1:
      string += ", "

  string += "]"
  print(string)