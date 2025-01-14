def find_pairs(num_string):
  nums = num_string.split()
  nums = [int(num) for num in nums]

  new_set = set()

  for num1 in nums:
    for num2 in nums:
      if num1 < num2:
        new_set.add((num1, num2))

  return new_set

# Test cases
assert find_pairs("7 3 99") == {(7, 99), (3, 7), (3, 99)}
assert find_pairs("2 1") == {(1, 2)}
assert find_pairs("24 7 365 94") == {(7, 94), (24, 94), (94, 365), (7, 365), (24, 365), (7, 24)}
assert find_pairs("94") == set()

print("All tests passed!")
print("Finished early? Discuss time & space complexity")