from transformers import AutoModelForCausalLM, AutoTokenizer

model_name = "./SmolLM3-3B"
device = "cuda"  # for GPU usage or "cpu" for CPU usage

# load the tokenizer and the model
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(
            model_name,
            ).to(device)

# prepare the model input
# prompt = "Give me a brief explanation of gravity in simple terms."
prompt = "用简单的术语给我一个关于重力的简短解释."

messages_think = [
            {"role": "user", "content": prompt}
            ]

text = tokenizer.apply_chat_template(
            messages_think,
                tokenize=False,
                    add_generation_prompt=True,
                    )
model_inputs = tokenizer([text], return_tensors="pt").to(model.device)

# Generate the output
generated_ids = model.generate(**model_inputs, max_new_tokens=32768)

# Get and decode the output
output_ids = generated_ids[0][len(model_inputs.input_ids[0]) :]
print(tokenizer.decode(output_ids, skip_special_tokens=True))





