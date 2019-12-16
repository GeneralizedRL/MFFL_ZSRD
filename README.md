# MFFL_ZSRD

## Process data
```
main.py --preprocess --data <dataset>
```
Note that <dataset> is the name of any dataset folder in the ./data directory. 
  
The datasets can be downloaded from the original literatures.


## Train models
```
main.py --train --data <dataset> --embmodel <emb_model> --lr 0.003 --gpu <gpu-ID>
```

  
Note that <emb_model> is the base model: distmult and conve.
  

  
## Evaluate models
```
main.py --test --data <dataset> --embmodel <emb_model> --lr 0.003 --gpu <gpu-ID>
```
```
main.py --test_open --data <dataset> --embmodel <emb_model> --lr 0.003 --gpu <gpu-ID>
```
More parameter settings can be found [here](https://github.com/GeneralizedRP/MFFL_ZSRD/blob/master/MFFL-code/args.py) and [here](https://github.com/GeneralizedRP/MFFL_ZSRD/blob/master/MFFL-code/config/config.py).

