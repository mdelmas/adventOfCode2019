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
        if opcode == 1 or opcode == 2 or opcode == 7 or opcode == 8:
            param1 = program[i+1] if math.floor(program[i]/100) % 10 else program[program[i+1]]
            param2 = program[i+2] if math.floor(program[i]/1000) % 10 else program[program[i+2]]
            if opcode == 1 or opcode == 2:
                program[program[i+3]] = operations[opcode](param1, param2)
            elif opcode == 7:
                program[program[i+3]] = 1 if param1 < param2 else 0
            elif opcode == 8:
                program[program[i+3]] = 1 if param1 == param2 else 0
            i += 4
        elif opcode == 3:
            program[program[i+1]] = int(input())
            i += 2
        elif opcode == 4 :
            param = program[i+1] if math.floor(program[i]/100) % 10 else program[program[i+1]]
            print("Diagnostic code is " + str(param))
            i += 2
        elif opcode == 5 or opcode == 6:
            param1 = program[i+1] if math.floor(program[i]/100) % 10 else program[program[i+1]]
            param2 = program[i+2] if math.floor(program[i]/1000) % 10 else program[program[i+2]]
            if opcode == 5 and param1 != 0 or opcode == 6 and param1 == 0:
                i = param2
            else:
                i += 3
    return program[0]


program = [int(x) for x in open("./input").readlines()[0].split(',')]
result = runIntcodeProgram(program)
