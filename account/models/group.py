from django.db import models

from account.models.base import BaseModel


class Group(BaseModel):
    """
    ArkID Group
    """

    name = models.CharField(max_length=255, blank=False, verbose_name='用户组名')
