import mimetypes
from pathlib import Path

from django.contrib import admin
from django.http import FileResponse, Http404, HttpResponseNotFound
from django.urls import include, path, re_path

DIST_DIR = Path(__file__).resolve().parent.parent.parent / 'school-dashboard' / 'dist'


def serve_asset(request, filename):
    asset = DIST_DIR / 'assets' / filename
    if not asset.exists():
        raise Http404
    mime, _ = mimetypes.guess_type(str(asset))
    return FileResponse(open(asset, 'rb'), content_type=mime or 'application/octet-stream')


def serve_react(request, *args, **kwargs):
    index = DIST_DIR / 'index.html'
    if index.exists():
        return FileResponse(open(index, 'rb'), content_type='text/html')
    return HttpResponseNotFound('React build not found. Run: npm run build inside school-dashboard/')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('school.urls')),
    path('api-auth/', include('rest_framework.urls')),
    re_path(r'^assets/(?P<filename>.+)$', serve_asset),
    re_path(r'^(?!api/|admin/|api-auth/|assets/).*$', serve_react),
]
