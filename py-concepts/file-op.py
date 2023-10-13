# File operations

# Reading a file ./ , ../../

# with open('../micro/backward-file.txt', 'r') as file:
#     fileContent = file.read()
#     print(fileContent)

# Write a file

# with open('../micro/backward-file.txt', 'w') as writtenFile:
#     isWriteSuccess = writtenFile.write('email: e@gmail.com')
#     print(isWriteSuccess)

# Appending to a file
with open('../micro/backward-file.txt', 'a') as appendingFile:
    isAppended = appendingFile.write('\nemail: e@gmail.com')
    print(isAppended)



























