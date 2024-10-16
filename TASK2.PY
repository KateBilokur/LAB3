def find_longest_repeated_char(string):

  max_length = 0
  current_length = 1

  for i in range(1, len(string)):
    if string[i] == string[i-1]:
      current_length += 1
    else:
      max_length = max(max_length, current_length)
      current_length = 1

  return max_length

# Приклад використання:
my_string = "aaabbbccdddd"
result = find_longest_repeated_char(my_string)
print("Найбільша кількість однакових символів підряд:", result)
