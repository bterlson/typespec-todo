package com.sample.todo;

import com.generic.core.credential.KeyCredential;
import com.generic.core.models.BinaryData;
import com.todo.TodoClientBuilder;
import com.todo.TodoItemsAttachmentsClient;
import com.todo.TodoItemsClient;
import com.todo.UsersClient;
import com.todo.models.TodoItem;
import com.todo.models.TodoItemPatch;
import com.todo.models.TodoItemPatchStatus;
import com.todo.models.TodoItemStatus;
import com.todo.models.User;
import com.todo.models.UserCreatedResponse;

/**
 * Sample code to demonstrate the use of ToDo APIs by demonstrating a simple
 * scenario of creating a user, creating a
 * todo item, updating the todo item and attaching a receipt to the todo item.
 */
public class TodoSample {
        public static void main(String[] args) {
                // Create a key credential to authenticate the client
                KeyCredential keyCredential = new KeyCredential("todo-api-key");

                // Configure the builder with endpoint and credential
                TodoClientBuilder clientBuilder = new TodoClientBuilder()
                                .endpoint("http://localhost:3000")
                                .credential(keyCredential);

                // Create a user client to manage users
                UsersClient usersClient = clientBuilder.buildUsersClient();

                User user = new User("testuser", "testuser@sample.com", "password");
                UserCreatedResponse userCreatedResponse = usersClient.create(user);

                System.out.println("New user created with id " + userCreatedResponse.getId());

                // Create a TodoItems client to manage todo items
                TodoItemsClient todoItemsClient = clientBuilder.buildTodoItemsClient();
                TodoItem todoItem = new TodoItem("Book an appointment for car maintenance", TodoItemStatus.NOT_STARTED)
                                .setDescription("The car is due for an oil change and tire rotation")
                                .setAssignedTo(user.getId());

                TodoItem createdTodoItem = todoItemsClient.create(todoItem);
                System.out.println("Todo item with id " + createdTodoItem.getId() + " was created at "
                                + createdTodoItem.getCreatedAt() + " by " + createdTodoItem.getCreatedBy());

                // Get a todo item
                TodoItem getTodoItem = todoItemsClient.get(createdTodoItem.getId());
                System.out.println(
                                "Retrieved todo item with title " + getTodoItem.getTitle() + " and status "
                                                + getTodoItem.getStatus());

                // Update a todo item
                todoItemsClient.update(getTodoItem.getId(),
                                new TodoItemPatch().setStatus(TodoItemPatchStatus.COMPLETED));

                // Create a TodoItemsAttachments client to manage attachments of todo items
                TodoItemsAttachmentsClient todoItemsAttachmentsClient = clientBuilder.buildTodoItemsAttachmentsClient();

                BinaryData attachment = BinaryData.fromObject(new Object() {
                        final String description = "Car maintenance receipt";
                        final String url = "https://sample.com/receipts/car-maintenance";
                });

                todoItemsAttachmentsClient.createUrlAttachment(getTodoItem.getId(), attachment);
                System.out.println("Successfully attached the receipt to car maintenance todo item");

        }
}
