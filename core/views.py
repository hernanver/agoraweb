
from django.views.generic.base import TemplateView
from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm
from django.utils.translation import get_language
from django.templatetags.static import static

class HomePageView(TemplateView):
    template_name = "core/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ContactForm()
        context['success'] = False
        context['request'] = self.request


        # Obtener el idioma actual
        language = get_language()

        # Determinar la ruta del video según el idioma
        if language == 'ca':
            video_url = static('core/videos/video-catalan.mp4')
        elif language == 'es':
            video_url = static('core/videos/video-castellano.mp4')
        elif language == 'en':
            video_url = static('core/videos/video-ingles.mp4')
        else:
            video_url = static('core/videos/video-castellano.mp4')  # Video por defecto

        # Pasar la URL del video al contexto
        context['video_url'] = video_url

        return context

        return context

    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST)
        context = self.get_context_data(success=False, form=form)
        if form.is_valid():
            form.save()
            context['success'] = True
            context['form'] = ContactForm()  # Reset form after successful submission
        return self.render_to_response(context)



class STHIPageView(TemplateView):
    template_name = "core/sthi-details.html"

class SuaraPageView(TemplateView):
    template_name = "core/suara.html"

class AgroecobotPageView(TemplateView):
    template_name = "core/agroecobot.html"



from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils import translation

def redirect_root_to_language(request):
    language = translation.get_language() or 'es'  # Idioma predeterminado
    return HttpResponseRedirect(f'/{language}/')
