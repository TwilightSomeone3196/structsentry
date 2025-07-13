import pytest
from app.struct_evaluator import evaluate_structure

def test_evaluate_structure():
    dummy_input = {"elements": ["Fe", "O"], "ratios": [2, 3]}
    result = evaluate_structure(dummy_input)
    assert isinstance(result, dict)
    assert "score" in result