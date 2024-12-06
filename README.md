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
