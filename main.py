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

def count_words(content):
  """
  Counts the number of words in the content and returns it as a number.

  Args:
    content: the content as (very long) string

  Returns:
    the words counted.
  """
  return len(content.split())

def main():
  """
  Just uses the other functions in this code to create an executable program.
  """
  content = get_book_text("books/frankenstein.txt")
  words = count_words(content)
  print(f"{words} words found in the document")

main()
