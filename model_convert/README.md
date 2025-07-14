# 模型转换

首先从 `HuggingFace` 上下载 `SmolLM3-3B` 模型

```bash
$ git clone https://huggingface.co/HuggingFaceTB/SmolLM3-3B
```

然后在 `AXERA` 工具链 `Docker` 环境下编译该模型, 示例命令如下:

```sh
pulsar2 llm_build --input_path SmolLM3-3B --output_path ./SmolLM3-3B_axmodel --hidden_state_type bf16 --prefill_len 128 --kv_cache_len 2559 --last_kv_cache_len 128 --last_kv_cache_len 256 --last_kv_cache_len 384 --last_kv_cache_len 512 --last_kv_cache_len 640 --last_kv_cache_len 768 --last_kv_cache_len 896 --last_kv_cache_len 1024 --chip AX650 -c 1 [--parallel 8]
```

注意, 当编译 `log` 中出现 `build llm model done!` 字样的提示后, 则表示模型编译成功, 后面如果出现 `Error` 可以暂时忽略.

关于 `pulsar2 llm_build` 更详细的文档请参考 [大模型编译(实验阶段)](https://pulsar2-docs.readthedocs.io/zh-cn/latest/appendix/build_llm.html).
