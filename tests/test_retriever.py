from retriever import clean_text, load_documents, retrieve_documents


def test_clean_text():
    words = clean_text("Score becomes NEGATIVE!")

    assert words == ["score", "becomes", "negative"]


def test_load_documents():
    documents = load_documents()

    assert len(documents) >= 5
    assert all("filename" in document for document in documents)
    assert all("content" in document for document in documents)


def test_retrieve_state_management_document():
    results = retrieve_documents(
        "The game score becomes negative after a penalty."
    )

    assert len(results) > 0
    assert results[0]["filename"] == "state_management.md"


def test_retrieve_type_error_document():
    results = retrieve_documents(
        "I am combining a string and integer and getting a TypeError."
    )

    filenames = [result["filename"] for result in results]

    assert "type_errors.md" in filenames


def test_empty_query():
    results = retrieve_documents("   ")

    assert results == []