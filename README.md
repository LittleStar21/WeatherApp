# Weather App
* Weather App is a program to check the weather condition of a selected country in the next 5 days.

## Usage
* Make sure to have Python3 installed.
* Make sure to have the required modules installed from requirements.txt.
* Make sure to insert the API_KEY(OpenWeatherApp) in the app.py file(line 17).
```Python
	def search():
		country = request.args.get("country")
		API_KEY = "Enter api key"
```
* Install geckodriver and then change the executable_path inside "test.py" into where the geckodriver lives.
```Python
class MyWebsiteTest(unittest.TestCase):
    def setUp(self):
        # Change the path to where the geckodriver file exists
        self.browser = webdriver.Firefox(executable_path=r"C:\Users\fifia\Desktop\geckodriver.exe")
```
* Then, on the terminal, run the flask application by typing
```bash
flask run
```
* After that, there will be a link to http://127.0.0.1:5000/
* Open this link on the browser to run the app manually or run test.py to do the automatic test by Selenium
```bash
python test.py
```