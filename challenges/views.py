from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound

# Create your views here.

monthly_challenges = {
    "january": "Eat no meat for the entire month!",
    "february": "Walk at least 20 minutes every day!",
    "march": "Learn Django for at least 20 minutes a day!",
    "april": "Read one book every week.",
    "may": "Meditate for 10 minutes every day.",
    "june": "Drink at least 2 liters of water daily.",
    "july": "Write a daily journal entry.",
    "august": "Try a new recipe every week.",
    "september": "Practice a new hobby for 30 minutes daily.",
    "october": "Take a short walk after every meal.",
    "november": "Send a kind message to someone every day.",
    "december": "Reflect on the year and set goals for the next."
}



def monthly_challenge_by_number(request,month):
  return HttpResponse(month)


def monthly_challenge(request,month):
  try:
      challenge_text = monthly_challenges[month]
      return HttpResponse(challenge_text)
  except:
      return HttpResponse("This month is not supported!")     
