import datetime

def check_coupon(entered_code, correct_code, current_date, expiration_date):

    if entered_code is correct_code and datetime.datetime.strptime(current_date, '%B %d, %Y') <= datetime.datetime.strptime(expiration_date, '%B %d, %Y'):
        return True
    return False








print(check_coupon('123','123','September 5, 2014','October 1, 2014'))
print(check_coupon('123a','123','September 5, 2014','October 1, 2014'))