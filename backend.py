import requests as rq


def get_data(city, first_date, last_date):
    API_KEY = 'CB93XCP3CPJN2SRCDKYZCP5TU'

    url = f'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{city}/{first_date}/{last_date}?unitGroup=metric&include=fcst%2Cdays&key={API_KEY}&contentType=json'

    response = rq.get(url)
    my_data = response.json()

    '''my_list1 = []
    for i in range(len(my_data['days'])):
        # my_data['days'] Is List
        # my_data['days'][i] Is Dict
        # my_date Is String
        my_date = my_data['days'][i]['datetime']

        # list
        my_list1.append(my_date) '''

    # i['datetime'] Is String (instead of above scripts)
    date = [i['datetime'] for i in my_data['days']]
    temp = [i['temp'] for i in my_data['days']]
    conditions = [i['conditions'] for i in my_data['days']]
    tempmax = [i['tempmax'] for i in my_data['days']]
    tempmin = [i['tempmin'] for i in my_data['days']]
    humidity = [i['humidity'] for i in my_data['days']]
    sunrise = [i['sunrise'] for i in my_data['days']]
    sunset = [i['sunset'] for i in my_data['days']]
    description = [i['description'] for i in my_data['days']]
    windspeed = [i['windspeed'] for i in my_data['days']]

    return date, temp, conditions


if __name__ == "__main__":
    get_data(city='Tehran', first_date='2023-08-09', last_date='2023-08-15')
