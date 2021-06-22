def logical_calc(array, op):
    result = 0
    if op == "AND":
        if len(array) == 2:
            result = array[0] & array[1]
        else:
            for i in range(0, len(array)-1):
                result = array[i] & array[i+1]
                array.append(result)
                array.pop(i)
                array.pop(i)
                if len(array) == 2:
                    break
            result = array[0] & array[1]

    elif op == "OR":
        if len(array) == 2:
            result = array[0] | array[1]
        else:
            for i in range(0, len(array)-1):
                result = array[i] | array[i+1]
                array.append(result)
                array.pop(i)
                array.pop(i)
                if len(array) == 2:
                    break
            result = array[0] | array[1]

    elif op == "XOR":
        if len(array) == 2:
            result = array[0] ^ array[1]
        else:
            for i in range(0, len(array)-1):
                result = array[i] ^ array[i+1]
                array.append(result)
                array.pop(i)
                array.pop(i)
                if len(array) == 2:
                    break
            result = array[0] ^ array[1]

    return result

print(logical_calc([True, True], "XOR"))
