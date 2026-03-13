def check_url(address):
  if address.startswith("http://"):
    domain = address[7:]
  elif address.startswith("https://"):
    domain = address[8:]
  else:
    return 'invalid'

  if "." not in domain:
    return 'invalid'

  for ch in domain:
    if not (ch.isalnum() or ch in '-.'):
      return 'invalid'
    
  return 'valid'

print(check_url("https://codedex.io"))
print(check_url("https://netflixcom"))