'''file to properly format our dates'''
def formation(date):
    """Here will take the dateTime String, and format it in a way
    that we like"""
    fulldate = "%d/%d/%d" % (date.month, date.day, date.year)
    return fulldate
