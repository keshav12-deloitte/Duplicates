import math


class paymentScreen:

    def sum_two_numbers(self, a, b):
        c = a + b
        return c

    def readAndWriteText(self):
        file1 = open("myfile.txt", "w")
        L = ["This is Delhi \n", "This is Paris \n", "This is London \n"]
        file1.writelines(L)
        file1.close()
        # Append-adds at last
        file1 = open("myfile.txt", "a")  # append mode
        file1.write("Today \n")
        file1.close()
        file1 = open("myfile.txt", "r")
        print("Output of Readlines after appending")
        print(file1.readlines())
        print()
        file1.close()

    def asfsaf(self, a, b):
        soo = math.ceil(a * b)
        return soo

    def rajajaijdaisjf(self):
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        # Sum of the two input numbers
        sum = num1 + num2
        # Output the result
        print("The sum of", num1, "and", num2, "is", sum)

    def prime_checker_ValidateChecker(self, low, high, primes):
        for num in range(low, high + 1):
            flag = 0
            if num < 2:
                flag = 1
            if num % 2 == 0:
                continue
            if num % 3 == 0:
                continue
            iter = 3

            while iter < int(pow(num, 0.5)):
                if num % iter == 0:
                    flag = 1
                    break
                iter += 2
            if flag == 0:
                primes.append(num)

        print(primes)
