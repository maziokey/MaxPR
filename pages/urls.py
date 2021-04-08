from django.urls import path

from .views import HomePageView, AboutPageView, ServicesPageView, MarketingPageView, PrcommPageView, BrandmgtPageView, SociallisteningPageView, SocialmediaPageView, InfluencermarketingPageView, ConsumerPageView, ReputationPageView, CrisiscommunicationPageView, MediarelationsPageView, StakeholderrelationsPageView, PRreportingPageView, ContactPageView, basecontactView, successView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('services/', ServicesPageView.as_view(), name='services'),
    path('marketing/', MarketingPageView.as_view(), name='marketing'),
    path('pr_communication/', PrcommPageView.as_view(), name='prcomm'),
    path('brand_management/', BrandmgtPageView.as_view(), name='brandmgt'),
    path('social_listening/', SociallisteningPageView.as_view(), name='sociallistening'),
    path('social_media_management/', SocialmediaPageView.as_view(), name='socialmedia'),
    path('influencer_marketing/', InfluencermarketingPageView.as_view(), name='influencermarketing'),
    path('consumer_audience/', ConsumerPageView.as_view(), name='consumer'),
    path('reputation_management/', ReputationPageView.as_view(), name='repmanagement'),
    path('crisis_communications/', CrisiscommunicationPageView.as_view(), name='crisiscomm'),
    path('media_relations/', MediarelationsPageView.as_view(), name='mediarelations'),
    path('stakeholder_relations/', StakeholderrelationsPageView.as_view(), name='stakeholderrelations'),
    path('pr_reporting/', PRreportingPageView.as_view(), name='prreporting'),
    path('contact/', ContactPageView.as_view(), name='contact'),

    path('basecontact/', basecontactView, name='basecontact'),
    path('success/', successView, name='success'),
]