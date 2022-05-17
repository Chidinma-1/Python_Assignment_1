
# ASSIGNMENT ONE------------------------------------>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# name = input(
#     "Hi user, to calculate an average please input a maximum of three numbers press enter to continue")

# maximum_input_number = 3
# input_number_1 = int(input("Choose a number: "))
# input_number_2 = int(input("Choose a second number: "))
# input_number_3 = int(input("Choose a third number: "))

# result = ((input_number_1 + input_number_2 +
#           input_number_3)/maximum_input_number)


# print(int(result))

# TASK TWO
# input_statement = input("type your statement: ")

# print(input_statement.capitalize())

# # TASK TWO.2
# input_statement = input("type your statement: ")

# result = (input_statement.split())
# result[0] = result[0].upper()

# print(" ".join(result))


# TASK THREE
# message = "I are learning Python"

# x = message.replace("I", "You")
# print(x)


# TASK FOUR

# text = "I hope you had fun today in class"

# print(text.count("a"))

# ------------------------------------------------------------------------------------------------------------------
# ASSIGNMENT TWO

# def prime_number(number: int):
#     if number > 1:
#         for item in range(2, number):
#             if(number % item == 0):
#                 return False
#                 break
#         return True
#     return False


# primeNum = [a for a in range(98, 175) if prime_number(a)]
# print(primeNum)


# --------------------------------------------------------------------------------------------
# ASSIGNMENT THREE


def mean(total_terms):
    total = 0
    for num in total_terms:
        total = total + num
    return total / len(total_terms)


print(mean([13, 13, 13, 13, 14, 14, 16, 18]))


def median(total_terms):
    total_terms.sort()
    if len(total_terms) % 2 != 0:
        middle_value = int((len(total_terms)-1)/2)
        return total_terms[middle_value]
    elif len(total_terms) % 2 == 0:
        middle_value1 = int(len(total_terms)/2)
        midddle_value2 = int(len(total_terms)/2)-1
        return int(mean([total_terms[middle_value1], total_terms[midddle_value2]]))


print(median([13, 13, 13, 13, 14, 14, 16, 18]))


def variance(total_terms):
    mean_ = mean(total_terms)
    numerator = sum([(x - mean_)**2 for x in total_terms])
    variance_term = (numerator/(len(total_terms)-1))
    return variance_term


print(variance([13, 13, 13, 13, 14, 14, 16, 18]))


def standard_dev(total_terms):
    mean_ = mean(total_terms)
    numerator = sum([(x - mean_)**2 for x in total_terms])
    standard_deviation = (numerator/len(total_terms)) ** 0.5
    return standard_deviation


print(standard_dev([13, 13, 13, 13, 14, 14, 16, 18]))


def skewness(total_terms):
    mean_ = mean(total_terms)
    numerator = sum([(x - mean_)**3 for x in total_terms])
    std_div = standard_dev(total_terms)
    skewness_result = (numerator)/(len(total_terms)-1) * std_div**3
    return skewness_result


print(skewness([13, 13, 13, 13, 14, 14, 16, 18]))
