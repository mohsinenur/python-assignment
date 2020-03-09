def get_synonyms_from_files():
    all_synonyms = {"family": ["class", "category", "folk", "kinsfolk", "fellowship"],
                    "eat": ["consume", "use up", "deplete", "exhaust", "feed"],
                    "house": ["household", "home", "firm", "mansion", "put up", "domiciliate"]}

    try:
        count = 1
        with open("synonyms.txt") as file:
            lines = file.readlines()
            for line in lines:
                if not line:
                    print("Error in line " + count + ":")
                else:
                    print(line)
                count += 1
            return all_synonyms
    except Exception as e:
        print(e)
        all_synonyms = {}
        return all_synonyms
