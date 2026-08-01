import json
from logger import log_interaction


def test_log_interaction(tmp_path, monkeypatch):
    test_log_path = tmp_path / "interactions.jsonl"

    monkeypatch.setattr(
        "logger.LOG_PATH",
        test_log_path,
    )

    result = {
        "success": True,
        "error": "",
        "analysis": {
            "category": "State Management Error",
            "explanation": "The score can become negative.",
            "suggested_fix": "Use max().",
            "suggested_test": "Test penalty greater than score.",
            "sources": ["state_management.md"],
        },
        "retrieved_documents": [
            {
                "filename": "state_management.md",
                "content": "State guidance",
                "score": 5,
            }
        ],
    }

    reliability = {
        "score": 1.0,
        "label": "High",
        "checks": {
            "category": True,
            "explanation": True,
            "suggested_fix": True,
            "suggested_test": True,
            "retrieval": True,
        },
    }

    log_interaction(
        code="score = score - penalty",
        description="The score should not become negative.",
        result=result,
        reliability=reliability,
    )

    assert test_log_path.exists()

    line = test_log_path.read_text(
        encoding="utf-8"
    ).strip()

    record = json.loads(line)

    assert record["success"] is True
    assert record["analysis"]["category"] == (
        "State Management Error"
    )
    assert record["retrieved_sources"] == [
        "state_management.md"
    ]
    assert record["reliability"]["score"] == 1.0
    assert "timestamp" in record