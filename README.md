# Compare-cpu-with-gpu
## GPU與CPU算力比較程式

## 需求套件
### tensorflow
### matplotlib

## 使用環境
建議使用 **Anaconda** 環境
__https://repo.anaconda.com/archive/Anaconda3-2020.02-Windows-x86_64.exe__

## 操作步驟
確認 顯示卡符合規格
確認網址 __https://developer.nvidia.com/cuda-gpus__
![image](https://github.com/edwardhome/Compare-cpu-with-gpu/blob/master/img/NVIDIA.png)

>下載 CUDA Toolkit

>>Windows 
>>>__http://developer.download.nvidia.com/compute/cuda/11.0.2/local_installers/cuda_11.0.2_451.48_win10.exe__

>>Linux
>>>__https://developer.nvidia.com/cuda-downloads?target_os=Linux__

安裝 tensorflow 如下
``` conda install tensorflow ```

修改 matplotlib 
使用 pip 管理器
`pip uninsatll matplotlib` 移除原有的套件包

再使用
`pip install matplotlib` 安裝最新版本的資料包

`pip show matplotlib ` 確認版本為3.3.0

`python main.py`執行程式

