# # def avg(sum,n) :
# #   return sum/n
# # print(avg(4,2))


def avg():
    list = []
    n = int(input("Enter number "))
    for i in range(n):
        val = int(input("Enter number "))
        list.append(val)

    return  sum(list)/n
        

print(avg())