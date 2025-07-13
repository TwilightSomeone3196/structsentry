import pytest
from app.xrd_decoder import decode_xrd

def test_decode_xrd_sample():
    sample_data = "20 100
21 200
22 300"
    result = decode_xrd(sample_data)
    assert isinstance(result, list)
    assert all("angle" in r and "intensity" in r for r in result)