"""Module for Alarm functions"""
import schedule
from alarmsong import run_music
import time as timelib
from builtingalarmfunctions import stringtimevalidator as timevalidator
import pyttsx3


class Alarm:
    """
    CallableAlarm functions
    """

    def add_alarm(self, text):
        """

        :param text:
        :return:
        """
        engine = pyttsx3.init()
        string_time_validator = timevalidator.StringTimeValidator()
        if "minutos" in text:
            self.handle_per_minute(text, string_time_validator, engine)
        if "horas" in text:
            self.handle_per_hour(text, string_time_validator, engine)
        if "segundos" in text:
            self.handle_per_second(text, string_time_validator, engine)
        # if (text.__contains__("domingo") or text.__contains__("segunda") or
        #     text.__contains__("terça") or text.__contains__("quarta") or
        #     text.__contains__("quinta") or text.__contains__("sexta") or
        #     text.__contains__("sábado")):
        try:
            self.schedule_per_week_day(text)
            engine.say("Alarme semanal criado com sucesso")
        except Exception:
            Exception("Não foi possível criar o alarme semanal")

        while True:
            # Checks whether a scheduled task
            # is pending To run or not
            schedule.run_pending()
            timelib.sleep(1)

    def schedule_per_second(self, time):
        """

        :param time: time int for create the alarm
        :return: none
        """
        schedule.every(time).seconds.do(run_music())

    def schedule_per_minute(self, time):
        """

        :param time: time int for create the alarm
        :return: none
        """
        schedule.every(time).minutes.do(run_music())

    def schedule_per_hour(self, time):
        """

        :param time: time int for create the alarm
        :return: none
        """
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

    def handle_per_minute(self, text, string_time_validator, engine):
        """

        :param text:
        :param string_time_validator:
        :param engine:
        :return:
        """
        string_minute = string_time_validator.string_minute_validator(text)
        if string_minute[1] == "minutos":  # this if clause redundant
            time_value = string_minute[0]
            try:
                self.schedule_per_minute(time_value)
                engine.say("Alarme criado com sucesso")
            except Exception:
                Exception(engine.say("Não foi possível criar o alarme"))

    def handle_per_hour(self, text, string_time_validator, engine):
        """

        :param text:
        :param string_time_validator:
        :param engine:
        :return:
        """
        string_hour = string_time_validator.string_hour_validator(text)
        if string_hour[1] == "horas":  # this if clause redundant
            time_value = string_hour[0]
            try:
                self.schedule_per_hour(time_value)
                engine.say("Alarme criado com sucesso")
            except Exception:
                Exception(engine.say("Não foi possível criar o alarme"))

    def handle_per_second(self, text, string_time_validator, engine):
        """

        :param text:
        :param string_time_validator:
        :param engine:
        :return:
        """
        string_second = string_time_validator.string_seconds_validator(text)
        if string_second[1] == "horas":  # this if clause redundant
            time_value = string_second[0]
            try:
                self.schedule_per_hour(time_value)
                engine.say("Alarme criado com sucesso")
            except Exception:
                Exception(engine.say("Não foi possível criar o alarme"))
