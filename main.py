from datetime import datetime


def hello_word(request):
    return f'{datetime.now()} Hello, World! {request}'