import pytest
from pytest_auth import is_valid_promo

@pytest.mark.parametrize("code, expected",
[
("ABC123XY90", True),
("ABCDEFGH12", True),
("QWERTYUIOP12", False),
("AB123", False),
("abc123defg", False),
("ABCDEFGHIJ",False),
(1234567890,False),
("ABC!@#123$",False),
])

def test_is_valid_promo(code,expected):
    assert is_valid_promo(code) == expected