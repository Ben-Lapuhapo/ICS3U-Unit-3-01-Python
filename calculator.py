#!/usr/bin/env python3

# Created by: Ben Lapuhapo
# Created on: September 25 2019
# This program is a simple calculator


def main():
    print("")
    number_1 = int(input("Please enter the First Number: "))
    print("")
    number_2 = int(input("Please enter the Second Number: "))
    total = number_1 + number_2
    print("")
    print('{} + {} = '.format(number_1, number_2), number_1 + number_2)


if __name__ == "__main__":
    main()
