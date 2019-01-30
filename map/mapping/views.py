from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, loader

def index(request):
    # template = loader.get_template("mapping/index.html")
    # return HttpResponse(template.render())
    return render(request, 'mapping/index.html')
# # Create your views here.
# conn = MySQLdb.connect(host = '',
#     user = 'root',
#     passwd = 'root',
#     db = 'myDB'   
# )

# cursor.execute('select <column> from <table>')
# rows = dictfetchall(cursor)


# conn.close()

# def dictfetchall(cursor):
#     "Return all rows from a cursor as a dictionary"
#     desc = cursor.description
#     return [
#         dict(zip([col[0] for col in desc], row))
#         for row in cursor.fetchall()
#     ]
