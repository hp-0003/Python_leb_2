with open('example.txt', 'w') as file:
    file.write('Hello, world!')
    

print('File created and data written.')


with open('example.txt', 'r') as file:
    content = file.read()

print('File contents:', content)

