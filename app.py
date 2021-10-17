from flask import Flask,session
from first import First
from alumni import Alumni
from student import Student
from teacher import Teacher
from direct import Direct
from mailhandler import Mailhandler
import pymongo
import os
from pymongo import MongoClient
from flask import request,jsonify,json,render_template


client=MongoClient('localhost', 27017)
app = Flask(__name__)

app.secret_key=os.urandom(24)
first=First() 
alma=Alumni()
stud=Student()
teach=Teacher()
di=Direct()
@app.route('/crash')
def main():
    raise Exception()


@app.route('/sign')
def signup():
    return render_template('sign.html')

@app.route('/colleges',methods=['GET'])
def getProducts():
    colleges=[]
    id=request.args['id']
    res=first.getCollegeByAttr("college_id",id)
    if (res==False):
        colleges.append("sorry no products found")
    else:    
        for i in res:   
            colleges.append({"college_id":i['college_id'],"college_name":i['college_name'],"eastablish_year":i['establish_year'],"email":i['email'],"location":i['location'],"website":i['website']})
    
    return jsonify({'result':colleges})

@app.route('/addcolleges',methods=['POST'])
def addCollege():
    colleges=[]
    id=request.form["clg_id"]
    name=request.form["clg_name"]
    esta_year=request.form["clg_esta_year"]
    email=request.form["clg_email"]
    password=request.form["clg_password"]
    website=request.form["clg_website"]
    location=request.form["clg_location"]
    college={"college_name":name,"college_id":id,"establish_year":esta_year,"email":email,"password":password,"website":website,"location":location}
    res=first.addNewCollege(college)

    if (len(res)<0):
        colleges.append("something went wrong ...product not added")
    else:    
        colleges.append(res)
    
    return jsonify({'result':colleges})


@app.route('/addalumni',methods=['POST','GET'])
    
def addAlumni():
    m=Mailhandler()
    m.py_mail_confirm()    
    
    alumnies=[]
    id=request.form["alumni_id"]
    name=request.form["alumni_name"]
    join_year=request.form["alumni_join_year"]

    end_year=request.form["alumni_end_year"]
    email=request.form["alumni_email"]
    password=request.form["alumni_password"]
    branch=request.form["alumni_branch"]
    desig=request.form["alumni_desig"]
    alma1={"alumni_name":name,"alumni_id":id,"alumni_join_year":join_year,"alumni_end_year":end_year,"alumni_email":email,"alumni_password":password,"alumni_branch":branch,"alumni_desig":desig}
    res=alma.addNewAlumni(alma1)

    if (len(res)<0):
        alumnies.append("something went wrong ...alumni not added")
    else:    
        alumnies.append(res)
    
    return jsonify({'result':alumnies})
   

@app.route('/addstudent',methods=['POST'])
def addStudent():
    students=[]
    id=request.form["student_id"]
    name=request.form["student_name"]
    join_year=request.form["student_join_year"]

    end_year=request.form["student_end_year"]
    email=request.form["student_email"]
    password=request.form["student_password"]
    branch=request.form["student_branch"]
    college=request.form["student_college"]
    student={"student_name":name,"student_id":id,"student_join_year":join_year,"student_end_year":end_year,"student_email":email,"student_password":password,"student_branch":branch,"student_college":college}
    res=stud.addNewStudent(student)

    if (len(res)<0):
        students.append("something went wrong ...student not added")
    else:    
        students.append(res)
    
    return jsonify({'result':students})


@app.route('/addteacher',methods=['POST'])
def addTeacher():
    teachers=[]
    id=request.form["teacher_id"]
    name=request.form["teacher_name"]
    email=request.form["teacher_email"]
    password=request.form["teacher_password"]
    branch=request.form["teacher_branch"]
    college=request.form["teacher_college"]
    teacher={"teacher_name":name,"teacher_id":id,"teacher_email":email,"teacher_password":password,"teacher_branch":branch,"teacher_college":college}
    res=teach.addNewTeacher(teacher)

    if (len(res)<0):
        teachers.append("something went wrong ...teacher not added")
    else:    
        teachers.append(res)
    
    return jsonify({'result':teachers})


@app.route('/adddirect',methods=['POST'])
def addDirect():
    directs=[]
    id=request.form["direct_id"]
    name=request.form["direct_name"]
    email=request.form["direct_email"]
    password=request.form["direct_password"]
    branch=request.form["direct_branch"]
    college=request.form["direct_college"]
    direct={"direct_name":name,"direct_id":id,"direct_email":email,"direct_password":password,"direct_branch":branch,"direct_college":college}
    res=di.addNewDirect(direct)

    if (len(res)<0):
        directs.append("something went wrong ...Directorate not added")
    else:    
        directs.append(res)
    
    return jsonify({'result':directs})


@app.route('/login',methods=['POST'])
def login():
  
    
        db=client.alumni
        role=request.form['role']
        username=request.form['username']
        password=request.form['password']
        results=[]
        stat=request.args['status']
        
        if(role=='student'):
            
            if db.students.find({ '$and': [ { 'student_name':username }, { 'student_password': password } ] }).count() > 0:
                results.append('login successfully')
                db.session.insert({'user':username})
                session["user"]=request.form['username']
            else:
                results.append('login not successfully')

        if(role=='direct'):
            if db.directs.find({ '$and': [ { 'direct_name':username }, { 'direct_password': password } ] }).count() > 0:
                results.append('login successfully')
                db.session.insert({'user':username})
                session["user"]=request.form['username']
            else:
                results.append('login not successfully')

            
        if(role=='teacher'):
            if db.teachers.find({ '$and': [ { 'teacher_name':username }, { 'teacher_password': password } ] }).count() > 0:
                results.append('login successfully')
                db.session.insert({'user':username})
                session["user"]=request.form['username']
            else:
                results.append('login not successfully')

            
        if(role=='alumni'):
            if db.alumnies.find({ '$and': [ { 'alumni_name':username }, { 'alumni_password': password } ] }).count() > 0:
                results.append('login successfully')
                db.session.insert({'user':username})
                session["user"]=request.form['username']
            else:
                results.append('login not successfully')

        if(role=='college'):
            if db.colleges.find({ '$and': [ { 'college_name':username }, { 'password': password } ] }).count() > 0:
                results.append('login successfully')
                db.session.insert({'user':username})
                session["user"]=request.form['username']
            else:
                results.append('login not successfully')

    return jsonify({'results':results})
    

@app.route('/showloggedin')
def showloggedin():
    return jsonify(session['user'])

@app.route('/createpost',methods=['POST'])
def cratepost():
    from Posting import Posting

    p=Posting()
    posts=[]
    
    name=session['user']
    post=request.form["userpost"]
    
    post1={"username":name,"post":post}
    res=p.addNewPost(post1)

    if (len(res)<0):
        posts.append("something went wrong ...post not added")
    else:    
        posts.append(res)
    
    return jsonify({'result':posts})

@app.route('/sendMail',methods=['GET'])

def sendMail():
    m=Mailhandler()
    m.py_mail_confirm()    
    


    return "Email Sent"


        

    

app.run(debug=True)
