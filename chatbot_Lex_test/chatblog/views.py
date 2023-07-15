from django.shortcuts import render
from django.http import HttpResponse

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatblog.adapters.authentication_adapter import AuthenticationAdapter
from chatblog.adapters.user_input_adapter import UserInputAdapter
from chatterbot.storage import DjangoStorageAdapter

storage_adapter = DjangoStorageAdapter()

bot = ChatBot('chatbot', read_only=False,
              storage_adapter = 'chatterbot.storage.DjangoStorageAdapter',
              logic_adapters=[
                  
                 
                  
                  
                  
                 ])

authentication_adapter = AuthenticationAdapter(bot)
user_input_adapter = UserInputAdapter(bot)

bot.logic_adapters.insert(0, authentication_adapter)


print(bot.logic_adapters)

list_teacher = [


    "Good",
    "Hello I am chatblog at your service",
    "What is your name?",
    "I am chatblog, your best friend!",
    "My name is Gaby",
    "Hello Gaby. How is Eevee doing? send a kiss to him!",
    "whats your favorite game?",
    "Chrono Trigguer, an absolute classic",
    "I am Camila",
    "Hello, Camila! Is guiness alright?",
    "My name is Paloma",
    "Hi, Paloma! The temperature here in Vitoria is very cold"

]


list_trainer = ListTrainer(bot)
list_trainer.train(list_teacher)

def index(request):
    return render(request, 'chatblog/index.html')

def test(request):
    return HttpResponse("Hello again , my old friend")

def getResponse(request):
    userMessage = request.GET.get('userMessage')
    chat_response = str(bot.get_response(userMessage, request=request))
    return HttpResponse(chat_response)








