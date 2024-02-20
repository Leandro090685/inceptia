import requests

class GeoAPI:
    API_KEY = "d81015613923e3e435231f2740d5610b"
    LAT = "-35.836948753554054"
    LON = "-61.870523905384076"

    @classmethod
    def is_hot_in_pehuajo(cls):
        url = f"https://api.openweathermap.org/data/2.5/weather?lat={cls.LAT}&lon={cls.LON}&appid={cls.API_KEY}&units=metric"
        
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an exception for HTTP errors
            data = response.json()
            temperature = data['main']['temp']
            if temperature > 28:
                return True
            else:
                return False
        except requests.exceptions.RequestException:
            return False  # Return False for any HTTP exception
        except KeyError:
            return False  # Return False if the required data is not found in the response

a=GeoAPI
print(a.is_hot_in_pehuajo())