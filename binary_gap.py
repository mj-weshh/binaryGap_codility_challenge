#this function calculates the binary gap of a binary code
def binaryGap(num):
     differences = []
     gap = 0
     index = []

     #this for loop picks the indices of 1's in the binary code and stores them in a list named index
     for i in range(len(num)):
          if int(num[i]) == 1:
               index.append(i)
     print(f"The indices with 1's are: {index}")

     #this for loop calculates/counts the gaps present in the binary code and stores them in differences
     for n in range(len(index) - 1):
          difference = index[n + 1] - index[n] - 1
          differences.append(difference)
     print(f"the gaps are: {differences}")

     #if there is only one gap in differences then the difference becomes the binaryGap for the binary code
     if len(differences) == 1:
          gap = differences[0]

     #if there are more than one gaps in the list(differences) then the loop is implemented
     else:
          #if there are more than one, the greatest difference is assigned to gap
          gap = max(differences)
                    
     #the function returns gap
     return gap

def main():
     #asking for input from the user
     num = int(input("Enter a positive integer: "))
     #converting the integer into binary format
     num_bin = bin(num)
     #removing '0b' which is a signal that it is a binary code to remain with just the binary code
     num_bin2 = num_bin[2::]

     #outputs the representation of the users input as a binary code
     print(f"The binary rep of {num} is: {num_bin2}")

     #calling the binaryGap function and passing an argument and assigning it's return value to gap
     gap = binaryGap(num_bin2)
     #outputing the largest gap as the binary gap of the code to the user
     print(f"The binary gap of {num_bin2} is: {gap}")

#calling the main function
if __name__ == "__main__":
    main()
