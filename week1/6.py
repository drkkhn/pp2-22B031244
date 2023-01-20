age = int(input())
fee = int(input())
isConsent = input()

if isConsent == 'true':
    isConsent = True
else:
    isConsent = False

if ((age in [11, 12] and fee >= 900 and isConsent) or (age in [13, 14, 15, 16] and fee >= 900) or (age in [17, 18, 19, 20, 21, 22] and fee >= 1400) or (age > 22 and fee >= 1900)):
    print("Allowed")
else:
    print("Not Allowed")


