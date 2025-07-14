from transformers import AutoProcessor, AutoModelForImageTextToText
import torch
import onnx
import onnxruntime as ort
import numpy as np
import os
from tqdm import tqdm
from transformers import AutoConfig, AutoTokenizer
from typing import List, Tuple
from axengine import InferenceSession
from ml_dtypes import bfloat16
from utils.infer_func import InferManager
import argparse
from PIL import Image
from torchvision.transforms import Resize, ToTensor, Normalize, Compose
from transformers.image_utils import OPENAI_CLIP_MEAN, OPENAI_CLIP_STD


if __name__ == "__main__":

    prompt = None
    parser = argparse.ArgumentParser(description="Model configuration parameters")
    parser.add_argument("--hf_model", type=str, default="./SmolLM3-3B/",
                        help="Path to HuggingFace model")
    parser.add_argument("--axmodel_path", type=str, default="./SmolLM3-3B_axmodel/",
                        help="Path to save compiled axmodel of llama model")
    parser.add_argument("--vit_model", type=str, default=None,
                        help="Path to save compiled axmodel of llama model")
    parser.add_argument("-i", "--images", type=str, default="../assets/bee.jpg",
                        help="Path to the test image.")
    parser.add_argument("--disable-think", action="store_true", default=False,
                        help="Disable thinking.")
    parser.add_argument("-q", "--question", type=str, default="Give me a brief explanation of gravity in simple terms.",
                        help="Your question that you want to ask the model.")
    args = parser.parse_args()

    hf_model_path = args.hf_model
    axmodel_path = args.axmodel_path
    images = args.images
    prompt = args.question

    device = "cuda" if torch.cuda.is_available() else "cpu"
    embeds = np.load(os.path.join(axmodel_path, "model.embed_tokens.weight.npy"))

    # load the tokenizer and the model
    tokenizer = AutoTokenizer.from_pretrained(hf_model_path)
    cfg = AutoConfig.from_pretrained(hf_model_path, trust_remote_code=True)

    # model = AutoModelForCausalLM.from_pretrained(
    #     hf_model_path,
    # ).to(device)

    # prepare the model input
    if not args.disable_think:
        messages = [
            {"role": "user", "content": prompt}
        ]
    else:
        messages = [
            {"role": "system", "content": "/no_think"},
            {"role": "user", "content": prompt}
        ]

    text = tokenizer.apply_chat_template(
        messages,
        tokenize=False,
        add_generation_prompt=True,
    )
    model_inputs = tokenizer([text], return_tensors="pt").to(device)
    input_ids = model_inputs.input_ids

    token_ids = input_ids[0].cpu().numpy().tolist()
    token_len = len(token_ids)
    prefill_data = np.take(embeds, token_ids, axis=0)
    prefill_data = prefill_data.astype(bfloat16)

    imer = InferManager(cfg, axmodel_path)

    token_ids = imer.prefill(tokenizer, token_ids, prefill_data, slice_len=128)
    imer.decode(tokenizer, token_ids, embeds, slice_len=128)
    print("\n")
