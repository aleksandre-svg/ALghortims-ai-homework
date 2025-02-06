a = 2323
b = 13131313
c = 232234
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
# ითვლის რამდენი c ს ჯერადია c დან b მდეა ან რამდენი c ს ჯერადი c დან a მდე, გადაამოწმეთ თუგინდათ