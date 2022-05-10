from tokenize import String
from attr import fields
from flask_restx import fields

from src.server.instance import server

book = server.api.model("Book",{
    'id': fields.String(description="O ID do registro."),
    'title': fields.String(required=True, min_length=1, max_length=200, description="O nome do livro.")
})