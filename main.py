from stats import get_num_words,get_num_characters,get_sorted_characters
import sys

def get_book_text(file_path):
  """
  Reads the content of a book file and returns it as a string.
    
  Args:
    file_path: The path to the book file.
      
  Returns:
    The content of the book.
  """
  with open(file_path, 'r', encoding='utf-8') as file:
    return file.read()

def usage():
  print("Usage: python3 main.py <path_to_book>")

def main():
  if len(sys.argv) != 2:
    usage()
    exit(1)

  book = sys.argv[1]
  print("============ BOOKBOT ============")
  print(f"Analyzing book found at {book}...")

  content = get_book_text(book)
  num_words = get_num_words(content)
  print("----------- Word Count ----------")
  print(f"Found {num_words} total words")

  num_characters = get_num_characters(content)
  sorted_characters = get_sorted_characters(num_characters)
  print("--------- Character Count -------")
  for entry in sorted_characters:
    if entry["char"].isalpha():
      print(f"{entry["char"]}: {entry["num"]}")
  print("============= END ===============")

main()
