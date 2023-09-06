from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import routers, permissions


#  Для Swagger-a
schema_view = get_schema_view(  # new
    openapi.Info(
        title="Moblen API",
        default_version='v1',
        description="""**Сие творение предназначено для упрощения жизни многоуважаемого frontend'а моблена.**
        ----------------------------------------------------------------------------------------------------------------------------------------
        \nПо всем вопросам к *API* вам придется связываться со следующими разработчиками в Telegram:
        🧑‍💻 [Сергей Гузенко](https://t.me/serguzeo)
        🧑‍💻 [Артем Тарасов](https://t.me/tarasovxxx)""",
    ),
    # url=f'{settings.APP_URL}/api/v3/',
    patterns=[
        path('api/', include('auth_and_reg.urls')),
    ],
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    #  Для Swagger-a.  Один для описания схемы в форматах JSON или YAML,
    #  а второй для отображения TemplateView в удобном интерактивном интерфейсе.
    path(  # new
        'swagger-ui/',
        TemplateView.as_view(
            template_name='swaggerui/swaggerui.html',
            extra_context={'schema_url': 'openapi-schema'}
        ),
        name='swagger-ui'),
    re_path(  # new
        r'^swagger(?P<format>\.json|\.yaml)$',
        schema_view.without_ui(cache_timeout=0),
        name='schema-json'),

    path('admin/', admin.site.urls),
    path('', include("mainsite.urls")),

    path('api/', include('auth_and_reg.urls'))
]

