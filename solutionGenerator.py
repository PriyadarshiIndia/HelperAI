from g4f.client import Client

def generate_solution(image_path, option):
    client = Client()

    # Choose the model based on the option
    model = "claude-3-sonnet" if option == "true" else "gpt-4-turbo"

    with open(image_path, "rb") as image_file:
        response = client.chat.completions.create(
            model=model,
            messages=[
                {
                    "role": "user",
                    "content": "Choose the correct option in the given image. Please don't explain; return the correct option as it is."
                }
            ],
            image=image_file
        )
    type(response.choices[0].message.content)
    return response.choices[0].message.content

# Example usage
if __name__ == "__main__":
    result = generate_solution("image.png", "true")
    print(result)
