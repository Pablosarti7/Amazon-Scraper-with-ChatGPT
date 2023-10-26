from chatgpt import ChatGPT
from dataframe import CreateDataFrame
from tkinter import *
import re


chat_gpt = ChatGPT()
response_two, response_three = chat_gpt.assistant_response()

df = chat_gpt.df_instance.df

#### this should be a function ####

# regular expression pattern to match numbered sentences
pattern = re.compile(r'(\d+\..+?)(?=\n\d+\.|\n\n|$)', re.DOTALL)

# use re.findall() to find all occurrences of the pattern
numbered_sentences = re.findall(pattern, response_two)

response_two_list = []
# if you want to print each numbered sentence
for sentence in numbered_sentences:
    response_two_list.append(sentence)


max_length = max(len(response_two_list), len(df))

response_two_list += [None] * (max_length - len(response_two_list))

df['Answer 1'] = response_two_list

#### this should be a function ####

pattern = re.compile(r'(\d+\..+?)(?=\n\d+\.|\n\n|$)', re.DOTALL)

numbered_sentences = re.findall(pattern, response_three)

response_three_list = []
for sentence in numbered_sentences:
    response_three_list.append(sentence)


max_length = max(len(response_three_list), len(df))

response_three_list += [None] * (max_length - len(response_three_list))

df['Answer 2'] = response_three_list

####

to_excel = CreateDataFrame()
to_excel.convert_to_xlsx(df)