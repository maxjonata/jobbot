# General bot settings

# browser you want the bot to run ex: ["Firefox"], ["Chrome"] choose one only
browser = ["Firefox"]
# Optional! run browser in headless mode, no browser screen will be shown it will work in background.
headless = True
# Optional! for Firefox enter profile dir to run the bot without logging in your account each time
firefoxProfileRootDir = r""
# If you left above field empty enter your Linkedin password and username below
# Linkedin credits
email = ""
password = ""

# location you want to search the jobs - ex : ["Poland", "Singapore", "New York City Metropolitan Area", "Monroe County"]
# continent locations:["Europe", "Asia", "Australia", "NorthAmerica", "SouthAmerica", "Africa", "Australia"]
location = ["European Economic Area"]
# keywords related with your job search
keywords = ["lead developer", "chief technical officer", "cto", "python"]
# keywords = ["programming"]
#job experience Level - ex:  ["Internship", "Entry level" , "Associate" , "Mid-Senior level" , "Director" , "Executive"]
experienceLevels = ["Mid-Senior level" , "Director" , "Executive"]
#job posted date - ex: ["Any Time", "Past Month" , "Past Week" , "Past 24 hours"] - select only one
datePosted = ["Past 24 hours"]
# datePosted = ["Past 24 hours"]
#job type - ex:  ["Full-time", "Part-time" , "Contract" , "Temporary", "Volunteer", "Intership", "Other"]
jobType = ["Full-time", "Part-time" , "Contract"]
#remote  - ex: ["On-site" , "Remote" , "Hybrid"]
remote = ["On-site" , "Remote" , "Hybrid"]
#salary - ex:["$40,000+", "$60,000+", "$80,000+", "$100,000+", "$120,000+", "$140,000+", "$160,000+", "$180,000+", "$200,000+" ] - select only one
salary = [""]
#sort - ex:["Recent"] or ["Relevent"] - select only one
sort = ["Recent"]
#Blacklist companies you dont want to apply - ex: ["Apple","Google"]
blacklist = ["EPAM Anywhere"]
#Blaclist keywords in title - ex:["manager", ".Net"]
blackListTitles = [""]
#Only Apply these companies -  ex: ["Apple","Google"] -  leave empty for all companies 
onlyApply = [""]
#Only Apply titles having these keywords -  ex:["web", "remote"] - leave empty for all companies 
onlyApplyTitles = [""] 
#Follow companies after sucessfull application True - yes, False - no
followCompanies = False
# your country code for the phone number - ex: fr
country_code = "fr"
# Your phone number without identifier - ex: 123456789
phone_number = ""
# Your complete phone number with identifier - ex: +3312345678901
phone_number_with_identifier = ""


FirstName = "Name"
LastName = "Lastname"
Email = "*@*.com"
LinkedInProfileURL = "https://www.linkedin.com/in/***/"
Phone = "" #OPTIONAL
Location = "" #OPTIONAL
HowDidYouHeard = "" #OPTIONAL
ConsiderMeForFutureOffers = True #true = yes, false = no
Salary = "" #OPTIONAL
specificCitySelectOption = "" #OPTIONAL
aptidoes = "" #NEEDED IF USING createAnswers.py