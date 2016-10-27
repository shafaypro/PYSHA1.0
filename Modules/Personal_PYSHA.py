import datetime

def Personal_PYSHA(text_input=""):
    text_input = text_input.strip()  # striping the extra white spaces.
    if text_input == "name":
        #Text_to_speech("PYSHA")
        print("")
    elif text_input == "age":
        date_of_birth=datetime.datetime.strptime("Oct 24 2016",'%b %d %Y')
        current_date = datetime.date.today()
        dob = current_date - date_of_birth

        print(current_date)
        current_date = datetime.datetime.now()  # getting the current date from the OS
        # now subtract the date from the date of creation

def days_between(d1, d2):
    d1 = datetime.datetime.strptime(d1, "%Y-%m-%d")
    d2 = datetime.datetime.strptime(d2, "%Y-%m-%d")
    return abs((d2 - d1).days)

if __name__ == '__main__':
    #Personal_PYSHA("age")
#    print(datetime.datetime.strftime('2016-10-25','%Y-%m-%d'))
    b_date = datetime.date(2016,10,24)
    c_date = datetime.date.today()

    print(c_date -b_date)