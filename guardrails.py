def validate_input(code: str, description: str) -> tuple[bool, str]:
    """
    Validate the user's input before sending it to the AI.
    """

    # Check that both inputs are strings
    if not isinstance(code, str) or not isinstance(description, str):
        return False, "Code and description must be text."

    # Check if code is empty
    if not code.strip():
        return False, "Please paste the Python code you want to debug."

    # Check if description is empty
    if not description.strip():
        return False, "Please describe what the program is supposed to do."

    # Check if the code is too large
    if len(code) > 10000:
        return False, "The code is too large. Please submit a smaller example."

    return True, ""