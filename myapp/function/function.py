from ast import With


def hundle_uploaded_file(f):
    with open('myapp/static/myapp/upload', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)