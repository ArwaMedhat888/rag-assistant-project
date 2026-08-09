import ollama


def generate_answer(context: str, question: str):
    prompt = f"""
You are a document question-answering assistant.

Answer the question using ONLY the context provided below.

Do not use outside knowledge.
Do not invent information.
Give a short and direct answer.

If the context does not contain the answer, say:
"I could not find the answer in the provided documents."

Context:
{context}

Question:
{question}

Answer:
"""

    response = ollama.chat(
        model="smollm2:135m",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"].strip()