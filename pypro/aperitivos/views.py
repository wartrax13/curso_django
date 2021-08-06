from django.urls import reverse

from django.shortcuts import render


class Video:
    def __init__(self, slug, titulo, vimeo_id):
        self.titulo = titulo
        self.slug = slug
        self.vimeo_id = vimeo_id

    def get_absolute_url(self):
        return reverse('aperitivos:video', args=(self.slug,))


videos = [
    Video('motivacao', 'Video Aperitivos: Miles Davis', 578570237),
    Video('instalacao-windows', 'Instalação Windows', 578570237),
]

videos_dct = {v.slug: v for v in videos}


def indice(request):
    return render(request, 'aperitivos/indice.html', context={'videos': videos})


def video(request, slug):
    video = videos_dct[slug]
    return render(request, 'aperitivos/video.html', context={'video': video})
