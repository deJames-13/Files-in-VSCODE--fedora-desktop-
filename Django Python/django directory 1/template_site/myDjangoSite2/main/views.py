from django.http import HttpResponse
from django.shortcuts import render

def create_default_view(label: str):
    label = "".join("".join(label.rsplit("<")).rsplit(">")).rsplit("%")
    default_view = """
<div class="">
    <div class="d-flex justify-content-center align-items-center" style="height: 100vh;">
        <h1>        
            {}
        </h1>
    </div>
</div>
""".format(*label)
    return default_view


# Create your views here.
def base(response, label: str = None):
    label = "This is the Base Template" if not label else label
    c = {"default_view": create_default_view(label),
         
    }
    
    return render(response, "main/base.html", c)

def index(response):
    label = "This is the Index Page"
    c = {"default_view": create_default_view(label),
         
    }
    
    return render(response, "main/index.html", c)

def home(response):
    label = "This is the Home Page"
    c = {"default_view": create_default_view(label),
         
    }
    
    return render(response, "main/home.html", c)
