import unittest
import my_lambda
from datetime import datetime
from dateutil import tz

class Test_My_Lambda(unittest.TestCase):
    def test_givenValidTimeZone_isValidTimeZone_shouldReturnTrue(self):
         self.assertEqual(my_lambda._isValidTimezone("GMT"), True)

    def test_givenInvalidTimeZone_isValidTimezone_ShouldReturnFalse(self):
         self.assertEqual(my_lambda._isValidTimezone("ZZZ"), False)


    def test_givenValidHour_isValidHour_ShouldReturnTrue(self):
        self.assertEqual(my_lambda._isValidHour("24"), True)   


    def test_givenhourOutSide24Hr_isValidHour_shouldReturnFalse(self):
        self.assertEqual(my_lambda._isValidHour("25"), False)  

    def test_givenblankHour_isValidHour_shouldReturnFalse(self):
        self.assertEqual(my_lambda._isValidHour(""), False) 


    def test_givenValidTag_isValidShutdownTagValue_shouldReturnTrue(self):
        self.assertEqual(my_lambda._isValidShutdownTagValue("GMT-7"), True) 

    def test_givenInValidTag_isValidShutdownTagValue_shouldReturnFalse(self):
        self.assertEqual(my_lambda._isValidShutdownTagValue("BMT-7"), False) 


    def test_givenTimezone_currentHourForTimezone_shouldReturnValidHour(self):
        hour = datetime.now(tz.gettz("Etc/GMT")).hour
        self.assertEqual(my_lambda._getCurrentHourForTimezone("GMT"), hour)

        psthour = datetime.now(tz.gettz("US/Pacific")).hour
        print('pst:' +str(psthour))
        self.assertEqual(my_lambda._getCurrentHourForTimezone("PST"), psthour)

        csthour = datetime.now(tz.gettz("US/Central")).hour
        print('cst:' +str(csthour))
        self.assertEqual(my_lambda._getCurrentHourForTimezone("CST"), csthour)

        esthour = datetime.now(tz.gettz("US/Eastern")).hour
        print('est:' +str(esthour))
        self.assertEqual(my_lambda._getCurrentHourForTimezone("EST"), esthour)


    def test_givenAnAbbreviation_getTimeZoneDescriptor_shouldReturnValidTimeZone(self):
        self.assertEqual(my_lambda._getTimeZoneDescriptor("PST"),"US/Pacific")


    def test_givenEmptyString_getTimezoneFromTagValue_shouldReturnEmptyString(self):
        self.assertEqual(my_lambda._getTimezoneFromTagValue(""),"")

    def test_givenStringWithValidDelimiter_getTimezoneFromTagValue_shouldReturnValidString(self):
        self.assertEqual(my_lambda._getTimezoneFromTagValue("GMT-24"),"GMT")
        self.assertEqual(my_lambda._getTimezoneFromTagValue("GMT-"),"GMT")

    def test_givenStringWithValidDelimiter_getHourFromTagValue_shouldReturnValidString(self):
        self.assertEqual(my_lambda._getHourFromTagValue("GMT-24"),"24")
        self.assertEqual(my_lambda._getHourFromTagValue("-24"),"24")



if __name__ == '__main__':
    unittest.main()