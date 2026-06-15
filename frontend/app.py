import streamlit as st
import requests
import time
from datetime import datetime

# ============================================
# PAGE CONFIG
# ============================================

st.set_page_config(
    page_title="AI Research Assistant",
    page_icon="📚",
    layout="wide",
)

# ============================================
# CUSTOM CSS
# ============================================

st.markdown("""
<style>

    /* Main App Background */
    .stApp {
        background-color: #0f1117;
        color: white;
    }

    /* Sidebar */
    section[data-testid="stSidebar"] {
        background-color: #161a23;
        border-right: 1px solid #2a2f3a;
    }

    /* Chat Bubble - User */
    .user-message {
        background-color: #2563eb;
        padding: 14px;
        border-radius: 14px;
        margin-bottom: 10px;
        color: white;
        font-size: 15px;
    }

    /* Chat Bubble - AI */
    .assistant-message {
        background-color: #1e2430;
        padding: 16px;
        border-radius: 14px;
        margin-bottom: 20px;
        border: 1px solid #2d3748;
        color: white;
        font-size: 15px;
    }

    /* Titles */
    h1, h2, h3 {
        color: white;
    }

    /* Buttons */
    .stButton>button {
        background-color: #2563eb;
        color: white;
        border-radius: 10px;
        border: none;
        padding: 10px 18px;
        font-weight: 600;
    }

    .stButton>button:hover {
        background-color: #1d4ed8;
    }

    /* Text Input */
    .stTextInput>div>div>input {
        background-color: #1e2430;
        color: white;
        border-radius: 10px;
        border: 1px solid #2d3748;
    }

    /* Uploaded File */
    .uploadedFile {
        background-color: #1e2430;
    }

    /* Expander */
    .streamlit-expanderHeader {
        background-color: #1e2430;
        border-radius: 10px;
    }

</style>
""", unsafe_allow_html=True)

# ============================================
# SESSION STATE INITIALIZATION
# ============================================

if "messages" not in st.session_state:
    st.session_state.messages = []

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "uploaded_files" not in st.session_state:
    st.session_state.uploaded_files = []

# ============================================
# SIDEBAR
# ============================================

with st.sidebar:

    st.title("📚 AI Research Assistant")

    st.markdown("---")

    st.subheader("Upload Research PDF")

    uploaded_file = st.file_uploader(
        "Choose a PDF",
        type=["pdf"]
    )

    # Upload Logic
    if uploaded_file is not None:

        files = {
            "file": uploaded_file
        }

        with st.spinner("Uploading and processing PDF..."):

            response = requests.post(
                "http://127.0.0.1:8000/upload",
                files=files
            )

        if response.status_code == 200:

            st.success("PDF uploaded successfully!")

            # Store uploaded file name
            if uploaded_file.name not in st.session_state.uploaded_files:
                st.session_state.uploaded_files.append(
                    uploaded_file.name
                )

    st.markdown("---")

    # Display Uploaded Files
    st.subheader("Uploaded Files")

    if st.session_state.uploaded_files:

        for file in st.session_state.uploaded_files:
            st.markdown(f"✅ {file}")

    else:
        st.caption("No files uploaded yet.")

    st.markdown("---")

    # Clear Chat Button
    if st.button("🗑 Clear Chat"):

        st.session_state.messages = []
        st.session_state.chat_history = []

        st.success("Chat cleared!")

# ============================================
# MAIN HEADER
# ============================================

st.title("💬 Research Chat")

st.caption(
    "Ask questions about your uploaded documents using local AI."
)

# ============================================
# DISPLAY CHAT HISTORY
# ============================================

for message in st.session_state.messages:

    # USER MESSAGE
    if message["role"] == "user":

        st.markdown(
            f"""
            <div class="user-message">
                <strong>You</strong><br>
                {message["content"]}
            </div>
            """,
            unsafe_allow_html=True
        )

    # ASSISTANT MESSAGE
    else:

        st.markdown(
            f"""
            <div class="assistant-message">
                <strong>AI Assistant</strong><br><br>
                {message["content"]}
            </div>
            """,
            unsafe_allow_html=True
        )

        # Show Retrieved Context
        if "chunks" in message:

            with st.expander("📖 Retrieved Context"):

                for idx, chunk in enumerate(message["chunks"]):

                    st.markdown(
                        f"""
                        ### Chunk {idx + 1}

                        {chunk}
                        """
                    )

                    st.divider()

# ============================================
# QUESTION INPUT
# ============================================

user_question = st.chat_input(
    "Ask something about your document..."
)

# ============================================
# PROCESS USER QUESTION
# ============================================

if user_question:

    # Store user message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_question
        }
    )

    # Display user message immediately
    st.markdown(
        f"""
        <div class="user-message">
            <strong>You</strong><br>
            {user_question}
        </div>
        """,
        unsafe_allow_html=True
    )

    # Prepare payload
    payload = {
        "question": user_question,
        "chat_history": st.session_state.chat_history
    }

    # AI Thinking Spinner
    with st.spinner("AI is analyzing your documents..."):

        response = requests.post(
            "http://127.0.0.1:8000/query",
            json=payload
        )

    # ============================================
    # HANDLE RESPONSE
    # ============================================

    if response.status_code == 200:

        data = response.json()

        ai_answer = data["answer"]

        retrieved_chunks = data["retrieved_chunks"]

        # Typing Animation Effect
        typing_placeholder = st.empty()

        displayed_text = ""

        for char in ai_answer:

            displayed_text += char

            typing_placeholder.markdown(
                f"""
                <div class="assistant-message">
                    <strong>AI Assistant</strong><br><br>
                    {displayed_text}
                </div>
                """,
                unsafe_allow_html=True
            )

            time.sleep(0.005)

        # Final Render
        typing_placeholder.markdown(
            f"""
            <div class="assistant-message">
                <strong>AI Assistant</strong><br><br>
                {ai_answer}
            </div>
            """,
            unsafe_allow_html=True
        )

        # Retrieved Chunks Section
        with st.expander("📖 Retrieved Context"):

            for idx, chunk in enumerate(retrieved_chunks):

                st.markdown(
                    f"""
                    ### Chunk {idx + 1}

                    {chunk}
                    """
                )

                st.divider()

        # Save AI message
        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": ai_answer,
                "chunks": retrieved_chunks
            }
        )

        # Save conversation memory
        st.session_state.chat_history.append(
            {
                "role": "user",
                "content": user_question
            }
        )

        st.session_state.chat_history.append(
            {
                "role": "assistant",
                "content": ai_answer
            }
        )

    else:

        st.error(
            f"Error {response.status_code}: {response.text}"
        )