# SmolLM3-3B.axera

> HuggingFaceTB SmolLM3-3B DEMO on Axera.

- 目前支持 `Python` 语言, `C++` 代码在开发中.
- 预编译模型可以从[百度网盘](https://pan.baidu.com/s/13tPQfSHaixXHYKNvnJQE3w?pwd=7a5b)下载.
- 如需自行编译 `LLM Layer` 模型请参考 [模型转换](/model_convert/README.md).

## 支持平台

- [x] AX650N
- [ ] AX630C

## Git Clone

首先使用如下命令 `clone` 本项目, 然后进入 `python` 文件夹:

```bash
$ git clone git@github.com:AXERA-TECH/SmolLM3-3B.axera.git
$ cd SmolLM3-3B.axera/python
```

之后在开发板上下载或安装以下支持库:

- 从 `huggingface` 下载 `SmolLM3-3B` 模型:

    ```bash
    $ git clone https://huggingface.co/HuggingFaceTB/SmolLM3-3B
    ```

- 在开发板上安装配置 `pyaxengine`, [点击跳转下载链接](https://github.com/AXERA-TECH/pyaxengine/releases). 注意板端 `SDK` 最低版本要求:

    - AX650 SDK >= 2.18
    - AX620E SDK >= 3.12
    - 执行 `pip3 install axengine-x.x.x-py3-none-any.whl` 安装

将下载后的预编译模型解压到当前文件夹[🔔可选], 默认文件夹排布如下:

```bash
(npu-dev-env) (npu) ➜  python tree -L 2 .
.
├── infer_axmodel.py
├── infer.py
├── SmolLM3-3B
│   ├── chat_template.jinja
│   ├── config.json
│   ├── generation_config.json
│   ├── model-00001-of-00002.safetensors
│   ├── model-00002-of-00002.safetensors
│   ├── model.safetensors.index.json
│   ├── notebook.ipynb
│   ├── README.md
│   ├── special_tokens_map.json
│   ├── tokenizer_config.json
│   └── tokenizer.json
├── SmolLM3-3B_axmodel
│   ├── model.embed_tokens.weight.npy
│   ├── smollm3_p128_l0_together.axmodel
│   ├── smollm3_p128_l10_together.axmodel
│   ├── smollm3_p128_l11_together.axmodel
│   ├── smollm3_p128_l12_together.axmodel
│   ├── smollm3_p128_l13_together.axmodel
│   ├── smollm3_p128_l14_together.axmodel
│   ├── smollm3_p128_l15_together.axmodel
│   ├── smollm3_p128_l16_together.axmodel
│   ├── smollm3_p128_l17_together.axmodel
│   ├── smollm3_p128_l18_together.axmodel
│   ├── smollm3_p128_l19_together.axmodel
│   ├── smollm3_p128_l1_together.axmodel
│   ├── smollm3_p128_l20_together.axmodel
│   ├── smollm3_p128_l21_together.axmodel
│   ├── smollm3_p128_l22_together.axmodel
│   ├── smollm3_p128_l23_together.axmodel
│   ├── smollm3_p128_l24_together.axmodel
│   ├── smollm3_p128_l25_together.axmodel
│   ├── smollm3_p128_l26_together.axmodel
│   ├── smollm3_p128_l27_together.axmodel
│   ├── smollm3_p128_l28_together.axmodel
│   ├── smollm3_p128_l29_together.axmodel
│   ├── smollm3_p128_l2_together.axmodel
│   ├── smollm3_p128_l30_together.axmodel
│   ├── smollm3_p128_l31_together.axmodel
│   ├── smollm3_p128_l32_together.axmodel
│   ├── smollm3_p128_l33_together.axmodel
│   ├── smollm3_p128_l34_together.axmodel
│   ├── smollm3_p128_l35_together.axmodel
│   ├── smollm3_p128_l3_together.axmodel
│   ├── smollm3_p128_l4_together.axmodel
│   ├── smollm3_p128_l5_together.axmodel
│   ├── smollm3_p128_l6_together.axmodel
│   ├── smollm3_p128_l7_together.axmodel
│   ├── smollm3_p128_l8_together.axmodel
│   ├── smollm3_p128_l9_together.axmodel
│   └── smollm3_post.axmodel
└── utils
    └── infer_func.py
```

## 上板部署

- `AX650N` 的设备已预装 `Ubuntu 22.04`
- 以 `root` 权限登陆 `AX650N` 的板卡设备
- 接入互联网, 确保 `AX650N` 的设备能正常执行 `apt install`, `pip install` 等指令
- 已验证设备: `AX650N DEMO Board`、`爱芯派Pro(AX650N)`

### Python API 运行

#### Requirements

```bash
$ mkdir /opt/site-packages
$ cd python
$ pip3 install -r requirements.txt --prefix=/opt/site-packages
``` 

#### 添加环境变量

将以下两行添加到 `/root/.bashrc`(实际添加的路径需要自行检查)后, 重新连接终端或者执行 `source ~/.bashrc`

```bash
$ export PYTHONPATH=$PYTHONPATH:/opt/site-packages/local/lib/python3.10/dist-packages  
$ export PATH=$PATH:/opt/site-packages/local/bin
``` 

#### 运行

在 `Axera 开发板` 上运行以下命令开启对话功能(包含 think 过程):

```sh
$ cd SmolLM3-3B.axera/python # 注意路径
$ python3 infer_axmodel.py.py
```

```bash
$ python3 infer_axmodel.py -q "帮我求解函数y=3x^2+1的导数." # 默认开启 think
...
Model loaded successfully!
slice_indices: [0, 1, 2]
Slice prefill done: 0
Slice prefill done: 1
Slice prefill done: 2
answer >> <think>
Okay, so I need to find the derivative of the function y = 3x² + 1. Hmm, let me think about how to approach this. I remember that when taking derivatives, we use the^@ power rule. The power rule says that if you have a function like x^n, its derivative is n*x^(n-1). Right? So, for each term in the function, I can apply this rule.

First, let's break down the function into its components. The function is 3x^@² + 1. The first term is 3x², and the second term is 1. The constant term 1 doesn't have an x in it, so when I take the derivative of 1, it should be 0 because the derivative of a constant is zero. That part seems straightforward^@.

Now, the main part is the term 3x². Here, the coefficient is 3, and the exponent is 2. Applying the power rule, the derivative of x² is 2x. But since there's a coefficient 3 in front of the x², I need to multiply^@ the derivative of the function by that coefficient. So, 3 times the derivative of x², which is 2x. That gives me 3*2x = 6x. So the derivative of 3x² is 6x.

Putting it all together, the derivative of the entire function^@ y = 3x² + 1 should be the derivative of 3x² plus the derivative of 1. The derivative of 3x² is 6x, and the derivative of 1 is 0. Therefore, the derivative of the whole function is 6x + 0,^@ which simplifies to 6x.

Wait, let me double-check that. If I have a function like 3x², the derivative is 6x. Let me verify that with the power rule. The power rule states that if you have a function f(x) = ax^n, then f'(^@x) = a*n*x^(n-1). In this case, a is 3 and n is 2. So f'(x) = 3*2*x^(2-1) = 6x. Yes, that's correct. So the derivative of 3x² is indeed ^@6x. And the derivative of the constant 1 is 0. So combining those, the derivative of the entire function is 6x. That seems right.

Is there anything else I need to consider here? Maybe I should check if there are any other terms or if I missed any steps. The original^@ function is a simple polynomial, so there shouldn't be any hidden complexities here. The power rule applies straightforwardly to each term. Since there are no other terms besides the 3x² and the constant, the process is complete.

Another way to think about it is to consider the limit definition of a derivative.^@ If I were to use the limit definition, the derivative of 3x² + 1 would be the limit as h approaches 0 of [ (3(x+h)² + 1) - (3x² + 1) ] / h. Simplifying that expression would lead me through the^@ same steps as before, but since I already applied the power rule, I can be confident that the result is correct.

Therefore, after going through the process step by step, I can be sure that the derivative of y = 3x² + 1 is indeed 6x. There's no mistake^@ in the calculation, and all the steps follow logically from the power rule. So the final answer is 6x.

Just to recap, the key steps were:

1. Identify the function: 3x² + 1.
2. Apply the power rule to each term.
3. For the term^@ 3x², the derivative is 3*2x^(2-1) = 6x.
4. For the term 1, the derivative is 0.
5. Combine the derivatives: 6x + 0 = 6x.

Yes, that all checks out. I^@ think that's thorough enough. I don't see any errors in this reasoning. Therefore, the derivative of the function y = 3x² + 1 is 6x.

**Final Answer**
The derivative of the function \( y = 3x^2 + 1 \) is \(\boxed{6x}\).
</think>
To find the derivative of the function \( y = 3x^2 + 1 \), we can use the power rule of differentiation. The power rule states that if we have a function of the form \( ax^n \), its derivative is \( a \cdot^@ n \cdot x^{n-1} \).

1. **Identify the terms in the function:**
   - The first term is \( 3x^2 \).
   - The second term is \( 1 \).

2. **Apply the power rule to each term:**
  ^@ - For the term \( 3x^2 \):
     - The coefficient \( a \) is 3.
     - The exponent \( n \) is 2.
     - The derivative is \( 3 \cdot 2 \cdot x^{2-1} = 6x \).
^@   - For the term \( 1 \):
     - The derivative of a constant is 0.

3. **Combine the results:**
   - The derivative of \( 3x^2 \) is \( 6x \).
   - The derivative of \( 1 \) is \( ^@0 \).

4. **Final result:**
   - The derivative of the entire function \( 3x^2 + 1 \) is \( 6x + 0 = 6x \).

Thus, the derivative of the function \( y = 3x^2 + 1^@ \) is \( 6x \).

\[
\boxed{6x}
\]
```

指定 `--disable-think` 参数关闭推理时的 `think` 过程:

```bash
$ python3 infer_axmodel.py -q "帮我求解函数y=3x^2+1的导数." --disable-think

Model loaded successfully!
slice_indices: [0]
Slice prefill done: 0
answer >> 要求解函数 \( y = 3x^2 + 1 \) 的导数，我们可以使用导数的基本规则。

函数导数的导数可以通过导数的导数规则来求解。对于多项式^@函数，导数可以通过导数的导数规则来求解。对于函数 \( y = 3x^2 + 1 \)，我们可以逐步求导：

1. **求导函数 \( y = 3x^2 \)**:
   根据导数的导^@数规则，导数规则中对于 \( x^n \) 的导数规则，导数规则为：
   \[
   \frac{d}{dx} (x^n) = n x^{n-1}
   \]
   在这里，\( n = 2^@ \)，所以：
   \[
   \frac{d}{dx} (3x^2) = 3 \cdot \frac{d}{dx} (x^2) = 3 \cdot 2x^{2-1} = 6x
   \]

2. **求^@导数规则中的常数项**:
   对于常数项 \( 1 \)，其导数为零，因为导数规则中常数项的导数为零：
   \[
   \frac{d}{dx} (1) = 0
   \]

将^@以上结果结合起来，我们得到：
\[
\frac{d}{dx} (y) = \frac{d}{dx} (3x^2 + 1) = 6x + 0 = 6x
\]

因此，函数 \( y = 3x^2 +^@ 1 \) 的导数为：
\[
\frac{dy}{dx} = 6x
\]

所以，求解函数 \( y = 3x^2 + 1 \) 的导数，我们得到：
\[
\frac{d}{dx} (3x^^@2 + 1) = 6x
\]

```

#### 文本对话·推理耗时统计

模型共有 `36` 层 `layer`, 具体耗时如下:

Model | Time |
---| ---|
Prefill TTFT | 8287.46 ms |
Decoder | 171.375 ms |

- `Prefill` 阶段, 各个子图耗时如下, 单层最大耗时 `229.84 ms`:

   ```sh
   g1: 11.164 ms
   g2: 14.512 ms
   g3: 18.382 ms
   g4: 22.024 ms
   g5: 25.838 ms
   g6: 29.234 ms
   g7: 32.487 ms
   g8: 36.083 ms
   g9: 40.119 ms
   ```

- `Decoder` 阶段, 每一层的 `llama_layer` 平均耗时 `4.396 ms`.
- `llama_post` 耗时 `13.119 ms`.

模型解码速度为: 1000 / 171.375ms = 5.83 tokens/s.

## 技术讨论

- Github issues
- QQ 群: 139953715
