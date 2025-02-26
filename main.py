from get_news import download_all_news
from ollama_llm import OllamaLlm
from baidu_api import get_response


download_all_news()

model = OllamaLlm('llama3.1:8b')

for i in range(292):
    file_path = f"news/{i + 1}.txt"
    response1 = model.get_response(file_path)
    response2 = get_response(file_path)
    with open(file_path, 'a', encoding='utf-8') as file:
        file.write("\n----------\n")
        file.write(response1)
        file.write("\n----------\n")
        file.write(response2)
        file.write("\n----------")
    # print(response)
    print(i)
