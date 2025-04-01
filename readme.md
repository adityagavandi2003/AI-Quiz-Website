# AI Quiz Website

An AI-powered Quiz Website built using **Django, TailwindCSS, Ollama, Llama3.2, and SQLite**. Users can generate quizzes dynamically based on prompts and the desired number of questions. The platform also includes a complete authentication system with login and registration functionalities.

## 🚀 Features

- **AI-Generated Quizzes**: Users can generate quizzes by providing a prompt and selecting the number of questions.
- **User Authentication**: Secure login, registration, and authentication system.
- **TailwindCSS for UI**: A clean and responsive design using TailwindCSS.
- **Ollama & Llama3.2 Integration**: AI-powered question generation for dynamic and engaging quizzes.
- **SQLite Database**: Lightweight and efficient data storage for quizzes and user information.
- **Score Tracking**: Users can track their scores after completing quizzes.

## 🛠️ Tech Stack

- **Backend**: Django (Python)
- **Frontend**: TailwindCSS, JavaScript, HTML
- **AI Model**: Ollama, Llama3.2
- **Database**: SQLite

## 🔧 Installation & Setup

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/yourusername/ai-quiz-website.git
   cd ai-quiz-website
   ```

2. **Create a Virtual Environment & Activate It:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run Migrations:**
   ```bash
   python manage.py migrate
   ```

5. **Start the Development Server:**
   ```bash
   python manage.py runserver
   ```

6. **Access the Application:**
   Open your browser and go to `http://127.0.0.1:8000/`

## 📸 Screenshots
### Home Page
![Home Page](screenshot\home.png)
### Quiz Generation
![Quiz Generation](screenshot\questions.png)
### Wrong Answer
![Wrong Answer](screenshot\wrongquestion.png)
### History
![History](screenshot\history.png)
### All Quiz
![All Quiz](screenshot\history2.png)

## 📌 Future Enhancements
- Add leaderboard and user progress tracking
- Implement AI-powered explanations for quiz answers
- Enhance UI with additional TailwindCSS components

## 🤝 Contributing
Feel free to fork this repository and contribute! Pull requests are welcome.

## 📜 License
This project is licensed under the MIT License.

---
🔗 **Connect with Me:** On linkedIn [Aditya Gavandi](https://www.linkedin.com/in/adityagavandi/)