# DjangoQuizApp
Hi, This is a simple Quiz App for the Capitals of Countries.

#Purpose Of the Quiz App:

The quiz is designed to test your knowledge on the Capitals of various Countries.
The Player can enter their name and click on proceed to start the quiz.
The question is then displayed on the screen and player has to enter the answer.
For each correct answer, a message appears confirming the same and for each wrong answer, a message will notify that and the correct answer will be displayed for the player's reference.

#Working:

The quiz application uses HTML, CSS, JS for the Frontend. 
The App is Responsive and can be used in both laptop and mobile view. 
The functionality has been incorporated using Django framework as the Backend. 
The questions are displayed randomly and the player can choose to attempt a different question if needed.
After finishing the quiz, the player can logout of the application by clicking on the logout button.


## Prerequisites for running the project:
Python 3 
Django  
A web browser 

#Getting Started:

1. Clone the repository to your local machine: 
git clone https://github.com/shubhi16-sha/DjangoQuizApp.git

2. Navigate to the project directory:
cd CountryCapitalQuiz

3. Create a virtual environment and activate it: (if needed)

   python -m venv venv 
   source venv/bin/activate 
   # On Windows, use venv\Scripts\activate

4. Install the project dependencies:
   
   pip install -r requirements.txt

5. Run the Django development server:
   bash

   python3 manage.py runserver 

6. Access the application in your web browser at http://127.0.0.1:8000/ 


#Usage:

  Enter your name on the welcome screen and click "Start Quiz."

	Guess the capital of the displayed country and click "Check."
	
	See if your guess is correct, and click "New Question" for a new one.

	Click "Logout" to return to the welcome screen and start a new session.
