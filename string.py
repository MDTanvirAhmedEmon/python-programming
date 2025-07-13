hello = "hello python"
print(hello)
print(type(hello))

for i in hello:
    print(i)

# print(hello[50]) IndexError: string index out of range

print(len(hello))

print(hello[len(hello) - 1])
print(hello[- 1]) #nagative indexing

print(hello.upper())

txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")

print(txt[2:5])

price = 59
txt2 = f"The price is {price:.2f} dollars"
print(txt2)
