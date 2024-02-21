from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello!, Welcome to Index page")

def vision(request):
    msg ="<h1><center><br>CCMS VISION<br><br></h1>\
<h3><center>The College of Computing and Multimedia Studies shall be a center of excellence in delivering Computing and Multimedia education.</h3>"
    return HttpResponse(msg)

def mission(request):
    msg ="<h1><center><br>CCMS MISSION<br><br></h1>\
<h3><center>The College of Computing and Multimedia Studies shall produce competent and innovative professionals or Technopreneurs in the Information\
      and Communication Technology (ICT) industry adequately prepared in the practice of their profession supportive of national development goals and\
          standards of global excellence.</h3>"
    return HttpResponse(msg)

def objectives(request):
    msg ="<h1><center><br>CCMS OBJECTIVES<br></h1>\
<h4><center>At the College of Computing and Multimedia Studies, we are driven by a steadfast commitment to excellence in every aspect of our work.\
      Our quality objectives serve as the guiding principles that propel us toward continuous improvement and the delivery of exceptional educational experiences.\
</h4><br><br>"\
"<h3><center> Increase faculty performance by obtaining a minimum rating of 4.00 in the semestral faculty evaluation of each faculty for the next fiveyears.</h3> "\
"<h3><center> Maintain competent faculty line-up by sending all permanent fulltime faculty to at least one (1) IT related training, conference, orseminar\
      annually for the next five years. </h3>"\
"<h3><center> Conduct a minimum of two (2) researches, IT projects or production of instructional materials annually for the next five years.Achieve a minimum of 50 student\
      passing percentage in the IT certification annually for the next five years.</h3>"\
    "<h3><center>Maintain state-of-the-art information technology learning environment through annual procurement or upgrading of hardwareor software licenses for at least one\
          computer laboratory for the next five years.</h3>"\
        "<h3><center>Maintain state-of-the-art information technology learning environment through annual procurement or upgrading of hardwareor software licenses for at least one computer laboratory for the next five years.</h3>"
    
    return HttpResponse(msg)