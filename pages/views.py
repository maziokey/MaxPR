from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages

from .forms import ContactForm

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'home.html'

class AboutPageView(TemplateView):
    template_name = 'about.html'

class ServicesPageView(TemplateView):
    template_name = 'services.html'

class MarketingPageView(TemplateView):
    template_name = 'marketing.html'

class PrcommPageView(TemplateView):
    template_name = 'prcomms.html'

class BrandmgtPageView(TemplateView):
    template_name = 'brand_mgt.html'

class SociallisteningPageView(TemplateView):
    template_name = 'social_list.html'

class SocialmediaPageView(TemplateView):
    template_name = 'social_media_mgt.html'

class InfluencermarketingPageView(TemplateView):
    template_name = 'influencer_mkt.html'

class ConsumerPageView(TemplateView):
    template_name = 'consumer_aud.html'

class ReputationPageView(TemplateView):
    template_name = 'rep_mgt.html'

class CrisiscommunicationPageView(TemplateView):
    template_name = 'crisis_comm.html'

class MediarelationsPageView(TemplateView):
    template_name = 'media_rels.html'   

class StakeholderrelationsPageView(TemplateView):
    template_name = 'stakeholder.html' 

class PRreportingPageView(TemplateView):
    template_name = 'pr_rep.html' 

class ContactPageView(TemplateView):
    template_name = 'contact.html' 


def inject_form(request):
    return {'form': ContactForm()}


def basecontactView(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = "Website Inquiry"
            body = {
                'name': form.cleaned_data['name'],
                'email': form.cleaned_data['email'],
                'company': form.cleaned_data['company'],
                'phone': form.cleaned_data['phone'],
                'message': form.cleaned_data['message'],
            }
            message = "\n".join(body.values())

            try:
                send_mail(subject, message, 'maxprng@gmail.com', ['admin@maxprng.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            messages.success(request, 'Message Successfully Sent!')
            return redirect('home')
        messages.warning(request, 'Error. Message was not sent!')
    return render(request, "_base.html", {'form': form})

def successView(request):
    return HttpResponse('Success! Thank you for your message.')