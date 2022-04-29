
from django.shortcuts import render,redirect
#for calling the current url
#varaibale from setting.spy file
from django.conf import settings
import datetime


#FOR URL ROUTING
curl=settings.CURRENT_URL

#for import models
from . import models

def Home(request):
 return render(request,"Home.html",{'curl':curl})

def Blog(request):
 return render(request,"Blog.html",{'curl':curl})

def Dance(request):
 return render(request,"Dance.html",{'curl':curl}) 
 
def Login(request):
 if request.method=="GET":  	  
  return render(request,"login.html",{'curl':curl,'msg':''})
 else:
  emailid=request.POST.get("emailid")
  pwd=request.POST.get("pwd")        
  query="select emailid,role from mstuser where emailid='%s' and pwd='%s'" %(emailid,pwd)
  models.cursor.execute(query)
  rs=models.cursor.fetchone()
  role=rs[1]  

  #for create a new session .......................
  request.session["emailid"]=emailid
  request.session["role"]=role
  #end here...............................................

  if rs==None:
   return render(request,"home.html",{'curl':curl,'msg':'Invalid Email Id or Pwd'})         
  else:
   if rs[1]=="admin":    
    return redirect("/AdminHome/") 
   else:
    return redirect("/StudentHome/")	

     
 return render(request,"Login.html",{'curl':curl})

def Register(request):
 if request.method=="GET": 
  return render(request,"Register.html",{'curl':curl})
 else:
  fnm=request.POST.get("fnm")
  mno=request.POST.get("mno") 
  gender=request.POST.get("gender") 
  address=request.POST.get("address") 
  emailid=request.POST.get("emailid") 
  pwd=request.POST.get("pwd")
  role="student"
  
  query="insert into mstuser(fnm,mno,gender,address,emailid,pwd,role) values('%s','%s','%s','%s','%s','%s','%s')" %(fnm,mno,gender,address,emailid,pwd,role) 
  print(query)
  models.cursor.execute(query)
  models.db.commit()
  return render(request,"Register.html",{'curl':curl})
    
def AdminHome(request):
 #for Fetch session .......................
 emailid=request.session["emailid"]
 role=request.session["role"]
 #end here...............................................

 return render(request,"AdminHome.html",{'curl':curl,'emailid':emailid,'role':role})    

def AddCourse(request):
 if request.method=="GET": 
  return render(request,"AddCourse.html",{'curl':curl,'msg':''})
 else:
  coursename=request.POST.get("coursename")   
  duration=request.POST.get("duration")   
  fees=request.POST.get("fees")   
  shortdesc=request.POST.get("shortdesc")   
  coursedetail=request.POST.get("coursedetail")     
  query="insert into course(coursename,duration,fees,shortdesc,coursedetail) values('%s','%s','%s','%s','%s')" %(coursename,duration,fees,shortdesc,coursedetail)
  print(query)
  models.cursor.execute(query)
  models.db.commit()
 return render(request,"AddCourse.html",{'curl':curl,'msg':'Course Saved'}) 

def CourseList1(request):
 query="select * from course order by coursename"
 models.cursor.execute(query)
 rs=models.cursor.fetchall()
 return render(request,"CourseList1.html",{'curl':curl,'rs':rs}) 
 
def AddBatch(request):
 if request.method=="GET": 
  query="select courseid,coursename from course "
  models.cursor.execute(query)
  rs=models.cursor.fetchall() 
  return render(request,"AddBatch.html",{'curl':curl,'rs':rs})
 else:
  courseid=request.POST.get("courseid")
  startdate=request.POST.get("startdate")
  batchtime=request.POST.get("batchtime")
  facultyname=request.POST.get("facultyname")
  query="insert into batch(courseid,startdate,batchtime,facultyname) values('%s','%s','%s','%s')" %(courseid,startdate,batchtime,facultyname)
  print(query)
  models.cursor.execute(query)
  models.db.commit()
 return render(request,"AddBatch.html",{'curl':curl,'rs':''})   

def NewBatchList (request):
 query="select b.coursename,b.duration,b.fees,a.startdate,a.batchtime,a.facultyname from batch as a inner join course as b on a.courseid=b.courseid where a.batchstatus=0"
 models.cursor.execute(query)
 rs=models.cursor.fetchall()
 return render(request,"NewBatchList1.html",{'curl':curl,'rs':rs})  

def Logout(request):
 if 'emailid' in request.session:
  del request.session['emailid']
  return render(request,"Home.html",{'curl':curl}) 
 
def StudentHome(request):
 #for Fetch session .......................
 emailid=request.session["emailid"]
 role=request.session["role"]
 #end here...............................................

 return render(request,"StudentHome.html",{'curl':curl,'emailid':emailid,'role':role})    

def CourseList2(request):
 query="select * from course order by coursename"
 models.cursor.execute(query)
 rs=models.cursor.fetchall()
 return render(request,"CourseList2.html",{'curl':curl,'rs':rs})

def NewBatchList2 (request):
 query="select b.coursename,b.duration,b.fees,a.startdate,a.batchtime,a.facultyname,a.batchid from batch as a inner join course as b on a.courseid=b.courseid where a.batchstatus=0"
 models.cursor.execute(query)
 rs=models.cursor.fetchall()
 return render(request,"NewBatchList2.html",{'curl':curl,'rs':rs})

def Admission(request):
 #for fetch data from query string
 batchid=request.GET.get("batchid")
 query="select b.coursename,b.duration,b.fees,a.startdate,a.batchtime,a.facultyname,a.batchid from batch as a inner join course as b on a.courseid=b.courseid where a.batchstatus=0 and a.batchid='%s'" %(batchid)
 models.cursor.execute(query)
 rs=models.cursor.fetchone() 
 return render(request,"Admission.html",{'curl':curl,'rs':rs})

def BatchBooking(request):
 if request.method=="POST":
  batchid=request.POST.get("batchid")
  emailid=request.session["emailid"]

  x=datetime.datetime.now()
  admissiondate=x.strftime("%Y/%m/%d")
  #print(admissiondate) 
  query="insert into admission(batchid,emailid,admissiondate) values('%s','%s','%s')" %(batchid,emailid,admissiondate)
  print(query)
  models.cursor.execute(query)
  models.db.commit()
 return render(request,"showresult.html",{'curl':curl})

def SearchProfile(request):
 #for fetch emailid from session
 emailid=request.session["emailid"]
 query="select * from mstuser where emailid='%s'" %(emailid)
 models.cursor.execute(query)
 rs=models.cursor.fetchone() 
 return render(request,"SearchProfile.html",{'curl':curl,'rs':rs})

def UpdateProfile(request):
 if request.method=="POST":
  fnm=request.POST.get("fnm")
  mno=request.POST.get("mno")
  address=request.POST.get("address")
  pwd=request.POST.get("pwd")
  emailid=request.POST.get("emailid")
  query="update mstuser set fnm='%s',mno='%s',address='%s',pwd='%s' where emailid='%s'" %(fnm,mno,address,pwd,emailid)
  print(query)
  models.cursor.execute(query)
  models.db.commit()
 return render(request,"StudentHome.html",{'curl':curl,'emailid':emailid,'role':''})

def DeleteContact(request):
 if request.method=="GET":
  return render(request,"deleteentry.html",{'curl':curl,'msg':''})
 else:
  srno=request.POST.get("srno")
  query="delete from contact where srno='%s'" %(srno)
  print(query)
  models.cursor.execute(query)
  models.db.commit()
 return render(request,"deleteentry.html",{'curl':curl,'msg':'Record Deleted'})  


def Contact(request):
  if request.method=="GET":
   return render(request,"Contact.html",{'curl':curl})  
  else:
   nm=request.POST.get("nm")
   email=request.POST.get("email")
   msg=request.POST.get("msg")
  query="insert into Contact(nm,email,msg) values('%s','%s','%s')" %     (nm,email,msg); 
  
  models.cursor.execute(query)
  models.db.commit()
  return render(request,"Contact.html",{'curl':curl})