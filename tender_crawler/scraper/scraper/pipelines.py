# useful for handling different item types with a single interface
from romanian_tender.models import TenderModel
from jsonschema import validate, ValidationError


class TenderPipeline:
    """ Scrapy class that describe how data will be processed  """

    def process_item(self, item, spider):
        """ Validation and transforming into propper format """

        # Template for data, that we will get
        tender_schema = {
            'properties': {
                'date': {'type': 'string'},
                'notice_number': {'type': 'string'},
                'tender_name': {'type': 'string'},
                'procedure_state': {'type': 'string'},
                'contract_type': {'type': 'string'},
                'procurement_type': {'type': 'string'},
                'estimated_value': {'type': 'string'}
            },
            'required': ['date', 'notice_number', 'tender_name', 'procedure_state', 'contract_type', 'procurement_type', 'estimated_value']
        }
        
        # If recieved data will not be valid just return None
        try:
            validate(instance=item, schema=tender_schema)
        except ValidationError as validation_exception:
            print(validation_exception)
            return 
        
        # Actually if data is not in db already - process it and save
        if not TenderModel.objects.filter(notice_number=item['notice_number']).exists():
            if item.get('date'):
                item['date'] = item['date'][:10]

            if item.get('estimated_value'):
                item['estimated_value'] = item['estimated_value'].replace(' RON', '')
            item.save() 
            return item



 

