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

user = client.users.create(
    user=User(
        id=str(uuid.uuid4()),
        username="lmazuel",
        password="password",
        email="me@you.com",
    )
)

assert user.username == "lmazuel"

result_item = client.todo_items.create(
    item=TodoItem(
        id=str(uuid.uuid4()),
        title="title",
        created_by=user.id,
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
