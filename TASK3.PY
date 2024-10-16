def swap_first_last_words(sentence):

  words = sentence.split()
  words[0], words[-1] = words[-1], words[0]
  return ' '.join(words)

# Приклад використання:
my_sentence = "Це приклад речення для демонстрації задачі"
result = swap_first_last_words(my_sentence)
print(result)  # Виведе: "задачі приклад речення для демонстрації Це"
