# Time System 

daysPast = 0 # POTENTIAL BUG: ... I shouldn't change a immutable object in functions
# daysPast = 0.4 # The game starts at around 10am in the morning. 
# x.25 - 6am, x.5 - 12pm, x.75 - 6pm, x.00 - 12am; 
# 0.1 - 2.4h

def currentTime():
    ''' tell current period of day given daysPast
    input: None - but use global daysPast(int)
    output: dayPeriod(str)
    '''
    daytime = daysPast % 1
    if daytime<0.25:
        dayPeriod = 'dawn'
    elif daytime<0.45:
        dayPeriod = 'morning'
    elif daytime<0.55:
        dayPeriod = 'noon'
    elif daytime<0.70:
        dayPeriod = 'afternoon' 
    elif daytime<0.80:
        dayPeriod = 'dawn'
    else:
        dayPeriod = 'night'
    return dayPeriod