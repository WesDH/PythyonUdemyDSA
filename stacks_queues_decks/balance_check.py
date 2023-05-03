from stack_si import Stack 

def balance_check(s):
    if len(s) % 2 != 0:
        return False

    stack = Stack()
    opening = set("([{")
    pairs = {"()", "{}", "[]"}

    for a_bracket in s:
        if a_bracket in opening:
            stack.push(a_bracket)
        else:
            closing_bracket = a_bracket
            if stack.is_empty() == True:
                return False
            opening_bracket = stack.pop()
            if opening_bracket + closing_bracket not in pairs:
                return False
    return stack.is_empty()


if __name__ == "__main__":
    print(balance_check('[]'))
    print(balance_check('([])'))
    print(balance_check(')[)]'))
