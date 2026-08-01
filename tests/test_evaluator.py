from evaluator import calculate_reliability


def test_complete_response_has_high_reliability():
    analysis = {
        "category": "State Management Error",
        "explanation": "The score becomes negative.",
        "suggested_fix": "Use max().",
        "suggested_test": "Test penalty > score."
    }

    documents = [
        {
            "filename": "state_management.md",
            "content": "",
            "score": 4
        }
    ]

    result = calculate_reliability(
        analysis,
        documents,
    )

    assert result["score"] == 1.0
    assert result["label"] == "High"


def test_missing_retrieval():
    analysis = {
        "category": "Logic Error",
        "explanation": "Condition is incorrect.",
        "suggested_fix": "Check comparison.",
        "suggested_test": "Test edge cases."
    }

    result = calculate_reliability(
        analysis,
        [],
    )

    assert result["score"] == 0.85
    assert result["label"] == "High"


def test_partial_analysis():
    analysis = {
        "category": "Logic Error",
        "explanation": "Condition incorrect.",
        "suggested_fix": "",
        "suggested_test": "Boundary tests."
    }

    documents = [
        {
            "filename": "logic_errors.md",
            "content": "",
            "score": 3
        }
    ]

    result = calculate_reliability(
        analysis,
        documents,
    )

    assert result["score"] == 0.75
    assert result["label"] == "Moderate"


def test_no_analysis():
    result = calculate_reliability(
        None,
        [],
    )

    assert result["score"] == 0.0
    assert result["label"] == "Low"