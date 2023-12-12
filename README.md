# ScrapNTF
A Python Flask API that utilizes a web scrapper to extract SNTF train schedules from their website.

## Setup
You can either fetch the data using the deployed api link https://scrapntf.onrender.com or run the api locally :
* Install Python through the official link https://www.python.org/downloads/ .
* Instal Pip, usually Pip is automaticlly installed with Python installation.
  You can check if you have Pip by running the command :
  ```
  pip --version
  ```
  If you don't have it you can install it using the command :
  ```
  python get-pip.py
   ```
*  Install all the required modules stored in the ' requirements.text ' file using the command :
    ```
    pip install -r requirements.txt
    ```

## How to use
* Run the server using the command :
  ```
  python api.py
  ```
  You can also run it through the Dockerfile that is available inside the project.
* To get all the stations available, you can send a GET Request to the endpoint :
  ```
  127.0.0.1:5000/getAllStations/
  ```
  <img width="911" alt="333" src="https://github.com/marouanosb/ScrapNTF/assets/40308566/1c83c8d3-1e09-492a-9849-ec4b14473742">


## Examples
