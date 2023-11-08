from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Country
import random

def index(request):
    user_name = request.GET.get('user_name', None)
    countries = Country.objects.all()
    random_country = random.choice(countries)
    context = {
        'country': random_country,
        'country_id': random_country.id,  # Passing the country ID as a variable
        'user_name': user_name,  # Include the user_name in the context to display it later
    }
    return render(request, 'capital_guess/index.html', context)


def play_quiz(request):
    user_name = request.GET.get('user_name')
    if not user_name:
        return redirect('index')  # Redirect to the index page if user_name is not provided

    countries = Country.objects.exclude(capital="")
    random_country = None

    # Keep selecting a random country until a valid one is found
    while not random_country:
        random_country = random.choice(countries)

        # Check if the selected country has a valid capital
        if not random_country.capital:
            random_country = None

    context = {
        'user_name': user_name,
        'country': random_country,
        'country_id': random_country.id,  # Passing the country ID as a variable
    }
    return render(request, 'capital_guess/play_quiz.html', context)



def check_guess(request):
    if request.method == 'POST':
        country_id = request.POST.get('country_id')
        user_guess = request.POST.get('user_guess').strip().lower()

        try:
            country = Country.objects.get(pk=country_id)
            correct = user_guess == country.capital.lower()
            response_data = {
                'correct': correct,
                'correct_answer': country.capital,
            }
        except ObjectDoesNotExist:
            response_data = {
                'correct': False,
                'correct_answer': 'Not found',
            }

        if request.session.get('answered', False):
            # User has already answered
            response_data['answered'] = True

        else:
            request.session['answered'] = True  # Mark the user as answered
            response_data['answered'] = False

        return JsonResponse(response_data)


def get_new_question(request):
    user_name = request.GET.get('user_name')
    if not user_name:
        return redirect('index')
    # Generate a random country index
    max_country_id = Country.objects.count()
    random_country_id = random.randint(1, max_country_id)

    # Get a random country from the database
    random_country = Country.objects.get(pk=random_country_id)

    return render(request, 'capital_guess/play_quiz.html', {'user_name': user_name, 'country': random_country})
