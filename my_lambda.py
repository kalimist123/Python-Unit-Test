
import logging
from pprint import pprint
from datetime import datetime
from dateutil import tz

logger = logging.getLogger()
logger.setLevel(logging.INFO)



_shutdown_delim = "-"
_timeZoneMap =	{
  "GMT": "Etc/GMT",
  "EST": "US/Eastern",
  "PST": "US/Pacific",
  "CST": "US/Central"
}
           


def _isShutdownRequired(shutdownTagValue):
    if _isValidShutdownTagValue(shutdownTagValue):
        tagValueTimeZone=_getTimezoneFromTagValue(shutdownTagValue)
        tagValueHour=_getHourFromTagValue(shutdownTagValue)
        
        if _currentHourForTimeZoneMatchesTagHour(tagValueHour,tagValueTimeZone):
           return True
        else:
           return False


def _printInstanceDetails(instance):
    pprint("instance details:")
    pprint(instance.__dict__)
    

def _isValidShutdownTagValue(shutdownTagValue):
    if shutdownTagValue.find(_shutdown_delim)==-1:
        return False
    if not _isValidHour(_getHourFromTagValue(shutdownTagValue)):
        return False
    if not _isValidTimezone(_getTimezoneFromTagValue(shutdownTagValue)):
        return False
    return True

def _isValidHour(hourStr):
    if not hourStr.isdigit():
        return False
    if not 1 <= int(hourStr) <= 24:
        return False
    return True
    

def _isValidTimezone(tz):
    if tz in _timeZoneMap:
        return True
    return False
    
def _getTimezoneFromTagValue(tagValue):
    return tagValue.split(_shutdown_delim)[0]
    
def _getHourFromTagValue(tagValue):
    return tagValue.split(_shutdown_delim)[1]

def _currentHourForTimeZoneMatchesTagHour(tagValueHour, timeZone):
     if _getCurrentHourForTimezone(timeZone) == int(tagValueHour):
         return True
     return False
     
def _getCurrentHourForTimezone(timeZone):
    timezoneDescriptor=_getTimeZoneDescriptor(timeZone)
    timezone=_getTimeZone(timezoneDescriptor)
    return datetime.now(timezone).hour
   

def _getTimeZone(timeZoneDescriptor):
    return tz.gettz(timeZoneDescriptor)

def _getTimeZoneDescriptor(timeZoneAbbreviation):
    return _timeZoneMap.get(timeZoneAbbreviation)
