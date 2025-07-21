from openai import AsyncOpenAI, OpenAI

OPENAI_API_KEY = ""

client = AsyncOpenAI(
    api_key=OPENAI_API_KEY
)

sync_client = OpenAI(
    api_key=OPENAI_API_KEY
)

def llm_call(prompt : str, model : str = "gpt-4o-mini") -> str:
    # LLM을 호출하면 바로 답변을 받으며 받은 답변을 텍스트로 출력
    messages = []
    messages.append({"role":"user","content":prompt})
    chat_completion = sync_client.chat.completions.create(
        model=model,
        messages=messages
    )
    return chat_completion.choices[0].message.content

async def llm_call_async(prompt: str, model : str = "gpt-4o-mini") -> str:
    # 비동기방식이나 병렬처리 등 다양한 함수처리를 동시 다발적으로 하고 싶을 때 활용하기 위해서 만들어둔 함수
    messages = []
    messages.append({"role":"user", "content":prompt})
    chat_completion = await client.chat.completions.create(
        model=model,
        messages=messages
    )
    print(model, "완료")
    return chat_completion.choices[0].message.content

if __name__ == "__main__":
    test = llm_call("안녕")
    print(test)