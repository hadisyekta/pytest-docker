
class Point():
    def __init__(self, name, latitude, longitude):
        if not isinstance(name, str):
            raise TypeError("City name must be String")
        self._name = name
        if not (-90 <=latitude <=90) or not (-90 <=longitude <=90):
            raise ValueError("Invalid Latitude or Longitude")
        self._latitude = latitude
        self._longitude = longitude

    def get_lat_long(self):
        return (self._latitude, self._longitude)  
