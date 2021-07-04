
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<p align="center">

  <h2 align="center">Activity-Analyzer-with-Wearable</h2>

  <p align="center">
    Create an ELT system to classify a person’s activities by analyzing the data collected by wearable devices.
    <br />
    <a href="https://github.com/angelxd84130/Activity-Analyzer-with-Wearable/blob/master/NewsClassification_Demo.pdf">View Demo</a>
    ·
    <a href="https://github.com/angelxd84130/Activity-Analyzer-with-Wearable/issues">Report Bug</a>
    ·
    <a href="https://github.com/angelxd84130/Activity-Analyzer-with-Wearable/issues">Request Feature</a>
  </p>
</p>



<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#data-mining">Feature Engineering</a></li>
        <li><a href="#data-preprocessing">Data Modeling</a></li>
        <li><a href="#data-modeling">Data Processing</a></li>
        <li><a href="#evaluation">Evaluation</a></li>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project
  
Download data from the website of the Huawei Challenge and upload it to related database AWS Aurora to create an environment where big data is stored in the cloud service. 
Realize the concept of ELT(Extraction, Loading, Transformation), use SQL to load the required data from the cloud and use machine learning algorithms to classify a person's activities. 
The calculated machine model can be used on wearable devices or mobile phones to classify people's activities, and even plan people's travel speed and trajectory, which can be used in sports bracelets, maps, and anti-lost tools.

Here's why:
* Real-world data is very complicated and needs to be handled carefully
* The ELT method is more conducive to future big data processing
* The results of machine training can be applied to a wider range of content and products

### Feature Engineering  
In the dataset, it stores a record of a person carrying 4 sensors on his body's hand, hip, backpack, and torso and performing eight activities: still, 
walking, run, bike, bus, car, train, and subway. Indeed, each sensor records the person's continuous activity amplitude vectors (x,y,z). 
x represents the forward/backward shock amplitude of the body, y represents the left/right amplitude of the body, z Indicates the amplitude of body jumping/squatting movements.   

![Sensors][product-screenshot2]

After observation, it is found that each sensor contains a variety of calculation methods for vibration amplitude. 
Among them, the three methods of Acceleration, Gyroscope, and Magnetyometer store the most complete and stable data. 
Therefore, the next experiment will focus on analyzing the data of these three methods.  

### Data Modeling  
The identification method of the eight activities is the most important theme of this experiment. 
After detailed discussions, we believe that using the amplitude of xyz during the activity is the best way to judge the activity the user is doing.   
The xyz amplitude generated by the user during each activity should be within a reference range, 
such as the amplitude of human walking in a straight(x) per second, the amplitude of riding a bicycle in a straight(x), to left and right(y), and to the up and down(z) shaking.  

![Sensors][product-screenshot3]
  
Considering that the xyz amplitude of each activity is within a certain range, the decision tree is our priority algorithm that can help us calculate the scope of the activity and do classification effectively. 

### Data Processing  
Considering that the amount of data for each activity is different, we must unify the number of examples for each activity to maintain the balance of training, 
so we extracted 160,000 examples for each activity in the data set.  
(130,000 examples for training & 30,000 examples for testing)  

![DataDistribution][product-screenshot0]
  
First, the data extracted from the four parts of the body are combined according to time, 
and then the features needed for the next step of machine learning are extracted. Each part only refers to 9 features, 
a total of four body parts, so the training set will contain a total of 4x9+1(time) features.  

![DataDescription][product-screenshot1]
  
Next, consider the modeling method of the decision tree algorithm that the tree structure will expand the branches when encountering new exceptions, randomly disrupting the time-continuous activity examples can balance the tree structure and prevent overfitting problems.  

### Data Training & Testing  
Use 1,040,000(81.25%) examples as training data and 240,000(18.75%) examples as testing data.  
Use the built-in decision tree algorithm of the scikit-learn library for training and testing, the final result shows that the accuracy is up to 71.61%.  


### Evaluation


  

### Built With


* [scikit-learn](https://scikit-learn.org/stable/#)
* [matplotlib](https://matplotlib.org/)



<!-- GETTING STARTED -->
## Getting Started



### Prerequisites


1. Download the dataset from Huawei Challenge Website [Huawei]()
2. Data Processing
   - Deal with missing data
   - Combine data of 4 sensors come from the user's body
3. Data Modeling
   - Decision Tree
   - Random Froest (imporve)
4. Check the plot to see predict results
   - Accuracies
   - Confusion Matrix



<!-- USAGE EXAMPLES -->
## Usage

Use the plots to check result.  
### Data 

 
 
 
### Accuracy
  
 

### confused matrix 
  

or copy an article content and apply it on the model to make predition.



<!-- ROADMAP -->
## Roadmap

See the [open issues](https://github.com/othneildrew/Best-README-Template/issues) for a list of proposed features (and known issues).


<!-- CONTACT -->
## Contact

Yu-Chieh Wang - [LinkedIn](https://www.linkedin.com/in/yu-chieh-wang/)  
email: angelxd84130@gmail.com


<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements
* [Multi-Class Text Classification with Scikit-Learn](https://towardsdatascience.com/multi-class-text-classification-with-scikit-learn-12f1e60e0a9f)
* [Text Classification Using Naive Bayes: Theory & A Working Example](https://towardsdatascience.com/text-classification-using-naive-bayes-theory-a-working-example-2ef4b7eb7d5a)





<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/angelxd84130/Activity-Analyzer-with-Wearable.svg?style=for-the-badge
[contributors-url]: https://github.com/angelxd84130/Activity-Analyzer-with-Wearable/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/angelxd84130/Activity-Analyzer-with-Wearable.svg?style=for-the-badge
[forks-url]: https://github.com/angelxd84130/Activity-Analyzer-with-Wearable/network/members
[stars-shield]: https://img.shields.io/github/stars/angelxd84130/Activity-Analyzer-with-Wearable.svg?style=for-the-badge
[stars-url]: https://github.com/angelxd84130/Activity-Analyzer-with-Wearable/stargazers
[issues-shield]: https://img.shields.io/github/issues/angelxd84130/Activity-Analyzer-with-Wearable.svg?style=for-the-badge
[issues-url]: https://github.com/angelxd84130/Activity-Analyzer-with-Wearable/issues
[license-shield]: https://img.shields.io/github/license/angelxd84130/Activity-Analyzer-with-Wearable.svg?style=for-the-badge
[license-url]: https://github.com/angelxd84130/Activity-Analyzer-with-Wearable/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/yu-chieh-wang/
[product-screenshot0]: data/DataDistribution.png
[product-screenshot1]: data/DataDescription.png
[product-screenshot2]: data/Sensors.png
[product-screenshot3]: data/Sensor.png
[product-screenshot4]: data/Sensor.png
[product-screenshot5]: data/Sensor.png

