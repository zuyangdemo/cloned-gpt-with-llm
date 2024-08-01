from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from langchain_openai import ChatOpenAI
import os


def generate_search_result(question, memory, openai_api_key, openai_api_base):
    model = ChatOpenAI(model="gpt-3.5-turbo", openai_api_base=openai_api_base,
                       openai_api_key=openai_api_key)

    chain = ConversationChain(llm=model, memory=memory)

    result = chain.invoke({"input": question})

    return result['response']


# test_memory = ConversationBufferMemory(return_messages=True)
# print(generate_search_result("牛顿定律有哪些？", test_memory, os.getenv("OPENAI_API_KEY")))
# print(generate_search_result("我上一个问题是什么？", test_memory, os.getenv("OPENAI_API_KEY")))
