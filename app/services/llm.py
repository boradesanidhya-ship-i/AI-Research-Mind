import ollama


def generate_answer(question: str, context_chunks: list, chat_history: list):
    """
    Generate conversational AI answer using Ollama
    """

    # Combine retrieved chunks
    context = "\n\n".join(context_chunks)

    # System prompt
    system_prompt = f"""
You are an AI research assistant.

Answer ONLY using the provided context.

Context:
{context}
"""

    # Start messages with system prompt
    messages = [
        {
            "role": "system",
            "content": system_prompt
        }
    ]

    # Add previous chat history
    messages.extend(chat_history)

    # Add current user question
    messages.append(
        {
            "role": "user",
            "content": question
        }
    )

    # Generate response
    response = ollama.chat(
        model="llama3",
        messages=messages
    )

    return response["message"]["content"]