### Creating a Phonebook with MongoDB

The idea of this repo to show how we can build our phonebook over mongodb. In order to start this application you need to have a accessible MongoDB somewhere. In my example I have created my FreeTier MongoDB on https://cloud.mongodb.com/.


## Step-1:
Cluster0 is created on cloud.mongodb

<img width="1490" alt="image" src="https://user-images.githubusercontent.com/36086368/231450127-bb2b20a5-adbd-4ddb-8aaa-5bccc42fbf6e.png">


## Step-2
Created test database and phonebook collection

<img width="1313" alt="image" src="https://user-images.githubusercontent.com/36086368/231450738-bfe6f3db-3bf1-4331-88fd-c3e66cdf791e.png">



## Step-3
Inserted some initial documents

<img width="1302" alt="image" src="https://user-images.githubusercontent.com/36086368/231450891-d5392ab1-5c38-4d17-b682-0f51f39cde99.png">



## Step-4:

# add_record() method

```sh
In [16]: new_record={'name': 'Utku Haydaroglu','phone': '6666-94134', 'email': 'utku@gmail.com', 'address': 'there, Turkiye'}

In [17]: phonebook.add_record(new_record)

In [18]: 
```


```sh
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

## GUI view
<img width="1348" alt="image" src="https://user-images.githubusercontent.com/36086368/231453668-07534012-001a-437d-8a9f-50ec59462eae.png">

