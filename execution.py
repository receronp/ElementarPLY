import json
import elementar as el

execution_temp_stack = [None] * 10


def main():
    # el.parse("test_files/numbers.el")
    el.parse("test_files/roots.el")
    program_count = 0
    while program_count < len(el.jump_stack):
        if el.jump_stack[program_count][0] == "Gz":
            program_count = int(el.jump_stack[program_count][1])
        elif el.jump_stack[program_count][0] == "Gzf":
            value = get_val(program_count, 1)
            if value == False:
                program_count = el.jump_stack[program_count][2]
            else:
                program_count += 1
        elif el.jump_stack[program_count][0] == "AUS":
            val = get_val(program_count, 1)
            print(val)
            program_count += 1
        elif el.jump_stack[program_count][0] == "EIN":
            value = input()
            while len(value) == 0:
                value = input()
            value = fix_type(value, program_count)
            el.variable_table[el.jump_stack[program_count][1]]["value"] = value
            program_count += 1
        else:
            evaluate(program_count)
            program_count += 1
    with open("./data_tables/variable_table.json", "w") as var_output:
        var_output.write(json.dumps(el.variable_table, indent=2))
    with open("./data_tables/subroutine_table.json", "w") as subprocess_output:
        subprocess_output.write(json.dumps(el.subroutine_table, indent=2))
    with open("./data_tables/jump_stack.json", "w") as jump_stack_output:
        jump_stack_output.write(json.dumps(el.jump_stack, indent=2))


def evaluate(count):
    if el.jump_stack[count][0] == "=":
        value = fix_type(get_val(count, 2), count)
        el.variable_table[el.jump_stack[count][1]]["value"] = value
    elif el.jump_stack[count][0] in "+ - * / %".split():
        operator1 = get_val(count, 2)
        operator2 = get_val(count, 3)
        if el.jump_stack[count][0] == "+":
            execution_temp_stack[int(el.jump_stack[count][1][0])] = (
                operator1 + operator2
            )
        elif el.jump_stack[count][0] == "-":
            execution_temp_stack[int(el.jump_stack[count][1][0])] = (
                operator1 - operator2
            )
        elif el.jump_stack[count][0] == "*":
            execution_temp_stack[int(el.jump_stack[count][1][0])] = (
                operator1 * operator2
            )
        elif el.jump_stack[count][0] == "/":
            execution_temp_stack[int(el.jump_stack[count][1][0])] = (
                operator1 / operator2
            )
        elif el.jump_stack[count][0] == "%":
            execution_temp_stack[int(el.jump_stack[count][1][0])] = (
                operator1 % operator2
            )
    elif el.jump_stack[count][0] in "> >= == != <= <".split():
        operator1 = get_val(count, 2)
        operator2 = get_val(count, 3)
        if el.jump_stack[count][0] == ">":
            execution_temp_stack[int(el.jump_stack[count][1][0])] = (
                operator1 > operator2
            )
        elif el.jump_stack[count][0] == ">=":
            execution_temp_stack[int(el.jump_stack[count][1][0])] = (
                operator1 >= operator2
            )
        elif el.jump_stack[count][0] == "==":
            execution_temp_stack[int(el.jump_stack[count][1][0])] = (
                operator1 == operator2
            )
        elif el.jump_stack[count][0] == "!=":
            execution_temp_stack[int(el.jump_stack[count][1][0])] = (
                operator1 != operator2
            )
        elif el.jump_stack[count][0] == "<=":
            execution_temp_stack[int(el.jump_stack[count][1][0])] = (
                operator1 <= operator2
            )
        elif el.jump_stack[count][0] == "<":
            execution_temp_stack[int(el.jump_stack[count][1][0])] = (
                operator1 < operator2
            )


def get_val(count, index):
    if type(el.jump_stack[count][index]) == list:
        return execution_temp_stack[int(el.jump_stack[count][index][0])]
    elif (
        type(el.jump_stack[count][index]) == str
        and el.jump_stack[count][index] in el.variable_table
    ):
        return el.variable_table[el.jump_stack[count][index]]["value"]
    else:
        return el.jump_stack[count][index]


def fix_type(val, count):
    if el.variable_table[el.jump_stack[count][1]]["type"] == "word":
        return int(val)
    elif el.variable_table[el.jump_stack[count][1]]["type"] == "float":
        return float(val)
    else:
        return val


if __name__ == "__main__":
    main()
