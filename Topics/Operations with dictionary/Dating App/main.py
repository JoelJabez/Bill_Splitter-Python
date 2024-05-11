def select_dates(potential_dates):
    dates = ""
    for potential_date in potential_dates:
        if potential_date["age"] > 30 and "art" in potential_date["hobbies"]:
            if potential_date["city"] == "Berlin":
                dates += potential_date["name"] + ",".join()

    return dates