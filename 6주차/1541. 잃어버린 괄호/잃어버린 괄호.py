import sys

formula = sys.stdin.readline()
formula_li = []
str_elem = ''

for i in range(len(formula)):
    if formula[i] == '+' or formula[i] == '-':
        formula_li.append(str_elem)
        formula_li.append(formula[i])
        str_elem = ''
    else:
        str_elem += formula[i]
    if i == len(formula) - 1:
        formula_li.append(str_elem)

res, plus_sum = 0, 0
is_minus = False

for i in range(len(formula_li)):
    if i == 0:
        res += int(formula_li[i])
        continue
    elif i == len(formula_li) - 1:
        plus_sum += int(formula_li[i])
        if is_minus:
            res -= plus_sum
        else:
            res += plus_sum
        break
    if formula_li[i] == '+':
        continue
    elif formula_li[i] == '-':
        if is_minus:
            res -= plus_sum
        else:
            res += plus_sum
        plus_sum = 0
        is_minus = True
    else:
        elem = int(formula_li[i])
        plus_sum += elem

print(res)        