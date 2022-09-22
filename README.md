# code_template


## About  
This is a project developed to create a code template for Machine Learning application development lifecycle. This code template includes folder structure as well as some boilerplate code used for typical ML project to be developed and pushed to production.   

This code template can be used for end to end ML project development as well as deployment.   

The code template considers following phases in ML project development lifecycle:  
Requirement gathering    
Data Collection   
Model Building   
Inference   
Testing     
Deployment   

There are a lot of commercial as well as open source libraries avaialable to achieve this but this project is created to start on your own with simple base code.   

During typical ML project lifecycle,this code template can be used in following way:   
1. Keep all Requirement gathering documents in docs folder.       
2. Keep Data Collection and exploration notebooks  in src/training folder.  
3. Keep datasets in data folder.    
4. Keep model building notebooks at src/training folder.      
5. Keep generated model files at src/models.  
6. Write and keep inference code in src/inference.   
7. Write Logging and configuration code in src/utility.      
8. Write unit test cases in tests folder.<a href="https://docs.pytest.org/en/7.1.x/">pytest</a>,<a href="https://pytest-cov.readthedocs.io/en/latest/readme.html">pytest-cov</a>    
9. Write performance test cases in tests folder.<a href="https://locust.io/">locust</a>     
10. Build docker image.<a href="https://www.docker.com/">Docker</a>  
11. Use and configure code formatter.<a href="https://black.readthedocs.io/en/stable/">black</a>     
12. Use and configure code linter.<a href="https://pylint.pycqa.org/en/latest/">pylint</a>     
13. Add Git Pre-commit hooks.     
14. Use Circle Ci for CI/CD.<a href="https://circleci.com/developer">Circlci</a>    
 
Clone this repo locally and add/update/delete as per your requirement.   
Please note that this template is in no way complete or the best way for your project structure.   
This template is just to get you started quickly with almost all basic phases covered.   

## Project Organization


├── README.md         		<- top-level README for developers using this project.    
├── pyproject.toml         		<- black code formatting configurations.    
├── .dockerignore         		<- Files to be ognored in docker image creation.    
├── .gitignore         		<- Files to be ignored in git check in.    
├── .pre-commit-config.yaml         		<- Things to check before git commit.    
├── .circleci/config.yml         		<- Circleci configurations       
├── .pylintrc         		<- Pylint code linting configurations.    
├── Dockerfile         		<- A file to create docker image.    
├── environment.yml 	    <- stores all the dependencies of this project    
├── main.py 	    <- A main file to run API server.    
├── src                     <- Source code files to be used by project.    
│       ├── inference 	        <- model output generator code   
│       ├── model	        <- model files   
│       ├── training 	        <- model training code  
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
Here we have created ML inference on FastAPI server with dummy model output.

1. Go inside 'Code_Template' folder on command line.  
2. Run:
  ``` 
      conda activate code_template  
      python main.py       
  ```
3. Open 'http://localhost:5000/docs' in a browser.
   
 
### Unit Testing
1. Go inside 'tests' folder on command line.
2. Run:
  ``` 
      pytest -vv 
      pytest --cov-report html:tests/cov_html --cov=src tests/ 
  ```
 
### Performance Testing
1. Go inside 'tests' folder on command line.
2. Run:
  ``` 
      locust -f locust_test.py  
  ```

### Black- Code formatter
1. Go inside 'Code_Template' folder on command line.
2. Run:
  ``` 
      black src 
  ```

### Pylint -  Code Linting
1. Go inside 'Code_Template' folder on command line.
2. Run:
  ``` 
      pylint src  
  ```

### Containerization
1. Go inside 'Code_Template' folder on command line.
2. Run:
  ``` 
      docker build -t myimage .  
      docker run -d -name mycontainer -p 80:80 myimage       
  ```

### Pre-commit hooks
1. Go inside 'Code_Template' folder on command line.
2. Run:
  ``` 
      pre-commit install  
  ```
3. Whenever the command git commit is run, the pre-commit hooks will automatically be applied.

### CI/CD using Circleci
1. Add project on circleci website then monitor build on every commit.


## Contributing
Please create a Pull request for any change. 

## License


NOTE: This software depends on other packages that are licensed under different open source licenses.

