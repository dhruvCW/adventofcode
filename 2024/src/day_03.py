from parsers.day03 import parse_from_file


def process_mul_instruction(input: str) -> int:
    operations = parse_from_file(input)
    return sum(operation.x * operation.y for operation in operations)

def process_all_instructions(input: str) -> int:
    enabled = True
    summation = 0
    operations = parse_from_file(input)

    for operation in operations:
        if operation.instruction == 'do':
            enabled = True
        elif operation.instruction == "don't":
            enabled = False
        elif operation.instruction == 'mul' and enabled:
            summation += operation.x * operation.y

    return summation
        