import math


def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

operations = { 1: add, 2: multiply }


def runIntcodeProgram(program):
    i = 0
    while i < len(program):
        opcode = program[i] % 100
        if opcode == 99:
            break
        if opcode == 1 or opcode == 2:
            param1 = program[i+1] if math.floor(program[i]/100) % 10 else program[program[i+1]]
            param2 = program[i+2] if math.floor(program[i]/1000) % 10 else program[program[i+2]]
            program[program[i+3]] = operations[opcode](param1, param2)
            i += 4
        elif opcode == 3:
            program[program[i+1]] = int(input())
            i += 2
        elif opcode == 4:
            param = program[i+1] if math.floor(program[i]/100) % 10 else program[program[i+1]]
            print("Output is " + str(param))
            i += 2
    return program[0]


program = [int(x) for x in open("./input").readlines()[0].split(',')]
result = runIntcodeProgram(program)
