import json
from box.get_interface import get_wifi_boxes
WIFI_BOXES_JSON = './www/wifi_boxes.json'

def save_wifi_boxes_json():
    wifi_boxes = get_wifi_boxes()
    with open(WIFI_BOXES_JSON, 'w') as file:
        json.dump(wifi_boxes, file)