import pytest

from translation import detect_language


@pytest.mark.parametrize(
    "content,expected",
    [
        pytest.param("Ostrava je statutární, krajské a univerzitní město.", 'ces'),
        pytest.param("ОО́страва — місто на північному сході Чехії, третє за", 'ukr'),
        pytest.param("Ostrava — місто на північному сході Чехії, третє за", 'ukr'),
    ],
)
def test_detect_language(content: str, expected: str) -> None:
    assert detect_language(content) == expected
