a = 3
b = 42
c = 7
if c < a and c > b or c < b and c > a:
    def jeradi(num1, num2, num3):
        if num2 < num1 and num2 > num3 or num1 < num3 and num2 > num1:
            if num1 > num3:
                return int(num1/num2)
            elif num3 > num1:
                return int(num3/num2)
            else:
                return 'erron'
print(jeradi(a, c, b))
# დავალებად იყო მარტო პირველი ,რადგან გაკვეთლზეც თვქეს მეორე და მესამე არ გვქონია დავალებად რადგან არ გაგვივლია ჯერ.