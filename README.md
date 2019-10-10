<div align="center">

![hng](https://res.cloudinary.com/iambeejayayo/image/upload/v1554240066/brand-logo.png)

<br>

</div>

## :page_with_curl: _About_
- This is a user and article recommendation API built using the database dump from [Lucid](https://lucid.blog)
- There is a limitation on the API being used on Windows due to the fact of the unavailability of [Turicreate](https://github.com/apple/turicreate) on Windows
- The API can be used on Linux, Mac and Windows WSL.
- For those that do not have the above mentioned options, [Docker](https://www.docker.com) procedures are available for building Docker image and running the container

## :page_with_curl: _Installation Guide For Linux, Mac and Windows WSL_

**1)** Fire up your favourite console & clone this repo somewhere:

__`❍ git clone https://github.com/yusuffjamal3/Docker-Recommender-System.git`__

**2)** Enter this directory:

__`❍ cd Docker-Recommender-System`__

**3)** Update pip:

__`❍ python -m pip install --upgrade pip`__

**4)** Install other python packages/dependencies using the requirement file:

__`❍ pip3 install -r requirements.txt`__

**5)** Run the App:

__`❍ python app.py`__

**6)** Open your browser and type in this URL on procedures for running a Recommendation:

__`❍ http://127.0.0.1:5000/`__


## :page_with_curl: _Installation Guide for Docker_

**1)** Fire up your favourite console & clone this repo somewhere:

__`❍ git clone https://github.com/yusuffjamal3/Docker-Recommender-System.git`__

**2)** Enter this directory:

__`❍ cd Docker-Recommender-System`__

**3)** Run Docker compose to build the Image and start the container:

__`❍ docker-compose up`__

**4)** Open your browser and type in this URL on procedures for running a Recommendation:

__`❍ http://127.0.0.1:5000/`__

**5)** Stop the application by running the below command from within your project directory in the second terminal, or by hitting CTRL+C in the original terminal where you started the app:

__`❍ docker-compose down`__

__*Happy developing!*__
