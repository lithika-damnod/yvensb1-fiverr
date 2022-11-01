# REST FRAMEWORK FOR CAR ADVERTISMENT SERVICE

### API Endpoints

###### SUCCESS EVENTS RETURN `{ success: true } `

- #### API Server Status<br>

  `"/api/"`<br>

  ##### Allowed Methods: [GET]

  <img width="343" alt="image" src="https://user-images.githubusercontent.com/61654812/199179902-a0d0bba7-3baf-46a2-92d2-f96556ed77e9.png">
    <br>

- #### User Options<br>

  `"/api/user"`<br>

  ##### Allowed Methods: [POST, PUT]

  - ##### POST

    - can be used to create new users
    - ###### JSON STRUCTURE

    ```
        {
            "first_name": "value",
            "last_name": "value",
            "age": value,
            "address_no": "value",
            "address_street":"value",
            "address_city":"value",
            "address_country":"value"
        }
    ```

    <br>

  - ##### PUT

            - for updating user details
            - user_id is compulsory to be specified
            - pass in field names that needs to be changed along with the updated value
            - ###### JSON STRUCTURE

            ```
                {
                    "user_id": value,
                    "first_name": "updated_value",
                    "last_name": "updated_value",
                    "age": updated_value,
                    "address_no": "updated_value",
                    "address_street":"updated_value",
                    "address_city":"updated_value",
                    "address_country":"updated_value"
                }
            ```

            - #### `"/api/user/<id>"`
              ##### Allowed Methods: [GET]
        - ##### Example: `/api/user/1`
        <img width="597" alt="image" src="https://user-images.githubusercontent.com/61654812/199191205-08fb6298-57ef-4124-9d02-3d7891a50645.png">

    <br>
