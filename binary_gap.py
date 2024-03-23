import decimal


def binaryGap(num):
     diff = []
     gap = 0
     index = []

     for i in range(len(num)):
          if int(num[i]) == 1:
               index.append(i)
     print(f"The indices with 1's are: {index}")

     for n in range(len(index) - 1):
          dif = index[n + 1] - index[n] - 1
          diff.append(dif)
     print(f"the gaps are: {diff}")

     if len(diff) == 1:
          gap = diff[0]
     else:
          for x in range(len(diff) - 1):
               if diff[x] > diff[x + 1]:
                    gap = diff[x]
               elif diff[x] < diff[x + 1]:
                    gap = diff[x + 1]

     return gap

def main():
     num = int(input("Enter a positive integer: "))

     num_bin = bin(num)
     num_bin2 = num_bin[2::]

     print(f"The binary rep of {num} is: {num_bin2}")

     gap = binaryGap(num_bin2)
     print(f"The binary gap of {num_bin2} is: {gap}")

if __name__ == "__main__":
    main()
