num_list = []
for i in range(int(input())):
    num_list.append(input())
print("".join(sorted(num_list, reverse = True)))
