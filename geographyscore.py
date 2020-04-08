# Can take Pond, Creek, Farmland, Residential, and Marshland as parameters.
# Scores are based on the total number of mosquitoes at each geography type. Highest number = Highest score
def geography_Score(place):
    if place == "Pond":
        return 0.75
    elif place == "Creek":
        return 0.2
    elif place == "Farmland":
        return 0.15
    elif place == "Residential":
        return 0.25
    elif place == "Marshland":
        return 1
    else:
        print("geographyScore didnt recive a valid parameter")
