from django.shortcuts import render, redirect
from django.http import HttpResponse

from chatterbot import ChatBot
from chatterbot.logic import LogicAdapter
from chatterbot.conversation import Statement

class AuthenticationAdapter(LogicAdapter):
    def __init__(self, chatbot, **kwargs):
        super().__init__(chatbot, **kwargs)

    def can_process(self, statement):
        keywords = ["hello", "goodbye", "good", "i want"]
        for keyword in keywords:
            if keyword in statement.text.lower().strip():
                return True
        return False
    
    def process(self, statement, additional_response_selection_parameters=None):
        request = additional_response_selection_parameters.get('request')
        if not request:
            return Statement("Error: 'request' parameter not found.")
        
        session = request.session

        # Verifique se a sessão possui um valor para 'username'
        if 'username' in session:
            username = session['username']
        else:
            username = None

        # Verifique se a sessão possui um valor para 'password'
        if 'password' in session:
            password = session['password']
        else:
            password = None
        
        if username and password:
            response = Statement("Hi! You are already authenticated.")
        elif username:
            response = Statement("Hi {}! Can you please type your password?".format(username))
        else:
            response = Statement("Hi! Can you please type your username?")
        return response