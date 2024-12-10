from tinytroupe.agent import TinyPerson
from tinytroupe.environment import TinyWorld
from tinytroupe.factory import TinyPersonFactory
from tinytroupe.extraction import ResultsExtractor

from dotenv import load_dotenv
import json

load_dotenv()
export_path = "./try/outputs/try-01"

# エージェントを作成
factory = TinyPersonFactory("新しい日本の産業を生み出すためのワークショップ")
ai_engineer = factory.generate_person(
  """
  AIエンジニア。機械学習と生成AIを組み合わせて、企業向けのAIツールを開発及び展開している。
  エンドユーザの課題を見つけ出し、AIを活用して解決することに注力している。
  """
)
financial_specialist = factory.generate_person(
  """
  金融のスペシャリスト。銀行業務、投資、資産運用に精通しており、金融市場の動向を常に把握している。
  新しい金融商品やサービスの開発に携わっており、特にテクノロジーを活用した金融イノベーションに関心がある。
  日本の金融業界の発展に貢献することを目指している。
  """
)
automotive_chairman = factory.generate_person(
  """
  自動車業界の会長。自動車産業における豊富な経験と知識を持ち、業界の発展と革新に尽力している。
  新しい技術やサービスの導入を推進し、グローバルな視点で自動車業界の未来を見据えている。
  """
)

ai_engineer.save_spec("./try/brainstorm_auto_traits/ai_engineer.json")
financial_specialist.save_spec("./try/brainstorm_auto_traits/financial_specialist.json")
automotive_chairman.save_spec("./try/brainstorm_auto_traits/automotive_chairman.json")

world = TinyWorld("Meeting Room", [ai_engineer, financial_specialist, automotive_chairman])
world.make_everyone_accessible()

instruct = '''
新しい世界的なサービスを生み出すためのワークショップです。
自由な発想で新たなサービスを考え、議論してください！！！
'''

world.broadcast(instruct)

world.run(10)

# 結果の出力
extractor = ResultsExtractor()

results = extractor.extract_results_from_world(world, extraction_objective="会話の内容を要約してください。重要な議論はより詳細に説明してください。")

print("results: ", results)