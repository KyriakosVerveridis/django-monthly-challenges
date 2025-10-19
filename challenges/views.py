from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound,HttpResponseRedirect
from django.urls import reverse

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
    "december": "Reflect on the year and set goals for the next.",
}


def index(request):
   """Display a list of all months as links to their challenge pages."""
   list_items = ""
   months = list(monthly_challenges.keys())
   for month in months:
      capitalized_month = month.capitalize()
       # Generate URL for each month's challenge
      month_path = reverse("month-challenge",args=[month])
      list_items += f" <li><a href=\"{month_path}\">{capitalized_month}</a></li>"


   respose_data =f"<ul>{list_items}</ul>"
   return HttpResponse(f"<h1>{respose_data}</h1>")


def monthly_challenge_by_number(request,month):
  """
    Redirect the user to the monthly challenge page 
    based on the month number provided in the URL.
    
    Example:
        /challenge/2 → redirects to /challenge/february
    """

  # Create a list containing all the month names (dictionary keys)
  months = list(monthly_challenges.keys())

  if month > len(months):
     return HttpResponseNotFound("<h1>Invalid month!</h1>")
     
  # Use the number provided by the user to select the correct month name
  redirect_month = months[month - 1]
  redirect_path = reverse("month-challenge",args=[redirect_month]) # /challenge/january

  # Redirect the user to the page of the selected month
  return HttpResponseRedirect(f"{redirect_path}")


def monthly_challenge(request,month):
  """
    Display the challenge text for the given month.

    If the month does not exist in the dictionary, 
    return a '404 Not Found' style response.
    """
  try:
      challenge_text = monthly_challenges[month]
      responce_data = f"<h1>{challenge_text}</h1>"
      return HttpResponse(f"{responce_data}")
  except:
      return HttpResponseNotFound("<h1>This month is not supported!</h1>")     

      
