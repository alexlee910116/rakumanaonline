from django.urls import path, include, re_path
from django.views.decorators.csrf import csrf_exempt
from django.views.static import serve

import xadmin

from apps.users.views import LoginView, LogoutView, SendSmsView, DynamicLoginView, RegisterView
from mxonline.settings import MEDIA_ROOT
from operations.views import IndexView

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('xadmin/', xadmin.site.urls),
    path('', IndexView.as_view(), name="index"),
    path('login/', LoginView.as_view(), name="login"),
    path('register/', RegisterView.as_view(), name="register"),
    path('d_login/', DynamicLoginView.as_view(), name="d_login"),
    path('logout/', LogoutView.as_view(), name="logout"),
    re_path(r'^captcha/', include('captcha.urls')),
    re_path(r'^send_sms/', csrf_exempt(SendSmsView.as_view()), name='send_sms'),
    # 配置上传文件的访问URL
    re_path(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),
    # re_path(r'^static/(?P<path>.*)$', serve, {"document_root": STATIC_ROOT}),

    # 机构相关页面
    re_path(r'^org/', include(('apps.organizations.urls', "organizations"), namespace="org")),

    # 课程相关页面
    re_path(r'^course/', include(('apps.courses.urls', "courses"), namespace="course")),

    # 用户相关操作页面
    re_path(r'^op/', include(('apps.operations.urls', "operations"), namespace="op")),

    # 个人中心
    re_path(r'^users/', include(('apps.users.urls', "users"), namespace="users")),
]
