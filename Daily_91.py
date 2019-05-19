# Problem the lambda function is not capture the value but the reference
functions = []
for i in range(10):
    functions.append(lambda: i)

for f in functions:
    print(f())

# How to fix it without changing the semantics?
# Add a default parameter to the lambda function
functions = []
for i in range(10):
    functions.append(lambda i=i: i)

for f in functions:
    print(f())
