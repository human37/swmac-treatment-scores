from geographyscore import geography_Score
from locationscore import location_Score
from tempscore import temperature_Score

class Location:

    def __init__(self, geography, location, temperature):
        self.rainfall = False
        self.treatment = False
        self.days_since_treatment = 0
        self.geography = geography
        self.location = location
        self.temperature = temperature
    def getGeographyScore(self):
        score = geography_Score(self.geography)
        return score
    def getLocationScore(self):
        score = location_Score(self.location)
        return score
    def getTemperatureScore(self, temperature):
        score = temperature_Score(self.temperature)
        return score
