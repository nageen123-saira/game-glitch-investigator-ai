from logger import log_interaction
from agent import analyze_bug
from evaluator import calculate_reliability
import random
import streamlit as st
from logic_utils import get_range_for_difficulty, parse_guess, check_guess, update_score

st.set_page_config(page_title="Glitchy Guesser", page_icon="🎮")

st.title("🎮 Game Glitch Investigator")
st.caption("An AI-generated guessing game. Something is off.")

st.sidebar.header("Settings")

difficulty = st.sidebar.selectbox(
    "Difficulty",
    ["Easy", "Normal", "Hard"],
    index=1,
)

attempt_limit_map = {
    "Easy": 6,
    "Normal": 8,
    "Hard": 5,
}
attempt_limit = attempt_limit_map[difficulty]

low, high = get_range_for_difficulty(difficulty)

st.sidebar.caption(f"Range: {low} to {high}")
st.sidebar.caption(f"Attempts allowed: {attempt_limit}")

if "secret" not in st.session_state:
    st.session_state.secret = random.randint(low, high)

if "attempts" not in st.session_state:
    st.session_state.attempts = 1

if "score" not in st.session_state:
    st.session_state.score = 0

if "status" not in st.session_state:
    st.session_state.status = "playing"

if "history" not in st.session_state:
    st.session_state.history = []

st.subheader("Make a guess")

st.info(
    f"Guess a number between 1 and 100. "
    f"Attempts left: {attempt_limit - st.session_state.attempts}"
)

with st.expander("Developer Debug Info"):
    st.write("Secret:", st.session_state.secret)
    st.write("Attempts:", st.session_state.attempts)
    st.write("Score:", st.session_state.score)
    st.write("Difficulty:", difficulty)
    st.write("History:", st.session_state.history)

raw_guess = st.text_input(
    "Enter your guess:",
    key=f"guess_input_{difficulty}"
)

col1, col2, col3 = st.columns(3)
with col1:
    submit = st.button("Submit Guess 🚀")
with col2:
    new_game = st.button("New Game 🔁")
with col3:
    show_hint = st.checkbox("Show hint", value=True)

if new_game:
    st.session_state.attempts = 0
    st.session_state.score = 0
    st.session_state.status = "playing"
    st.session_state.history = []
    st.session_state.secret = random.randint(low, high)
    st.rerun()

if st.session_state.status != "playing":
    if st.session_state.status == "won":
        st.success("You already won. Start a new game to play again.")
    else:
        st.error("Game over. Start a new game to try again.")
    st.stop()

if submit:
    ok, guess_int, err = parse_guess(raw_guess)

    if not ok:
        st.error(err)
    else:
        st.session_state.attempts += 1
        st.session_state.history.append(guess_int)

        secret = st.session_state.secret

        outcome, message = check_guess(guess_int, secret)

        if show_hint:
            st.warning(message)

        st.session_state.score = update_score(
            current_score=st.session_state.score,
            outcome=outcome,
            attempt_number=st.session_state.attempts,
        )

        if outcome == "Win":
            st.balloons()
            st.session_state.status = "won"
            st.success(
                f"You won! The secret was {st.session_state.secret}. "
                f"Final score: {st.session_state.score}"
            )
        else:
            if st.session_state.attempts >= attempt_limit:
                st.session_state.status = "lost"
                st.error(
                    f"Out of attempts! "
                    f"The secret was {st.session_state.secret}. "
                    f"Score: {st.session_state.score}"
                )

st.divider()
st.caption("Built by an AI that claims this code is production-ready.")

st.divider()

st.header("🤖 AI Bug Investigator")
st.write(
    "Paste Python code and describe the expected behavior. "
    "The system will retrieve debugging guidance, classify the likely bug, "
    "and calculate a reliability score."
)

debug_description = st.text_area(
    "What should the code do?",
    placeholder="Example: The score should never become negative.",
    key="debug_description",
)

debug_code = st.text_area(
    "Paste the Python code:",
    placeholder="score = score - penalty",
    height=180,
    key="debug_code",
)

analyze_button = st.button("Analyze Bug 🔍")

if analyze_button:
    result = analyze_bug(
        code=debug_code,
        description=debug_description,
    )

    if not result["success"]:
        st.error(result["error"])

    else:
        analysis = result["analysis"]
        retrieved_documents = result["retrieved_documents"]

        reliability = calculate_reliability(
            analysis=analysis,
            retrieved_documents=retrieved_documents,
        )
        log_interaction(
    code=debug_code,
    description=debug_description,
    result=result,
    reliability=reliability,
       )

        st.subheader("Analysis Result")

        st.write("**Likely bug category:**")
        st.info(analysis["category"])

        st.write("**Explanation:**")
        st.write(analysis["explanation"])

        st.write("**Suggested fix:**")
        st.write(analysis["suggested_fix"])

        st.write("**Suggested test:**")
        st.write(analysis["suggested_test"])

        st.write("**Retrieved sources:**")

        if analysis["sources"]:
            for source in analysis["sources"]:
                st.write(f"- {source}")
        else:
            st.warning("No strongly relevant source was found.")

        st.write("**Reliability score:**")
        st.metric(
            label=reliability["label"],
            value=f"{reliability['score']:.0%}",
        )

        with st.expander("Reliability checks"):
            for check_name, passed in reliability["checks"].items():
                symbol = "✅" if passed else "❌"
                st.write(f"{symbol} {check_name.replace('_', ' ').title()}")

        st.caption(
            "The reliability score measures response completeness and retrieval "
            "grounding. It does not guarantee that the diagnosis is correct."
        )