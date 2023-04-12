## Creating a Phonebook with MongoDB

Welcome to the phonebook application readme! This application is designed to showcase how you can easily build your own phonebook using MongoDB with Python. The purpose of this document is to guide you through the setup process so that you can quickly get started with using the application.

Before we begin, please ensure that you have access to a MongoDB instance. In this example, I have used the FreeTier option available on https://cloud.mongodb.com/. However, you can use any MongoDB instance that is accessible to you.

To get started, follow these steps:

Clone the repository to your local machine
Install the required dependencies by running pip install -r requirements.txt
Set up a .env file with the necessary environment variables for connecting to your MongoDB instance (e.g. MONGODB_URI, PORT, etc.)
Start the application by running python app.py


### Step-1:
Cluster0 is created on cloud.mongodb

<img width="1490" alt="image" src="https://user-images.githubusercontent.com/36086368/231450127-bb2b20a5-adbd-4ddb-8aaa-5bccc42fbf6e.png">


### Step-2
Created test database and phonebook collection

<img width="1313" alt="image" src="https://user-images.githubusercontent.com/36086368/231450738-bfe6f3db-3bf1-4331-88fd-c3e66cdf791e.png">



### Step-3
Inserted some initial documents

<img width="1302" alt="image" src="https://user-images.githubusercontent.com/36086368/231450891-d5392ab1-5c38-4d17-b682-0f51f39cde99.png">



### Step-4:

#### add_record() method

```sh
In [16]: new_record_1={'name': 'Utku Haydaroglu','phone': '6666-94134', 'email': 'utku@gmail.com', 'address': 'there, Turkiye'}

In [17]: phonebook.add_record(new_record_1)

In [18]: new_record_2={'name': 'Melih Teke','phone': '6666-94134', 'email': 'melihteke@melihteke.com', 'address': 'Somewhere, Turkiye'}

In [19]: phonebook.add_record(new_record_2)

In [20]: new_record_3={'name': 'Haydar Haydaroglu','phone': '555-313131', 'email': 'haydar@gmail.com'}

In [21]: phonebook.add_record(new_record_3)

```


```sh

#### view_all_records method:

In [15]: phonebook.view_all_records()
Out[15]: 
[{'_id': ObjectId('64368cf4da9a26534d27f6a9'),
  'name': 'John Doe',
  'phone': '555-1234',
  'email': 'johndoe@example.com',
  'address': '123 Main St, Anytown, USA'},
 {'_id': ObjectId('64368d30da9a26534d27f6ab'),
  'name': 'Jane Smith',
  'phone': '555-5678',
  'email': 'janesmith@example.com',
  'address': '456 Elm St, Anytown, USA'},
 {'_id': ObjectId('64368d44da9a26534d27f6ac'),
  'name': 'Bob Johnson',
  'phone': '555-9012',
  'email': 'bobjohnson@example.com',
  'address': '789 Oak St, Anytown, USA'},
 {'_id': ObjectId('64368d90da9a26534d27f6ad'),
  'name': 'Melih Teke',
  'phone': '6666-94134',
  'email': 'melihteke@melihteke.com',
  'address': 'Somewhere, Turkiye'},
 {'_id': ObjectId('6436901b9f17289deb29a7e8'),
  'name': 'Haydar Haydaroglu',
  'phone_number': '555-313131',
  'email': 'haydar@gmail.com'},
 {'_id': ObjectId('643697ad44336b29c882e31e'),
  'name': 'Utku Haydaroglu',
  'phone': '6666-94134',
  'email': 'utku@gmail.com',
  'address': 'there, Turkiye'}]
```

#### GUI view
<img width="1348" alt="image" src="https://user-images.githubusercontent.com/36086368/231453668-07534012-001a-437d-8a9f-50ec59462eae.png">


### Step-5:

#### view_specific_record() method

```sh
In [21]: phonebook.view_specific_record({'name':'Haydar Haydaroglu'})
Out[21]: 
[{'_id': ObjectId('6436901b9f17289deb29a7e8'),
  'name': 'Haydar Haydaroglu',
  'phone_number': '555-313131',
  'email': 'haydar@gmail.com'}]
```

### Step-6:

#### update_record() method:

```sh
In [23]: updated_record = {'name': 'Haydar Haydaroglu',
    ...:   'phone_number': '555-313131',
    ...:   'email': 'haydar2@gmail.com',
    ...:   'country':'NO_COUNTRY'}

In [24]: phonebook.update_record('6436901b9f17289deb29a7e8', updated_record)

In [25]: phonebook.view_all_records()
Out[25]: 
[{'_id': ObjectId('64368cf4da9a26534d27f6a9'),
  'name': 'John Doe',
  'phone': '555-1234',
  'email': 'johndoe@example.com',
  'address': '123 Main St, Anytown, USA'},
 {'_id': ObjectId('64368d30da9a26534d27f6ab'),
  'name': 'Jane Smith',
  'phone': '555-5678',
  'email': 'janesmith@example.com',
  'address': '456 Elm St, Anytown, USA'},
 {'_id': ObjectId('64368d44da9a26534d27f6ac'),
  'name': 'Bob Johnson',
  'phone': '555-9012',
  'email': 'bobjohnson@example.com',
  'address': '789 Oak St, Anytown, USA'},
 {'_id': ObjectId('64368d90da9a26534d27f6ad'),
  'name': 'Melih Teke',
  'phone': '6666-94134',
  'email': 'melihteke@melihteke.com',
  'address': 'Somewhere, Turkiye'},
 {'_id': ObjectId('6436901b9f17289deb29a7e8'),
  'name': 'Haydar Haydaroglu',
  'phone_number': '555-313131',
  'email': 'haydar2@gmail.com',
  'country': 'NO_COUNTRY'},
 {'_id': ObjectId('643697ad44336b29c882e31e'),
  'name': 'Utku Haydaroglu',
  'phone': '6666-94134',
  'email': 'utku@gmail.com',
  'address': 'there, Turkiye'},
]

In [26]: 
```

### Step-7:

#### remove_record() method:
```sh
In [26]: phonebook.remove_record('6436901b9f17289deb29a7e8')

In [28]: phonebook.view_all_records()
Out[28]: 
[{'_id': ObjectId('64368cf4da9a26534d27f6a9'),
  'name': 'John Doe',
  'phone': '555-1234',
  'email': 'johndoe@example.com',
  'address': '123 Main St, Anytown, USA'},
 {'_id': ObjectId('64368d30da9a26534d27f6ab'),
  'name': 'Jane Smith',
  'phone': '555-5678',
  'email': 'janesmith@example.com',
  'address': '456 Elm St, Anytown, USA'},
 {'_id': ObjectId('64368d44da9a26534d27f6ac'),
  'name': 'Bob Johnson',
  'phone': '555-9012',
  'email': 'bobjohnson@example.com',
  'address': '789 Oak St, Anytown, USA'},
 {'_id': ObjectId('64368d90da9a26534d27f6ad'),
  'name': 'Melih Teke',
  'phone': '6666-94134',
  'email': 'melihteke@melihteke.com',
  'address': 'Somewhere, Turkiye'},
 {'_id': ObjectId('643697ad44336b29c882e31e'),
  'name': 'Utku Haydaroglu',
  'phone': '6666-94134',
  'email': 'utku@gmail.com',
  'address': 'there, Turkiye'}]



#### Gui view:

<img width="1352" alt="image" src="https://user-images.githubusercontent.com/36086368/231460168-1b1e4a8e-a0b1-41d4-8881-789d853bc362.png">

