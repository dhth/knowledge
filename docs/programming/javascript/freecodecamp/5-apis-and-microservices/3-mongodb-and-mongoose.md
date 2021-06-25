
- Scalability: by default, non-relational databases are split (or "shared") across many systems instead of only one. This makes it easier to improve performance at a lower cost.
- Flexibility: new datasets and properties can be added to a document without the need to make a new table for that data.
- Replication: copies of the database run in parallel so if one goes down, one of the copies becomes the new primary data source.

While there are many non-relational databases, Mongo's use of JSON as its document storage structure makes it a logical choice when learning backend JavaScript. Accessing documents and their properties is like accessing objects in JavaScript.

Mongoose.js is an npm module for Node.js that allows you to write objects for Mongo as you would in JavaScript. This can make it easier to construct documents for storage in Mongo.

## Setup

```javascript
//package.json
"dependencies": {
    "mongodb": "^3.3.4",
    "mongoose": "^5.7.12"
  }
```

```javascript
//.env
MONGO_URI="mongodb+srv://<username>:<password>@cluster0-ghkrk.mongodb.net/test?retryWrites=true&w=majority"
```

```javascript
//app.js
var mongoose = require('mongoose');
mongoose.connect(process.env.MONGO_URI);
```

## Create a Schema

**C**RUD Part I - CREATE

First of all we need a Schema. Each schema maps to a MongoDB collection. It defines the shape of the documents within that collection. Schemas are building block for Models. They can be nested to create complex models, but in this case we’ll keep things simple. A model allows you to create instances of your objects, called documents.

Glitch is a real server, and in real servers the interactions with the db happen in handler functions. These function are executed when some event happens (e.g. someone hits an endpoint on your API). We’ll follow the same approach in these exercises. The `done()` function is a callback that tells us that we can proceed after completing an asynchronous operation such as inserting, searching, updating or deleting. It’s following the Node convention and should be called as `done(null, data)` on success, or `done(err)` on error. Warning - When interacting with remote services, errors may occur!

```javascript
/* Example */

var someFunc = function(done) {
  //... do something (risky) ...
  if(error) return done(error);
  done(null, result);
};
```

---

Create a person having this prototype :

```
- Person Prototype 
---------------------
name : string [:fontawesome-solid-link: required]
age : number
favoriteFoods : array of strings (*) 
```

```javascript
var Schema = mongoose.Schema;
var PersonSchema = new Schema({
  name: {type: 'String', required: true},
  age: {type: 'Number'},
  favoriteFoods: {type: [:fontawesome-solid-link: 'String']}
});

var Person = mongoose.model('Person', PersonSchema);
```

## Create and Save a Record of a Model

Create a document instance using the `Person` constructor you built before. Pass to the constructor an object having the fields `name`, `age`, and `favoriteFoods`. Their types must conform to the ones in the Person Schema. Then call the method `document.save()` on the returned document instance. Pass to it a callback using the Node convention. This is a common pattern, all the following CRUD methods take a callback function like this as the last argument.

```javascript
/* Example */

// ...
person.save(function(err, data) {
  //   ...do your stuff here...
});
```

```javascript
//solution

var Schema = mongoose.Schema;
var PersonSchema = new Schema({
  name: {type: 'String', required: true},
  age: {type: 'Number'},
  favoriteFoods: {type: [:fontawesome-solid-link: 'String']}
});

var Person = mongoose.model('Person', PersonSchema);

var createAndSavePerson = function(done) {
  const doc = new Person({name: "Dhruv Thakur", age:26, favoriteFoods:[:fontawesome-solid-link: "Chicken","Omelette","Coffee"]});
  doc.save((err, data)=>{
    if (err) done(err);
    if (data) done(null , data);
  });
};
```

## Create Many Record

```javascript
var arrayOfPeople = [:fontawesome-solid-link: 
  {
    name: "Dhruv Thakur",
    age: 26,
    favoriteFoods: [:fontawesome-solid-link: "Chicken"]
  },
  {
    name: "Dhruv Thakur2",
    age: 26,
    favoriteFoods: [:fontawesome-solid-link: "Chicken"]
  },
  {
    name: "Dhruv Thakur3",
    age: 26,
    favoriteFoods: [:fontawesome-solid-link: "Chicken"]
  }
];

var createManyPeople = function(arrayOfPeople, done) {
  Person.create(arrayOfPeople, (err, people) => {
    if (err) return console.log(err);
    done(people);
  });
};
```

## `Model.find()`

```javascript
var findPeopleByName = function(personName, done) {
  var matchedPeople = Person.find({name:personName}, (err, people)=>{
    if (err) return console.log(err);
    done(null, people);
  });
};
```

## `Model.findOne()`

```javascript
var findOneByFood = function(food, done) {
  const matchedPerson = Person.findOne({favoriteFoods:[:fontawesome-solid-link: food]}, (err, matched)=>{
    if (err) return console.log(err);
    done(null, matched)
  });
};
```

## `Model.findById()`

```javascript
var findPersonById = function(personId, done) {
  const matched = Person.findById({_id:personId}, (err, matched)=>{
    if (err) return console.log(err);
    done(null, matched);
  });
};
```

## Classic Find, Edit, then Save

In the good old days this was what you needed to do if you wanted to edit a document and be able to use it somehow e.g. sending it back in a server response. Mongoose has a dedicated updating method : `Model.update()`. It is bound to the low-level mongo driver. It can bulk edit many documents matching certain criteria, but it doesn’t send back the updated document, only a `‘status’` message. Furthermore it makes model validations difficult, because it just directly calls the mongo driver.

```javascript
var findEditThenSave = function(personId, done) {
  var foodToAdd = "hamburger";
  var matched = Person.findById({_id:personId}, (err, matched)=>{
    if (err) return console.log(err);
    matched.favoriteFoods.push(foodToAdd);
    matched.save((err, data)=>{
      if (err) return console.log(err);
      done(null, data);
    });
  });
};
```

## `Model.findOneAndUpdate()`

Recent versions of mongoose have methods to simplify documents updating. Some more advanced features (i.e. pre/post hooks, validation) behave differently with this approach, so the Classic method is still useful in many situations. findByIdAndUpdate() can be used when searching by Id.

```javascript
A.findOneAndUpdate(conditions, update, options, callback) // executes
A.findOneAndUpdate(conditions, update, options)  // returns Query
A.findOneAndUpdate(conditions, update, callback) // executes
A.findOneAndUpdate(conditions, update)           // returns Query
A.findOneAndUpdate()                             // returns Query
```

```javascript
var findAndUpdate = function(personName, done) {
  var ageToSet = 20;
  var matched = Person.findOneAndUpdate(
    { name: personName }, {age: ageToSet}, {new: true},
    (err, data) => {
      if (err) return console.log(err);
      matched.age = ageToSet;
      done(null, data);
    }
  );
};
```

## `Model.findByIdAndRemove()`

Delete one person by the person's _id. You should use one of the methods `findByIdAndRemove()` or `findOneAndRemove()`. They are like the previous update methods. They pass the removed document to the cb. As usual, use the function argument personId as the search key.

```javascript
var removeById = function(personId, done) {
  var deleted = Person.findByIdAndRemove({_id:personId}, (err,data)=>{
    if (err) return console.log(err);
    done(null, data);
  });
};
```

## `Model.remove()`

`Model.remove()` is useful to delete all the documents matching given criteria.

Delete all the people whose name is “Mary”, using `Model.remove()`. Pass it to a query document with the `name` field set, and of course a callback.

**Note:** The `Model.remove()` doesn’t return the deleted document, but a JSON object containing the outcome of the operation, and the number of items affected. Don’t forget to pass it to the `done()` callback, since we use it in tests.

```javascript
var removeManyPeople = function(done) {
  var nameToRemove = "Mary";
  var deleteStats = Person.remove({name:nameToRemove},(err, deleted)=>{
    if (err) return console.log(err);
    done(null, deleted);
  });
};
```

## Chain Search Query Helpers to Narrow Search Results

If you don’t pass the callback as the last argument to `Model.find()` (or to the other search methods), the query is not executed. You can store the query in a variable for later use. This kind of object enables you to build up a query using chaining syntax. The actual db search is executed when you finally chain the method `.exec()`. You always need to pass your callback to this last method. There are many query helpers, here we’ll use the most ‘famous’ ones.

Find people who like `burrito`. Sort them by name, limit the results to two documents, and hide their age. Chain `.find()`, `.sort()`, `.limit()`, `.select()`, and then `.exec()`. Pass the `done(err, data)` callback to `exec()`.

[:fontawesome-solid-link: Mongoose v5.7.13:](https://mongoosejs.com/docs/api/query.html#query_Query-sort)

[:fontawesome-solid-link: Mongoose v5.7.13:](https://mongoosejs.com/docs/api/query.html#query_Query-limit)

[:fontawesome-solid-link: Mongoose v5.7.13:](https://mongoosejs.com/docs/api/query.html#query_Query-select)

```javascript
var queryChain = function(done) {
  var foodToSearch = "burrito";

  var results = Person.find({favoriteFoods: foodToSearch}).sort('name').limit(2).select('name favoriteFoods').exec((err, data)=>{
    if (err) return console.log(err);
    done(null, data);
  });
};
```

## Mongo Atlas and Robo 3T

[:fontawesome-solid-link: How to Connect to MongoDB Atlas | Studio 3T](https://studio3t.com/knowledge-base/articles/connect-to-mongodb-atlas/)

## Finding select fields

```javascript
// Retrieving only certain fields

Model.find({}, 'first last', function (err, docs) {

});
```

## Ref

```javascript
const Schema = mongoose.Schema;

const userSchema = new Schema({
  username: String,
  userid: String,
  exercises: [:fontawesome-solid-link: { type: Schema.Types.ObjectId, ref: "Exercise" }]
});

const exerciseSchema = new Schema({
  user: { type: Schema.Types.ObjectId, ref: "User" },
  description: String,
  duration: Number,
  date: Date
});

const UserModel = mongoose.model("User", userSchema);
const ExerciseModel = mongoose.model("Exercise", exerciseSchema);

app.post("/api/exercise/add", (req, res) => {
  let exerciseDate;
  if(!(req.body.date)){
    exerciseDate = new Date();
  }
  else{
    exerciseDate = req.body.date;
  }
  const newExercise = new ExerciseModel({
    user: req.body.userId,
    description: req.body.description,
    duration: req.body.duration,
    date: exerciseDate
  });
  
  newExercise.save((err, savedExercise) => {  //save exercise first
    if (err) {
      res.send("Internal Server Error");
    }
    if (savedExercise) {
      UserModel.update(           //then update user
        {
          _id: req.body.userId
        },
        {
          $push: {
            exercises: savedExercise._id       //push ref to array
          }
        }
      ).exec(function(err, savedUser) {
        if (err) {
          res.send("500");
        }
        if (savedUser) {
          res.json({
            user: savedUser.id,
            description: savedExercise.description,
            duration: savedExercise.duration,
            date: new Date(savedExercise.date).toDateString()
          });
        }
      });
    }
  });
});
```

## Populate

```javascript
//continued from above

app.get("/api/exercise/log", (req, res) => {
  const userId = req.query.userId;
  const from = req.query.from;
  const to = req.query.to;
  const limit = req.query.limit;

  let matchConditions = {};
  if (from) {
    if (!matchConditions[:fontawesome-solid-link: "date"]) {
      matchConditions[:fontawesome-solid-link: "date"] = {};
    }
    matchConditions[:fontawesome-solid-link: "date"][:fontawesome-solid-link: "$gte"] = from;
  }
  if (to) {
    if (!matchConditions[:fontawesome-solid-link: "date"]) {
      matchConditions[:fontawesome-solid-link: "date"] = {};
    }
    matchConditions[:fontawesome-solid-link: "date"][:fontawesome-solid-link: "$lte"] = to;
  }

  let options = {};
  if (limit) {
    options[:fontawesome-solid-link: "limit"] = limit;
  }

  console.log(userId, from, to, limit);
  UserModel.findOne({ _id: req.query.userId })
    .populate({
      path: "exercises",
      select: "description duration date -_id",
      match: matchConditions,
      options: options,
    })
    .exec((err, data) => {
      res.json(
        // data
        {
          username: data.username,
          _id: data.id,
          count: data.exercises.length,
          exercises: data.exercises
        }
      );
    });
});
```
