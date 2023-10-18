from django.utils import timezone
# from django.db import models
from django.db.models import JSONField
from django.contrib.gis.db import models
from django.contrib.gis.geos import Polygon
# from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
import uuid


class CurbArea(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    # city_id = models.ForeignKey(CityMaster, on_delete=models.CASCADE)
    geometry = models.PolygonField()
    # coordinates = models.CharField(max_length=2048)
    # geometry = models.PolygonField(default = Polygon(((0, 0), (0, 1), (1, 1), (1, 0), (0, 0))))
    name = models.CharField(max_length=255, unique=True, null=False)
    published_date = models.DateTimeField()
    last_updated_date = models.DateTimeField()
    is_active = models.BooleanField(default=False)
    class Meta:
        db_table = 'area'


# class CurbZone(models.Model):
#     id = models.UUIDField(primary_key=True)
#     # city_id = models.ForeignKey(CityMaster, on_delete=models.CASCADE)
#     area_id = models.ForeignKey(CurbArea, on_delete=models.CASCADE)
#     # geometry = models.PolygonField(default = Polygon(((0, 0), (0, 1), (1, 1), (1, 0), (0, 0))))
#     name = models.CharField(max_length=255, null=True, blank=True)
#     user_zone_id = models.CharField(max_length=255, null=True, blank=True)
#     street_name = models.CharField(max_length=255, null=True, blank=True)
#     cross_street_start_name = models.CharField(max_length=255, null=True, blank=True)
#     cross_street_end_name = models.CharField(max_length=255, null=True, blank=True)
#     length = models.IntegerField(null=True, blank=True)
#     available_space_lengths = JSONField(null=True, blank=True)
#     availability_time = models.DateTimeField(null=True, blank=True)
#     width = models.IntegerField(null=True, blank=True)
#     parking_angle = models.CharField(max_length=255, null=True, blank=True)
#     num_spaces = models.IntegerField(null=True, blank=True)
#     street_side = models.CharField(max_length=2, null=True, blank=True)
#     median = models.BooleanField(default=False)
#     entire_roadway = models.BooleanField(default=False)
#     created_datetime = models.DateTimeField()
#     created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_zone')
#     updated_datetime = models.DateTimeField()
#     updated_by =  models.ForeignKey(User, on_delete=models.CASCADE, related_name='updated_zone')
#     is_active = models.BooleanField(default=False)
#     class Meta:
#         db_table = 'zone'



# class CurbSpace(models.Model):
#     id = models.UUIDField(primary_key=True)
#     city_id = models.ForeignKey(CityMaster, on_delete=models.CASCADE)
#     zone_id = models.ForeignKey(CurbZone, on_delete=models.CASCADE)
#     # geometry = models.PolygonField(default = Polygon(((0, 0), (0, 1), (1, 1), (1, 0), (0, 0))))
#     name = models.CharField(max_length=255, null=True, blank=True)
#     space_number = models.IntegerField(null=True, blank=True)
#     length = models.IntegerField()
#     width = models.IntegerField(null=True, blank=True)
#     available = models.BooleanField(default=False)
#     availability_time = models.DateTimeField(null=True, blank=True)
#     created_datetime = models.DateTimeField()
#     created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_space')
#     updated_datetime = models.DateTimeField()
#     updated_by =  models.ForeignKey(User, on_delete=models.CASCADE, related_name='updated_space')
#     is_active = models.BooleanField(default=False)
#     class Meta:
#         db_table = 'curb_space'




# class Policy(models.Model):
#     id = models.UUIDField(primary_key=True)
#     city_id = models.ForeignKey(CityMaster, on_delete=models.CASCADE)
#     priority = models.IntegerField()
#     data_source_operator_id = JSONField(null=True, blank=True)
#     created_datetime = models.DateTimeField()
#     created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_policy')
#     updated_datetime = models.DateTimeField()
#     updated_by =  models.ForeignKey(User, on_delete=models.CASCADE, related_name='updated_policy')
#     is_active = models.BooleanField(default=False)

#     class Meta:
#         db_table = 'policy'


# class ZonePolicy(models.Model):
#     id = models.UUIDField(primary_key=True)
#     city_id = models.ForeignKey(CityMaster, on_delete=models.CASCADE)
#     zone_id = models.ForeignKey(CurbZone, on_delete=models.CASCADE)   
#     policy_id = models.ForeignKey(Policy, on_delete=models.CASCADE)   
#     created_datetime = models.DateTimeField()
#     created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_zone_policy')
#     updated_datetime = models.DateTimeField()
#     updated_by =  models.ForeignKey(User, on_delete=models.CASCADE, related_name='updated_zone_policy')
#     is_active = models.BooleanField(default=False)

#     class Meta:
#         db_table = 'zone_policy'

# class PolicyRule(models.Model):
#     id = models.UUIDField(primary_key=True)
#     city_id = models.ForeignKey(CityMaster, on_delete=models.CASCADE)
#     policy_id = models.ForeignKey(Policy, on_delete=models.CASCADE)   
#     activity = models.CharField(max_length=255)
#     max_stay = models.IntegerField(null=True, blank=True)
#     max_stay_unit = models.CharField(max_length=255, default='minute')
#     no_return = models.IntegerField(default=0)
#     no_return_unit = models.CharField(max_length=255, default='minute')
#     user_classes = JSONField(null=True, blank=True)
#     created_datetime = models.DateTimeField()
#     created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_policy_rule')
#     updated_datetime = models.DateTimeField()
#     updated_by =  models.ForeignKey(User, on_delete=models.CASCADE, related_name='updated_policy_rule')
#     is_active = models.BooleanField(default=False)
#     class Meta:
#         db_table = 'policy_rule'

# class PolicyTimespan(models.Model):
#     id = models.UUIDField(primary_key=True)
#     city_id = models.ForeignKey(CityMaster, on_delete=models.CASCADE)
#     policy_id = models.ForeignKey(Policy, on_delete=models.CASCADE)   
#     start_date = models.DateField()
#     end_date = models.DateField()
#     day_of_week  = JSONField(null=True, blank=True)
#     day_of_month  = JSONField(null=True, blank=True)
#     months  = JSONField(null=True, blank=True)
#     time_of_day_start =  models.CharField(max_length=2, null=True, blank=True)
#     time_of_day_end =  models.CharField(max_length=2, null=True, blank=True)
#     designated_period_except =  models.CharField(max_length=2, null=True, blank=True)
#     designated_period =  models.CharField(max_length=2, null=True, blank=True)
#     created_datetime = models.DateTimeField()
#     created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_policy_timespan')
#     updated_datetime = models.DateTimeField()
#     updated_by =  models.ForeignKey(User, on_delete=models.CASCADE, related_name='updated_policy_timespan')
#     is_active = models.BooleanField(default=False)
#     street_side = models.CharField(max_length=2, null=True, blank=True)

#     class Meta:
#         db_table = 'policy_timespan'




# class PolicyRate(models.Model):
#     id = models.UUIDField(primary_key=True)
#     city_id = models.ForeignKey(CityMaster, on_delete=models.CASCADE)
#     policy_rule_id = models.ForeignKey(PolicyRule, on_delete=models.CASCADE)   
#     rate =  models.IntegerField(null=True, blank=True)
#     rate_unit =  models.CharField(max_length=255)
#     rate_unit_period =  models.CharField(max_length=255)
#     increment_duration =  models.IntegerField(null=True, blank=True)
#     increment_amount =  models.IntegerField(null=True, blank=True)
#     start_duration =  models.IntegerField(null=True, blank=True)
#     end_duration =  models.IntegerField(null=True, blank=True)
#     created_datetime = models.DateTimeField()
#     created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_policy_rate')
#     updated_datetime = models.DateTimeField()
#     updated_by =  models.ForeignKey(User, on_delete=models.CASCADE, related_name='updated_policy_rate')
#     is_active = models.BooleanField(default=False)
#     class Meta:
#         db_table = 'policy_rule_rate'