from guardrails import validate_input


def test_valid_input():
    is_valid, message = validate_input(
        "score = max(0, score - penalty)",
        "The score should never become negative."
    )

    assert is_valid is True
    assert message == ""


def test_empty_code():
    is_valid, message = validate_input(
        "   ",
        "The score should never become negative."
    )

    assert is_valid is False
    assert message == "Please paste the Python code you want to debug."


def test_empty_description():
    is_valid, message = validate_input(
        "score = score - penalty",
        ""
    )

    assert is_valid is False
    assert message == "Please describe what the program is supposed to do."


def test_code_too_large():
    large_code = "a" * 10001

    is_valid, message = validate_input(
        large_code,
        "Test a very large input."
    )

    assert is_valid is False
    assert message == "The code is too large. Please submit a smaller example."


def test_non_text_input():
    is_valid, message = validate_input(
        None,
        "The program should calculate a score."
    )

    assert is_valid is False
    assert message == "Code and description must be text."