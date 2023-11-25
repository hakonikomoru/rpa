import openai
import os

# APIキーを設定
openai.api_key = os.environ["OPENAI_API_KEY"]

prompt = "こんにちは、あなたの名前は何ですか？"

# 日本語のGPT-3モデルを初期化
model_engine = "text-davinci-002"
model_engine_ja = "text-davinci-002-ja"
completions = openai.Completion.create(
    engine=model_engine_ja,
    prompt=prompt,
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.5,
)

# 日本語の文章を生成
message = completions.choices[0].text.strip()
print(message)
