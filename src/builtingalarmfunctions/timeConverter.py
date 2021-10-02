"""
Class used to transform the gived time in other time types
"""


class TimeConverter:
    """
    TimeConverter Class
    """

    def convert_hour_to_minutes(self, hours):
        """
        Function to convert hours in minutes
        :param hours: quantity of hours you want to convert to minutes
        :return: Time in minutes
        """
        hours_minutes = hours * 60
        return hours_minutes

    def convert_hour_to_seconds(self, hours):
        """
        Function to convert hours in seconds
        :param hours: quantity of hours you want to convert to seconds
        :return: Time in seconds
        """
        minutes = TimeConverter.convert_hour_to_minutes(hours)
        seconds = minutes * 60
        return seconds

    def convert_minutes_to_hour(self, minutes):
        """
        Function to convert minutes in hours
        :param minutes: quantity of minutes to convert to hours
        :return: Time in hours
        """
        minute_hours = minutes / 60
        return minute_hours

    def convert_minutes_to_seconds(self, minutes):
        """
        Function to convert minutes in seconds
        :param minutes: quantity of minutes to convert to seconds
        :return:
        """
        seconds = minutes * 60
        return seconds

    def convert_seconds_to_hour(self, seconds):
        """
        Function to convert seconds in hours
        :param seconds: quantity of seconds to convert to hours
        :return: Time in hours
        """
        seconds_hours = seconds / 3600
        return seconds_hours

    def convert_seconds_to_minutes(self, seconds):
        """
        Function to convert secinds in minutes
        :param seconds: quantity of seconds to convert to minutes
        :return:  Time in minutes
        """
        h_minutes = TimeConverter.convert_seconds_to_hour(seconds)
        m_seconds = h_minutes * 60
        return m_seconds
