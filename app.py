import streamlit as st
from code_parser import parse_code
from error_detector import detect_errors
from ai_suggester import get_ai_suggestion


ai_suggestions = []
suggestion_index = 0

# Add at top, after imports
if "ai_suggestions" not in st.session_state:
    st.session_state.ai_suggestions = []

if "suggestion_index" not in st.session_state:
    st.session_state.suggestion_index = 0


st.set_page_config(
    page_title="AI Code Reviewer Application",
    page_icon="logo.jpeg",
    layout="wide"
)
st.image("logo.jpeg", width=120)

st.title("AI Code Reviewer")

# Initialize session state safely
if "ai_suggestions" not in st.session_state:
    st.session_state.ai_suggestions = []

if "suggestion_index" not in st.session_state:
    st.session_state.suggestion_index = 0

# Input
code = st.text_area("Paste your code")

# Tabs
tab1, tab2 = st.tabs(["Errors", "AI Suggestions"])

# Analyze button
if st.button("Analyze"):
    if not code.strip():
        st.warning("Please enter some code to analyze.")
    else:
        # ---------------- Errors Tab ----------------
        with tab1:
            st.subheader("Detected Issues")

            errors = detect_errors(code)

            if errors:
                for err in errors:
                    st.error(err)
            else:
                st.success("No errors found")

        # ---------------- AI Suggestions Tab ----------------
        with tab2:
            st.subheader("AI Suggestions")

            ai_suggestions = get_ai_suggestion(code)

            # Normalize to list
            if not isinstance(ai_suggestions, list):
                ai_suggestions = [ai_suggestions]

            # Save to session state
            st.session_state.ai_suggestions = ai_suggestions
            st.session_state.suggestion_index = 0

            if ai_suggestions:
                st.info(ai_suggestions[0]["message"])
            else:
                st.success("No suggestions available.")

# Refresh button (outside Analyze)
if st.button("Refresh"):
    if code.strip() and "ai_suggestions" in st.session_state:
        new_suggestion = get_ai_suggestion(
            code,
            previous_suggestions=st.session_state.ai_suggestions
        )

        st.session_state.ai_suggestions.append(new_suggestion)
        st.session_state.suggestion_index = (
            len(st.session_state.ai_suggestions) - 1
        )


    st.return()

