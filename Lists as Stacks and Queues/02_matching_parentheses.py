def extract_parentheses(expression):
    parentheses = []
    stack = []

    for i, char in enumerate(expression):
        if char == '(':
            stack.append(i)
        elif char == ')':
            if stack:
                start = stack.pop()
                parentheses.append(expression[start:i+1])

    return parentheses

if __name__ == "__main__":
    expression = input("Enter an algebraic expression with parentheses: ")
    extracted_parentheses = extract_parentheses(expression)
    print("Extracted parentheses:")
    for p in extracted_parentheses:
        print(p)
