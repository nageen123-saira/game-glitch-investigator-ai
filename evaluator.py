def calculate_reliability(
    analysis: dict | None,
    retrieved_documents: list[dict],
) -> dict:
    """
    Evaluate the completeness of the debugging response.
    """

    if analysis is None:
        return {
            "score": 0.0,
            "label": "Low",
            "checks": {
                "category": False,
                "explanation": False,
                "suggested_fix": False,
                "suggested_test": False,
                "retrieval": False,
            },
        }

    checks = {
        "category": bool(analysis.get("category")),
        "explanation": bool(analysis.get("explanation")),
        "suggested_fix": bool(analysis.get("suggested_fix")),
        "suggested_test": bool(analysis.get("suggested_test")),
        "retrieval": len(retrieved_documents) > 0,
    }

    weights = {
        "category": 0.20,
        "explanation": 0.20,
        "suggested_fix": 0.25,
        "suggested_test": 0.20,
        "retrieval": 0.15,
    }

    score = sum(
        weights[name]
        for name, passed in checks.items()
        if passed
    )

    score = round(score, 2)

    if score >= 0.80:
        label = "High"
    elif score >= 0.60:
        label = "Moderate"
    else:
        label = "Low"

    return {
        "score": score,
        "label": label,
        "checks": checks,
    }