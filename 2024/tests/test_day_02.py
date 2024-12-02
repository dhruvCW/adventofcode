import pytest
from day_02 import is_safe, problem_dampner, problem_dampner_safe_report_count, safe_report_count

class TestDay02:
    @pytest.mark.parametrize('report, result', [
        ([7, 6 ,4 ,2 ,1], True),
        ([1, 2, 7, 8, 9], False), 
        ([9, 7, 6, 2, 1], False), 
        ([1, 3, 2, 4, 5], False),
        ([8, 6, 4, 4, 1], False), 
        ([1, 3, 6, 7, 9], True)
    ])
    def test_is_safe(self, report, result):
        assert is_safe(report) == result

    @pytest.mark.parametrize('report, result', [
        ([7, 6 ,4 ,2 ,1], True),
        ([1, 2, 7, 8, 9], False), 
        ([9, 7, 6, 2, 1], False), 
        ([1, 3, 2, 4, 5], True),
        ([8, 6, 4, 4, 1], True), 
        ([1, 3, 6, 7, 9], True)
    ])
    def test_problem_dampner_is_safe(self, report, result):
        assert problem_dampner(report, is_safe) == result


    @pytest.mark.parametrize("data_file, count", [
        ('data/day_02_sample.txt', 2), 
        ('data/day_02.txt', 371)
    ])
    def test_safe_report_count(self, data_file, count):
        assert safe_report_count(data_file) == count

    @pytest.mark.parametrize("data_file, count", [
        ('data/day_02_sample.txt', 4), 
        ('data/day_02.txt', 426)
    ])
    def test_problem_dampner_safe_report_count(self, data_file, count):
        assert problem_dampner_safe_report_count(data_file) == count