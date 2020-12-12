from flask import Flask, render_template, request
import requests, json, pycountry

app = Flask(__name__)

app.config["TEMPLATES_AUTO_RELOAD"] = True

@app.route("/")
def index():
    countries = list(pycountry.countries)
    countries = [country.name for country in countries]
    return render_template("index.html", countries=countries)

@app.route("/search")
def search():
    country = request.args.get("country")
    API_KEY = "Enter api key"
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={country}&appid={API_KEY}&units=metric"

    response = requests.get(url).json()
    if response["cod"] == 401:
        return render_template("error.html", message="Please insert the API key")
    
    if response["cod"] == "200":
        # Saving weather info
        city = response["city"]["name"]
        weathers = {}
        avg_temp = 0
        avg_diff = 0

        # For calculations
        date = None
        total_temp_day = 0
        temp_max_day = 0
        temp_min_day = 0
        counter = 0

        # Iterate over all forecast
        for item in response["list"]:

            # Obtain the current weather info
            cur_date = item["dt_txt"].split()[0]
            cur_temp = float(item["main"]["temp"])
            cur_temp_min = float(item["main"]["temp_min"])
            cur_temp_max = float(item["main"]["temp_max"])
        
            if cur_date != date:
                if date != None:
                    # Append dict
                    avg_temp_day = total_temp_day / counter
                    diff_temp_day = temp_max_day - temp_min_day
                    weathers[date] = [avg_temp_day, diff_temp_day]

                    # Calculating averages
                    avg_temp += avg_temp_day
                    avg_diff += diff_temp_day

                # Reset for new date
                total_temp_day = 0
                counter = 0
                temp_max_day = cur_temp_max
                temp_min_day = cur_temp_min
                date = cur_date
        
            # Get the average of temps
            total_temp_day += cur_temp
            counter += 1
            temp_max_day = max(temp_max_day, cur_temp_max)
            temp_min_day = min(temp_min_day, cur_temp_min)

        return render_template("search.html", city=city, weathers=weathers, avg_temp=avg_temp / 5, avg_diff=avg_diff / 5)

    else:
        return render_template("error.html", message="Sorry, we cannot get the data about this country. Try searching other countries.")