class Reminders:  # This is the reminder class
    def __init__ (self):  # this is the constructor intializer when the class object is created
        print("Reminders Class Created !")

    def reminders_access (self, date=''):  # if you want to specify the specific address
        """

        :param date:
        """
        print(date)

    def reminder_write(self, data):
        data = str(data) # converting the data into the string form.
        write_file = open("Reminder_way/reminder_store.txt", "w")  # this is the writing to the file specified !@
        write_file.write(data) # this writes the data to the specified file
        write_file.close()  # closing the self file so there is no need for the writing of the File in th

    def check_reminder(self):
        data_read = open("Reminder_way/reminder_store.txt").readlines()
        for line in data_read:
            pass  # here you need to check the reminders for the specified Checks.!