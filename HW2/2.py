num_list = []
for i in range(int(input())):
    num_list.append(input())
num_list = sorted(num_list, reverse = True)
print("".join(num_list))