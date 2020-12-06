# Time in seconds conversion to H:M:S format

def convert(seconds):
    seconds = seconds % (24 * 3600)
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60

    return "%d:%02d:%02d" % (hour, minutes, seconds)


print("Input time in seconds:")
sec = input()
secTime = int(sec)
newTime = convert(secTime)
print(newTime)
