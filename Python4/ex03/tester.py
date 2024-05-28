from new_student import Student


student = Student(name="Edward", surname="agle")
print(student)

# expected output
# $> python tester.py
# Student(name='Edward', surname='agle', active=True,
#         login='Eagle', id='trannxhndgtolvh')
# $>

# student = Student(name="Edward", surname="agle", login="toto")
# print(student)

# expected output
# $> python tester.py
# ...
# TypeError: Student.__init__() got an unexpected keyword argument 'login'
# $>

student = Student(name="Edward", surname="agle", id="toto")
print(student)

# expected output
# $> python tester.py
# ...
# TypeError: Student.__init__() got an unexpected keyword argument 'id'
# $>
