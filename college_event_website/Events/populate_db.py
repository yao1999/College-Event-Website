import urllib.request, json
import re, html
from Events.models import Event
from Events.models import Locations

def populate_events():
    # get the events in the db
    events = Event.objects.all()

    # if the db for events is empty, populate it with some UCF events
    if not events:
        # open UCF json events feed
        with urllib.request.urlopen("https://events.ucf.edu/feed.json") as url:
            events_feed = json.loads(url.read().decode())
            

            # fill out each event using the feed and save to database
            for event in events_feed:
                # split up the start/end times
                start_date_time = event['starts'].split(" ")
                end_date_time = event['ends'].split(" ")

                # fix the event description
                description = re.sub("<[^<]+?>", "", event['description'])
                description = html.unescape(description)
                print(description)

                # assign as ucf location with name from feed, since not all events have locations
                latitude = 28.6024
                longitude = -81.2001
                event_location = Locations(
                    location_name = event['location'],
                    latitude = latitude,
                    longitude = longitude
                )
                event_location.save()

                # create and add event to the db
                new_event = Event(
                    name = event['title'],
                    category = event['category'],
                    description = description,
                    date = get_date(start_date_time),
                    start_time = start_date_time[4],
                    end_time = end_date_time[4],
                    location = event_location,
                    phone = event['contact_phone'],
                    email = event['contact_email'],
                    is_public = True,
                    is_private = False,
                    is_RSO = False,
                    is_approved = True,
                    university = None,
                    rso = None,
                    admin = None,
                )
                new_event.save()

def get_date(date_time):
    date = date_time[1]
    month = date_time[2]
    year = date_time[3]

    # if date not 2 digits, adjust
    if len(date) < 2:
        date = "0" + date
    
    # adjust the month to be 2 digits
    if month == "Jan":
        month = "01"
    elif month == "Feb":
        month = "02"
    elif month == "Mar":
        month = "03"
    elif month == "Apr":
        month = "04"
    elif month == "May":
        month = "05"
    elif month == "Jun":
        month = "06"
    elif month == "Jul":
        month = "07"
    elif month == "Aug":
        month = "08"
    elif month == "Sep":
        month = "09"
    elif month == "Oct":
        month = "10"
    elif month == "Nov":
        month = "11"
    elif month == "Dec":
        month = "12"
    
    return year + "-" + month + "-" + date