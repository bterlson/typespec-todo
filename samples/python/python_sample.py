import uuid

from corehttp.credentials import ServiceKeyCredential
from todo import TodoClient
from todo.models import TodoItem, TodoUrlAttachment


client = TodoClient(ServiceKeyCredential("token"), endpoint='http://localhost:3000')


result_item = client.todo_items.create_json(
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

# result_item2 = client.todo_items.create_form(
#     item=TodoItem(
#         id=str(uuid.uuid4()),
#         title="title",
#         status="NotStarted",
#         labels=["label1", "label2"],
#     )
# )

assert result_item.title == "title"