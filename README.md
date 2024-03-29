# COMS4771-Spring-2022-Regression-Competition

Comptetition link - https://www.kaggle.com/competitions/coms4771-spring-2022-regression-competition/leaderboard

| Username | `vt2353` |
| ---      | ---      |
| Rank     | 1/167    |

<p align="center">
  <img src="/reports/standings.png" width="600" height="200" title="Standings">
</p>

##

Large-scale regressor for predicting trip duration for an Uber-esque transportation service.

It uses a deep neural network to regress on features obtained post feature-selection for predicting trip duration in seconds.

The neural network minimizes L1 loss and uses Adam optimizer.

The training phase includes validating the model to find the best epoch based on validation loss.

<p align="center">
  <img src="/reports/loss-curve.png" width="400" height="300" title="Standings">
</p>


## Setup Instructions

### Move into top-level directory
```
cd CS4771-Spring-2022-Regression-Competition
```

### Install environment
```
conda env create -f environment.yml
```

### Activate environment
```
conda activate dnn
```

### Install package
```
pip install -e src/dnn
```
Including the optional -e flag will install package in "editable" mode, meaning that instead of copying the files into your virtual environment, a symlink will be created to the files where they are.

### Run jupyter server
```
jupyter notebook notebooks/
```

You can now use the jupyter kernel `dnn` to run notebooks.
