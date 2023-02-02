from notion_client import Client
from datetime import datetime
import json

with open("./secrets.json", "r") as f:
    secrets = json.load(f)

client = Client(auth=secrets.get("token"))


def check_out(title, start, end):
    client.pages.create(
        parent={
            "database_id": secrets.get("database_id")
            },
        properties={
            'Clock-In Clock-out': {
                'date':{
                        'end': end,
                        'start': start,
                        'time_zone': "Europe/Moscow"
                    },
                'id': 'eB%60j',
                'type': 'date'
            },
            "Name": {"title": [
                {"text": 
                    {"content": f"{title}"}
                }
            ], "type": "title"}
        }
    )