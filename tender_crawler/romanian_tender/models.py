from django.db import models

class TenderModel(models.Model):
    """ Django model that describe tender recieved data and 
    how it should look and the database """

    date = models.DateField()
    notice_number = models.CharField(max_length=150, unique=True)
    tender_name = models.CharField(max_length=150)
    procedure_state = models.CharField(max_length=150)
    contract_type = models.CharField(max_length=150)
    procurement_type = models.CharField(max_length=150)
    estimated_value = models.CharField(max_length=150)

    class Meta:
        verbose_name = "e-licitatie romanian tenders"