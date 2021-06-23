from django.urls import path

from . import views

urlpatterns = [
    path('', views.ComingSoonPageView.as_view(), name='coming_soon'),
    path('home/', views.HomePageView.as_view(), name='home'),
    path('about/', views.AboutPageView.as_view(), name='about'),
    path('services/', views.ServicesPageView.as_view(), name='services'),
    path('marketing/', views.MarketingPageView.as_view(), name='marketing'),
    path('pr_communication/', views.PrcommPageView.as_view(), name='prcomm'),
    path('brand_management/', views.BrandmgtPageView.as_view(), name='brandmgt'),
    path('social_listening/', views.SociallisteningPageView.as_view(), name='sociallistening'),
    path('social_media_management/', views.SocialmediaPageView.as_view(), name='socialmedia'),
    path('influencer_marketing/', views.InfluencermarketingPageView.as_view(), name='influencermarketing'),
    path('consumer_audience/', views.ConsumerPageView.as_view(), name='consumer'),
    path('reputation_management/', views.ReputationPageView.as_view(), name='repmanagement'),
    path('crisis_communications/', views.CrisiscommunicationPageView.as_view(), name='crisiscomm'),
    path('media_relations/', views.MediarelationsPageView.as_view(), name='mediarelations'),
    path('stakeholder_relations/', views.StakeholderrelationsPageView.as_view(), name='stakeholderrelations'),
    path('pr_reporting/', views.PRreportingPageView.as_view(), name='prreporting'),
    path('contact/', views.ContactPageView.as_view(), name='contact'),

    path('basecontact/', views.basecontactView, name='basecontact'),
    path('success/', views.successView, name='success'),
]