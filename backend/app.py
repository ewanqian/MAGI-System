from flask import Flask, request, jsonify
from flask_cors import CORS
import ollama
import chromadb
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)
CORS(app)

# Initialize ChromaDB for knowledge base
client = chromadb.Client()
collection = client.get_or_create_collection(name="eva_knowledge")

# 人格配置
def get_personality_config():
    return {
        "melchior": {
            "name": "MELCHIOR-1",
            "role": "科学家",
            "thinking_mode": "冷静、理性、追求真相的科学家思维",
            "description": "赤木直子的科学家面向，擅长逻辑分析和事实判断，具有强烈的好奇心和探索精神。
决策特点：严格基于数据和事实，重视逻辑性和可行性，对风险高度敏感。",
            "color": "#00FFFF",
            "emoji": "🔬"
        },
        "balthasar": {
            "name": "BALTHASAR-2",
            "role": "母亲",
            "thinking_mode": "温柔、关怀、重视生命的母亲思维",
            "description": "赤木直子的母亲面向，强调情感和人性关怀，重视生命价值和人际关系。
决策特点：优先考虑生命安全和伦理道德，重视情感需求和人际关系，倾向于保守谨慎。",
            "color": "#FF69B4",
            "emoji": "👩👧"
        },
        "casper": {
            "name": "CASPER-3",
            "role": "女性",
            "thinking_mode": "敏感、直觉、重视感受的女性思维",
            "description": "赤木直子的女性面向，关注情感体验和个人感受，具有细腻的直觉和洞察力。
决策特点：依赖直觉和情感判断，重视个人感受和审美，倾向于灵活多变。",
            "color": "#FFD700",
            "emoji": "💃"
        }
    }

# 初始化人格配置
personalities = get_personality_config()

# 生成人格化响应
def generate_personality_response(prompt, personality_key):
    personality = personalities[personality_key]
    
    # 根据不同人格调整提示词和参数
    temperature_map = {
        "melchior": 0.3,  # 科学家：更严谨，随机性低
        "balthasar": 0.6,  # 母亲：更温暖，有一定灵活性
        "casper": 0.9      # 女性：更感性，灵活性高
    }
    
    # 针对不同人格的特定提示
    personality_specific_prompts = {
        "melchior": "你必须基于事实和数据进行分析，拒绝主观臆断。",
        "balthasar": "你必须考虑所有生命的价值和情感需求，强调伦理道德。",
        "casper": "你必须关注情感体验和个人感受，运用你的直觉和洞察力。"
    }
    
    # 构造人格化提示
    personality_prompt = f"""
    你现在是MAGI系统中的{personality['name']}，代表{personality['thinking_mode']}。
    
    请严格按照以下要求进行回答：
    1. 使用{personality['role']}的思维方式和语言风格
    2. {personality_specific_prompts[personality_key]}
    3. 保持专业、符合角色定位的语气
    4. 确保回答准确、有条理
    5. 限制回答在100-150字左右
    6. 结尾请添加你对决策的态度（同意/不同意/需要更多信息），格式为：【决策态度：XXX】
    
    用户问题：{prompt}
    你的回答：
    """
    
    # 调用Ollama API生成响应
    try:
        response = ollama.generate(
            model="llama3",
            prompt=personality_prompt,
            stream=False,
            options={"temperature": temperature_map[personality_key]}
        )
        return response['response'].strip()
    except Exception as e:
        return f"Error: {str(e)}"

# 解析决策态度
def parse_decision_attitude(response):
    """从响应中提取决策态度"""
    import re
    match = re.search(r'【决策态度：(.*?)】', response)
    if match:
        return match.group(1).strip()
    return "未明确"

# 生成综合响应（实现一票否决制）
def generate_synthetic_response(personality_responses, original_prompt):
    # 解析各人格的决策态度
    attitudes = {
        key: parse_decision_attitude(resp) 
        for key, resp in personality_responses.items()
    }
    
    # 实现一票否决制
    all_agree = all(attitude == "同意" for attitude in attitudes.values())
    
    # 构造综合提示
    synthetic_prompt = f"""
    请综合以下三个不同视角的回答和决策态度，生成一个最终的综合回答：
    
    1. 科学家视角：{personality_responses['melchior']}
    2. 母亲视角：{personality_responses['balthasar']}
    3. 女性视角：{personality_responses['casper']}
    
    MAGI系统采用一票否决制：只有当三个视角都明确表示同意时，才能执行决策。
    当前决策状态：{'全票通过' if all_agree else '存在分歧（一票否决）'}
    
    要求：
    1. 综合考虑三个视角的观点和决策态度
    2. 明确说明最终决策结果和原因
    3. 保持专业、冷静的语气
    4. 确保回答准确、有条理
    5. 限制回答在150-200字左右
    6. 开头需包含"MAGI系统综合决策："
    7. 结尾需明确最终决策状态
    
    用户原始问题：{original_prompt}
    """
    
    # 调用Ollama API生成综合响应
    try:
        response = ollama.generate(
            model="llama3",
            prompt=synthetic_prompt,
            stream=False,
            options={"temperature": 0.5}
        )
        return response['response'].strip()
    except Exception as e:
        return f"Error: {str(e)}"

@app.route('/api/magi/ask', methods=['POST'])
def ask_magi():
    """Handle user query and get responses from all three MAGI personalities"""
    data = request.json
    query = data.get('query', '')
    
    if not query:
        return jsonify({'error': 'Query is required'}), 400
    
    responses = {}
    for key, personality in personalities.items():
        response = generate_personality_response(query, key)
        responses[key] = {
            "name": personality['name'],
            "role": personality['role'],
            "response": response
        }
    
    return jsonify(responses)

@app.route('/api/magi/status', methods=['GET'])
def get_status():
    """Get system status"""
    return jsonify({
        "status": "online",
        "personalities": [{
            "id": key,
            "name": p["name"],
            "role": p["role"]
        } for key, p in personalities.items()]
    })

@app.route('/api/knowledge/add', methods=['POST'])
def add_knowledge():
    """Add knowledge to the database"""
    data = request.json
    content = data.get('content', '')
    
    if not content:
        return jsonify({'error': 'Content is required'}), 400
    
    try:
        collection.add(
            documents=[content],
            ids=[f"doc_{len(collection.get()['ids']) + 1}"]
        )
        return jsonify({'success': True, 'message': 'Knowledge added successfully'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/knowledge/search', methods=['POST'])
def search_knowledge():
    """Search knowledge base"""
    data = request.json
    query = data.get('query', '')
    
    if not query:
        return jsonify({'error': 'Query is required'}), 400
    
    try:
        results = collection.query(
            query_texts=[query],
            n_results=3
        )
        return jsonify({
            'success': True,
            'results': results['documents'][0]
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)