from django.urls import path

from . import views

app_name= 'courses'

urlpatterns = [
    path('cursos/', views.index, name = 'index'),
    path('cursos/<slug:slug>/', views.details, name = 'details'),
    path('cursos/<slug:slug>/inscricao/', views.enrollment, name='enrollment'),
    path('cursos/<slug:slug>/cancelar-inscricao/', views.undo_enrollment, name='undo_enrollment'),
    path('cursos/<slug:slug>/anuncios/', views.announcements, name='announcements'),
    path('cursos/<slug:slug>/anuncios/<int:pk>', views.show_announcement, name='show_announcement'),
    path('cursos/<slug:slug>/aulas/', views.lessons, name='lessons'),
    path('cursos/<slug:slug>/aulas/<int:pk>', views.lesson, name='lesson'),
    path('cursos/<slug:slug>/materiais/<int:pk>', views.material, name='material'),

]