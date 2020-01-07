# from random import *


# class What():

#     def words(self):
#         words = []
#         word = ''
#         chance = randint(0, 11)
#         while len(words) != self.total:
#             while len(word) != chance:
#                 if randint(0, 1) == 1:
#                     letter = self.alphabet[randint(0, 25)]
#                 else:
#                     letter = self.vowels[randint(0, 5)]
#                 word += letter
#             chance = randint(0, 10)
#             words.append(word)
#             word = ''
#         return words

#     def numbers(self):
#         nums = []
#         while len(nums) != self.total:
#             nums.append(randint(0, 10))
#         return nums

#     def match(self):
#         words = self.words()
#         lengths = self.numbers()
#         match = {}
#         for word, length in zip(words, lengths):
#             if len(word) == length:
#                 match[word] = length
#         return match

#     def average(self):
#         print("How many tests do you want to run? ")
#         tests = int(input())
#         num_matches = []
#         sum = 0
#         while len(num_matches) != tests:
#             num_matches.append(len(self.match()))
#         for index in range(len(num_matches)):
#             sum += num_matches[index]
#         print(sum)
#         return sum/tests

#     print("How many total items do you want to reach? ")
#     total = int(input())
#     alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
#                 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#     vowels = ['a', 'e', 'i', 'o', 'u', 'y']


# lol = What()
# print(lol.words())
# print(lol.average())

# from collections import defaultdict

# towns = defaultdict(lambda: "huh?")

# for i in range(1, 999+1):
#     towns[i] += 'lol'

# print(dict(towns))
# red, green, blue = (255, 250, 245)
# print(red, green, blue)


# cities = ['john', 'snow', 'hello', 'crystal', 'ter', 'marry', 'marry']
# random_list = []
# for i in set(cities):
#     random_list.append(i)
# print(random_list)

# Stopped here -----------------------------------------------------
# def factorialOf(number):
#     num_list = list(range(1, number+1))
#     factorial = 1
#     for index in range(len(num_list)):
#         if index != 0:
#             factorial *= num_list[index-1]
#     return factorial * number


# scope = range(0, 100+1)

# factorials = [factorialOf(num) for num in scope]
# match = set(zip(scope, factorials))
# print(match)
# evil = [[key, factorial]
#         for key, factorial in match if key <= 50]
# print(evil)
# for pair in evil.copy():
#     pair.append(pair[0]**2)
# # [pair.append(pair[0]**2) for pair in evil.copy()]
# [print(reg, factorial, square) for reg, factorial, square in evil]
# dexter = tuple(['hi', 'yo', 'face', 'hide'])
# for i, a, b, c in dexter:
#     print(i)
# --------------------------------------------------------------------------
# print(factorialOf(100))


# def first(message):
#     text = []
#     for i in town:
#         if i.isalpha() == False:
#             text.append('( ._.)')
#         else:
#             break
#     return text

class test():

    def text(self, block, string):
        if block == 1:
            return string
        elif block == 2:
            return string[len(self.first(string)):].rstrip(" ")
        elif block == 3:
            return ""

    def first(self, text):
        text = []
        for i in self.text(1, town):
            if i.isalpha() == False:
                text += ['( ._.)']
            else:
                break
        return text

    def second(self, text):
        text = []
        for i in self.text(2, town):
            if i == " ":
                text.append("( ._. )")
            else:
                text.append(i)
        return text

    def third(self, text):
        return ["(._. )" for i in self.text(2, town)]

    def run(self, message):
        print(self.first(message)+self.second(message)+self.third(message))


town = "      Flag of le merica         "

# print("".join(test().first(town))
print(test().second(town))
# print(test().third(town))
# print(test().run(town))
