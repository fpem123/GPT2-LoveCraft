# GPT2 LoveCraft

[![Run on Ainize](https://ainize.ai/images/run_on_ainize_button.svg)](https://ainize.web.app/redirect?git_repo=https://github.com/fpem123/GPT2-LoveCraft)


This project generate Love craft fiction using GPT-2 model.

Fine tuning data: [Kaggle](https://www.kaggle.com/bennijesus/lovecraft-fiction)

### Model information


    Base model: gpt-2 large
    Epoch: 30
    Train runtime: 10307.3488 secs
    Loss: 0.0292



### How to use

    * First, Fill what the base text. This will be base of Love craft fiction.
    * And then, Fill number in length. Text is created as long as "length". I recommend between 100 and 300.
    * If length is so big, generate time will be long.

### Post parameter

    text: The base of Love craft fiction.
    length: The size of generated text.


### Output format

    {"0": generated text}


## * With CLI *

### Input example


    

### Output example




## * With swagger *

API page: [Ainize](https://ainize.ai/fpem123/GPT2-LoveCraft?branch=master)

## * With a Demo *

Demo page: [End-point](https://master-gpt2-love-craft-fpem123.endpoint.ainize.ai/)