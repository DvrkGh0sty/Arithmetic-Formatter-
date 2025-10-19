def arithmetic_arranger(problems, show_answers=False):
    return problems
def split_problems(problems):
    after_split = []
    for x in problems:
        after_split.append(x.split())
    return after_split
def main():
    print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])}')


print(split_problems(['3 + 4', '67 + 41']))