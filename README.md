# 🎮 Game Glitch Investigator AI

## Overview

**Game Glitch Investigator AI** is an applied AI system built with **Python** and **Streamlit** that combines an interactive number guessing game with an AI-assisted debugging tool.

This project began as the **Module 1 "Game Glitch Investigator"**, where the goal was to identify and fix bugs in an AI-generated guessing game. For the final project, I extended it into a complete AI system by adding input guardrails, a retrieval-based knowledge system (RAG), an AI debugging agent, reliability evaluation, and interaction logging.

The AI Bug Investigator helps users analyze Python code by retrieving relevant debugging knowledge, identifying likely bug categories, suggesting fixes, recommending test cases, and providing a reliability score.

---

# Original Project

The original **Game Glitch Investigator** was a Streamlit number guessing game containing several intentional bugs. The objective was to debug the application, refactor the game logic into reusable functions, and create automated tests.

The final project preserves the original game while extending it with an AI-powered debugging assistant.

---

# Features

## 🎮 Number Guessing Game

- Three difficulty levels (Easy, Normal, Hard)
- Random secret number generation
- Score tracking
- Attempt limits
- Higher / Lower hints
- Session State management
- New Game reset

---

## 🤖 AI Bug Investigator

- Input Guardrails
- Retrieval-Augmented Debugging (Knowledge Base)
- Bug Category Identification
- Suggested Fixes
- Suggested Test Cases
- Reliability Scoring
- Interaction Logging
- Modular AI Workflow

---

# AI Components

This project includes the following AI-inspired modules:

| Component | Purpose |
|------------|---------|
| Guardrails | Validates user input before analysis |
| Knowledge Base | Stores debugging documentation |
| Retriever | Searches the knowledge base for relevant information |
| Agent | Coordinates the debugging workflow |
| Evaluator | Calculates reliability scores |
| Logger | Saves debugging interactions for future analysis |

---

# Technologies Used

- Python 3
- Streamlit
- Pytest
- Markdown Knowledge Base
- Git & GitHub

---

# Project Structure

```text
game-glitch-investigator-ai/

│
├── app.py
├── logic_utils.py
├── guardrails.py
├── retriever.py
├── agent.py
├── evaluator.py
├── logger.py
│
├── knowledge_base/
│
├── diagrams/
│
├── logs/
│
├── tests/
│
├── README.md
├── model_card.md
├── requirements.txt
```

---

# Installation

Clone the repository:

```bash
git clone https://github.com/nageen123-saira/game-glitch-investigator-ai.git

cd game-glitch-investigator-ai
```

Install the required packages:

```bash
pip install -r requirements.txt
```

---

# Running the Application

Run the Streamlit application:

```bash
streamlit run app.py
```

The application will launch at:

```
http://localhost:8501
```

---

# System Architecture

The AI Bug Investigator follows this workflow:

```text
User
   │
   ▼
Input Guardrails
   │
   ▼
Knowledge Retriever
   │
   ▼
Knowledge Base
   │
   ▼
AI Debugging Agent
   │
   ▼
Reliability Evaluator
   │
   ▼
Interaction Logger
   │
   ▼
Streamlit User Interface
```

*A Mermaid architecture diagram is included in the `diagrams/` folder.*

---

# Reproducible Execution Evidence

## Example 1

### Description

```text
The score should never become negative after applying a penalty.
```

### Code

```python
score = score - penalty
```

### Output

```text
Likely Bug Category:
State Management Error

Suggested Fix:
Use boundary checks when updating the score.

Suggested Test:
Test normal input, boundary values, and invalid input.

Retrieved Sources:
state_management.md
logic_errors.md

Reliability:
High (100%)
```

---

## Example 2

### Description

```text
Invalid user input should not crash the program.
```

### Code

```python
guess = int(user_input)
```

### Output

```text
Likely Bug Category:
Input Validation Error

Suggested Fix:
Validate user input before converting it.

Suggested Test:
Test empty strings, letters, and symbols.

Reliability:
High
```

---

## Example 3

### Description

```text
The hint says "Go Higher" even when the guess is already too high.
```

### Code

```python
if guess > secret:
    return "Go Higher"
```

### Output

```text
Likely Bug Category:
Logic Error

Suggested Fix:
Reverse the comparison logic.

Suggested Test:
Test guesses above and below the secret number.

Reliability:
High
```

---

# Running the Tests

Run all automated tests:

```bash
python -m pytest -v
```

Example output:

```text
tests/test_game_logic.py ........
tests/test_guardrails.py .....
tests/test_retriever.py .....
tests/test_agent.py .....
tests/test_evaluator.py ....
tests/test_logger.py .

=========================
22 passed
=========================
```

---

# Reliability and Guardrails

The AI Bug Investigator includes several mechanisms to improve reliability:

- Validates user input before analysis
- Rejects empty or invalid submissions
- Retrieves relevant debugging documentation before generating a response
- Assigns a reliability score based on response completeness
- Logs every debugging interaction for future analysis

These features help make the debugging workflow more transparent and reliable.

---

# What I Learned

This project taught me that building AI systems involves much more than generating answers. A reliable AI application also needs input validation, retrieval of relevant knowledge, evaluation of outputs, logging, and testing.

I learned how modular design makes complex systems easier to develop, test, and maintain. Building each component separately and then integrating them into a complete workflow improved both the quality and reliability of the final application.

---

# Portfolio Reflection

This project demonstrates my ability to design and build modular AI-assisted software using Python and Streamlit. It highlights my understanding of retrieval-based systems, automated testing, software reliability, and responsible AI design. The experience strengthened my software engineering skills and showed me how multiple AI components can work together to solve practical debugging problems.

---

# GitHub Repository

**Repository**

https://github.com/nageen123-saira/game-glitch-investigator-ai