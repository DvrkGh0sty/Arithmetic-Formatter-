def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        print('Error: Too many problems.')
    return problems
def split_problems(problems):
    after_split = [x.split()for x in problems]
    return after_split

def validate_split(after_split):
    while True:
        operations = ['+', '-']
        for pair in after_split:
            num1, operator, num2 = pair
            if operator not in operations:
                print('"Error: Operator must be '+' or '-'."')
                continue
            if len(num1) > 4 or len(num2) > 4:
                print('Error: Numbers cannot be more than four digits.')
                continue
            try:
                new_num1 = int(num1)
                new_num2 = int(num2)
            except ValueError:
                print('Error: Numbers must only contain digits.')
                continue
            print(f"valid problem: {num1}, {operator}, {num2}")
        else:
            break

def width(after_split):
    for num in after_split:
        num1, operator, num2 = pair
        if len(num1) > len(num2):
            return num1
        else:
            return num2


def main():
    print(f'\n{split_problems(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])}')
main()
#validate_split(split_problems(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))