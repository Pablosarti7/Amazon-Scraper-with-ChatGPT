import openai
from dataframe import CreateDataFrame


class ChatGPT:

    openai.api_key = "API_KEY"
    
    def __init__(self) -> None:
        self.df_instance = CreateDataFrame()
        self.list_str = self.get_books_list()
        self.messages = [
            {"role": "system", "content": "You are a knowledgeable assistant."},
            {"role": "user", "content": f"Here is a list of books:\n{self.list_str}\nPlease tell me the topic of each book on this list."}
        ]
        

    def get_books_list(self):
        book_titles_list = self.df_instance.make_titles_list()
        # create a string with the book titles, each on a new line
        books_list_str = "\n".join(book_titles_list)


        return books_list_str
    

    def get_response(self):
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=self.messages,
        )
        response = completion['choices'][0]['message']['content']
        self.messages.append({"role": "assistant", "content": response})


        return response


    def assistant_response(self):
        self.get_response()
        self.messages.append({"role": "user", "content": 'Thank you. Can you summarize each topic into 2 to 6 words.'})
        
        second_response = self.get_response()
        self.messages.append({"role": "user", "content": 'Please reword each topic using less than 6 words each.'})
        third_response = self.get_response()
        

        return second_response, third_response
        
        