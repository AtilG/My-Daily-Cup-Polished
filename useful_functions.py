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
    for i in range(0, len(entries)):
        if sort_key in tones[i]:
            new_entries.append(entries[i])
            new_tones.append(tones[i])
    return new_entries, new_tones

if __name__=='__main__':
    entry = ['I am well', 'Today was a wonderful day', 'Today was the worst day of my life.']
    tones = [['Excited'],['Excited', 'Happy'], ['sad']]
    commence, pop = sort_emotions(entry, 'Excited', tones)
    print(commence)