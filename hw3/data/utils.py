from transformers import BitsAndBytesConfig
import torch


def get_prompt(instruction: str) -> str:
    '''Format the instruction as a prompt for LLM.'''
    return f"翻譯成文言文：\n雅裏惱怒地說： 從前在福山田獵時，你誣陷獵官，現在又說這種話。\n答案：{instruction}"


def get_bnb_config() -> BitsAndBytesConfig:
    return BitsAndBytesConfig(
        # load_in_4bit=True,
        # bnb_4bit_use_double_quant=True,
        # #sequence_len=4096,
        # bnb_4bit_quant_type="nf4",
        # bnb_4bit_compute_dtype=torch.bfloat16,
        load_in_4bit = True,
        bnb_4bit_compute_dtype = torch.bfloat16,
        bnb_4bit_use_double_quant = True,
        bnb_4bit_quant_type = 'nf4'

    )
    pass
