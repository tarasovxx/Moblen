from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions


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
        path('api/', include('customers.urls')),
        path('api/', include('courses.urls')),
        path('api/', include('groups.urls')),
        path('api/', include('accounts.urls'))
    ],
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    #  Для Swagger-a.  Два для описания схемы в форматах JSON или YAML,
    #  а третий для отображения TemplateView в удобном интерактивном интерфейсе.
    path(  # new
        'api/swagger/',
        TemplateView.as_view(
            template_name='swaggerui/swaggerui.html',
            extra_context={'schema_url': 'openapi-schema'}
        ),
        name='swagger-ui'),
    path(  # new
        'api/swagger.json',
        schema_view.without_ui(cache_timeout=0),
        name='schema-json'),
    path(  # new
        'api/swagger.yaml',
        schema_view.without_ui(cache_timeout=0),
        name='schema-yaml'),

    path('api/admin/', admin.site.urls),

    #  Регаем все апихи
    path('api/', include('customers.urls')),
    path('api/', include('courses.urls')),
    path('api/', include('groups.urls')),
    path('api/', include('accounts.urls')),
]

