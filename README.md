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
  
*  Install all the required modules stored in the *requirements.text* file using the command :
    ```
    pip install -r requirements.txt
    ```

## How to use
* Run the server using the command :
  ```
  python api.py
  ```
  You can also run it through the Dockerfile that is available inside the project.
  
* To get all the stations available, you can send a GET Request to the following endpoint :
  ```
  127.0.0.1:5000/getAllStations/
  ```
  <img width="911" alt="333" src="https://github.com/marouanosb/ScrapNTF/assets/40308566/1c83c8d3-1e09-492a-9849-ec4b14473742">
  
  The reponse if in a JSON String format and is as follows :
  ```
  station{
    "id" : id,
    "name" : name
  }
  ```
  
* To get specific schedules between two different stations, you can send a GET Request to the following endpoint :
  ```
  127.0.0.1:5000/getTrains/?departureStation={station1Id}&arrivalStation={station2Id}
  ````
  
  Replace *{station1Id}*  and *{station2Id}* with the station IDs that you can get as a reponse from calling the */getAllStations/* endpoint.
  <img width="910" alt="444" src="https://github.com/marouanosb/ScrapNTF/assets/40308566/50fad5a1-7f2a-4144-8b80-c3e8e509b090">

* If you want to extract all the available schedules (for all the stations) you can send a GET Request to the following endpoint :
  ```
  127.0.0.1:5000/getAllTrains/
  ```
  This will go through all the available stations one by one, and extract all the available train schedules for each station.
  **BE AWARE THAT THIS REQUEST MAY TAKE A LOT OF TIME (COULD TAKE HOURS DEPENDING ON HARDWARE/NETWORK) AND SHOULD BE USED ONCE A DAY AT MAX SINCE THE SCHEDULES GET UPDATED DAILY.**
