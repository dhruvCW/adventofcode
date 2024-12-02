
from itertools import combinations, pairwise
from typing import Callable

from parsers.day02 import parse_from_file
from utils import count_if


def is_safe(report: list[int]) -> bool:
    prev_diff = None

    for level, next_level in pairwise(report):
        diff = level - next_level
        if 1 < abs(diff) > 3 or (prev_diff is not None and (prev_diff * diff) <= 0):
            return False
        
        prev_diff = diff

    return True

def problem_dampner(reports: list[int], callable: Callable) -> bool:
    if callable(reports):
        return True
    
    for combination in combinations(reports, len(reports) - 1):
        if callable(combination):
            return True
        
    return False

def safe_report_count(input: str) -> int:
    reports = parse_from_file(input)
    return count_if(reports, is_safe)

def problem_dampner_safe_report_count(input: str) -> int:
    reports = parse_from_file(input)
    return count_if(reports, lambda report: problem_dampner(report, is_safe))

