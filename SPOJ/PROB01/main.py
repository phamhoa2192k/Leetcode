import sys


def solution(st):
    if len(st) == 1:
        return st
    else:
        return solution(str(sum([int(val) for val in st])))


def main():
    # import time
    # start_time = time.time()
    input = sys.stdin.read().split()
    for index, s in enumerate(input[1:], 1):
        print("#{n1} {n2}".format(n1 = index, n2 = solution(s)))
    # print("--- %s seconds ---" % (time.time() - start_time))


main()