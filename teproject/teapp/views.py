import requests
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect

api_key = "3032256437fc458:pbeddn0ri9bdx0g"

def index(request):

    return render(request, 'teapp/index.html')

def result(request):
    if request.method == 'POST':
        first_country = request.POST.get('country1')
        second_country = request.POST.get('country2')
        two_country_url = f"https://api.tradingeconomics.com/ratings/{first_country.lower()},{second_country.lower()}?c={api_key}&f=json"
        
        try: 
            response = requests.get(two_country_url)
            if response.status_code == 200:
            # API call was successful
                data = response.json() 
                '''
                The response has different indexes, hence looping wont be efficient, the code 
                below gets the specific rating agency and display its results at the end of api call
                '''
                country_1_outlook = data[0]['SP_Outlook']
                country_1_rating = data[0]['SP']
                country_1 = data[0]['Country']

                #second country
                country_2_outlook = data[1]['SP_Outlook']
                country_2_rating = data[1]['SP']
                country_2 = data[1]['Country']
        except ObjectDoesNotExist:
            return "Maximum Tries Exceeded"
        except Exception as e:
            print(e)
            redirect('index.html')
    
    
    context = {
        'country_1_outlook': country_1_outlook,
        'country_1_rating': country_1_rating,
        'country_1': country_1,
        'country_2_outlook': country_2_outlook,
        'country_2_rating': country_2_rating,
        'country_2': country_2,
    }
    return render(request, 'teapp/result.html', context)
   

