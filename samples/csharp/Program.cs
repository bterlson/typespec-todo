﻿using System.ClientModel;
using Todo;
using Todo.Models;

TodoClient client = new TodoClient(new Uri("http://localhost:3000"), new KeyCredential("token"), new TodoClientOptions());
TodoItems itemsClient = client.GetItemsClient();

Result<TodoItem> result = await itemsClient.CreateAsync(
    item: new TodoItem("title", TodoItemStatus.NotStarted)
    {
        Labels = BinaryData.FromObjectAsJson(new string[] { "label1", "label2" })
    }
);

if (result.Value != null)
{
    Console.WriteLine($"Created item with id: {result.Value.Id}");
}