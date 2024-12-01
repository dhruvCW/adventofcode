import pytest
from day_01 import total_distance, similarity_score

class TestDay01:
    @pytest.mark.parametrize("data_file, distance", [('data/day_01_sample.txt', 11), ('data/day_01.txt', 1530215)])
    def test_total_distance(self, data_file, distance):
        assert total_distance(data_file) == distance

    @pytest.mark.parametrize("data_file, score", [('data/day_01_sample.txt', 31), ('data/day_01.txt', 26800609)])
    def test_similarity_score(self, data_file, score):
        assert similarity_score(data_file) == score