class StringTimeValidator:
    """

    """

    def string_minute_validator(self, text):
        """
        :param text: phrase passed throught voice recognition
        :return: Return a new time formatted string in minutes
        """
        word_not_alpha= ""
        word_minutes= ""
        position_not_alpha = 0
        position_alpha = 0
        new_word = ""
        if "minutos" in text:

            word_minutes = "minutos"

            wordSpllitted = text.split()

            for word in wordSpllitted:
                position_alpha = wordSpllitted.index("minutos")
                print(position_alpha)

                print(f"{word} and is alpha? {word.isalpha()}")

                if not word.isalpha():
                    word_not_alpha = word
                    position_not_alpha = wordSpllitted.index(word_not_alpha)
                    print(f"position_not_alpha {position_not_alpha}")
                    print(f"word_not_alpha {word_not_alpha}")

                    if position_alpha - position_not_alpha == 1:
                        new_word = tuple((word_not_alpha, word_minutes))
                        print(new_word)
                        break #break or continue
        return new_word


    def string_hour_validator(self, text):
        """
        :param text: phrase passed throught voice recognition
        :return: Return a new time formatted string in hours
        """
        word_not_alpha= ""
        word_hours= ""
        position_not_alpha = 0
        position_alpha = 0
        if "horas" in text:

            word_hours = "horas"

            wordSpllitted = text.split()

            for word in wordSpllitted:
                position_alpha = wordSpllitted.index("horas")
                print(position_alpha)

                print(f"{word} and is alpha? {word.isalpha()}")

                if not word.isalpha():
                    word_not_alpha = word
                    position_not_alpha = wordSpllitted.index(word_not_alpha)
                    print(f"position_not_alpha {position_not_alpha}")
                    print(f"word_not_alpha {word_not_alpha}")

                    if position_alpha - position_not_alpha == 1:
                        new_word = tuple((word_not_alpha, word_hours))
                        print(new_word)
                        break #break or continue
        return new_word

    def string_seconds_validator(self, text):
        """
        :param text: phrase passed throught voice recognition
        :return: Return a new time formatted string in seconds
        """
        word_not_alpha= ""
        word_seconds= ""
        position_not_alpha = 0
        position_alpha = 0
        if "horas" in text:

            word_seconds = "segundos"

            wordSpllitted = text.split()

            for word in wordSpllitted:
                position_alpha = wordSpllitted.index("segundos")
                print(position_alpha)

                print(f"{word} and is alpha? {word.isalpha()}")

                if not word.isalpha():
                    word_not_alpha = word
                    position_not_alpha = wordSpllitted.index(word_not_alpha)
                    print(f"position_not_alpha {position_not_alpha}")
                    print(f"word_not_alpha {word_not_alpha}")

                    if position_alpha - position_not_alpha == 1:
                        new_word = tuple((word_not_alpha, word_seconds))
                        print(new_word)
                        break #break or continue
        return new_word
