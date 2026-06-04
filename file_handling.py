#File_Handling :


file = open("employees.txt", "w")   #open() Used to open a file.

file.write("1, Ajay, AI\n")        #write() Used to write data into the file.
file.write("2, Rahul, HR\n")
file.write("3, Priyanka, AI\n")     #/n is the new line charecter
file.write("4, Kiran, AI\n")
file.write("5, Sneha, HR\n")
file.write("6, Surya, Finance\n")
file.write("7, Ramesh, AI\n")
file.write("8, Pooja, HR\n")
file.write("9, Vikram, Finance\n")
file.write("10, Neha, AI\n")

file.close()      #close()Closes the file after work is finished.


file = open("employees.txt", "r")     # r Read mode.

content = file.read()

print(content)

file.close()


# output :
# 1, Ajay, AI
# 2, Rahul, HR
# 3, Priyanka, AI
# 4, Kiran, AI
# 5, Sneha, HR
# 6, Surya, Finance
# 7, Ramesh, AI
# 8, Pooja, HR
# 9, Vikram, Finance
# 10, Neha, AI