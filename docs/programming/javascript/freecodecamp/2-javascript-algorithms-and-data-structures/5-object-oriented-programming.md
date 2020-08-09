# Object Oriented Programming

## `instanceof`

`instanceof` allows you to compare an object to a constructor, returning true or false based on whether or not that object was created with the constructor.

```javascript
let Bird = function(name, color) {
  this.name = name;
  this.color = color;
  this.numLegs = 2;
}

let crow = new Bird("Alexis", "black");

crow instanceof Bird; // => true
```

## prototype

The prototype is an object that is shared among ALL instances of the class.

**It erases the constructor property!**

```javascript
Bird.prototype = {
	constructor: Bird,
  numLegs: 2, 
  eat: function() {
    console.log("nom nom nom");
  },
  describe: function() {
    console.log("My name is " + this.name);
  }
};
```

## `obj.hasOwnProperty`

object instances can have two kinds of properties: own properties and prototype properties.

Own properties are defined directly on the object instance itself. And prototype properties are defined on the prototype.

## Inheritance

```javascript
function Animal() { }

Animal.prototype = {
  constructor: Animal,
  eat: function() {
    console.log("nom nom nom");
  }
};

function Dog() { }

// Add your code below this line
Dog.prototype = Object.create(Animal.prototype);
Dog.prototype.constructor = Dog;

let beagle = new Dog();
beagle.eat();  // Should print "nom nom nom"
```

## Overriding

```javascript
function Animal() { }
Animal.prototype.eat = function() {
  return "nom nom nom";
};
function Bird() { }

// Inherit all methods from Animal
Bird.prototype = Object.create(Animal.prototype);
Bird.prototype.constructor = Bird;

// Bird.eat() overrides Animal.eat()
Bird.prototype.eat = () => "peck peck peck";

/*
If you have an instance let duck = new Bird(); and you call duck.eat(), this is how JavaScript looks for the method on duck’s prototype chain:

duck => Is eat() defined here? No.
Bird => Is eat() defined here? => Yes. Execute it and stop searching.
Animal => eat() is also defined, but JavaScript stopped searching before reaching this level.
Object => JavaScript stopped searching before reaching this level.
*/
```

## Mixin

There are cases when inheritance is not the best solution. Inheritance does not work well for unrelated objects like Bird and Airplane. They can both fly, but a Bird is not a type of Airplane and vice versa.

```javascript
let flyMixin = function(obj) {
  obj.fly = function() {
    console.log("Flying, wooosh!");
  }
};

let bird = {
  name: "Donald",
  numLegs: 2
};

let plane = {
  model: "777",
  numPassengers: 524
};

flyMixin(bird);
flyMixin(plane);

bird.fly(); // prints "Flying, wooosh!"
plane.fly(); // prints "Flying, wooosh!"
```

## Immediately Invoked Function Expression

```javascript
(() => {console.log("A cozy nest is ready")})();
```

```javascript
let motionModule = (function () {
  return {
    glideMixin: function(obj) {
      obj.glide = function() {
        console.log("Gliding on the water");
      };
    },
    flyMixin: function(obj) {
      obj.fly = function() {
        console.log("Flying, wooosh!");
      };
    }
  }
})(); // The two parentheses cause the function to be immediately invoked

motionModule.glideMixin(duck);
duck.glide(); //Gliding on the water
```
