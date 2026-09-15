"""The finished Gradio interface for the AI Resume Grader workshop."""

import gradio as gr

from ai import grade_resume


def build_app():
    """Build the interface. Workshop attendees do not need to edit this file."""
    with gr.Blocks(title="AI Resume Grader") as app:
        gr.Markdown(
            "# AI Resume Grader\n"
            "Paste a plain-text resume and get constructive, actionable feedback."
        )

        resume_input = gr.Textbox(
            label="Resume text",
            placeholder="Paste a resume here...",
            lines=18,
        )
        grade_button = gr.Button("Grade Resume", variant="primary")
        feedback_output = gr.Markdown(label="AI feedback")

        grade_button.click(
            fn=grade_resume,
            inputs=resume_input,
            outputs=feedback_output,
        )

    return app


if __name__ == "__main__":
    build_app().launch()
