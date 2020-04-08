# numbers determeined by the average amount of mosquitos per pickup at each loaction. Higher average = Higher score.
def location_Score(location):
    if location == "WAS008":
        return 1
    elif location == "WAS001":
        return 0.7
    elif location == "HUR009":
        return 0.5
    else:
        return 0.3
