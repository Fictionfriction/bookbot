def main():
    with open("books/frankenstein.txt") as f:
      file_contents = f.read()
    length = words(file_contents)
    count = char_count(file_contents)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{length} words found in the document")
    print()
    sorted_dict = dict(sorted(count.items(), key=lambda item: item[1], reverse=True))
    for char in sorted_dict:
       print(f"The '{char}' character was found {count[char]} times")

def words(file):
    words = file.split()
    return len(words)

def char_count(file):
    count = {}
    words = file.split()
    for word in words:
      char_list = list(word)
      for char in char_list:
        char = char.lower()
        if char not in count:
          count[char] = 1
        else:
          count[char] += 1
    return count

main()
