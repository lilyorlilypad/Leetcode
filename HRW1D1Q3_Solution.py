def timeConversion(s):
    # Write your code here
    if s[8:]=="PM":
        if s[0:2]=="12":
            return s[0:8]
        else:
            return str(int(s[0:2])+12) + s[2:8]
    else:
        if s[0:2]=="12":
            return "00" + s[2:8]
        else:
            return s[0:8]