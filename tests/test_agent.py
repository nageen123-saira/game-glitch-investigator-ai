from agent import analyze_bug, identify_bug_category


def test_identify_state_management_category():
    documents = [
        {
            "filename": "state_management.md",
            "content": "Score and state guidance",
            "score": 4,
        }
    ]

    category = identify_bug_category(documents)

    assert category == "State Management Error"


def test_analyze_negative_score_bug():
    result = analyze_bug(
        "score = score - penalty",
        "The score should never become negative after applying a penalty.",
    )

    assert result["success"] is True
    assert result["analysis"] is not None
    assert result["analysis"]["category"] == "State Management Error"
    assert "state_management.md" in result["analysis"]["sources"]


def test_analyze_type_error():
    result = analyze_bug(
        'result = "10" + 5',
        "The program raises a TypeError when combining a string and integer.",
    )

    assert result["success"] is True
    assert result["analysis"]["category"] == "Type Error"


def test_agent_rejects_empty_code():
    result = analyze_bug(
        "",
        "The program should calculate the score.",
    )

    assert result["success"] is False
    assert result["analysis"] is None
    assert result["error"] == (
        "Please paste the Python code you want to debug."
    )


def test_agent_handles_unclear_retrieval():
    result = analyze_bug(
        "x = 1",
        "Something unusual happens with unrelated behavior.",
    )

    assert result["success"] is True
    assert "sources" in result["analysis"]