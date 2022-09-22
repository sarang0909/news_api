# news_api


## About 
In many use cases we need news articles data for ML model building or for any other purposes.  
There are a lot of commercial as well as open source libraries avaialable to get news data.  
<a href="https://newsapi.org/">Newsapi</a> is one such library. It has many APIs to get news data in different categories,format etc.  
However,currently they don't provide complete news article text,so we've integrated newsapi with another amazing library <a href="https://newspaper.readthedocs.io/en/latest/">newspaper3k</a>.     
This is a project developed to create an api application to access news articles given a query to search for.  

## Basics
Get the news metadata using newsapi library   
Get actual news article text with newspaper3k   
This project can be used as upstream or downstream component in news data analysis application.  


## Project Organization


├── README.md         		<- top-level README for developers using this project.    
├── pyproject.toml         		<- black code formatting configurations.    
├── .dockerignore         		<- Files to be ognored in docker image creation.    
├── .gitignore         		<- Files to be ignored in git check in.    
├── .circleci/config.yml         		<- Circleci configurations       
├── .pylintrc         		<- Pylint code linting configurations.    
├── Dockerfile         		<- A file to create docker image.    
├── environment.yml 	    <- stores all the dependencies of this project    
├── main.py 	    <- A main file to run API server.    
├── src                     <- Source code files to be used by project.    
│       ├── news_api.py 	        <- Code to get news data.    
│       ├── utility	        <- contains utility  and constant modules.   
├── logs                    <- log file path   
├── config                  <- config file path   
├── data              <- datasets files   
├── docs               <- documents from requirement,team collabaroation etc.   
├── tests               <- unit and performancetest cases files.   
│       ├── cov_html 	        <- Unit test cases coverage report    

## Installation
Development Environment used to create this project:  
Operating System: Windows 10 Home  

### Softwares
Anaconda:4.8.5  <a href="https://docs.anaconda.com/anaconda/install/windows/">Anaconda installation</a>   
 

### Python libraries:
Go to location of environment.yml file and run:  
```
conda env create -f environment.yml
```

 

## Usage   
config/app_config.json:
  Get and configure newsapi key from <a href="https://newsapi.org/">Newsapi</a>        
  Configure news sources in news_sources. (Currently we've put only 2 resources reuters,abc-news as they are free.You can try different free or paid resources)   

Then start FastAPI server.

1. Go inside 'news_api' folder on command line.  
2. Run:
  ``` 
      conda activate news_api  
      python main.py       
  ```
3. Open 'http://localhost:5000/docs' in a browser.
4. Pass query and num_articles to get article texts.
5. If you want to explore different apis from newsapi then experiment with src/news_api.py code.
   
 
### Unit Testing
1. Go inside 'tests' folder on command line.
2. Run:
  ``` 
      pytest -vv 
      pytest --cov-report html:tests/cov_html --cov=src tests/ 
  ```
 
### Performance Testing
1. Open 2 terminals and start main application in one terminal  
  ``` 
      python main.py 
  ```

2. In second terminal,Go inside 'tests' folder on command line.
3. Run:
  ``` 
      locust -f locust_test.py  
  ```

### Black- Code formatter
1. Go inside 'news_api' folder on command line.
2. Run:
  ``` 
      black src 
  ```

### Pylint -  Code Linting
1. Go inside 'news_api' folder on command line.
2. Run:
  ``` 
      pylint src  
  ```

### Containerization
1. Go inside 'news_api' folder on command line.
2. Run:
  ``` 
      docker build -t myimage .  
      docker run -d --name mycontainer -p 5000:5000 myimage         
  ```


### CI/CD using Circleci
1. Add project on circleci website then monitor build on every commit.


## Contributing
Please create a Pull request for any change. 

## License


NOTE: This software depends on other packages that are licensed under different open source licenses.

