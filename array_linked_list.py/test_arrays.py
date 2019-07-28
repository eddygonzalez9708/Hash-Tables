import pytest

from arrays import (
  Array,
  resize_array,
  array_read,
  array_insert,
  array_append,
  array_remove,
  array_pop,
  array_print)

def test_one_arrays(capsys):
  # Instatiate Array
  arr = Array(1)

  # Insert item to the array
  array_insert(arr, "STRING1", 0)
  # Print the array items
  array_print(arr)

  # Test the output of the array print function
  captured = capsys.readouterr()
  assert captured.out == "[STRING1]\n"

  # Pop first item from the array
  array_pop(arr, 0)
  # Print the array items
  array_print(arr)

  # Test the output of the array print function
  captured = capsys.readouterr()
  assert captured.out == "[]\n"
  
  # Insert item to the array
  array_insert(arr, "STRING1", 0)
  # Append item to the end of the array
  array_append(arr, "STRING4")
  # Insert item to the array at index 1
  array_insert(arr, "STRING2", 1)
  # Insert item to the array at index 2
  array_insert(arr, "STRING3", 2)
  # Print the array items
  array_print(arr)

  # Test the output of the array print function
  captured = capsys.readouterr()
  assert captured.out == "[STRING1, STRING2, STRING3, STRING4]\n"
  
def test_two_arrays(capsys):
  # Instatiate Array
  arr = Array(5)

  # Append item to the end of the array
  array_append(arr, 0)
  # Append item to the end of the array
  array_append(arr, 1)
  # Append item to the end of the array
  array_append(arr, 2)
  # Print the array items
  array_print(arr)

  # Test the output of the array print function
  captured = capsys.readouterr()
  assert captured.out == "[0, 1, 2]\n"

  # Insert item to the array at index 0
  array_insert(arr, -1, 0)
  # Insert item to the array at index 2
  array_insert(arr, 1.5, 3)
  # Insert item to the array at index 5
  array_insert(arr, 3, 5)
  # Print the array items
  array_print(arr)

  # Test the output of the array print function
  captured = capsys.readouterr()
  assert captured.out == "[-1, 0, 1, 1.5, 2, 3]\n"

  # Pop the last item from array
  assert array_pop(arr) == 3
  # Pop the first item from array
  assert array_pop(arr, 0) == -1
  # Pop the third item from array
  assert array_pop(arr, 2) == 1.5
  # Print the array items
  array_print(arr)

  # Test the output of the array print function
  captured = capsys.readouterr()
  assert captured.out == "[0, 1, 2]\n"

  # Try popping an item at an index position that does not exist.
  array_pop(arr, 100)

  # Test the output of the array print function
  captured = capsys.readouterr()
  assert captured.out == "Error: Index 100 out of range.\n"

def test_three_arrays(capsys):
  # Instatiate Array
  arr = Array(5)

  # Try inserting an item at index position that does not exist.
  array_insert(arr, -1, -2)
 # Try inserting an item at index position that does not exist.
  array_insert(arr, 1.5, 3)
  # Try inserting an item at index position that does not exist.
  array_insert(arr, 3, 100)

  # Ready array at index 0
  assert array_read(arr, 0) == -1
  # Read array at index 2
  assert array_read(arr, 1) == 1.5
  # Read array at index 2
  assert array_read(arr, 2) == 3
  # Try reading array at an index position that does not exist
  array_read(arr, 100)

  # Test the output of the array print function
  captured = capsys.readouterr()
  assert captured.out == "Error: Index 100 out of range.\n"

  # Remove 3 from the array
  assert array_remove(arr, 3) == 3
  # Print the array items
  array_print(arr)

  # Test the output of the array print function
  captured = capsys.readouterr()
  assert captured.out == "[-1, 1.5]\n"

  # Try removing an item from the array that does not exist.
  array_remove(arr, 99)

  # Test the output of the array print function
  captured = capsys.readouterr()
  assert captured.out == "Error: 99 not in list.\n"