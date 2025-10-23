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

def width_of_arithmetric(after_split):
    width = []
    for num in after_split:
        num1, operator, num2 = num
        if len(num1) > len(num2):
            padding = len(num1) + 2
            width.append(padding)
        else:
            padding = len(num2) + 2
            width.append(padding)
    return width


def format_arithmetic(after_split):
    top_rows = []
    bottom_rows = []
    dash_rows = []

    widths = width_of_arithmetric(after_split)
    for i in range(len(after_split)):
        num1, operator, num2 = after_split[i]
        width = widths[i]
        top_spaces = width - len(num1)
        bottom_spaces = (width - 1) - len(num2)
        top = (" " * top_spaces) + num1
        bottom = operator + (" " * bottom_spaces) + num2
        dash = "-" * width

        top_rows.append(top)
        bottom_rows.append(bottom)
        dash_rows.append(dash)

    arranged = "    ".join(top_rows) + "\n" + "    ".join(bottom_rows) + "\n" + "    ".join(dash_rows)
    return arranged

def main():
    print(format_arithmetic([['32', '+', '698'], ['3801', '-', '2'], ['45', '+', '43'], ['123', '+', '49']]))
main()

