# 🌌 Galactic Quiz

Welcome to **Galactic Quiz**, a fun and interactive quiz application built using **Streamlit**. Challenge yourself with questions on various topics like **DSA**, **DBMS**, and **Python**. Test your knowledge, improve your skills, and have fun while doing it! 🚀

---

## Features

- **User Registration & Login**: Register with your name, username, email, class, and password to start your journey.
- **Quiz Categories**: Choose from topics like **DSA**, **DBMS**, and **Python**.
- **Randomized Questions**: Enjoy a unique set of questions every time you play.
- **Score Tracking**: Get instant feedback on your performance.
- **Data Persistence**: User data and quiz questions are stored in a JSON file.

---

## Installation & Setup

### Prerequisites

1. Python 3.8 or above installed.
2. Install Streamlit:
```bash
pip install streamlit
```

### Clone the Repository

```bash
git clone https://github.com/your-repo/galactic-quiz.git
cd galactic-quiz
```

### Install Required Dependencies

```bash
pip install -r requirements.txt
```

### Run the Application

```bash
streamlit run app.py
```

---

## File Structure

```plaintext
.
├── data.json               # Contains user and question data
├── app.py        # Main application logic
├── requirements.txt        # List of required Python packages
├── README.md               # Project documentation
```

### `data.json`

Stores the quiz questions and user data. Example structure:

```json
{
  "users": {
        "username": {
            "name": "name",
            "email": "xyz@gmail.com",
            "class": "CSE",
            "pwd": "password"
        },
  "questions": {
    "DSA": {
      "1": {
        "ques": "What is a stack?",
        "opt": ["Data Structure", "Algorithm", "Loop"],
        "ans": "Data Structure"
      }
    },
    "DBMS": {
      "1": {
        "ques": "What is normalization?",
        "opt": ["Data organization", "Data replication", "Data deletion"],
        "ans": "Data organization"
      }
    },
    "PYTHON": {
      "1": {
        "ques": "What is PEP 8?",
        "opt": ["Python standard", "Python library", "Python IDE"],
        "ans": "Python standard"
      }
    }
  }
}
```

### `app.py`

Contains the main Streamlit application logic:

- User registration, login, and logout.
- Quiz question display and scoring system.

---

## Requirements

The application uses the following Python libraries:

- **Streamlit**: For building the web app.
- **Random**: For selecting random questions.
- **JSON**: For managing user and quiz data.

### `requirements.txt`

```plaintext
streamlit>=1.22.0
```

---

## Usage Instructions

1. **Registration**:

   - Enter your details including name, username, email, class, and password to create an account.

2. **Login**:

   - Use your registered username and password to log in.

3. **Select a Quiz**:

   - Choose your favorite topic (DSA, DBMS, or Python).

4. **Answer Questions**:

   - Select answers for each question. You can randomize questions if desired.

5. **Submit**:
   - Submit your quiz to see your score.

---

## Future Improvements

- Add more quiz topics.
- Include a leaderboard feature.
- Allow users to create their own quizzes.
- Integrate with a database for better scalability.

---

## Contributions

Contributions are welcome! Feel free to fork the repository and create pull requests for bug fixes, feature additions, or any improvements.

---

## License

This project is licensed under the MIT License. Feel free to use, modify, and distribute it.

---

## Author

**Rohit Tudu**  
Connect with me on [LinkedIn](https://linkedin.com/in/rohittudu).
