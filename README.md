# LinkedIn Post Recommender

A **Few-Shot LLM powered system** that generates engaging LinkedIn posts based on **topic, language, and length preferences**.

The system uses example LinkedIn posts from a dataset and applies **few-shot prompting with the Llama-3.3-70B-Versatile model** to generate posts that follow a similar writing style and tone.

---

## Features

- Generate LinkedIn posts based on **topic/tag**
- Control **post length**
  - Short (1–5 lines)
  - Medium (6–10 lines)
  - Long (11–15 lines)
- Supports **multiple languages**
  - English
  - Hinglish (Hindi + English written in English script)
- Uses **Few-Shot Prompting** to maintain writing style
- Automatically retrieves **relevant example posts** from a dataset
- Powered by **Llama-3.3-70B-Versatile LLM**

---

## How It Works

1. Load curated LinkedIn posts from a dataset.
2. Filter posts based on:
   - Topic (tag)
   - Language
   - Post length
3. Use filtered posts as **few-shot examples** in the prompt.
4. Generate a new LinkedIn post using **Llama-3.3-70B-Versatile**.

---

## Model Used

- **Llama-3.3-70B-Versatile**
- Large Language Model optimized for **instruction following and content generation**
- Used to generate **structured and engaging LinkedIn posts**

---

## Project Structure

LinkedIn-Post-Recommender
│
├── data/
│ └── processed_posts.json
│
├── llm_helper.py
├── few_shot.py
├── post_generator.py
│
└── README.md
