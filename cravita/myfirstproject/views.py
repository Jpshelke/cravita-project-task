from django.shortcuts import render 
from .models import Task

# Create your views here.
from django.shortcuts import render

def home(request):
    return render(request, "home.html")
def index(request):
    return render( request,"index.html")


def login_page(request):

    if request.method == "POST":

        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(username=username, password=password)

        if user is not None:

            login(request, user)

            return redirect("dashboard")

        else:

            messages.error(request, "Invalid Username or Password")

    return render(request, "login.html")


def dashboard(request):

    total = Task.objects.count()

    pending = Task.objects.filter(status="Pending").count()

    progress = Task.objects.filter(status="In Progress").count()

    completed = Task.objects.filter(status="Completed").count()

    tasks = Task.objects.all().order_by("-id")

    context = {

        "total": total,

        "pending": pending,

        "progress": progress,

        "completed": completed,

        "tasks": tasks,

    }

    return render(request, "dashboard.html", context)