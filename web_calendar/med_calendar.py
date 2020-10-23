from flask import Flask
import boto3
from datetime import datetime
import json


now = datetime.now()
dates_meds_taken = {}
html_events = "events: ["


def month_to_number(month):
    if month.upper() == "JAN":
        return "01"
    if month.upper() == "FEB":
        return "02"
    if month.upper() == "MAR":
        return "03"
    if month.upper() == "APR":
        return "04"
    if month.upper() == "MAY":
        return "05"
    if month.upper() == "JUN":
        return "06"
    if month.upper() == "JUL":
        return "07"
    if month.upper() == "AUG":
        return "08"
    if month.upper() == "SEP":
        return "09"
    if month.upper() == "OCT":
        return "10"
    if month.upper() == "NOV":
        return "11"
    if month.upper() == "DEC":
        return "12"


def med_not_taken_warnings(dates_meds_taken):
    global html_events
    for i in range(1, now.day+1):
        check_date = "{0}-{1}-{2:02d}".format(now.year, now.month, i)
        if check_date not in dates_meds_taken:
            # Color day red (to indicate med not taken).
            html_events += """{{
                overlap: false,
                display: 'background',
                color: '#ff9f89',
                start: '{0}',
                end: '{0}'
            }},""".format(check_date)

            html_events += """{{
                title: 'Missed dose - Amlodipine',
                start: '{}'
            }},""".format(check_date)


app = Flask(__name__)
# Get page templates.
html_top = open('calendar_top.html', 'r').read()
html_bottom = open('calendar_bottom.html', 'r').read()

# Set current date in calendar.
startDate = "initialDate: '{}',".format(now.strftime("%Y-%m-%d"))

# Connect to DB; specify table.
dynamodb = boto3.resource('dynamodb', region_name='us-east-2')
table = dynamodb.Table('memory_pill')

# Get data from memory_pill AWS table.
response = table.scan()
items = response.get('Items', [])

for item in items:
    j = str(item).replace("'", "\"")
    j = json.loads(j)
    time_split = j["Time"].split(" ") # Tue Oct 20 12:32:35 2020

    # Show time med taken.
    html_events += """{{
        title: 'Amlodipine',
        start: '{0}-{1}-{2}T{3}'
    }},""".format(time_split[4], month_to_number(time_split[1]), time_split[2], time_split[3])

    # Color day green (to indicate med taken).
    html_events += """{{
        overlap: false,
        display: 'background',
        color: '#89FF89',
        start: '{0}-{1}-{2}',
        end: '{0}-{1}-{2}'
    }},""".format(time_split[4], month_to_number(time_split[1]), time_split[2], time_split[3])

    date = "{0}-{1}-{2}".format(time_split[4], month_to_number(time_split[1]), time_split[2])
    dates_meds_taken[date] = True

med_not_taken_warnings(dates_meds_taken)

html_events += "]});"

@app.route("/")
def home():
	return html_top + startDate + html_events + html_bottom


###
# Start server.
###

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
