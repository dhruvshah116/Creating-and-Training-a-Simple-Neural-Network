# Creating-and-Training-a-Simple-Neural-Network

![problem set](https://user-images.githubusercontent.com/71009946/125917722-ee218494-8397-41e8-b102-d3d361394dd0.JPG)

A Neural Network with no Hidden Layers is called a Perceptron.

![perceptron](https://user-images.githubusercontent.com/71009946/125916592-d6500de9-c6d9-48da-9b55-3133c9c0b87f.JPG)

Synapses are a connection between input and a Neuron. Each synapse is initialised with a weight. Weights are very important to get accurate output.

To understand what happens in a neuron , we need a little math :
A neuron basically gets an output by doing a weighted sum on the inputs.

We'll use our sigmoid function as the normalizing function to build the basic form of perceptron in python.

![normalising function](https://user-images.githubusercontent.com/71009946/125917691-4268062e-2d0a-44a9-a3cd-7c52f94707d5.JPG)

Some Basic Calculations :

![image](https://user-images.githubusercontent.com/71009946/125918558-c228f1db-32a1-4d2a-8658-526568f2f7ad.png)
![some calculations](https://user-images.githubusercontent.com/71009946/125918655-2d532786-00d2-46e2-b4fe-504893a6b405.JPG)
![some calculations_1](https://user-images.githubusercontent.com/71009946/125918686-db7eb4e1-f030-4a0d-ab2f-214ad9497590.JPG)

The output we get is nowhere close to the actual output , this is because the weights we initialised our synapses with are random numbers , our neural network is yet to be trained.

The Training Process :

![training process](https://user-images.githubusercontent.com/71009946/125919052-30c8c6da-8d1c-488c-a634-3769d6667976.JPG)

Calculating the Error :

![error calculation](https://user-images.githubusercontent.com/71009946/125919243-339a0ca8-3605-477d-8e36-03d8c8b51cf8.JPG)

This whole process is called Back Propagation.

To know by whcih values we need to adjust the weights :

![image](https://user-images.githubusercontent.com/71009946/125926822-0eab4a42-6386-4b63-bf7c-c339c2519671.png)

Now making adjustments to the weights:

![image](https://user-images.githubusercontent.com/71009946/125926908-6c11b12b-ff63-4f27-aaac-222a01c0f4a7.png)

If the output of the neuron is a large positive or negative number ,the weight was pretty heavy, which indicates the neuron was pretty confident in its output.
Since we dont want to mess to mess with the weights that are pretty confident , lets look at the derivative at larger outputs :

![image](https://user-images.githubusercontent.com/71009946/125927559-993d38d1-a5a6-40b8-83d6-48486a6bec5e.png)

As we can see adjustments for larger weights is lesser because the confident in neurons are best left alone.

![image](https://user-images.githubusercontent.com/71009946/125927896-17e941e0-18a0-46cb-8bea-709100c15b13.png)

CODES:
perceptron.py : Takes you through the entire training process.
neural_network.pu : To Test the trained model on new inputs( Our main Utility Program)









