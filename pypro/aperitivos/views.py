from django.shortcuts import render


def video(request, slug):
    video = {'titulo': 'Video Aperitivos: Miles Davis', 'vimeo_id': 578570237}
    return render(request, 'aperitivos/video.html', context={'video': video})
