from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Question, Choice
from django.shortcuts import get_object_or_404

def Index(request):
      questions = Question.objects.all()
      context = {'question': questions}
      return render(request,'polls/index.html', context)


def Detalle(request, question):
      question = Question.objects.get(pk=question)
      choice = Choice.objects.all()
     
      Dic = {
            'numb': question,
            'question': question,
            'choice': choice,
          }
      return render(request,'polls/detalle.html', Dic)


def Vote(request,question):
      question = get_object_or_404(Question, pk=question)
      try:
        selected_choice = question.choice_set.get(
            pk=request.POST['choice'])
      except (KeyError, Choice.DoesNotExist):
   
        return render(request, 'polls/detalle.html', {
            'question': question,
            'error_message': "Debes seleccionar una respusta.",
        })
      else:
        selected_choice.vote += 1
        selected_choice.save()
      return render(request,'polls/resultados.html')


# Resultados traera las respuesta de las mas famosas y las compara con 
# algo llamado  (Moda de respuestas)
#  (Moda de respuestas) sera una clase con metodos para 
# crear un analisis de los usuarios, sus respuestas y preguntas  votadas.
# En  la --> def ViewsModa(request,Eleccion) <-- 
# de acuerdo a la respuestas     
def Resultados(request,question):
      
      return render(request, 'polls/resultados.html')
      
      
      
      
      
      

         
          