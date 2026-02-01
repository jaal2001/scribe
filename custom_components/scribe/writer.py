from homeassistant.core import HomeAssistant
from .utils import replace_non_finite

    def _flush(self):
        # ... (other code)
        def _process_batch(self):
            # ... (other code)  
            if isinstance(x.get('attributes'), dict):
                safe_attrs = replace_non_finite(x['attributes'])
                x['attributes'] = json.dumps(safe_attrs, default=str, allow_nan=False)
            
            if isinstance(x.get('event_data'), dict):
                safe_event = replace_non_finite(x['event_data'])
                x['event_data'] = json.dumps(safe_event, cls=JSONEncoder, allow_nan=False)
            
        # ... (other code)