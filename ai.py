"""Completed facilitator version of the Gemini connection."""

import os

from dotenv import load_dotenv
from google import genai

from prompt import build_grading_prompt


def grade_resume(resume_text: str) -> str:
    """Send a resume to Gemini and return its feedback as plain text."""
    if not resume_text or not resume_text.strip():
        return "Please paste a resume before grading it."

    # load_dotenv reads GEMINI_API_KEY from a local .env file during development.
    load_dotenv()
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        return "Missing GEMINI_API_KEY. Add it to your .env file and try again."

    # The client holds the API key and sends requests to the Gemini API.
    client = genai.Client(api_key=api_key)
    prompt = build_grading_prompt(resume_text)

    # One request in, one text response out: perfect for a first API project.
    response = client.interactions.create(
        model="gemini-3.8-flash",
        input=prompt,
    )

    return response.output_text or "Gemini did not return any feedback. Please try again."
