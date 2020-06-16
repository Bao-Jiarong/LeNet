## LeNet Implementation

### LeNet Architecrure
<p></p>
<center>
<img src="img/lenet.png" align="center" width="700" height="300"/>
</center>

image is taken from [source](https://tianhaoo.github.io/2019/05/22/LeNet-5%E8%AF%86%E5%88%AB%E6%89%8B%E5%86%99%E6%95%B0%E5%AD%97/)   

<center>   
<img src="img/1.png" width="700" height="200"/>   
</center>

image is taken from [source](https://neurohive.io/en/popular-networks/vgg16/)   

### Training on MNIST
<p></p>
<center>
<img src="img/mnist.png" width="400" height="350"/>
</center>

### Requirement
```
python==3.7.0
numpy==1.18.1
```
### How to use
Training & Prediction can be run as follows:    
`python train.py train`  
`python train.py predict img.png`  


### More information
* Please refer to the original paper of LeNet [here](http://yann.lecun.com/exdb/publis/pdf/lecun-01a.pdf) for more information.

### Implementation Note
* LeNet used 'relu' as activate function, and MaxPool2D for pooling.
* LeNet_5 used 'tanh' as activate function, and AveragePooling2D for pooling.

### Result for MNIST:   
* Learning rate = 0.001  
* Batch size = 32  
* Optimizer = Adam   

Name |  epochs  | Training Accuracy |  Validation Accuracy  |
:---: | :---: | :---: | :---:
LeNet   | 2  |  96.62% | 96.85%
LeNet_5 | 2 |  96.54% | 96.64%
LeNet   | 10  |  98.28% | 97.69%
LeNet_5 | 10 |  98.82% | 98.30%
