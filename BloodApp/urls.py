from django.urls import path
from .import views

urlpatterns = [
    path('',views.Home),                           #PAGES
    path('register',views.Register),
    path('signin',views.SignIn),
    path('adminregister',views.Adminregister),
    path('adminsignin',views.AdminSignIn),
    path('blogs',views.Blog),
    path('whydonateblood',views.blog1,name='whydonateblood'),
    path('whatisblooddonation',views.blog2,name='whatisblooddonation'),
    path('apheresis',views.blog3,name='apheresis'),
    path('about',views.About),
    path('contact',views.Contact),
    path('funccontact',views.FuncContactform),
    path('viewhospitals',views.Viewhospitals),
    path('userprofile',views.Userprofile),        #PROFILE PAGES
    path('userviewhospital',views.UserViewHopsital),
    path('userbloodrequest',views.UserBloodRequest),
    path('bothrequests',views.SendRequests),
    path('usersendrequest',views.UserSendRequest),
    path('funcusersendrequest',views.FuncUserSendRequest),
    path('userdonorrequest',views.UserDonorRequests),
    path('funcuserdonorrequest',views.FuncUserDonorRequests),
    path('mykey',views.my_view),
    path('adminprofile',views.Adminprofile),
    path('adminregister', views.FuncAdminRegister),
    path('funcadminsignin', views.FuncAdminSignin),
    path('adminsignout',views.FuncAdminSignOut),
    path('addhospitals',views.Addhospitals),
    path('bloodrequest',views.BloodRequest),
    path('donorrequest',views.DonorRequest),
    path('adminsendrequest',views.AdminSendRequest),
    path('getusers',views.GetUsers),
    path('delete <int:uid>',views.deleteUser,name='delete'),
    path('funcregisters',views.FuncRegister),     #FUNCTIONS
    path('funcsignins',views.FuncSignin),
    path('funcsignouts',views.FuncSignout),
    path('funcaddhospital',views.Funcaddhospitals),
    path('funcadminsendrequest',views.FuncAdminSendRequest),
    path('donorsuserview',views.DonorsUserview,name='donorsuserview'),
    path('donors',views.Donors,name='donors'),
    path('patients',views.Patients,name='patients'),
    path('acceptdonor/<int:did>/<str:dphone>',views.AcceptDonor,name='acceptdonor'),
    path('rejectdonor/<int:rdid>/<str:rdphone>',views.RejectDonor,name='rejectdonor'),
    path('acceptblood/<int:pid>/<str:pphone>', views.AcceptBlood, name='acceptblood'),
    path('rejectblood/<int:rpid>/<str:rpphone>', views.RejectBlood, name='rejectblood'),
]


