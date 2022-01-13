def func(string: str) -> str:
  print(string)
  uniqueCharacters = set(string)
  print(uniqueCharacters)
  for uniqueCharacter in uniqueCharacters:
    if string.count(uniqueCharacter) != 1:
      string = string.replace(uniqueCharacter, "*")
  return string

f = func('лол')
print(f)
