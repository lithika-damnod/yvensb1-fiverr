# REST FRAMEWORK FOR CAR ADVERTISMENT SERVICE

### API Endpoints

###### SUCCESS EVENTS RETURN `{ success: true } `

- #### API Server Status<br>

  `"/api/"`<br>

  ##### Allowed Methods: [GET]

  <img width="343" alt="image" src="https://user-images.githubusercontent.com/61654812/199179902-a0d0bba7-3baf-46a2-92d2-f96556ed77e9.png">
    <br>

- #### User Options<br>

  `"/api/user/"`<br>

  ##### Allowed Methods: [POST, PUT]

  - ##### POST

    - can be used to **create** new users
    - ###### JSON STRUCTURE

    ```
        {
            "first_name": "value",
            "last_name": "value",
            "age": value,
            "address_no": "value",
            "address_street": "value",
            "address_city": "value",
            "address_country": "value"
        }
    ```

    <br>

  - ##### PUT

    - for **updating** user details
    - user_id is compulsory to be passed in
    - pass in field names that needs to be changed along with the updated value
    - ###### JSON STRUCTURE

    ```
        {
            "user_id": value,
            "first_name": "value",
            "last_name": "value",
            "age": value,
            "address_no": "value",
            "address_street": "value",
            "address_city": "value",
            "address_country": "value"
        }
    ```

    - #### `"/api/user/<id>/"`
    - **_ lists down details for a specific user id _**

      ##### Allowed Methods: [GET]

    - ##### Example: `/api/user/1`
    <img width="597" alt="image" src="https://user-images.githubusercontent.com/61654812/199191205-08fb6298-57ef-4124-9d02-3d7891a50645.png">

<br>

- #### Car Options<br>

  `"/api/car/"`<br>

  ##### Allowed Methods: [GET, POST, PUT, DELETE]

  - ##### GET

    - Lists down **all** the available Cars

      <img width="447" alt="image" src="https://user-images.githubusercontent.com/61654812/199205421-c76ba1b5-b02e-4d39-8ff1-441bd36ac5e6.png">

  - ##### POST

    - for creating **new** car objects
    - ###### JSON STRUCTURE

    ```
        {
            "model": "value",
            "brand": "value",
            "number_plate": "value",
            "user_id": value
        }
    ```

  - ##### PUT

    - for updating created **car** objects
    - user_id is compulsory to be passed in
    - pass in field names that needs to be changed along with the updated value
    - ###### JSON STRUCTURE

    ```
        {
            "car_id": value,
            "model": "value",
            "brand": "value",
            "number_plate": "value",
            "user_id": value
        }
    ```

  - ##### DELETE

    - for deleting existing **car** records
    - pass in only the value of car_id and it'll delete the record
    - ###### JSON STRUCTURE

    ```
        {
            "car_id": value
        }
    ```

    - #### `"/api/car/<id>/"`

      - **_ lists down details for a specific car id _**

      ##### Allowed Methods: [GET]

    - ##### Example: `/api/car/2`
      <img width="386" alt="image" src="https://user-images.githubusercontent.com/61654812/199207370-a4e0c3fb-d674-41b7-89ab-6582e618899c.png">

- #### Ad Options<br>

  `"/api/ad/"`<br>

  ##### Allowed Methods: [GET, POST, PUT, DELETE]

  - ##### GET

    - Lists down **all** the available Ads

      <img width="682" alt="image" src="https://user-images.githubusercontent.com/61654812/199208455-2d78ac0e-a4b3-41dc-90bc-b02f4448f178.png">

  - ##### POST

    - for creating **new** ads
    - ###### JSON STRUCTURE

    ```
        {
          "title": "value",
          "description": "value",
          "price": "value",
          "user_id": value,
          "car_id": value
        }
    ```

  - ##### PUT

    - for updating **Ad** objects
    - ad_id is compulsory to be passed in
    - pass in field names that needs to be changed along with the updated value
    - ###### JSON STRUCTURE

    ```
        {
            "ad_id": value,
            "car_id": value,
            "model": "value",
            "brand": "value",
            "number_plate": "value",
            "user_id": value
        }
    ```

  - ##### DELETE

    - for deleting existing **Ad** records
    - pass in only the value of **ad_id** and it'll delete the record
    - ###### JSON STRUCTURE

    ```
        {
            "ad_id": value
        }
    ```

    - #### `"/api/ad/<id>/"`

      - **_ lists down details for a specific Ad id _**

      ##### Allowed Methods: [GET]

    - ##### Example: `/api/ad/1`
      <img width="667" alt="image" src="https://user-images.githubusercontent.com/61654812/199209428-76910927-9ae0-4a01-ac82-835e40fa8550.png">
