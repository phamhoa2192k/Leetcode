import sys


def solution(st):
    s = []
    operation = ["+", "-", "*", "/", "^"]
    result = ""
    for val in st:
        if val == "(":
            s.append(val)
        elif val == ")":
            while s and s[-1] != "(":
                result += s.pop()
            s.pop()
        elif val in operation:
            s.append(val)
        else:
            result += val
    return result


def main():
    import time
    start_time = time.time()
    input = sys.stdin.read().split()
    for s in input[1:]:
        print(solution(s))
    print("--- %s seconds ---" % (time.time() - start_time))


main()
