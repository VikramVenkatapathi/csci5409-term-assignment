## About

The cloud application developed for my term assignment is titled 
**Serverless Image Processing System**. This project aims to provide users with an intuitive and feature-rich platform to analyze
images, detect labels, and analyze face details using Amazon Rekognition. The application leverages
a combination of modern technologies and AWS cloud services to deliver a seamless and efficient user
experience.

## Documentation
The [Documentation](https://github.com/VikramVenkatapathi/csci5409-term-assignment/tree/main/Submission/Report) section contains a detailed description of my project. 

## Demo

🔗Link :  https://drive.google.com/file/d/1zSriZxzGk5e8dBypItgE-zxE3quNaC5q/view?usp=sharing

<!--- 
## Features

#### Login To An Existing Account 🔑

![ LOGIN  GIF](./)

#### Create An Account 🔐

![ SIGN-UP  GIF](./)

 --->
## Architecture

![Architecture](https://github.com/VikramVenkatapathi/csci5409-term-assignment/blob/main/Architecture%20diagram/arch%20diag.drawio%20-v2.png)

## AWS Services

Storage: 
```
    User registration data               : DynamoDB
    Images & prediction results storage  : S3
```

Compute:
```
    Application Hosting     :   EC2
    Image Analysis workflow :   Step-Function 
```

Image Analysis:
```
    Amazon Rekognition (using API to detect labels, celebrities, facial analysis)
```

Notification:
```
    Notify users about detection results: SNS
```


## Tech Stack

**Frontend:** React

**Backend:** Python Flask App (handle user registration, login and image upload)


## Author

- [@vikramv](https://git.cs.dal.ca/vikramv)




