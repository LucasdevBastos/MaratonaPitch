from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.db.models import Count
from .models import Startup, Voto, Comentario

def lista_startups(request):
    startups = Startup.objects.all().annotate(total_votos=Count('votos')).order_by('-total_votos', 'nome')
    return render(request, 'votacao/lista_startups.html', {'startups': startups})

def detalhe_startup(request, pk):
    startup = get_object_or_404(Startup, pk=pk)
    comentarios = startup.comentarios.order_by('-criado_em')
    usuario_votou = False
    if request.user.is_authenticated:
        usuario_votou = Voto.objects.filter(usuario=request.user, startup=startup).exists()
    return render(request, 'votacao/detalhe_startup.html', {
        'startup': startup,
        'comentarios': comentarios,
        'usuario_votou': usuario_votou
    })

@login_required
def votar_startup(request, pk):
    startup = get_object_or_404(Startup, pk=pk)
    if not startup.is_votacao_aberta:
        return redirect('detalhe_startup', pk=pk)

    Voto.objects.get_or_create(usuario=request.user, startup=startup)
    return redirect('detalhe_startup', pk=pk)

@login_required
def comentar_startup(request, pk):
    startup = get_object_or_404(Startup, pk=pk)
    if request.method == 'POST' and startup.is_votacao_aberta:
        texto = request.POST.get('texto')
        if texto:
            Comentario.objects.create(usuario=request.user, startup=startup, texto=texto)
    return redirect('detalhe_startup', pk=pk)


def is_admin(user):
    return user.is_staff or user.is_superuser

@user_passes_test(is_admin)
def dashboard_admin(request):
    # Ranking geral
    ranking = Startup.objects.annotate(
        total_votos=Count('votos')
    ).order_by('-total_votos')

    # Infos extras
    total_votos = Voto.objects.count()
    total_usuarios = request.user.__class__.objects.count()
    total_startups = Startup.objects.count()

    return render(request, 'votacao/dashboard_admin.html', {
        'ranking': ranking,
        'total_votos': total_votos,
        'total_usuarios': total_usuarios,
        'total_startups': total_startups,
    })
