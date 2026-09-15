# AI Resume Grader

A beginner-friendly AI application built for a hands-on **Cal Poly CS AI workshop**. Users paste a resume into a Gradio interface and receive structured feedback generated through the Gemini API.

## Overview

I designed this project as an interactive workshop for students learning how AI applications connect user interfaces, Python functions, prompts, and external APIs.

The project demonstrates the full flow of a simple AI application:

**User → Gradio Interface → Python → Gemini API → AI Feedback**

Students can modify the prompt and AI connection to experiment with how changes affect the model's responses.

## Features

- Interactive resume input through a Gradio web interface
- Integration with the Gemini API
- AI-generated resume scoring and feedback
- Structured feedback on strengths and areas for improvement
- Actionable resume recommendations
- Customizable prompt and scoring rubric
- Sample resumes for testing different outputs

## Technologies

- Python
- Gradio
- Google Gemini API
- google-genai
- python-dotenv
- Git / GitHub

## Project Structure

`app.py`  
Builds the Gradio user interface.

`ai.py`  
Connects the application to the Gemini API and returns model responses.

`prompt.py`  
Defines the resume-review prompt and scoring rubric.

`sample_resumes/`  
Contains fictional resumes for testing the application.

`WORKSHOP_GUIDE.md`  
Provides instructions for completing the hands-on workshop activity.

## Running the Project

Install the dependencies:

```bash
pip install -r requirements.txt
