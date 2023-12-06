from django.urls import path
from . import views
from django.views.generic import TemplateView
from .views import MyView
from .views import AboutView
from .views import IndexView
from .views import DetailView
from .views import ResultsView
from .views import VoteView
# from .views import BaseView

app_name = 'polls'
urlpatterns = [
    # path('', views.index, name='index'),
    path('', IndexView.as_view()),
    # path('<int:question_id>', views.detail, name='detail'),
    path('<int:question_id>', DetailView.as_view()),
    # path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/results/', ResultsView.as_view(), name='results'),
    # path('<int:question_id>/vote/', views.vote, name='vote'),
    path('<int:question_id>/vote/', VoteView.as_view(), name='vote'),

    # # 이하는 poll 어플과 상관이 없음
    # path('template-extends/', TemplateView.as_view(template_name='polls/child_template.html')),
    # path('name/', views.name),
    # path('form-class-ex-thanks/', TemplateView.as_view(template_name='form_class_ex_thanks.html')),
    # path('name2/', views.MyFormView.as_view()),
    # path('name3/', views.MyFormView2.as_view()),
    # path('about/', MyView.as_view()),
    # path('about2/', AboutView.as_view()),
    # path('basepoll/', BaseView.as_view(), name='baseview'),
    # path('test/', )



]