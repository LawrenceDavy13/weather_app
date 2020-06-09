from django.shortcuts import render


def home(request):
    import json, requests

# POST

    if request.method == "POST":
        zipcode = request.POST['zipcode']

         # Get data from weather api
        api_requests = requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=" + zipcode + "&distance=5&API_KEY=08181FB1-D601-4C1F-8734-CA753616C2E5")

        # Covert json api data to python object
        try:
            api = json.loads(api_requests.content)
        except Exception as e:
            api = "Error..."


        
        if api[0]['Category']['Name'] == "Good":
            category_description = "(0 - 50) Air quality is considered satisfactory, and air pollution poses little or no risk."
            category_color = "good"
        elif api[0]['Category']['Name'] == "Moderate":
            category_description = "(51 -100) Air quality is acceptable; however, for some pollutants there may be a moderate health concern for a very small number of people who are usually sensitive to air pollution"
            category_color = "moderate"
        elif api[0]['Category']['Name'] == "Unhealthy for Sensitive Groups":
            category_description = "(101 - 150) Although general public is not likely to be affected at this AQI range, people with lung disease, older adults and children are at a greater risk from exposure to ozone, whereas persons with heart and lung disease, older adults and children are at greater risk from the presence of particles in the air."
            category_color = "Unhealthy for Sensitive Groups"
        elif api[0]['Category']['Name'] == "Unhealthy":
            category_description = "(151 - 200) Everyone may begin to experience health effects; members of sensitive groups may experience more serious health effects."
            category_color = "unhealthy"
        elif api[0]['Category']['Name'] == "Very Unhealthy":
            category_description = "(201 - 300) Health alert: everyone may experience more serious health effects."
            category_color = "veryhealthy"
        elif api[0]['Category']['Name'] == "Hazardous":
            category_description = "(301 - 500) Health warnings of emergancy conditions. The entire population is more likely to be affected."
            category_color = "hazardous"


        return render(request, 'home.html', {'api': api, 'category_description': category_description, 'category_color' : category_color}) # Pass through api data to webpage


# GET
    
    else:


        # Get data from weather api
        api_requests = requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=10019&distance=5&API_KEY=08181FB1-D601-4C1F-8734-CA753616C2E5")

        # Covert json api data to python object
        try:
            api = json.loads(api_requests.content)
        except Exception as e:
            api = "Error..."


        
        if api[0]['Category']['Name'] == "Good":
            category_description = "(0 - 50) Air quality is considered satisfactory, and air pollution poses little or no risk."
            category_color = "good"
        elif api[0]['Category']['Name'] == "Moderate":
            category_description = "(51 -100) Air quality is acceptable; however, for some pollutants there may be a moderate health concern for a very small number of people who are usually sensitive to air pollution"
            category_color = "moderate"
        elif api[0]['Category']['Name'] == "Unhealthy for Sensitive Groups":
            category_description = "(101 - 150) Although general public is not likely to be affected at this AQI range, people with lung disease, older adults and children are at a greater risk from exposure to ozone, whereas persons with heart and lung disease, older adults and children are at greater risk from the presence of particles in the air."
            category_color = "Unhealthy for Sensitive Groups"
        elif api[0]['Category']['Name'] == "Unhealthy":
            category_description = "(151 - 200) Everyone may begin to experience health effects; members of sensitive groups may experience more serious health effects."
            category_color = "unhealthy"
        elif api[0]['Category']['Name'] == "Very Unhealthy":
            category_description = "(201 - 300) Health alert: everyone may experience more serious health effects."
            category_color = "veryhealthy"
        elif api[0]['Category']['Name'] == "Hazardous":
            category_description = "(301 - 500) Health warnings of emergancy conditions. The entire population is more likely to be affected."
            category_color = "hazardous"


        return render(request, 'home.html', {'api': api, 'category_description': category_description, 'category_color' : category_color}) # Pass through api data to webpage


def about(request):
    return render(request, 'about.html', {})
