# Efficient-Quantification-of-Parkinson-s-Disease-Severity-Using-Augmented-Time-Series-Data


## Organization of the Repository
```
├── dataset
├── DA_methods
    ├── DA_MagWarp.py
    ├── Jittering.py
    ├── Permutation.py
    ├── Random_Sampling.py
    ├── Rotation.py
    ├── Scaling.py
    ├── Time_Warping.py
    ├── generateLPresidual.m
├── 1D-ConvNet_only.py
├── Transformers_only.py
├── README.md
└── requirements
```

## Getting Started
- Install Matlab
- Install Python dependencies

    ```
    pip install -r requirements.txt
    ```
- Download dataset from [Phisionet](https://physionet.org/content/gaitpdb/1.0.0/) and place it in ```dataset```.
- Run the python script ```DA_methods\*.py``` and ```DA_methods\generateLPresidual.m``` to preprocess the dataset and generate LPresiduals
- View and Run python file with pycharm which can be started with the following command.

    ```
    python 1D-ConvNet_only.py
    ```
        ```
    python Transformers_only.py
    ```
