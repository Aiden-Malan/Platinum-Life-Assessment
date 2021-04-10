def formatNumber(mobile_number):
    """returns a formatted mobile phone number according to the following
       logic and returns it:
                1. remove non-digits
                2. prepend '0' if it does not start with '0'
                3. raise an exception if the length is incorrect

    Keyword arguments:
    mobile_number -- the mobile number to format
    """

    mobile_number = ''.join(c for c in mobile_number if c.isdigit())
    if (mobile_number[0] != '0'):
        mobile_number = '0' + mobile_number
    if (len(mobile_number) != 10):
        raise Exception('Mobile number is of the wrong length')
    return mobile_number


print(formatNumber("0815423235"))
print(formatNumber("815423235"))
print(formatNumber("+815423235"))
print(formatNumber("081-542-3235"))
print(formatNumber("+27815423235"))
