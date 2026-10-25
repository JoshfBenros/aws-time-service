# Goal of app.py:
# 1. Get current UTC time
# 2. Convert UTC time to America/New_York
# 3. Display both values

from datetime import datetime, timezone
from zoneinfo import ZoneInfo
# import Flask 
from flask import Flask, render_template

# creat Flask app
app = Flask(__name__)

# route
@app.route("/")
def home():
    # datetime = the class
    #.now(...) = asks the current datetime 
    #timezone.utc = tells python which timezone I want 
    # = class.method(argument) 

    # gets the UTC time 
    utc = datetime.now(timezone.utc)
    #format UTC datetime into time, and timezone to display 
    utcTime = utc.strftime("%I:%M:%S %p")
    utcDate = utc.strftime("%B %d, %Y")
    utcZone = utc.strftime("%Z")

    # defines the local timezone used for conversion
    timeZone = ZoneInfo("America/New_York")
    # converts UTC time to the selected local timezone
    localTime = utc.astimezone(timeZone)
    # format local datetime info into time, date, and timezone for display
    localTimeFormatted = localTime.strftime("%I:%M:%S %p")
    localDate = localTime.strftime("%B %d, %Y")
    localZone = localTime.strftime("%Z")

    
    return render_template(
        # renders index.html and passes formatted time values to the template
        "index.html",
        utcTime = utcTime,
        utcDate = utcDate,
        utcZone = utcZone,
        localTime = localTimeFormatted,
        localDate = localDate,
        localZone = localZone
    )

if __name__ == "__main__":
    app.run(debug=True)