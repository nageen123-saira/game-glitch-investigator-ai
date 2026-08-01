from pathlib import Path
import re


KNOWLEDGE_BASE_PATH = Path("knowledge_base")


def clean_text(text: str) -> list[str]:
    """
    Convert text into lowercase searchable words.
    """
    return re.findall(r"\b[a-zA-Z]+\b", text.lower())


def load_documents() -> list[dict]:
    """
    Read all Markdown files from the knowledge_base folder.
    """
    documents = []

    for file_path in KNOWLEDGE_BASE_PATH.glob("*.md"):
        content = file_path.read_text(encoding="utf-8")

        documents.append(
            {
                "filename": file_path.name,
                "content": content,
            }
        )

    return documents


def retrieve_documents(query: str, top_k: int = 2) -> list[dict]:
    """
    Return the most relevant knowledge-base documents for a query.
    """
    if not isinstance(query, str) or not query.strip():
        return []

    query_words = set(clean_text(query))
    documents = load_documents()
    scored_documents = []

    for document in documents:
        document_words = clean_text(document["content"])

        score = sum(
            1 for word in document_words
            if word in query_words
        )

        if score > 0:
            scored_documents.append(
                {
                    "filename": document["filename"],
                    "content": document["content"],
                    "score": score,
                }
            )

    scored_documents.sort(
        key=lambda document: document["score"],
        reverse=True,
    )

    return scored_documents[:top_k]