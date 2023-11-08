from django.urls import path
from . import views_test,views
#여기서 url 매핑
'''연습용
urlpatterns = [
        # path('',admin.site.urls)
        path("",views_test.test_html_data),
        path('test_JS',views_test.test_html_JSdata),
        path("test_multidata",views_test.test_html_multidata),
        path('test_userget',views_test.test_html_userget),
        path('test_pathvalue/<int:my_id>',views_test.test_html_pathvalue),
        path('test_post',views_test.test_post_new),
        path('select_one/<int:my_id>',views_test.test_select_one),
        path('select_all',views_test.test_select_all),
        path('select_all/<str:my_name>',views_test.test_select_filter),
        path('select_filter',views_test.test_select_filter),
        path('test_update',views_test.test_update)
        # path('test_post_form/new',views_test.test_post_new)
]'''

urlpatterns = [
    path('',views.home),
    path('authors/',views.authorls),
    path('authors/new',views.authornew),
    path('author/<int:my_id>',views.author_detail),
    path('author/<int:my_id>/update',views.author_update),
    path('posts/',views.posts),
    path('post/new',views.post_new),
    path('post/<int:my_id>',views.post_detail),
    path('post/<int:my_id>/update',views.post_update)
#     path('posts/',views.postls)

]