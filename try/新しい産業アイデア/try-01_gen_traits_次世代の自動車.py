from tinytroupe.agent import TinyPerson
from tinytroupe.environment import TinyWorld
from tinytroupe.factory import TinyPersonFactory
from tinytroupe.extraction import ResultsExtractor

from dotenv import load_dotenv
import json

load_dotenv()
export_path = "./try/outputs/try-01"

# エージェントを手動で作成
agent_economist = TinyPerson("鈴木次郎")
agent_economist.define("occupation", "経済学者")
agent_economist.define("personality_traits", [{"trait": "経済学の専門家。新しい産業を作るためのアイデアを提案します。"}])
agent_ai = TinyPerson("中村雅人")
agent_ai.define("occupation", "AIエンジニア")
agent_ai.define("personality_traits", [{"trait": "AIの技術のスペシャリストです。新技術をもとに新しいサービスを提案することに長けています。"}])
agent_sales = TinyPerson("山田紘一")
agent_sales.define("occupation", "自動車販売")
agent_sales.define("personality_traits", [{"trait": "自動車販売の専門家。自動車の販売に関するアイデアを提案します。自動車を購入し利用するユーザの動向に非常に詳しいです。"}])


world = TinyWorld("Meeting Room", [agent_economist, agent_ai, agent_sales])
world.make_everyone_accessible()

instruct = '''
次世代の自動車サービスについて考えます。
自動車開発、自動車車載サービス、自動車販売において、どのような新しいサービスが提供できるかを考えてください。
自動車にかかわらずユーザの社会にどう貢献できるかという点で、自由な発想で、アイデアを出してください！
'''

world.broadcast(instruct)

world.run(10)

# 結果の出力
extractor = ResultsExtractor()

results = extractor.extract_results_from_world(world, extraction_objective="会話の内容を要約してください。重要な議論はより詳細に説明してください。")

print("results: ", results)