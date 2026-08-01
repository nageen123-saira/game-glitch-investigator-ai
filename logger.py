import json
from datetime import datetime, timezone
from pathlib import Path


LOG_PATH = Path("logs/interactions.jsonl")


def log_interaction(
    code: str,
    description: str,
    result: dict,
    reliability: dict,
) -> None:
    """
    Save one debugging interaction as a JSON line.
    """
    LOG_PATH.parent.mkdir(parents=True, exist_ok=True)

    record = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "description": description,
        "code": code,
        "success": result.get("success", False),
        "error": result.get("error", ""),
        "analysis": result.get("analysis"),
        "retrieved_sources": [
            document.get("filename", "")
            for document in result.get("retrieved_documents", [])
        ],
        "reliability": reliability,
    }

    with LOG_PATH.open("a", encoding="utf-8") as log_file:
        log_file.write(json.dumps(record) + "\n")