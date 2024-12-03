import pytest
from day_03 import process_all_instructions, process_mul_instruction

class TestDay01:
    @pytest.mark.parametrize("data_file, result", [('data/day_03_sample.txt', 161), ('data/day_03.txt', 178886550)])
    def test_process_mul_instruction(self, data_file, result):
        assert process_mul_instruction(data_file) == result

    @pytest.mark.parametrize("data_file, result", [('data/day_03_sample.txt', 48), ('data/day_03.txt', 87163705)])
    def test_process_all_instructions(self, data_file, result):
        assert process_all_instructions(data_file) == result