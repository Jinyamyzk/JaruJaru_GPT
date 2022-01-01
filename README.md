# JaruJaru GPT
ジャルジャルネタのタネのタイトル『〜奴』を使って、rinnaのGPT2をファインチューニングをしました。

# Requirement
* PyTorch
* Transformer
* pandas
* googleapiclient

 
# Usage
 
ファインチューニングにはhttps://github.com/huggingface/transformers/examples/pytorch/language-modeling/のrun_clm.pyを使います。
 
```bash
git clone https://github.com/huggingface/transformers
python ./transformers/examples/pytorch/language-modeling/run_clm.py \
    --model_name_or_path=rinna/japanese-gpt2-medium \
    --train_file=テキストデータへのパス \
    --validation_file=テキストデータへのパス \
    --do_train \
    --do_eval \
    --num_train_epochs=10 \
    --save_steps=10000 \ # driveの容量が足りなくなるかもなので、保存するstepの間隔は要注意！
    --save_total_limit=3 \
    --per_device_train_batch_size=1 \ # バッチサイズ1で代替14,5GBほどGPUメモリ使います。
    --per_device_eval_batch_size=1 \
    --output_dir=drive/MyDrive/ColabNotebooks/GPT-2/output/ \
    --use_fast_tokenizer=False
    --block_size=512
    --use_fast_tokenizer=False
```

