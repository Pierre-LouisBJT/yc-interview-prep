# Mock YC interview using OpenAI real time API

> This is a personal project. It is not affiliated with the Y Combinator in any way.

Get ready for that YC interview!

## Installation

First, clone the repository:

```bash
git clone https://github.com/Pierre-LouisBJT/yc-interview-prep.git
```

Then, install the requirements:

```bash
pip install -r requirements.txt
```

Create a `.env` file in the root directory and add your OpenAI API key:

```
OPENAI_API_KEY=your-api-key
```

## Usage

To talk to the AI YC partner, run the following command:

```bash
chainlit run app.py
```

It should open a new tab in your browser with the chat interface (or just go to `http://localhost:8000`). You need to allow access to your microphone. Only tested on Chrome for now.
