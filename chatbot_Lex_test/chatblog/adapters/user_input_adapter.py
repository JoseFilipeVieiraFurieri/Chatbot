from chatterbot.logic import LogicAdapter
from chatterbot.conversation import Statement

from chatterbot.logic import LogicAdapter

from chatterbot.logic import LogicAdapter
from chatterbot.conversation import Statement

class UserInputAdapter(LogicAdapter):
    def __init__(self, chatbot):
        super().__init__(chatbot)

    def can_process(self, statement):
        # Sempre retorne True para que este adaptador seja chamado
        return True

    def process(self, statement, additional_response_selection_parameters=None):
        # Verifique se o chatbot solicitou o username anteriormente
        if "Please enter your username." in statement.text.strip():

            username = statement.text.strip()

            response = "Please enter your password."
            return Statement(response)

        # Se o chatbot solicitou o password anteriormente
        elif "Please enter your password." in statement.text.strip():
            # Obtenha o password fornecido pelo usuário
            password = statement.text.strip()

            response = f"Thank you, you are now authenticated with password: {password}."
            return Statement(response)

        return None
