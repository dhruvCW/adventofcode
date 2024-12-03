from parsers.day03 import Operation, parse_from_file


def process_mul_instruction(input: str) -> int:
    operations = parse_from_file(input)
    return sum(operation.x * operation.y for operation in operations)

class SkipMul:
    def __init__(self):
        self.disabled = False

    def __call__(self, operation: Operation) -> bool:
        if operation.instruction == 'do':
            self.disabled = False
        elif operation.instruction == "don't":
            self.disabled = True
        elif operation.instruction == 'mul':
             return self.disabled
        
        return True
        

def process_all_instructions(input: str) -> int:
    operations = parse_from_file(input)
    skip = SkipMul()
    
    return sum(operation.x * operation.y for operation in operations if not skip(operation))
        