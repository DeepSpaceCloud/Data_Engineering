filename = 'text_2_var_18'
with open(filename) as file:
    lines = file.readlines()
sum_lines = list()
for line in lines:
    nums = line.split(" ")
    sum_line = 0
    for num in nums:
        sum_line += int(num)
    sum_lines.append(sum_line)
with open('r_text_2.txt', 'w') as result:
    for value in sum_lines:
        result.write(str(value)+"\n")
