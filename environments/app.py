from flask import Flask, render_template, flash, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, DateTimeField, SelectField
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import *#create_engine, text
from datetime import datetime

app = Flask(__name__)

app.config['SECRET_KEY'] = "scrt"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'

db = SQLAlchemy(app)

engine = create_engine("sqlite:///mydatabase.db", echo = True, isolation_level="SERIALIZABLE")

meta=MetaData()

#examstable=Table('Exam', meta, Column('id', Integer, primary_key=True, autoincrement=True), Column('datetime', DateTime), Column('date', String), Column('time', String), Column('duration', Integer), Column('description', String), Column('professor_id', Integer), Column('class_id', Integer), Column('room_id', Integer), Column('offered', Integer), Column('taking', Integer))
examstable1=Table('Exam', meta, Column('id', Integer, primary_key=True, autoincrement=True), Column('datetime', DateTime, index=True), Column('duration', Integer), Column('description', String), Column('professor_id', Integer), Column('class_id', Integer), Column('room_id', Integer), Column('offered', Integer), Column('taking', Integer))
professors = Table('Professors', meta, Column('id', Integer, primary_key = True, autoincrement=True),
                    Column('name', String), Column('email', String))
room=Table('Room', meta, Column('id', Integer, primary_key=True, autoincrement=True), Column('building', String), Column('number', Integer), Column('capacity', Integer))

classes=Table('Classes', meta, Column('id', Integer, primary_key=True, autoincrement=True), Column('course_code', String, index=True), Column('department_id', Integer))

meta.create_all(engine)
#examstable1.drop(engine)
#professors.drop(engine)
#room.drop(engine)
#classes.drop(engine)
#class Students(db.Model):
#    id = db.Column(db.Integer, primary_key=True)
#    name = db.Column(db.String(200), nullable=False)
#    email = db.Column(db.String(120), nullable=False, unique=True)
#    date_added = db.Column(db.DateTime, default=datetime.utcnow)
#
#    def __repr__(self):
#        return '<Name %r>' % self.name

class Professors(db.Model):
    __tablename__ = "Professors"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)
    #date_added = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Name %r>' % self.name

class Room(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    building = db.Column(db.String(200), nullable=False)
    number = db.Column(db.Integer)
    capacity = db.Column(db.Integer)

class Classes(db.Model):
    __tablename__ = "Classes"

    id = db.Column(db.Integer, primary_key=True)
    course_code = db.Column(db.String(100))
    department_id = db.Column(db.Integer)

class Department(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)

class Exam(db.Model):
    __tablename__ = "Exam"
    
    id = db.Column(db.Integer, primary_key=True)
    datetime = db.Column(db.DateTime)
    #date = db.Column(db.String(100))
    #time = db.Column(db.String(100))
    duration = db.Column(db.Integer)
    description = db.Column(db.String(200))
    professor_id = db.Column(db.Integer)
    class_id = db.Column(db.Integer)
    room_id = db.Column(db.Integer)
    offered = db.Column(db.Integer)
    taking = db.Column(db.Integer, default= 0)

with app.app_context():
    #db.drop_all()
    #Exam.__table__.drop(db.engine)
    db.create_all()

#class NamerForm(FlaskForm):
#    name = StringField("What's Your Name", validators=[DataRequired()])
#    submit = SubmitField()

#class StudentForm(FlaskForm):
#    name = StringField("Name", validators=[DataRequired()])
#    email = StringField("Email", validators=[DataRequired()])
#    submit = SubmitField()
 
class ProfessorForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired()])
    submit = SubmitField()
class ProfessorDeleteForm(FlaskForm):
    id_prof = IntegerField("ID", validators=[DataRequired()])
    submit = SubmitField()

class ClassForm(FlaskForm):
    course_codes = StringField("Course Code", validators=[DataRequired()])
    dep_id = IntegerField("Department ID", validators=[DataRequired()])
    submit = SubmitField()
class ClassDeleteForm(FlaskForm):
    id_class = IntegerField("ID", validators=[DataRequired()])
    submit = SubmitField()

class RoomForm(FlaskForm):
    number = StringField("Room Number", validators=[DataRequired()])
    building = StringField("Building", validators=[DataRequired()])
    capacity = IntegerField("Capacity", validators=[DataRequired()])
    submit = SubmitField()
class RoomDeleteForm(FlaskForm):
    id_room = IntegerField("ID", validators=[DataRequired()])
    submit = SubmitField()

class ExamForm(FlaskForm):
    datetime = DateTimeField("Date & Time", format='%Y-%m-%d %H:%M' , validators=[DataRequired()])
    #date = StringField("Date", validators=[DataRequired()])
    #time = StringField("Time", validators=[DataRequired()])
    duration = IntegerField("Duration", validators=[DataRequired()])
    description = StringField("Description", validators=[DataRequired()])
    professor_id = IntegerField("Professor ID", validators=[DataRequired()])
    class_id = IntegerField("Class ID", validators=[DataRequired()])
    room_id = IntegerField("Room ID", validators=[DataRequired()])
    offered = IntegerField("How Many Students Can Take", validators=[DataRequired()])
    submit = SubmitField()

class DeleteForm(FlaskForm):
    exam_id = IntegerField("Exam ID", validators=[DataRequired()])
    submit = SubmitField()

class StudentUpdateForm(FlaskForm):
    exam_id = IntegerField("Exam ID", validators=[DataRequired()])
    submit = SubmitField()
class StudentUpdateForm2(FlaskForm):
    #with engine.connect() as connection:
    #    exams = connection.execute(text("SELECT id FROM Exam"))
    exam_id = SelectField("Exam ID", choices=[], validators=[DataRequired()])
    submit = SubmitField()
class TimeFrameForm(FlaskForm):
    time1 = DateTimeField("Start Date", format='%Y-%m-%d %H:%M', validators=[DataRequired()])
    time2 = DateTimeField("End Date  ", format='%Y-%m-%d %H:%M', validators=[DataRequired()])
    submit = SubmitField()
class ClassFindForm(FlaskForm):
    classes = SelectField("Class", choices=[], validators=[DataRequired()])
    submit = SubmitField()

@app.route('/')
def index():
    return render_template('index.html')


#@app.route('/user/<name>')
#def user(name):
#    words = ['taco', 'pasta', 'meatballs', 'chicken']
#    return render_template('user.html', name=name, words=words)

#@app.route('/name', methods=['GET', 'POST'])
#def name():
#    name = None
#    form = NamerForm()
#    if form.validate_on_submit():
#        name = form.name.data
#        form.name.data = ''
#
#    return render_template("name.html", name=name, form=form)

#@app.route('/student/add', methods=['GET', 'POST'])
#def add_student():
#    name = None
#    form = StudentForm()
#    if form.validate_on_submit():
#        student = Students.query.filter_by(email=form.email.data).first()
#        if student is None:
#            student = Students(name=form.name.data, email=form.email.data)
#            db.session.add(student)
#            db.session.commit()
#        name = form.name.data
#        form.name.data = ''
#        form.email.data = ''
#    our_users = Students.query.order_by(Students.date_added)
#    return render_template("add_user.html", form=form, name=name, our_users=our_users)

@app.route('/professor/add', methods=['GET', 'POST'])
def add_professor():
    name = None
    form = ProfessorForm()
    form2 = ProfessorDeleteForm()
    if form.validate_on_submit():
        prof = Professors.query.filter_by(email=form.email.data).first()
        #if prof is None:
        prof = Professors(name=form.name.data, email=form.email.data)
        db.session.add(prof)
        #db.session.commit()
        stmt = insert(Professors).values(name=form.name.data, email=form.email.data)
        with engine.connect() as conn:
            result = conn.execute(stmt)
            conn.commit()
        db.session.commit()
        #name = form.name.data
        form.name.data = ''
        form.email.data = ''
    if form2.validate_on_submit():
        db.session.query(Professors).filter(Professors.id == form2.id_prof.data).delete()
        db.session.commit()
        stmt1 = delete(Professors).where(Professors.id == form2.id_prof.data)
        with engine.connect() as conn:
            result = conn.execute(stmt1)
            conn.commit()
        form2.id_prof.data = 0
    #profs = Professors.query.order_by(Professors.name)
    with engine.connect() as conn:
        profs = conn.execute(text("SELECT * FROM Professors"))
        #connection.commit()
        conn.commit()
    return render_template("add_prof.html", form=form, form2=form2, name=name, our_profs=profs)

@app.route('/class/add', methods=['GET', 'POST'])
def add_class():
    name = None
    form = ClassForm()
    form2 = ClassDeleteForm()
    if form.validate_on_submit():
        #prof = Class.query.filter_by(email=form.email.data).first()
        #if prof is None:
        clas = Classes(course_code=form.course_codes.data, department_id=form.dep_id.data)
        db.session.add(clas)
        #db.session.commit()
        stmt = insert(Classes).values(course_code=form.course_codes.data, department_id=form.dep_id.data)
        with engine.connect() as conn:
            result = conn.execute(stmt)
            conn.commit()
        db.session.commit()
        #name = form.name.data
        form.course_codes.data = ''
        form.dep_id.data = ''
    if form2.validate_on_submit():
        db.session.query(Classes).filter(Classes.id == form2.id_class.data).delete()
        db.session.commit()
        stmt2 = delete(Classes).where(Classes.id == form2.id_class.data)
        with engine.connect() as conn:
            result = conn.execute(stmt2)
            conn.commit()
        form2.id_class.data = 0
    #profs = Professors.query.order_by(Professors.name)
    with engine.connect() as conn:
        classes = conn.execute(text("SELECT * FROM Classes"))
        conn.commit()
        #connection.commit()
    return render_template("add_class.html", form=form, form2=form2, name=name, our_classes=classes)

@app.route('/room/add', methods=['GET', 'POST'])
def add_room():
    name = None
    form = RoomForm()
    form2 = RoomDeleteForm()
    if form.validate_on_submit():
        #prof = Class.query.filter_by(email=form.email.data).first()
        #if prof is None:
        room = Room(building=form.building.data, number=form.number.data, capacity=form.capacity.data)
        db.session.add(room)
        db.session.commit()
        stmt = insert(Room).values(building=form.building.data, number=form.number.data, capacity=form.capacity.data)
        with engine.connect() as conn:
            result = conn.execute(stmt)
            conn.commit()
        db.session.commit()
        #name = form.name.data
        form.building.data = ''
        form.number.data = ''
        form.capacity.data = ''
    if form2.validate_on_submit():
        db.session.query(Room).filter(Room.id == form2.id_room.data).delete()
        db.session.commit()
        stmt2 = delete(Room).where(Room.id == form2.id_room.data)
        with engine.connect() as conn:
            result = conn.execute(stmt2)
        form2.id_room.data = 0
    #profs = Professors.query.order_by(Professors.name)
    with engine.connect() as conn:
        rooms = conn.execute(text("SELECT * FROM Room"))
        conn.commit()
    return render_template("add_room.html", form=form, form2=form2, name=name, our_rooms=rooms)

@app.route('/exam/add', methods=['GET', 'POST'])
def add_exam():
    form = ExamForm()
    form3 = DeleteForm()
    if form.validate_on_submit():
       # exam = Exam(date=form.date.data, time=form.time.data, duration=form.duration.data, description=form.description.data, professor_id=form.professor_id.data, class_id=form.class_id.data, room_id=form.room_id.data, offered=form.offered.data)
       # stmt = insert(Exam).values(date=form.date.data, time=form.time.data, duration=form.duration.data, description=form.description.data, professor_id=form.professor_id.data, class_id=form.class_id.data, room_id=form.room_id.data, offered=form.offered.data)
        exam = Exam(datetime=form.datetime.data, duration=form.duration.data, description=form.description.data, professor_id=form.professor_id.data, class_id=form.class_id.data, room_id=form.room_id.data, offered=form.offered.data)
        stmt = insert(Exam).values(datetime=form.datetime.data, duration=form.duration.data, description=form.description.data, professor_id=form.professor_id.data, class_id=form.class_id.data, room_id=form.room_id.data, offered=form.offered.data)
        with engine.connect() as conn:
            result = conn.execute(stmt)
            conn.commit()
        db.session.add(exam)
        db.session.commit()
        #form.date.data = ''
        #form.time.data = ''
        form.datetime.date = ''
        form.duration.data = 0
        form.description.data = 0
        form.professor_id.data = 0
        form.class_id.data = 0
        form.room_id.data = 0
        form.offered.data = 0
    if form3.validate_on_submit():
        db.session.query(Exam).filter(Exam.id == form3.exam_id.data).delete()
        db.session.commit()
        stmt1 = delete(Exam).where(Exam.id == form3.exam_id.data)
        with engine.connect() as conn:
            result = conn.execute(stmt1)
            conn.commit()
        form3.exam_id.data = 0
    #our_users = Students.query.order_by(Students.date_added)
    return render_template("add_exam.html", form=form, form3=form3)

@app.route('/report', methods=["GET", "POST"])
def report():
    timeform = TimeFrameForm()
    classform = ClassFindForm()
    with engine.connect() as connection:
        rooms = connection.execute(text("SELECT * FROM Room"))
        classes = connection.execute((text("SELECT course_code FROM Classes")))
        classform.classes.choices = [c.course_code for c in classes]
        if timeform.validate_on_submit():
            stmt = text("""SELECT Exam.id, Exam.datetime, Exam.duration, Exam.description, Professors.name, Classes.course_code, Room.building, Room.number, Exam.offered, Exam.taking FROM Exam JOIN Classes ON Exam.class_id = Classes.id JOIN Professors ON Exam.professor_id=Professors.id JOIN Room ON Exam.room_id = Room.id WHERE Exam.datetime >= :start_date AND Exam.datetime <= :end_date""")
            exams = connection.execute(stmt, {"start_date": timeform.time1.data, "end_date": timeform.time2.data})
        elif classform.validate_on_submit():
            stmt = text("""SELECT Exam.id, Exam.datetime, Exam.duration, Exam.description, Professors.name, Classes.course_code, Room.building, Room.number, Exam.offered, Exam.taking FROM Exam JOIN Classes ON Exam.class_id = Classes.id JOIN Professors ON Exam.professor_id=Professors.id JOIN Room ON Exam.room_id = Room.id WHERE Classes.course_code = :course""")
            exams = connection.execute(stmt, {"course": classform.classes.data})
        else:    
            exams = connection.execute(text("SELECT Exam.id, Exam.datetime, Exam.duration, Exam.description, Professors.name, Classes.course_code, Room.building, Room.number, Exam.offered, Exam.taking FROM Exam JOIN Classes ON Exam.class_id = Classes.id JOIN Professors ON Exam.professor_id=Professors.id JOIN Room ON Exam.room_id = Room.id"))
  #  exams = Exam.query.order_by(Exam.id)
        connection.commit()
        #classes1 = connection.execute(text("SELECT course_code FROM Classes"))
        #print([e.course_code for e in classes1])
        #print([e.id for e in exams])
    return render_template("report.html", exams=exams, timeform = timeform, classform = classform)

@app.route('/students', methods=["GET", "POST"])
def confirm():
    form = StudentUpdateForm2()
    form.exam_id.choices = [e.id for e in db.session.query(Exam).all()]
    #line = db.session.query(Exam).filter(Exam.id == form.exam_id.data).all()[0]
    #if line.taking == line.offered:
    #    flash("Sorry Exam is Full")
    alarm = None
    if form.validate_on_submit():
        for c in db.session.query(Exam).filter(Exam.id == form.exam_id.data).all():
            if c.taking == c.offered:
                #flash("Sorry Exam is Full")
                alarm = "Worries ahead"
                #print("taco")
            else:
                c.taking = c.taking + 1
                stmt = update(Exam).where(Exam.id == form.exam_id.data).values(taking=c.taking)
                with engine.connect() as conn:
                    conn.execute(stmt)
                    conn.commit()
        #line.taking = line.taking + 1

        db.session.commit()
        
    return render_template("students.html", form=form, alarm=alarm)
