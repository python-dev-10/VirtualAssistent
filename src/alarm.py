"""Module for Alarm functions"""
import schedule
from alarmsong import run_music
import time as timelib
import sched
from builtingalarmfunctions import stringtimevalidator as timevalidator
from builtingalarmfunctions import timeConverter


class Alarm:
    """
    CallableAlarm functions
    """

    def __init__(self):
        self.scheduled = sched.scheduler(timelib.time, timelib.sleep)
        self.time_converter = timeConverter.TimeConverter

    def add_alarm(self, text):
        """
        main function that will be called, when the intention is to 7
        create an alarm
        :param text: spelled user phrase
        :return: None
        """
        # engine = pyttsx3.init()
        string_time_validator = timevalidator.StringTimeValidator()
        print("entrou add_alarm")
        if "minutos" in text:
            self.handle_per_minute(text, string_time_validator)
        if "horas" in text:
            self.handle_per_hour(text, string_time_validator)
        if "segundos" in text:
            self.handle_per_second(text, string_time_validator)

    def sched_per_second(self,time):
        """
        Function to execute the alarm in seconds
        :param time: time int for create the alarm
        :return: None
        """
        self.scheduled.enter(time, 2, run_music())
        self.scheduled.run()

    def sched_per_minute(self, time):
        """
        Function to execute the alarm in minutes
        :param time: time int for create the alarm
        :return: None
        """
        self.scheduled.enter(self.time_converter.convert_minutes_to_seconds(time), 2, run_music())
        self.scheduled.run()

    def sched_per_hour(self, time):
        """
        Function to execute the alarm in hours
        :param time: time int for create the alarm
        :return: None
        """
        self.scheduled.enter(self.time_converter.convert_hour_to_seconds(time), 2, run_music())
        schedule.every().hour.do(run_music())

    def schedule_per_day(self):
        """

        :param time: time int for create the alarm
        :return: none
        """
        schedule.every().day.at("00:00").do(run_music())

    def schedule_per_week_day(self,text):
        """

        :param time: time int for create the alarm
        :return: none
        """
        return Alarm.verify_weekday(self, text)

    def verify_weekday(self, text):
        """

        :param text:
        :return:
        """
        print(text)
        if text.__contains__("domingo"):
            return schedule.every().sunday.do(run_music())
        if text.__contains__("segunda"):
            return schedule.every().monday.do(run_music())
        if text.__contains__("terça"):
            return schedule.every().tuesday.do(run_music())
        if text.__contains__("quarta"):
            return schedule.every().wednesday.do(run_music())
        if text.__contains__("quinta"):
            return schedule.every().thursday.do(run_music())
        if text.__contains__("sexta"):
            return schedule.every().friday.do(run_music())
        if text.__contains__("sabádo"):
            return schedule.every().saturday.do(run_music())

    def handle_per_minute(self, text, string_time_validator):
        """
        Handler function to deal with the time in minutes
        :param text:
        :param string_time_validator:
        :return: None
        """
        string_minute = string_time_validator.string_minute_validator(text)
        if string_minute[1] == "minutos":  # this if clause redundant
            time_value = string_minute[0]
            try:
                self.sched_per_minute(time_value)
            except Exception:
                Exception("Não foi possível criar o alarme")

    def handle_per_hour(self, text, string_time_validator):
        """
        Handler Function to deal with the time in hours
        :param text:
        :param string_time_validator:
        :return: None
        """
        string_hour = string_time_validator.string_hour_validator(text)
        if string_hour[1] == "horas":  # this if clause redundant
            time_value = string_hour[0]
            try:
                self.sched_per_hour(time_value)
            except Exception:
                Exception("Não foi possível criar o alarme")

    def handle_per_second(self, text, string_time_validator):
        """
        Handler Function to deal with the time in seconds
        :param text:
        :param string_time_validator:
        :return:
        """
        print(f"text: {text}")
        string_second = string_time_validator.string_seconds_validator(text)
        print(f"string_second: {string_second}")
        if string_second[1] == "segundos":  # this if clause redundant
            time_value = string_second[0]
            print(time_value)
            try:
                self.sched_per_second(time_value)
            except Exception:
                Exception("Não foi possível criar o alarme")
