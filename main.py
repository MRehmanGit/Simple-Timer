def format_time(hour, min, sec):
    """
    Formats the given hour, minute, and second into a string with leading zeros if necessary.
    
    :param hour: The hour to format (0-23).
    :param min: The minute to format (0-59).
    :param sec: The second to format (0-59).
    :return: A string representing the formatted time in "HH : MM : SS" format.
    """
    # Convert integer values to strings
    string_hour = str(hour)
    string_min = str(min)
    string_sec = str(sec)

    # Initialize final formatted time components
    final_hour = ""
    final_min = ""
    final_sec = ""

    # Add leading zero if hour is a single digit
    if len(string_hour) == 1:
        final_hour = str(0) + string_hour
    else:
        final_hour = string_hour

    # Add leading zero if minute is a single digit
    if len(string_min) == 1:
        final_min = str(0) + string_min
    else:
        final_min = string_min

    # Add leading zero if second is a single digit
    if len(string_sec) == 1:
        final_sec = str(0) + string_sec
    else:
        final_sec = string_sec

    # Return the formatted time string
    return f"{final_hour} : {final_min} : {final_sec}"


class Timer:
    """
    A class to model a timer that can increment and decrement time by one second.
    """

    def __init__(self, hours=0, minutes=0, seconds=0):
        """
        Initializes the Timer object with given hours, minutes, and seconds.

        :param hours: Initial hour value (0-23).
        :param minutes: Initial minute value (0-59).
        :param seconds: Initial second value (0-59).
        """
        self.__hours = hours
        self.__minutes = minutes
        self.__seconds = seconds

    def __str__(self):
        """
        Returns a string representation of the Timer object.

        A formatted string representing the current time.
        """
        return format_time(self.__hours, self.__minutes, self.__seconds)

    def next_second(self):
        """
        Increments the timer by one second.
        """
        self.__seconds += 1

        # Handle overflow for seconds
        if self.__seconds == 60:
            self.__seconds = 0
            self.__minutes += 1

            # Handle overflow for minutes
            if self.__minutes == 60:
                self.__minutes = 0
                self.__hours += 1

                # Handle overflow for hours
                if self.__hours == 24:
                    self.__hours = 0

    def prev_second(self):
        """
        Decrements the timer by one second.
        """
        self.__seconds -= 1

        # Handle underflow for seconds
        if self.__seconds == -1:
            self.__seconds = 59
            self.__minutes -= 1

            # Handle underflow for minutes
            if self.__minutes == -1:
                self.__minutes = 59
                self.__hours -= 1

                # Handle underflow for hours
                if self.__hours == -1:
                    self.__hours = 23


# Input validation for hours
hour_flag = True
while hour_flag:
    hour = int(input("Enter an hour between 0 - 23: "))
    if not 0 <= hour <= 23:
        print("Invalid Hour Input. Please Try Again!")
    else:
        hour_flag = False

# Input validation for minutes
min_flag = True
while min_flag:
    minutes = int(input("Enter minutes between 0 - 59: "))
    if not 0 <= minutes <= 59:
        print("Invalid Minutes Input. Please Try Again!")
    else:
        min_flag = False

# Input validation for seconds
second_flag = True
while second_flag:
    second = int(input("Enter seconds between 0 - 59: "))
    if not 0 <= second <= 59:
        print("Invalid Second Input. Please Try Again!")
    else:
        second_flag = False

# Create a Timer object with validated input
timer = Timer(hour, minutes, second)

# Main loop for user interaction
flag = True
while flag:
    # Display the current time
    print("THE TIME IS  ", timer)
    # Prompt the user for an action
    response = int(input("Enter 1 to increment the time by a second, 2 to decrement the time by a second, or -1 to EXIT: "))
    if response == 1:
        # Increment the time by one second
        timer.next_second()
    elif response == 2:
        # Decrement the time by one second
        timer.prev_second()
    elif response == -1:
        # Exit the loop
        flag = False
    else:
        # Handle invalid input
        print("Wrong input, please try again!")
