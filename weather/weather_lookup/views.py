from django.shortcuts import render


def home(request):
    import json, requests

    # Get data from weather api
    api_requests = requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=10019&distance=5&API_KEY=08181FB1-D601-4C1F-8734-CA753616C2E5")

    # Covert json api data to python object
    try:
        api = json.loads(api_requests.content)
    except Exception as e:
        api = "Error..."

    return render(request, 'home.html', {'api': api}) # Pass through api data to webpage


def about(request):
    return render(request, 'about.html', {})
