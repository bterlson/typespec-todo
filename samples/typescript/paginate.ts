import { TodoItemsList200Response, TodoApplicationClient } from "./lib";

export async function* paginate(client: TodoApplicationClient, initialResponse: TodoItemsList200Response) {
  let currentResponse = initialResponse;

  // Yield items from the initial response first
  for (const item of currentResponse.body.items) {
    yield item;
  }

  // Continue with pagination if there's a nextLink
  while (currentResponse.body.pagination && currentResponse.body.pagination.nextLink) {
    const nextPageResponse = await client.pathUnchecked(currentResponse.body.pagination.nextLink).get();

    if (nextPageResponse.status !== "200" || !isExpectedPageResponse(nextPageResponse)) {
      throw new Error(`Failed to fetch TODO items: status ${nextPageResponse.status}`);
    }

    // Yield items from the current page
    for (const item of nextPageResponse.body.items) {
      yield item;
    }

    currentResponse = nextPageResponse;
  }
}

function isExpectedPageResponse(response: any): response is TodoItemsList200Response {
  return response.status === "200" && response.body && Array.isArray(response.body.items);
}
