# cs348-project

### Indexes
There are two indexes:
An index on datetime in the Exam table
- this index is chosen because a major report query relies on datetime for filtering. The first report option utilizes datetime as a range to search by. Considering the ranges of dates that exams could take, indexes would help boost the speed as people would frequently filter the list of exams into their designated day for exams.
- The specific query is: "SELECT Exam.id, Exam.datetime, Exam.duration, Exam.description, Professors.name, Classes.course_code, Room.building, Room.number, Exam.offered, Exam.taking FROM Exam JOIN Classes ON Exam.class_id = Classes.id JOIN Professors ON Exam.professor_id=Professors.id JOIN Room ON Exam.room_id = Room.id WHERE Exam.datetime >= :start_date AND Exam.datetime <= :end_date"

An index on course_code in the Classes table
- this index is chosen because it is used heavily in the reports. One of the major filtering options is by course_code (the second option). This query would benefit from indexing on course_code. Also, the populating of the dropdown in the reports in done exclusively based on a query on course_code. Considering this runs every time the report page is opened, the frequency would be high enough to warrant an index.
- Specific queries are: "SELECT Exam.id, Exam.datetime, Exam.duration, Exam.description, Professors.name, Classes.course_code, Room.building, Room.number, Exam.offered, Exam.taking FROM Exam JOIN Classes ON Exam.class_id = Classes.id JOIN Professors ON Exam.professor_id=Professors.id JOIN Room ON Exam.room_id = Room.id WHERE Classes.course_code = :course" and "SELECT course_code FROM Classes"

### Concurrency
Individual Transactions are mainly concerned around the increasing of accepting to take exams. Mishaps in data could cause improper numbers to be able to sign up for exams. Due to this reason I chose to add a Serializable isolation level. This would make sure there is consistent data and each person cannot alter the count at the same time. This may slow things down, but considering the site is not used for something in which speed is much of a concern, I believe its a valid tradeoff.

### Lessons Learned
In this project I learned many things. Most of this came from the fact that I have never used databases all that much besides writing the queries for the homeworks. Actually setting up the databases was something I never learned how to do. Also I never knew how to host servers through python. I had learned a lot about Flask, as that is what I used for backend. SQLAlchemy (with respect to SQLite) was also something I learned as that is how I created and accessed the databases. I also learned some other front end technologies. I have used bootstrap in the past, but jinja became a big part of how I used my html files. Also, I had never really considered how html could work with variables provided into it. This also taught me a bit about the python library wtforms as that is the main way I structured all the inputs and submits on the front end.

As for just general things that I learned over the course of this project, I had to learn all of these things on my own. I had only ever used IDEs before for most of my coding in python and html, but I had only ever hosted a server through the linux terminal. Because of this, I decided to work through linux but had no clue how to on my personal laptop. I researched and found out about Ubuntu where I then developed my project. Because I developed in Ubuntu, I had to relearn git so then I could move my files to this repository directly, as I was struggling to transfer the files to my windows directories. Overall, The process through this project taught me how I could learn new technologies on my own. Although I may not have been very efficient in my learning, and the learning being very frustrating in itself considering I had no clue what to do, I was able to gain new knowledge on everything related to this project that allowed me to complete it. I had never used anything before that I used here, so it was almost all completely new. I learned how to search the internet better and use resources to aid not just in general learning of the topics, but also help in figuring out specific issues I was having. I also learned many different technologies that were new to me. I had also learned about the implementation of many different concepts from class that I did not know how to use before.

## Notes
Please ignore files: user.html, add_user.html, name.html
These were just used for testing
