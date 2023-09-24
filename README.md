# Auto Zip for 程設作業
* Auto Zip Script for NTNU Computer Programming Course
* 作者：116 盧昱安

## Overview
* 類似makefile的功能，python 一鍵打包程設作業 to .zip 
* 不需要額外下載其他plugin或是手動 zip [filename] [files] 來打包作業
* 輸入第幾次的作業後會自動從 hw0X01 開始查找所有的 hw0X 作業
* 只是一個 python script

## How to use
* Download the autozip_ntnu.py
* 把檔案放到和作業同一個目錄下後在 terminal輸入
* 再輸入要 auto zip 的作業 No. 就可以了
```linux=
$ python3 ./autozip_ntnu.py
```
## What does it do 
* Auto Zip all hw0x0x, makefile, README(or readme)
* Help you check if hw0x01 ~ hw0x0x 
## Screenshot

![](https://hackmd.io/_uploads/HkeSmn61p.png)
![](https://hackmd.io/_uploads/BkgL72TJT.png)

```
