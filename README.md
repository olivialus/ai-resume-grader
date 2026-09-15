# AI Resume Grader

A small beginner-friendly project for learning how a Python app calls an AI API. Paste a plain-text resume into the Gradio interface, then receive a score, strengths, improvements, and actionable recommendations from Gemini.

The interface is already finished. In the starter project, the AI connection is deliberately unfinished so you can build it during the workshop.

## What you need

- Python 3.9 or newer
- A Gemini API key from [Google AI Studio](https://aistudio.google.com/app/apikey)

## Setup

1. Clone or download this project, then open a terminal in the `resume-grader` folder.
2. Create and activate a virtual environment (recommended):

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

   On Windows PowerShell, use `.venv\Scripts\Activate.ps1` instead.

3. Install the packages:

   ```bash
   python -m pip install -r requirements.txt
   ```

4. Copy `.env.example` to `.env`, then replace `your_api_key_here` with your own key:

   ```bash
   cp .env.example .env
   ```

5. Start the starter app:

   ```bash
   python app.py
   ```

6. Open the local URL printed by Gradio. Paste a file from `sample_resumes/` to test the interface.

## Your task

The frontend is done. Your job is to give it AI functionality.

1. Open `ai.py`.
2. Read the Gemini API key from the environment.
3. Connect to Gemini with the `google-genai` SDK.
4. Send the resume and grading prompt to the model.
5. Read the model response.
6. Return that response to the frontend.
7. Modify the rubric in `prompt.py` and test it with the sample resumes.

Look for the clearly marked `TODO` comments in `ai.py`. The instructor has a completed reference in `instructor_solution/`—try the starter yourself before looking at it.

## The API flow

```text
User → Gradio frontend → Python function → Gemini API → Gemini model
     ← Gradio displays feedback ← Python returns response ← API response
```

In plain language: Gradio collects the resume text. `app.py` sends it to `grade_resume` in `ai.py`. Your code builds instructions, asks Gemini for feedback, and sends Gemini's text back to the screen.

## Test data

The three fictional resumes are intentionally different in quality:

- `weak_resume.txt`: vague skills and few details
- `average_resume.txt`: solid student work, but limited measurable impact
- `strong_resume.txt`: clear technical work with results and numbers

Your rubric should generally distinguish between them, but an AI score is coaching feedback—not an objective hiring decision.

## Optional challenges

After the core activity, you could add:

- PDF resume upload
- Comparison against a job description
- Separate category scores
- Structured JSON output
- Saving past results
- A job-match analyzer
- External tools or data through MCP

## SDK note

This project uses the current `google-genai` Python SDK. The instructor solution uses a Gemini client and the SDK's Interactions API; it does not use the older deprecated Python SDK.
