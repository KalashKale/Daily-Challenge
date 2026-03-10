import string

def find_unique_words(transcript):
  
  transcript = transcript.lower()
  transcript = transcript.translate(str.maketrans('','', string.punctuation))
  unique_words = len(set(transcript.split()))
  return unique_words

#test output
print(find_unique_words("Hello World!"))