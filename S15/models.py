from peewee import *

db = SqliteDatabase('dormitory.db')

class BaseModel(Model):
    class Meta:
        database = db

class Student(BaseModel):
    full_name = CharField()
    student_number = CharField(unique=True)
    faculty = CharField()
    course = IntegerField()
    phone = CharField()

class Dormitory(BaseModel):
    name = CharField()
    address = CharField()
    floors = IntegerField()

class Room(BaseModel):
    room_number = CharField()
    capacity = IntegerField()
    occupied_places = IntegerField()
    dormitory = ForeignKeyField(Dormitory)

class Settlement(BaseModel):
    student = ForeignKeyField(Student)
    room = ForeignKeyField(Room)
    check_in_date = DateField()
    check_out_date = DateField(null=True)
    status = CharField()

class Application(BaseModel):
    student = ForeignKeyField(Student)
    application_date = DateField()
    status = CharField()
    comment = TextField()
    
def init_db():
    db.connect()
    db.create_tables([
        Student,
        Dormitory,
        Room,
        Settlement,
        Application
    ])

if __name__ == "__main__":
    init_db()