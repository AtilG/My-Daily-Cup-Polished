"""file to properly format our dates"""


def formation(date):
    """Here will take the dateTime String, and format it in a way
    that we like"""
    fulldate = "%d/%d/%d" % (date.month, date.day, date.year)
    return fulldate


def sort_emotions(entries, sort_key, tones):
    """This method will filter out all the entries that don't have the emotion
    we are looking for, the emotion will be held in the variable called sort_key"""
    if sort_key == "All":
        return entries, tones
    new_entries = []
    new_tones = []
    length = len(entries)
    for i in range(length):
        if sort_key in tones[i]:
            new_entries.append(entries[i])
            new_tones.append(tones[i])
    return new_entries, new_tones
