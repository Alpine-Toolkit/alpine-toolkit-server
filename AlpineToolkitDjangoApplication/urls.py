####################################################################################################
#
# Alpine Toolkit - 
# Copyright (C) 2017 Fabrice Salvaire
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
####################################################################################################

####################################################################################################

from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse_lazy
from django.views.generic import TemplateView

from rest_framework import routers

####################################################################################################
#
# Main page
#

# from .views.main import MainView

urlpatterns = [
    # url(r'^$', MainView.as_view(), name='index'),

    url(r'^$',
        TemplateView.as_view(template_name='main.html'),
        name='index'),

    url(r'^about$',
        TemplateView.as_view(template_name='about.html'),
        name='about'),

    url(r'^mentions-legales$',
        TemplateView.as_view(template_name='mentions-legales.html'),
        name='mentions-legales'),
]

####################################################################################################
#
# Authentication
#

import django.contrib.auth.views as auth_views

from .views.account import (
    AuthenticationForm,
    PasswordChangeForm,
    PasswordResetForm,
    SetPasswordForm,
)

from .views import account as account_views

urlpatterns += [
   url(r'^account/login/$',
       auth_views.login,
       {'template_name': 'account/login.html',
        'authentication_form': AuthenticationForm},
       name='account.login'),

    url(r'^account/logout/$',
        auth_views.logout,
        {'template_name': 'account/logged_out.html'},
        name='account.logout'),

    url(r'^account/password/change/$',
        auth_views.password_change,
        {'template_name': 'account/password_change.html',
         'password_change_form': PasswordChangeForm,
         'post_change_redirect': reverse_lazy('account.password_change_done')},
        name='account.password_change'),

    url(r'^account/password/change/done/$',
        account_views.password_change_done,
        name='account.password_change_done'),

    url(r'^account/password/reset/$',
        auth_views.password_reset,
        {'template_name': 'account/password_reset.html',
         'email_template_name': 'account/password_reset_email.html',
         'password_reset_form': PasswordResetForm,
         'post_reset_redirect': reverse_lazy('account.password_reset_done')},
        name='account.password_reset'),

    url(r'^account/password/reset/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/$',
        auth_views.password_reset_confirm,
        {'template_name': 'account/password_reset_confirm.html',
         'set_password_form': SetPasswordForm},
        name='account.password_reset_confirm'),

    url(r'^account/password/reset/complete/$',
        auth_views.password_reset_complete,
        {'template_name': 'account/password_reset_complete.html'},
        name='password_reset_complete'),

    url(r'^account/password/reset/done/$',
        account_views.password_reset_done,
        name='account.password_reset_done'),

    url(r'^account/profile/$',
        account_views.profile,
        name='account.profile'),

    url(r'^account/profile/update/$',
        account_views.update,
        name='account.profile.update'),

    url(r'^account/delete/$',
        account_views.delete,
        name='account.delete'),
]

####################################################################################################
#
# REST
#

from rest_framework.documentation import include_docs_urls
from .views.rest import (DocumentViewSet)
from .views.schema_view import schema_view

router = routers.DefaultRouter()
router.register(r'document', DocumentViewSet)

API_TITLE = 'Alpine Toolkit REST API '
API_DESCRIPTION = ''

urlpatterns += [
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # url(r'^api-docs/', schema_view),
    url(r'^api-docs/', include_docs_urls(title=API_TITLE, description=API_DESCRIPTION))
]
