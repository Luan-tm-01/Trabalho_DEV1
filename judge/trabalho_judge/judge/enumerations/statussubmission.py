from django.db import models

class StatusSubmission(models.TextChoices):
    NOT_ANSWERED = "Não Respondida", "Não Respondida"
    IN_QUEUE = "Em fila de execução", "Em fila de execução"
    RUNNING = "Execução", "Execução"
    ACCEPTED = "Aceito", "Aceito"
    WRONG_ANSWER = "Resposta Errada", "Resposta Errada"
    TIME_LIMIT_EXCEEDED = "Tempo Limite Excedido", "Tempo Limite Excedido"
    MEMORY_LIMIT_EXCEEDED = "Limite de Memória Excedido", "Limite de Memória Excedido"
    RUNTIME_ERROR = "Erro de Runtime", "Erro de Runtime"
    COMPILATION_ERROR = "Erro de Compilação", "Erro de Compilação"
    PRESENTATION_ERROR = "Erro de Apresentação", "Erro de Apresentação"
    INTERNAL_ERROR = "Erro Interno", "Erro Interno"
