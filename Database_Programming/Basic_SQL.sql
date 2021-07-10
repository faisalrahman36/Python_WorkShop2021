Select * from courses

Select * from courses where weeks=14

Select * from courses where weeks<>14

Select * from courses where weeks=14 and teacher='Hira'

Select coursename, teacher from courses where teacher='Faisal'

Update courses set weeks=11 where cid<3

Insert into courses (coursename,course_id,teacher) values ('Computer Programming with Python', 'SST503','Faisal')

Insert into courses (coursename,course_id,teacher) values ('Computer Programming with Python', 'SST503',55)

Insert into courses (cid,course_id,teacher) values ('Computer Programming with Python', 'SST503','Faisal')

Insert into courses (coursename,course_id,teacher, weeks) values ('Computer Programming with Python-Lab', 'SST503', 'Hira',14)

Insert into courses (coursename,course_id,teacher, weeks) values ('astrophysics', 'SST302', 'faisal',14)

Delete courses where teacher='55'