from django.shortcuts import render, get_object_or_404

from pypro.aperitivos.models import Video

videos = [
    Video(slug='motivacao', titulo='Video Aperitivos: Miles Davis', vimeo_id='578570237'),
    Video(slug='instalacao-windows', titulo='Instalação Windows', vimeo_id='578570237'),
]

videos_dct = {v.slug: v for v in videos}


def indice(request):
    return render(request, 'aperitivos/indice.html', context={'videos': videos})


def video(request, slug):
    video = get_object_or_404(Video, slug=slug)
    return render(request, 'aperitivos/video.html', context={'video': video})
