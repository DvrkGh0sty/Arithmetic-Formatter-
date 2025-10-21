def arithmetic_arranger(problems, show_answers=False):
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
                print('Invalid operation, please either enter +, -.')
                continue
            try:
                new_num1 = int(num1)
                new_num2 = int(num2)
            except ValueError:
                print("The values have encountered an error, make sure that both numbers are integers, not decimals or negatives.")
                continue
            print(f"valid problem: {num1}, {operator}, {num2}")
        else:
            break

                    
def main():
    print(f'\n{split_problems(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])}')
main()
validate_split(split_problems(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))