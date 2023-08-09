import streamlit as sl
import plotly.express as px
from backend import get_data

sl.title("weather forecast".title())
city = sl.text_input(label='enter city:'.title())
first_date = sl.date_input(label='First date', key='first_date')
last_date = sl.date_input(label='Last date', key='last_date')
kind = sl.selectbox(label='Select A Kind:', options=['Temperature', 'Sky'])

try:
    if city:
        weather_date = get_data(city, first_date, last_date)
        sl.write(weather_date)
        x, y, z = weather_date

        match kind:

            case 'Temperature':
                figure = px.line(x=x, y=y, labels={'x': 'x_axis', 'y': 'y_axis'})
                sl.plotly_chart(figure)
            case 'Sky':

                for con in z:
                    match con:
                        case 'Clear':
                            sl.image('images/clear-day.png', width=110)
                            sl.write(x[z.index(con)])

                        case 'Rain, Partially cloudy':
                            sl.image('images/rain.png', width=110)
                            sl.write(x[z.index(con)])

                        case 'Snow':
                            sl.image('images/snow.png', width=110)
                            sl.write(x[z.index(con)])

                        case _:
                            sl.image('images/cloud.png', width=110)
                            sl.write(x[z.index(con)])

    else:
        sl.write("Please Enter A City")
except:
    sl.write("Please Enter An Existing City")
