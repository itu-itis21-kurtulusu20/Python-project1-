ratio_number = float(input("Enter the rational number: "))
int_part = int(ratio_number)
ratio_part = ratio_number - int_part
non_ratio_array = []
ratio_array = []
i = 0
while (ratio_part != 1):
    ratio_part *= 2
    if (ratio_part >= 1):
        ratio_array.append("1")
    else:
        ratio_array.append("0")

    i += 1
    if (ratio_part > 1):
        ratio_part -= 1


while(int_part != 0):
    remainder = int_part % 2
    int_part = int(int_part / 2)
    if (remainder == 1):
        non_ratio_array.append("1")
    else:
        non_ratio_array.append("0")


non_ratio_array.reverse()
print(*non_ratio_array, end = ".", sep='')
print(*ratio_array, sep='')