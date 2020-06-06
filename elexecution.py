import json
import math
import elementar as el

execution_temp_stack = [None] * 10
sub_stack = []


def main():
    # el.parse("test_files/numbers.el")
    # el.parse("test_files/roots.el")
    # el.parse("test_files/p1.el")
    # el.parse("test_files/p2.el")
    # el.parse("test_files/p3.el")
    el.parse("test_files/p4.el")
    program_count = 0
    while program_count < len(el.jump_stack):
        if el.jump_stack[program_count][0] == "Gz":
            program_count = int(el.jump_stack[program_count][1])
        elif el.jump_stack[program_count][0] == "Gzf":
            value = get_val(el.jump_stack[program_count], 1)
            if value == False:
                program_count = el.jump_stack[program_count][2]
            else:
                program_count += 1
        elif el.jump_stack[program_count][0] == "Call":
            sub_stack.append(program_count + 1)
            program_count = int(el.jump_stack[program_count][1])
        elif el.jump_stack[program_count][0] == "RUKKHER":
            program_count = sub_stack.pop()
        elif el.jump_stack[program_count][0] == "AUS":
            for index in range(len(el.jump_stack[program_count][1])):
                val = get_val(el.jump_stack[program_count][1], index)
                print(val, end=" ")
            print()
            program_count += 1
        elif el.jump_stack[program_count][0] == "EIN":
            value = input()
            while len(value) == 0:
                value = input()
            variable = el.jump_stack[program_count][1][0]
            value = fix_type(value, variable)
            if el.variable_table[variable]["dimension"] == 0:
                assign_value(variable, value)
            else:
                position = [
                    get_val(el.jump_stack[program_count][1], 1),
                    get_val(el.jump_stack[program_count][1], 2),
                    get_val(el.jump_stack[program_count][1], 3),
                ]
                assign_value(variable, value, position)
            program_count += 1
        elif el.jump_stack[program_count][0] == "MITT":
            arr, mean = get_mean(program_count)
            el.variable_table[el.jump_stack[program_count][1]]["value"] = mean
            program_count += 1
        elif el.jump_stack[program_count][0] == "ABWEICH":
            arr, mean = get_mean(program_count)
            sum = 0
            for x in arr:
                sum += (x - mean) ** 2
            sd = math.sqrt(sum / (len(arr) - 1))
            el.variable_table[el.jump_stack[program_count][1]]["value"] = sd
            program_count += 1
        else:
            evaluate(program_count)
            program_count += 1
    with open("./data_tables/variable_table.json", "w") as var_output:
        var_output.write(json.dumps(el.variable_table, indent=2))


def evaluate(count):
    if el.jump_stack[count][0] == "=":
        variable = el.jump_stack[count][1]
        value = fix_type(get_val(el.jump_stack[count], 2), el.jump_stack[count][1])
        dimension = el.variable_table[variable]["dimension"]
        if dimension == 0:
            assign_value(variable, value)
        else:
            position = [
                get_val(el.jump_stack[count], 3),
                get_val(el.jump_stack[count], 4) if dimension > 1 else None,
                get_val(el.jump_stack[count], 5) if dimension > 2 else None,
            ]
            assign_value(variable, value, position)
    elif el.jump_stack[count][0] in "+ - * / %".split():
        operator1 = get_val(el.jump_stack[count], 2)
        operator2 = get_val(el.jump_stack[count], 3)
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
        operator1 = get_val(el.jump_stack[count], 2)
        operator2 = get_val(el.jump_stack[count], 3)
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


def get_val(table, index):
    if type(table[index]) == list:
        ret_value = None
        if table[index][0] in el.variable_table:
            if el.variable_table[table[index][0]]["dimension"] == 0:
                ret_value = el.variable_table[table[index][0]]["value"]
            elif el.variable_table[table[index][0]]["dimension"] == 1:
                position = get_val(table[index], 1)
                ret_value = el.variable_table[table[index][0]][0][position]
            elif el.variable_table[table[index][0]]["dimension"] == 2:
                position_x = get_val(table[index], 1)
                position_y = get_val(table[index], 2)
                ret_value = el.variable_table[table[index][0]][position_x][position_y]
            elif el.variable_table[table[index][0]]["dimension"] == 3:
                position_x = get_val(table[index], 1)
                position_y = get_val(table[index], 2)
                position_z = get_val(table[index], 3)
                ret_value = el.variable_table[table[index][0]][position_x][position_y][
                    position_z
                ]
        # elif
        else:
            ret_value = execution_temp_stack[int(table[index][0])]
        return ret_value
    elif type(table[index]) == str and table[index] in el.variable_table:
        return el.variable_table[table[index]]["value"]
    else:
        return table[index]


def assign_value(variable, value, position=[0, 0, 0]):
    if el.variable_table[variable]["dimension"] == 0:
        el.variable_table[variable]["value"] = value
    elif el.variable_table[variable]["dimension"] == 1:
        position = position[0]
        el.variable_table[variable][0][position] = value
    elif el.variable_table[variable]["dimension"] == 2:
        position_x = position[0]
        position_y = position[1]
        el.variable_table[variable][position_x][position_y] = value
    elif el.variable_table[variable]["dimension"] == 3:
        position_x = position[0]
        position_y = position[1]
        position_z = position[2]
        el.variable_table[variable][position_x][position_y][position_z] = value


def get_mean(count):
    sum = 0
    arr = [x for x in el.variable_table[el.jump_stack[count][2]][0] if x is not None]
    for x in arr:
        sum += x
    return arr, sum / len(arr)


def fix_type(value, variable):
    try:
        if el.variable_table[variable]["type"] == "word":
            return int(math.floor(float(value)))
        elif el.variable_table[variable]["type"] == "float":
            return float(value)
        else:
            return value
    except:
        return None


if __name__ == "__main__":
    main()
