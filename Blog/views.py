from django.shortcuts import render,redirect
from .models import Post
from .forms import PostForm
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required



# Create your views here.


def home(request):
    # Seleccionamos un hecho aleatorio
    post = Post.objects.all()
    # Creamos el contenido de la respuesta
    context = {'posts': post}
    # Creamos la respuesta
    return render(request, 'Blog/home.html', context=context)
@login_required(login_url='/login_view/')
def create_view(request):
    # Verificamos si se envió el formulario
    if request.method == 'POST':
        # Creamos el formulario con los datos del POST
        form = PostForm(request.POST)
        # Verificamos si el formulario es válido
        if form.is_valid():
            # Guardamos el formulario
            Post = form.save(commit=False)
            Post.user = request.user
            Post.save()
            # Redireccionamos a la página principal
            return redirect('home')
    else:
        # Creamos el formulario
        form = PostForm()
    # Creamos el contenido de la respuesta
    # Creamos la respuesta
    return render(request, 'Blog/create.html', {'form':form})


def login_view(request):
    # Verificar si el usuario ya está autenticado
    if request.user.is_authenticated:
        return redirect('home')
    # Verificamos si se envió el formulario
    if request.method == 'POST':
        # Creamos el formulario con los datos del POST
        form = AuthenticationForm(request, data=request.POST)
        # Verificamos si el formulario es válido
        if form.is_valid():
            # Autenticamos al usuario
            user = form.get_user()
            login(request, user)
            # Obtenemos la URL a la que se debe redireccionar
            redirect_to = request.GET.get('next', '')
            # Redireccionamos a la página principal o a la URL
            return redirect(redirect_to or '/')
    else:
        # Creamos el formulario
        form = AuthenticationForm(request)
    # Creamos la respuesta
    return render(request, 'Blog/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('/')

def register_view(request):
    # Verificar si el usuario ya está autenticado
    if request.user.is_authenticated:
        return redirect('home')
    # Verificamos si se envió el formulario
    if request.method == 'POST':
        # Creamos el formulario con los datos del POST
        form = UserCreationForm(request.POST)
        # Verificamos si el formulario es válido
        if form.is_valid():
            # Guardamos el formulario
            form.save()
            # Redireccionamos a la página de inicio de sesión
            return redirect('/login_view/')
    else:
        # Creamos el formulario
        form = UserCreationForm()
    # Creamos la respuesta
    return render(request, 'Blog/register.html', {'form': form})
