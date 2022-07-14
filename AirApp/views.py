from django.shortcuts import render

# Create your views here.
def home(request):
    import json
    import requests
    if request.method == "POST":
        zipcode = request.POST['zipcode']
        url = "https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=" + zipcode + "&distance=25&API_KEY=D096BC2B-ADBD-4FFA-A694-8806AA7C4830"
        #this goes and makes request
        api_request = requests.get(url)

        try:
            #this loads result into variable - now json object
            result = json.loads(api_request.content)
        except Exception as e:
            result = "Error..."

        if result[0]['Category']['Name'] == "Good":
            category_description = "(0 - 50)  Air quality is satisfactory, and air pollution poses little or no risk."
            category_color = "good"
        elif result[0]['Category']['Name'] == "Moderate":
            category_description ="(51 - 100) Air quality is acceptable. However, there may be a risk for some people, particularly those who are unusually sensitive to air pollution."
            category_color = "moderate"
        elif result[0]['Category']['Name'] == "Uhealthy for Sensitive Groups":
            category_description ="(101 - 150) Members of sensitive groups may experience health effects. The general public is less likely to be affected."
            category_color = "usg"
        elif result[0]['Category']['Name'] == "Unhealthy":
            category_description ="(151 - 200) Some members of the general public may experience health effects; members of sensitive groups may experience more serious health effects."
            category_color = "unhealthy"
        elif result[0]['Category']['Name'] == "Very Unhealthy":
            category_description ="(201 - 300) Health alert: The risk of health effects is increased for everyone."
            category_color = "veryunhealthy"
        elif result[0]['Category']['Name'] == "Hazardous":
            category_description ="(301+) Health warning of emergency conditions: everyone is more likely to be affected."
            category_color = "hazardous"

        return render(request, 'home.html', {'result': result, 
            'category_description': category_description,
            'category_color': category_color,
            })

    else:
        #this goes and makes request
        api_request = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=98087&distance=25&API_KEY=D096BC2B-ADBD-4FFA-A694-8806AA7C4830")

        try:
            #this loads result into variable - now json object
            result = json.loads(api_request.content)
        except Exception as e:
            result = "Error..."

        if result[0]['Category']['Name'] == "Good":
            category_description = "(0 - 50)  Air quality is satisfactory, and air pollution poses little or no risk."
            category_color = "good"
        elif result[0]['Category']['Name'] == "Moderate":
            category_description ="(51 - 100) Air quality is acceptable. However, there may be a risk for some people, particularly those who are unusually sensitive to air pollution."
            category_color = "moderate"
        elif result[0]['Category']['Name'] == "Uhealthy for Sensitive Groups":
            category_description ="(101 - 150) Members of sensitive groups may experience health effects. The general public is less likely to be affected."
            category_color = "usg"
        elif result[0]['Category']['Name'] == "Unhealthy":
            category_description ="(151 - 200) Some members of the general public may experience health effects; members of sensitive groups may experience more serious health effects."
            category_color = "unhealthy"
        elif result[0]['Category']['Name'] == "Very Unhealthy":
            category_description ="(201 - 300) Health alert: The risk of health effects is increased for everyone."
            category_color = "veryunhealthy"
        elif result[0]['Category']['Name'] == "Hazardous":
            category_description ="(301+) Health warning of emergency conditions: everyone is more likely to be affected."
            category_color = "hazardous"

        return render(request, 'home.html', {'result': result, 
            'category_description': category_description,
            'category_color': category_color,
            })

def about(request):
    return render(request, 'about.html', {})
