class Station:

    def __init__(self, geography, location):
        self.rainfall = False
        self.treatment = False
        self.days_since_treatment = 0
        self.geography = geography
        self.location = location

    def getGeographyScore(self):
        score = geography_Score(self.geography)
        return score

    def getLocationScore(self):
        score = location_Score(self.location)
        return score

    def getTemperatureScore(self, temperature):
        score = temperature_Score(temperature)
        return score

    def getAverageScore(self, temperature):
        geoscore = self.getGeographyScore()
        locationscore = self.getLocationScore()
        tempscore = self.getTemperatureScore(temperature)
        return 100 * round(((geoscore + locationscore + tempscore) / 3), 3)

    def getStationInfo(self, temperature):
        return {'location' : self.location, 'score' : self.getAverageScore(temperature)}

def geography_Score(place):
    if place == "Marshland":
        return 1
    elif place == "Pond":
        return 0.75
    elif place == "Residential":
        return 0.25
    elif place == "Creek":
        return 0.2
    elif place == "Farmland":
        return 0.15
    else:
        return -1

def location_Score(location):
    if location == "WAS008":
        return 1
    elif location == "WAS001":
        return 0.7
    elif location == "HUR009":
        return 0.5
    else:
        return 0.3

def temperature_Score(temp):
    if temp <= 17 or temp >= 35:
        return 0
    else:
        score = ((1.975 * -((temp - 26) ** 2)) + 160) / 160
        return score