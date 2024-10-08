from .agent import Agent
import json

class Rewriter(Agent):
    def process_input(self, input_data):
        return self.select(input_data)

    
    
    def select(self, input_data):
        sys_prompt = """
        你是一个问题改写器，需要把历史QA和Result整理成一个确定的当前的问题
        """
        
        data = {"improper":"NO","rewritten": "I want to know the email of the man with ID 2."}
        json_string_1 = json.dumps(data)
        data = {"improper":"YES","answer":"mailto:Biden@mmsql.com?subject=EmailSubject\nReplace `EmailSubject` with the subject. This will open the default email client with a blank email addressed to the specified recipient and subject."}
        json_string_2 = json.dumps(data)
        
        usr_prompt = f"""[Instruction] 你需要根据evidence和previous QA及current question提炼出当前系统需要解答的完整问题，如果该问题有任何可能可以通过查询数据库来解答则improper为NO如果无关则YES The output should be in JSON format.
[Requirements] 你需要把整合全部信息整合成一个信息完整的问题使得系统可以仅根据该问题回答。json字段分为improper:""(YES/NO)rewritten:""(rewritten question)
[Previous QA]
Q: Do you know the name of the student with ID 1? A: SELECT name FROM students WHERE id = 1; Result:['Timmy']
Q: ok, how about id 2? A: SELECT name FROM students WHERE id = 1; A: SELECT name FROM students WHERE id = 2; Result:['Biden']
[Current question]
i want to know his email
[Rewritten question]
I want to see the email of the student with ID 2.
[Answer]
{json_string_1}
[Previous QA]
Q: Do you know the name of the student with ID 1? A: SELECT name FROM students WHERE id = 1; Result:['Timmy']
Q: ok, how about id 2? A: SELECT name FROM students WHERE id = 1; A: SELECT name FROM students WHERE id = 2; Result:['Biden']
Q: I want to know his email A: SELECT email FROM students WHERE id = 2; Result:['Biden@mmsql.com']
[Current question]
Make a link for this email
[Direct answer]
```
mailto:Biden@mmsql.com?subject=EmailSubject
```
Replace `EmailSubject` with the subject. This will open the default email client with a blank email addressed to the specified recipient and subject. 
[Answer]
{json_string_2}
Task Solved. 
==========
Here is a new example, please start answering:
[Schema] 
{input_data["db_desc"]}
[Evidence]
{input_data["evidence"]}
[Previous QA]
{input_data["previous_QA"]}
[Current question]
{input_data["question"]}
[Answer]
        """
        llm_ans = self.request_llm(sys_prompt,usr_prompt)

        # print("llm_ans")
        # print(llm_ans)
        
        json_object = self.extract_json_from_string(llm_ans)

        rewritten_output_json = ""

        # print("json_object")
        # print(json_object)

        if json_object:

            # print(json_object)
            
            rewriter_output = {
            "improper": json_object.get('improper', 'NO').upper(),
            "text": json_object.get('answer') or json_object.get('rewritten')
        }
        else:
            print("No valid JSON object found.")
            
        return rewriter_output