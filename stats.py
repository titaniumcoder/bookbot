def get_num_words(content):
  """
  Counts the number of words in the content and returns it as a number.

  Args:
    content: the content as (very long) string.

  Returns:
    the words counted.
  """
  return len(content.split())

def get_num_characters(content):
  """
  Counts the number of each possible character and symbols in the text and returns it as a dictionary

  Args:
    content: the content as (very long) string.

  Returns:
    a dictionary containing the characters and the count of them (including symbols)
  """
  lowered = content.lower()
  count = {}

  for c in lowered:
    if c in count:
      count[c] += 1
    else:
      count[c] = 1

  return count

def get_sorted_characters(num_characters):
  """
  Convert the dictionary into a sorted list of all characters with the most used characters first.

  Args:
    num_characters: a dictionary in the format of {"x": 33}

  Returns:
    a sorted list with [{"char": "x", "num": 33}]
  """
  result = [{"char": x, "num": num_characters[x]} for x in num_characters]
  result.sort(key=lambda c: c["num"], reverse=True)

  return result
  