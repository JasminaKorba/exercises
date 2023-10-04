def arithmetic_arranger(operations_problem):
    problems = operations_problem
    answer = False

    if len(problems) == 2 and problems[1] == True:
        problems, answer = problems

    if len(problems) > 5:
        return print("Error: Too many problems.")

    upper_number = []
    operation_symbol = []
    lower_number = []

    for operation in problems:
        splited_operation = operation.split(" ")
        upper_number.append(splited_operation[0])
        operation_symbol.append(splited_operation[1])
        lower_number.append(splited_operation[2])

    for symbol in operation_symbol:
        if symbol != "+" and symbol != "-":
            return print("Error: Operator must be '+' or '-'.")

    for number in upper_number:
        sliced_number = list(number)
        for slice in sliced_number:
            if slice not in "0123456789":
                return print("Error: Numbers must only contain digits.")

    for number in lower_number:
        sliced_number = list(number)
        for slice in sliced_number:
            if slice not in "0123456789":
                return print("Error: Numbers must only contain digits.")

    for number in upper_number:
        if len(number) > 4:
            return print("Error: Numbers cannot be more than four digits.")
    for number in lower_number:
        if len(number) > 4:
            return print("Error: Numbers cannot be more than four digits.")

    answers = []
    for index in range(len(problems)):
        if operation_symbol[index] == "+":
            answers.append(int(upper_number[index]) + int(lower_number[index]))
        if operation_symbol[index] == "-":
            answers.append(int(upper_number[index]) - int(lower_number[index]))

    for index in range(len(problems)):
        if len(upper_number[index]) > len(lower_number[index]):
            lower_number[index] = (
                " " * (len(upper_number[index]) - len(lower_number[index]))
            ) + lower_number[index]
        if len(upper_number[index]) < len(lower_number[index]):
            upper_number[index] = (
                " " * (len(lower_number[index]) - len(upper_number[index]))
            ) + upper_number[index]

    dashes = []
    for index in range(len(problems)):
        dashes.append(len(f"{operation_symbol[index]} {upper_number[index]}"))

    arranged_problems = ""

    if answer:
        for u_num in upper_number:
            arranged_problems += "  " + u_num + "    "
        arranged_problems += "\n"
        for index in range(len(problems)):
            arranged_problems += (
                operation_symbol[index] + " " + lower_number[index] + "    "
            )
        arranged_problems += "\n"
        for dash in dashes:
            arranged_problems += dash * "-" + "    "
        arranged_problems += "\n"
        for index in range(len(problems)):
            if dashes[index] > len(str(answers[index])):
                answers[index] = " " * (dashes[index] - len(str(answers[index]))) + str(
                    answers[index]
                )
            else:
                answers[index] = str(answers[index])
        for answer in answers:
            arranged_problems += answer + "    "
    else:
        for u_num in upper_number:
            arranged_problems += "  " + u_num + "    "
        arranged_problems += "\n"
        for index in range(len(problems)):
            arranged_problems += (
                operation_symbol[index] + " " + lower_number[index] + "    "
            )
        arranged_problems += "\n"
        for dash in dashes:
            arranged_problems += dash * "-" + "    "
        arranged_problems += "\n"

    return print(arranged_problems)


arithmetic_arranger(["32 + 69g8", "3801 - 2", "45 + 43", "123 + 49"])
arithmetic_arranger(["3801 - 2", "123 + 49"])
arithmetic_arranger(["1 + 2", "1 - 9380"])
arithmetic_arranger(["3 + 855", "3801 - 2", "45 + 43", "123 + 49"])
arithmetic_arranger(["11 + 4", "3801 - 2999", "1 + 2", "123 + 49", "1 - 9380"])
arithmetic_arranger(
    ["44 + 815", "909 - 2", "45 + 43", "123 + 49", "888 + 40", "653 + 87"]
)
arithmetic_arranger(["3 / 855", "3801 - 2", "45 + 43", "123 + 49"])
arithmetic_arranger(["24 + 85215", "3801 - 2", "45 + 43", "123 + 49"])
arithmetic_arranger(["98 + 3g5", "3801 - 2", "45 + 43", "123 + 49"])
arithmetic_arranger([["3 + 855", "988 + 40"], True])
arithmetic_arranger([["32 - 698", "1 - 3801", "45 + 43", "123 + 49", "988 + 40"], True])
