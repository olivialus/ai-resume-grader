# Facilitator Guide: AI Resume Grader

## What attendees start with

Attendees receive a complete Gradio interface in `app.py`, three fictional sample resumes, and a basic prompt builder in `prompt.py`. The app runs immediately, but `ai.py` returns a placeholder message instead of calling Gemini.

They should edit only `ai.py` during the core build, then experiment with `prompt.py`. They do not need to build a frontend, parse PDFs, use JSON, or implement MCP.

## What they change

| Step | Change | Difficulty |
| --- | --- | --- |
| 1 | Load `GEMINI_API_KEY` from `.env` | Easy |
| 2 | Create a `genai.Client` | Easy |
| 3 | Call `build_grading_prompt(resume_text)` | Easy |
| 4 | Send one request to Gemini | Medium |
| 5 | Return `response.output_text` | Easy |
| 6 | Tune the rubric in `prompt.py` | Creative |

## The completed API code, explained

The instructor reference is in `instructor_solution/ai.py`.

- `load_dotenv()` reads local variables from `.env`, so a key is not written into source code.
- `os.getenv("GEMINI_API_KEY")` retrieves the key by its name.
- `genai.Client(api_key=api_key)` creates an SDK client that authenticates requests.
- `build_grading_prompt(resume_text)` combines the model instructions and user-provided resume.
- `client.interactions.create(...)` sends that input to a named Gemini model.
- `response.output_text` is the text Gemini generated. Returning it makes Gradio display it.

This is the entire mental model: build a string, send it, receive a string, display it.

## Suggested 25-minute flow

1. **0–3 min — Demo the starter.** Run `python app.py`, paste a sample, and show the placeholder. Explain that the UI already works.
2. **3–7 min — Trace the flow.** Follow `app.py` → `grade_resume` → Gemini → returned text. Point out the TODOs.
3. **7–12 min — Key and client.** Have attendees create `.env`, load the key, and initialize `genai.Client`.
4. **12–17 min — First model call.** Build the prompt, send it with `client.interactions.create`, and return `response.output_text`.
5. **17–22 min — Test and compare.** Grade the weak, average, and strong examples. Discuss whether scores and suggestions feel reasonable.
6. **22–25 min — Prompt experiment and MCP bridge.** Change one rubric item or output rule, rerun, and explain the next topic.

## Good checkpoints to pause and explain

1. **Before code:** A frontend can call an ordinary Python function; the function does not need to know about buttons.
2. **After the API key:** Keys identify and authorize your application. `.env` stays out of Git.
3. **After the first response:** The model is not a database. Its output depends on the input and instructions.
4. **During prompt changes:** A prompt is part of the program's behavior. Rubrics make output more consistent.
5. **At the end:** The function returns plain text, which is why the interface needs no extra work.

## Common beginner errors

| Symptom | Likely cause | Helpful fix |
| --- | --- | --- |
| `ModuleNotFoundError` | Packages are not installed in the active environment | Activate `.venv`, then run `python -m pip install -r requirements.txt`. |
| “Missing GEMINI_API_KEY” | `.env` is absent, misspelled, or has no value | Copy `.env.example`, add the key, and restart the app. |
| Authentication error | Key is invalid or copied with extra characters | Create/copy a fresh key from AI Studio. |
| Attribute/name error | Import, variable, or method name differs from the reference | Compare just that line with `instructor_solution/ai.py`. |
| Blank or odd feedback | The prompt is too vague or response text was not returned | Add explicit headings/rubric items; return `response.output_text`. |
| Gradio page does not refresh | The Python server is still running old code | Stop it with `Ctrl+C` and run `python app.py` again. |

## Transition to MCP

The completed grader uses one model call: the model sees the resume and writes feedback. MCP becomes useful when the app needs outside context or actions. For example, a later version could use an MCP server to look up a job description, retrieve a rubric from a shared database, or save feedback to a spreadsheet. The core pattern stays familiar: your Python app connects components, but MCP provides a standard way to connect tools and data safely.

Keep this distinction clear: Gemini generates the feedback; MCP can provide extra information or tools around that generation.

## Facilitator testing commands

From the project folder:

```bash
python -m pip install -r requirements.txt
python app.py
```

To run the completed instructor version temporarily, copy its two files over the starter files (or make a separate copy of the folder first):

```bash
cp instructor_solution/ai.py ai.py
cp instructor_solution/prompt.py prompt.py
python app.py
```

Use a real `.env` and an active Gemini key for the instructor test.
