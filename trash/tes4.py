# with open("data.txt", 'r') as file:
#     for line in file:
#         print(line.strip())

# stop = input()
import random

counter = 0
line2 = []
with open("data.txt", 'r') as file:
    # каждая строчка с data.txt будет теперь отрабатывать for line in file кек
    for line in file:
        
        line2.append(line.strip())
        print(line2[counter]) # выведет каждую строчку с data.txt
        counter += 1

print(line2[2])

# with open("data.txt", 'r') as file:
#     # каждая строчка с data.txt будет теперь отрабатывать for line in file кек
    
#     for line in file:
#         counter += 1
#         print(counter)
#         line2 = line.strip()
#         print(line2)

# filename2 = []

# for i in range(0, counter):
#     print("aloe")
#     filename2.append(str(random.random()))
#     print(filename2[i])



stop = input()