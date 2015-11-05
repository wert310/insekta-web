from django.contrib import admin

from insekta.scenarios.models import Scenario, ScenarioGroup, Task


admin.site.register(Scenario)
admin.site.register(ScenarioGroup)
admin.site.register(Task)
