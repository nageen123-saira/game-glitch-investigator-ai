# Model Card

## Model Name

Game Glitch Investigator AI

---

# Purpose

The purpose of this project is to help users debug Python code by combining retrieval-based knowledge, rule-based bug classification, reliability evaluation, and interaction logging. The system also includes an interactive number guessing game that demonstrates debugging and software testing concepts.

---

# Intended Users

- Computer Science students
- Beginner Python programmers
- Developers learning debugging techniques
- Anyone interested in AI-assisted software engineering

---

# AI Components

This project includes several AI-inspired components:

- Input Guardrails
- Retrieval-Augmented Knowledge Base
- Rule-Based Bug Classification Agent
- Reliability Evaluator
- Interaction Logger

These components work together to provide debugging suggestions grounded in the project's knowledge base.

---

# Limitations

- Only supports Python code.
- Uses rule-based classification rather than a large language model.
- The knowledge base contains a limited number of debugging documents.
- Suggestions are based on retrieval quality and may not cover every programming bug.

---

# Potential Biases

The system can only classify bugs that resemble examples contained in the knowledge base. Bugs outside those categories may receive less accurate suggestions.

---

# Safety Features

The application includes several guardrails:

- Rejects empty code submissions.
- Rejects empty descriptions.
- Rejects non-text input.
- Rejects extremely large code snippets.
- Calculates a reliability score to indicate confidence in the generated response.

---

# Testing

The project includes automated tests for:

- Game logic
- Guardrails
- Knowledge retrieval
- AI agent
- Reliability evaluator
- Interaction logger

All tests pass successfully.

---

# AI Collaboration Reflection

AI was used throughout this project to assist with brainstorming, debugging, code explanations, and improving documentation. I reviewed, tested, and modified the generated code before integrating it into the final application.

---

# Helpful AI Suggestion

One of the most helpful AI suggestions was recommending that the project be divided into smaller modules (guardrails, retriever, agent, evaluator, and logger). This made the system easier to understand, test, and maintain.

---

# Incorrect AI Suggestion

At times, AI suggested solutions that did not fit the project requirements or produced incorrect logic. I verified each suggestion by running the application and executing automated tests before accepting any changes.

---

# What I Learned

This project taught me that building reliable AI applications requires more than generating responses. Good AI systems also need input validation, retrieval, evaluation, testing, logging, and modular software design. I also learned how retrieval-based systems improve transparency by grounding responses in known documentation.
