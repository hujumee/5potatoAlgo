import sys

num, name = sys.stdin.readline().split()
res = ""
original = []
removed_num = 0

for i in range(len(name)):
    if name[i] not in original:
        original.append(name[i])
        res += name[i]
    else:
        removed_num += 1
        
res += str(removed_num + 4)

num = int(num)
num += 1906
res = str(num) + res

reverse_name = list(res)
reverse_name.reverse()
res = ''.join(reverse_name)

res = "smupc_" + res

print(res)