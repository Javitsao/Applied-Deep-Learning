from transformers import BitsAndBytesConfig
import torch


# def get_prompt(instruction: str) -> str:
#     '''Format the instruction as a prompt for LLM.'''
#     return f"文言文翻譯：\n{instruction}\n答案："
# def get_prompt(instruction: str) -> str:
#     '''Format the instruction as a prompt for LLM.'''
#     return f"文言文翻譯：\n{instruction}\n答案："

# def get_prompt(instruction: str) -> str:
#     '''Format the instruction as a prompt for LLM.'''
#     return f"你是人工智慧助理，以下是用戶和人工智能助理之間的對話。你要對用戶的問題提供有用、安全、詳細和禮貌的回答。 USER: 沒過十天，鮑泉果然被拘捕。\n幫我把這句話翻譯成文言文。 ASSISTANT: 後未旬，果見囚執。 USER: 辛未，命吳堅為左丞相兼樞密使，常楙參知政事。\n把這句話翻譯成現代文。 ASSISTANT: 初五，命令吳堅為左承相兼樞密使，常增為參知政事。 USER: 文言文翻譯：\n明日，趙用賢疏入。 ASSISTANT: 答案：第二天，趙用賢的疏奏上。 USER: {instruction} ASSISTANT:"

# def get_prompt(instruction: str) -> str:
#     '''Format the instruction as a prompt for LLM.'''
#     return f"你是人工智慧助理，以下是用戶和人工智能助理之間的對話。你要對用戶的問題提供有用、安全、詳細和禮貌的回答。範例一: 翻譯成現代文：\n唐子謂尊師曰： 本入山為求長生，今反為虎狼之餐。\n回答: 唐臣對薛尊師說： 本來入山是為瞭尋求長生不死的，現在反倒成為虎狼之食瞭\n 範例二:父母很害怕，請薛二娘來治療。\n把這句話翻譯成文言文：\n回答:父母患之，迎薛巫以辨之。USER: {instruction} ASSISTANT:"

def get_prompt(instruction: str) -> str:
    '''Format the instruction as a prompt for LLM.'''
    return f"你是人工智慧助理，以下是用戶和人工智能助理之間的對話。你要對用戶的問題提供有用、安全、詳細和禮貌的回答。USER: {instruction} ASSISTANT:"

def get_bnb_config() -> BitsAndBytesConfig:
    return BitsAndBytesConfig(
        # load_in_4bit=True,
        # bnb_4bit_use_double_quant=True,
        # sequence_len=4096,
        # bnb_4bit_quant_type="nf4",
        # bnb_4bit_compute_dtype=torch.bfloat16,
        load_in_4bit = True,
        bnb_4bit_compute_dtype = torch.bfloat16,
        bnb_4bit_use_double_quant = True,
        bnb_4bit_quant_type = 'nf4'

    )
    pass
