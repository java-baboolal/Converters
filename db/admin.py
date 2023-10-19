from django.contrib import admin

from .models import *


class CurbAreaAdmin(admin.ModelAdmin):
    list_display = ('id','name','published_date','last_updated_date','is_active','geometry')

admin.site.register(CurbArea, CurbAreaAdmin)


class PolicyAdmin(admin.ModelAdmin):
    list_display = ('id','data_source_operator_id','created_date','updated_date','is_active','priority')

admin.site.register(Policy, PolicyAdmin)


class PolicyRateAdmin(admin.ModelAdmin):
    list_display = ('id','policy_rule_id','rate','rate_unit','is_active')

admin.site.register(PolicyRate, PolicyRateAdmin)


class PolicyRuleAdmin(admin.ModelAdmin):
    list_display = ('id','policy_id','activity','max_stay','is_active')

admin.site.register(PolicyRule, PolicyRuleAdmin)

class PolicyTimespanAdmin(admin.ModelAdmin):
    list_display = ('id','policy_id','start_date','end_date','is_active','street_side')

admin.site.register(PolicyTimespan, PolicyTimespanAdmin)

