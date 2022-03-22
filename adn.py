word = tuple(input("Please write the syntax to be analyzted : "))
empty_dict = {}
for i in word:
  
  
  empty_dict[i] = (word.count(i))
print(empty_dict)
