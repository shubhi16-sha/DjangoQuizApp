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
1. Python installation --->  Follow the link https://www.python.org/downloads/ for installation.
2. Django (can be installed from the requirements.txt file, the command is shown below) 
A web browser 

#Getting Started:

1. Clone the repository to your local machine from the master branch:
	git clone https://github.com/shubhi16-sha/DjangoQuizApp.git

2. Navigate to the project directory:
	cd DjangoQuizApp
	cd CountryCapitalQuiz 

3. Create a virtual environment and activate it: (optional)

   python -m venv venv
   
   source venv/bin/activate  #On Windows, use venv\Scripts\activate

5. Install the project dependencies:
	Python: https://www.python.org/downloads/
	Django  - (run the following command in the command prompt) python -m pip install Django
	pip install -r requirements.txt or pip install --user -r requirements.txt

7. Run the Django development server:

   python3 manage.py runserver  or
   python manage.py runserver

8. Access the application in your web browser at http://127.0.0.1:8000/ 


#Usage:

  Enter your name on the welcome screen and click "Start Quiz."

	Guess the capital of the displayed country and click "Check."
	
	See if your guess is correct, and click "New Question" for a new one.

	Click "Logout" to return to the welcome screen and start a new session.
