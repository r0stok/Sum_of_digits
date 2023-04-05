def sum_of_digits():
    num = input("Input value: ")
    sum=0

    sum = sum(int(i) for i in num)
print("Output result:", sum)

sum_of_digits()