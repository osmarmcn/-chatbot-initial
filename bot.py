


import json
from difflib import get_close_matches


def load_knowledge_base(file_path:str) ->dict:
    with open(file_path, 'r') as file:
        data: dict = json.load(file)

    return data

def save_knowledge_base(file_path: str, data:dict):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=2)


def find_best_match(user_question: str, question: list[str]) -> str | None:
    matches : list = get_close_matches(user_question,question,n=1, cutoff=0.6)
    return matches[0] if matches else None
   

def get_answer_for_question(question:str, knowledge_base:dict) -> str| None:
     for q in knowledge_base['question']:
         if q['question'] == question:
             return q['answer']
         


def chat_bot():
    knowledge_base: dict = load_knowledge_base(file_path="knowledge.json")

    while True:
        user_input: str = input('você: ')

        print('para sair digite quit')
        if user_input.lower() == 'quit':
            break

        best_match = find_best_match(user_input, [q['question'] for q in knowledge_base['question']])

        if best_match:
            answer:str = get_answer_for_question(best_match, knowledge_base)
            print(f'bot:{answer}')

        else:
            print(f'bot: eu não sei a resposta, você poderia ensinar?')
            new_answer: str = input("digte sua resposta: \'pular\' para sair: ")


            if new_answer.lower != 'pular':
                knowledge_base['question'].append({'question': user_input,
                                                   'answer': new_answer})
                
                save_knowledge_base('knowledge.json', knowledge_base)
                print('bot: obrigado! aprendi uma nova resposta')


chat_bot()