class Dificulty:

  def diff (self):

    # We check if the way to file is correct and if file exists.
    try:
      with open('data/words.txt', 'r', encoding='utf-8') as file: 
        words_all = file.read()
    except FileNotFoundError:
            print(f'File was not found. Please check the file and start again!')
            exit(1)
    words_split = []
    words_split = words_all.split("\n")

    easy_words = []
    medium_words = []
    hard_words = []
    # Letters that makes word harder in Latvian language
    hard_letters = ['Ā', 'Č', 'Ē', 'Ģ', 'Ī', 'Ķ', 'Ļ', 'Ņ', 'Š', 'Ū', 'Ž']

    #### dificulty 3. It's harder to gusess letter if there is less letters in word and it has special signs in it
    for words in words_split:
      for character in hard_letters:
        if character in words and len(words) < 7:
          hard_words.append(words)

    ### dificulty 2. Here is more letters but also it has special signs in it.
    for words in words_split:
      for character in hard_letters:
        if character in words and len(words) > 6:
          medium_words.append(words)

    #### difficulty 1. The easy way to guess the word if there is more letters in word and it has no special signs
    a = set(words_split)
    b = set(hard_words)
    c = set(medium_words)
    easy_words = a - b - c


    with open('data/easy_words.txt', 'w', encoding='utf-8') as file: 
      for word in set(easy_words):
        file.write(word + "\n")

    with open('data/medium_words.txt', 'w', encoding='utf-8') as file:
      for word in set(medium_words):
        file.write(word + "\n")

    with open('data/hard_words.txt', 'w', encoding='utf-8') as file:
      for word in set(hard_words):
        file.write(word + "\n")