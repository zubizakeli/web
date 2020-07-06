from django.conf.urls import url

from app1 import views

urlpatterns = [
    url(r'^helloworld/', views.helloworld, name='helloworld'),

    #url(r'^addarticle/', views.addarticle, name='addarticle'),

    url(r'^register/', views.register, name = 'register'),

    url(r'^get_verify_code/', views.get_verify_code, name = 'get_verify_code'),

    url(r'^checkusername/', views.check_username, name = 'check_username'),

    url(r'^login/', views.login, name = 'login'),

    url(r'^home/', views.home, name = 'home'),

    url(r'^logout/', views.logout, name = 'logout'),

    url(r'^addarticle/', views.add_article, name = 'add_article'),

    url(r'^article/(?P<article_id>\d+)', views.show_article, name = 'show_article'),

    url(r'^addlikerelationship/', views.add_like_relationship, name='add_like_relationship'),

    url(r'^recommendarticle/', views.recommend_article, name='recommend_article'),

    url(r'^markarticle/', views.mark_article, name='mark_article'),

    url(r'^addicon/', views.add_icon, name = 'add_icon'),

    url(r'^myblog/', views.my_blog, name = 'my_blog'),

    url(r'^changepassword/', views.change_password, name='change_password'),

    url(r'^changepasswordcheck/', views.change_password_check, name='change_password_check'),

    url(r'^deletearticle/(?P<article_id>\d+)', views.delete_article, name = 'delete_article'),

    url(r'^personalinformation/', views.personal_information, name = 'personal_information'),

    url(r'^blogs/', views.blogs, name = 'blogs'),

    url(r'^adddiscussion/', views.add_discussion, name = 'add_discussion'),

    url(r'^mydiscussion/', views.my_discussion, name='my_discussion'),

    url(r'^show_discussion/(?P<discussion_id>\d+)/', views.show_discussion, name='show_discussion'),

    url(r'^discussions/', views.discussions, name = 'discussions'),

    url(r'^addarticlecomment/(?P<article_id>\d+)/', views.add_article_comment, name = 'add_article_comment'),

    url(r'^deletediscussion/(?P<discussion_id>\d+)/', views.delete_discussion, name = 'delete_discussion'),

    url(r'^recommenddiscussion/', views.recommend_discussion, name='recommend_discussion'),

    url(r'^markdiscussion/', views.mark_discussion, name='mark_discussion'),

    url(r'^adddiscussioncomment/(?P<discussion_id>\d+)/', views.add_discussion_comment, name = 'add_discussion_comment'),

    url(r'^recommenddiscussionresponse/', views.recommend_discussion_response, name = 'recommend_discussion_response'),

    url(r'^explore/', views.explore, name = 'explore'),

    url(r'^mycollectedarticles/', views.my_collected_articles, name = 'my_collected_articles'),

    url(r'^myfans/', views.my_fans, name = 'my_fans'),

    url(r'^myidols/', views.my_idols, name = 'my_idols'),

    url(r'^$', views.index, name='index'),

]
