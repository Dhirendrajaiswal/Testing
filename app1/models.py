from django.db import models
import json
from django.utils import timezone
from datetime import datetime
 
 # Create your models here.

class EmployeeTable(models.Model):
    empid = models.AutoField(db_column='empid', primary_key=True)
    empfirstname = models.CharField(max_length=100, db_column='empfirstname')
    emplastname = models.CharField(max_length=100, db_column='emplastname')
    empdob = models.DateTimeField(db_column='empdob')
    status = models.CharField(max_length=100, db_column='status')

    def __str__(self):
        role_data = {}
        role_data['empid'] = self.empid
        role_data['empfirstname'] = self.empfirstname
        role_data['emplastname'] = self.emplastname
        role_data['empdob'] = str(self.empdob)
        role_data['status'] = self.status

        return json.dumps(role_data)
  
    class Meta:
        db_table = "EMPLOYE_RECORD"

