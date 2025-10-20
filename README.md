# Interactive Quiz App

A Streamlit-based interactive quiz application that allows users to test their knowledge on various subjects and topics.

## Features

- Multiple subjects to choose from
- Various topics within each subject
- Interactive quiz interface
- Instant feedback on answers
- Score tracking
- Detailed explanations for each answer

## Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

## Installation

1. Clone the repository or download the source code
2. Navigate to the project directory
3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Run the application:
   ```
   streamlit run app.py
   ```
2. Open your web browser and go to `http://localhost:8501`
3. Select a subject and topic to start the quiz
4. Answer the questions and see your score update in real-time

## Project Structure

- `app.py` - Main application file
- `data.json` - Quiz questions and answers
- `requirements.txt` - Python dependencies

## Adding New Questions

To add new questions or modify existing ones, edit the `data.json` file following this format:

```json
"Subject Name": [
  {
    "question": "Your question here",
    "options": ["Option 1", "Option 2", "Option 3", "Option 4"],
    "answer": 0,
    "explanation": "Explanation for the correct answer"
  }
]
```

## License

This is provided as-is for learning and experimentation.
