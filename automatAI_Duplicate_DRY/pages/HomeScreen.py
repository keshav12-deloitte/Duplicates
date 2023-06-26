import pandas
import math
import pandas as pd


class HomeScreen:

    def sum_two_numbers(self, a, b):
        c = a + b
        return c

    def subtraction_num(self, a, b):
        c = a - b
        return c

    def csv_reader(self):
        # reading the CSV file
        csvFile = pandas.read_csv('Giants.csv')
        # displaying the contents of the CSV file
        print(csvFile)

    def read_excelSheet_local(self, path):
        dataframe1 = pd.read_excel(path)
        print(dataframe1)

    def validator_prime_number(self, lo, hi, pe):
        for num in range(lo, hi + 1):
            flag = 0
            if num < 2:
                flag = 1
            if num % 2 == 0:
                continue
            if num % 3 == 0:
                continue
            iter = 2
            while iter < int(pow(num, 0.5)):
                if num % iter == 0:
                    flag = 1
                    break
                iter += 1
            if flag == 0:
                pe.append(num)
        print(pe)
