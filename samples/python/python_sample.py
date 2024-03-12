import uuid
import logging

from corehttp.credentials import ServiceKeyCredential
from todo import TodoClient
from todo.models import TodoItem, TodoUrlAttachment, User

logging.basicConfig(level=logging.DEBUG)


client = TodoClient(
    ServiceKeyCredential("token"),
    endpoint='http://localhost:3000',
)

result_item = client.todo_items.create(
    item=TodoItem(
        id=str(uuid.uuid4()),
        title="title",
        status="NotStarted",
        labels=["label1", "label2"],
    ),
    attachments=[
        TodoUrlAttachment(
            url="https://www.example.org",
            description="example",
        )
    ],
)

assert result_item.title == "title"

print(result_item)
