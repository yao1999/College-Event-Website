
# Design Needs

## User Groups
### Students
* Must be able to view events 
	* Events can be public, university only, and RSO only
	* Events in the same location as the student should be viewable
* Must be able to join an RSO
* Has:
	* University email
		* Used to help sort by university
		* If has email, can see private university events
	* RSO (if in one)
	* Name
	* Location
* Can add, remove, edit comments on event and rate out of 5 stars

### Admin
* Must be able to create events
* Must be able to set event status (public, private, etc)
* In general, is also a student
* Has:
	* RSO involvement
	* Student

### SuperAdmin
* Must be able to make a university
* Does not need to be connected w/ student



## Events, RSO, and Uni
### Events
* Created by Admin
* Has status
	* Public: all
	* Private: University emails can see
	* RSO: Only students in RSO can see
* Has:
	* Name
	* Status
	* Event Category
	* Description
	* Time
	* Date
	* Location (google maps)
	* Phone #
	* Email
* Can add, remove, edit comments on event and rate out of 5 stars
* Can post to facebook or twitter

### University
* Created by SuperAdmin
* Has:
	* Name
	* Location (google maps)
	* Description
	* Number of students
	* Pictures

## Frontend
### Navbar
* signin / signup buttons
* nav to search page or user page
* If admin, nav to ADD EVENT
* If superadmin, nav to ADD COLLEGE
### Welcome page
* Search feature for public
* Slideshow of events
* Login/sign up buttons
### Login page or popup
* user: email
* password
* signup button
* forgot password button
* terms of use button
### Signup popup
* register portion:
	* add email (if university, adds capabilities to view that uni)
	* add password
	* add name
* inspirational portion:
	* image of college
	* text: START YOUR ADVENTURE
	* descriptive text
### Search Page
* Go to this after signin
* Has a search bar + options
* Below search bar, shows public events in user's area
* Left of search bar, shows date + event title list for quick access
	* Can popup event
### Regular User Page
* Can change name or email
* Can signup / leave RSO

### ADD EVENT
* Page to add events for admins
* Can add name, status, category, description, date, time, location, phone #, and email


### ADD or MANAGE COLLEGE
* Page to add/manage college for superadmins
* Can add/modify name, location, description, photos, # students
