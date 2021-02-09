# job_source_resolver

A. Instructions to run the code
First git clone this repo.
You need Python 3 and pip 3, so install them if you don't yet have them.
Then you can run `pipenv install` to install django
run `cd job_source_resolver/job_source_resolver ; python manage.py migrate && python manage.py runserver`
In a browser go to http://127.0.0.1:8000/ and have fun!
Also run `python manage.py test` to run the unit tests

B. 3rd party stuff 
I pretty much just used what is available in default Django.

C. Explanation
The program reads through the data sets (in the /resolver/resources directory, btw) and resolves the job_source of the jobs on server startup. This is why I chose to put the code in resolver/apps.py (ResolverConfig class). Although, the first loading of the page is slow because of the bulk_create django does. I didn't have time to use a faster database than the default SQLite3, but I know if I could connect the app to MySQL or PostgreSQL it would be quicker.

D. Link to Part 2
(After the instructions in A)
In a browser go to http://127.0.0.1:8000/ for Page 1
For Page 2 go to http://127.0.0.1:8000/jobsource=Google. You can replace Google with any other job company in the jobSources.json

E. The file is job_source_resolver/job_source_resolver/complete_job_source_resolution_data.csv

F. Job board -> number of listings
Dribble -> 0
Wayup -> 0
YCombinator Jobs -> 0
Work At A Startup -> 0
Jopwell -> 0
Tech Ladies -> 0
Intern Supply -> 0
Underdog -> 0
Stella -> 0
SimplyHired -> 0
Gamasutra -> 0
Huntr Jobs -> 0
Github -> 0
Employbl -> 0
Who Is Hiring? -> 0
Government Jobs -> 0

Google -> 160
Glassdoor -> 298
AngelList -> 120
LinkedIn -> 6606
Indeed -> 898
Hired -> 27
Triplebyte -> 13
ZipRecruiter -> 66
Lever -> 2670
Monster -> 4
Stackoverflow -> 2
Jobvite -> 382
SmartRecruiters -> 69