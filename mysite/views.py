# created by me:
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request,'index.html') 

def link(request):
    return HttpResponse ('''<h1> One Click :<h1/> <h2> facebook</h2> <a href='http://facebok.com'> Facbook link</a> <br>
    <h2> Youtube</h2> <a href='http://youtube.com'> Youtube link</a> <br>
    <h2> Instagram</h2> <a href='http://instagram.com'> Instagram link</a> <br>''')

def analyzer(request): # with back button:
    #get and analyze text:
    djtext = (request.POST.get('text','default'))

    # chexkbox variable:
    removepunc = (request.POST.get('removepunc','off'))  
    capitalfirst = (request.POST.get('capitalfirst','off')) 
    newlineremover = (request.POST.get('newlineremover','off')) 
    extraspaceremover = (request.POST.get('extraspaceremover','off'))
   
    if removepunc == 'on':
        panctuate = ''' !@#$%^&*()_-|}{[]'":;./\?,'''
        analyzer = ''
        for char in djtext:
            if char not in panctuate:
                analyzer = analyzer + char
        params = {'purpose':'Remove Punctutation:','analyzed_text': analyzer}
        djtext = analyzer

    if ( capitalfirst == 'on'):
        fullcap =''
        for char in djtext:
            fullcap= fullcap + char.upper()
        params = {'purpose':'Changed to upper case :','analyzed_text': fullcap}
        djtext = fullcap
        
    if (newlineremover == "on"):
        NewLines = ""
        for char in djtext:
            if char != '\n' and char != '\r':
                NewLines = NewLines + char
        params = {'purpose': 'Removed NewLines', 'analyzed_text': NewLines}
        djtext = NewLines

    if (extraspaceremover == 'on'):
        space_line =''
        for index, char in enumerate (djtext):
            if not(djtext[index]==' ' and djtext[index+1] ==' '):
                space_line= space_line+ char
        params = {'purpose':'Extra Space remover :','analyzed_text': space_line}
        djtext = space_line
    
    return render(request,'analyzer.html',params)        
