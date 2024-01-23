from django.urls import path
from .views import *

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('enrol/', EnrollView.as_view(), name='enroll'),
    path('introduction/', IntroductionView.as_view(), name='introduction'),
    path('speaking/', SpeakingView.as_view(), name='speaking'),
    path('writing/', WritingView.as_view(), name='writing'),
    path('reading/', ReadingView.as_view(), name='reading'),
    path('listening/', ListeningView.as_view(), name='listening'),
    path('enquiry/', EnquiryView.as_view(), name='enquiry'),
    path('story/', StoryView.as_view(), name='story'),
]
