from guardrails import validate_input
from retriever import retrieve_documents


def identify_bug_category(retrieved_documents: list[dict]) -> str:
    """
    Infer a bug category from the highest-ranked retrieved document.
    """
    if not retrieved_documents:
        return "Unknown or insufficient context"

    filename = retrieved_documents[0]["filename"]

    category_map = {
        "logic_errors.md": "Logic Error",
        "input_errors.md": "Input Validation Error",
        "type_errors.md": "Type Error",
        "state_management.md": "State Management Error",
        "testing_strategies.md": "Testing or Reliability Issue",
    }

    return category_map.get(filename, "General Programming Error")


def build_debug_response(
    code: str,
    description: str,
    retrieved_documents: list[dict],
) -> dict:
    """
    Build a structured debugging response using retrieved documentation.
    """
    category = identify_bug_category(retrieved_documents)

    if not retrieved_documents:
        return {
            "category": category,
            "explanation": (
                "The system could not find enough relevant debugging "
                "information. Provide a clearer expected behavior or error message."
            ),
            "suggested_fix": (
                "Review the input, expected behavior, and exact error message."
            ),
            "suggested_test": (
                "Create a small test case that compares expected and actual output."
            ),
            "sources": [],
        }

    top_document = retrieved_documents[0]

    return {
        "category": category,
        "explanation": (
            f"The code may contain a {category.lower()}. "
            f"The retrieved guide '{top_document['filename']}' was the "
            "strongest match for the submitted code and description."
        ),
        "suggested_fix": (
            "Use the retrieved debugging guidance to inspect the relevant "
            "conditions, values, data types, or state updates."
        ),
        "suggested_test": (
            "Test one normal case, one invalid case, and one boundary case."
        ),
        "sources": [
            document["filename"]
            for document in retrieved_documents
        ],
    }


def analyze_bug(code: str, description: str) -> dict:
    """
    Run the complete debugging workflow.

    Steps:
    1. Validate input.
    2. Retrieve relevant debugging documents.
    3. Classify the likely bug.
    4. Build a structured response.
    """

    is_valid, error_message = validate_input(code, description)

    if not is_valid:
        return {
            "success": False,
            "error": error_message,
            "retrieved_documents": [],
            "analysis": None,
        }

    query = f"{description}\n{code}"

    retrieved_documents = retrieve_documents(query, top_k=2)

    analysis = build_debug_response(
        code=code,
        description=description,
        retrieved_documents=retrieved_documents,
    )

    return {
        "success": True,
        "error": "",
        "retrieved_documents": retrieved_documents,
        "analysis": analysis,
    }