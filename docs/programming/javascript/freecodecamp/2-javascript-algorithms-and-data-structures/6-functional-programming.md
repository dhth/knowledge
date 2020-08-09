# Functional Programming

## Basics

Functional programming follows a few core principles:

- Functions are independent from the state of the program or global variables. They only depend on the arguments passed into them to make a calculation
- Functions try to limit any changes to the state of the program and avoid changes to the global objects holding data
- Functions have minimal side effects in the program

Functional programming is all about creating and using non-mutating functions.

## Terminology

*Callbacks* are the functions that are slipped or passed into another function to decide the invocation of that function. You may have seen them passed to other methods, for example in `filter`, the callback function tells JavaScript the criteria for how to filter an array.

Functions that can be assigned to a variable, passed into another function, or returned from another function just like any other normal value, are called *first class* functions. In JavaScript, all functions are first class functions.

The functions that take a function as an argument, or return a function as a return value are called *higher order* functions.

When the functions are passed in to another function or returned from another function, then those functions which gets passed in or returned can be called a *lambda*.

## Principles of Functional Programming

- One of the core principles of functional programming is to not change things. Changes lead to bugs. It's easier to prevent bugs knowing that your functions don't change anything, including the function arguments or any global variable.
- Another principle of functional programming is to always declare your dependencies explicitly. This means if a function depends on a variable or object being present, then pass that variable or object directly into the function as an argument. There are several good consequences from this principle. The function is easier to test, you know exactly what input it takes, and it won't depend on anything else in your program.

## `Array.prototype.map()`

```javascript
// watchList is an object with data

let rating = [:fontawesome-solid-link: ];
rating = watchList.map(x=> {return {title: x[:fontawesome-solid-link: "Title"],rating: x[:fontawesome-solid-link: "imdbRating"]}});
// [:fontawesome-solid-link: {"title":"Inception","rating":"8.8"},{"title":"Interstellar","rating":"8.6"},{"title":"The Dark Knight","rating":"9.0"},{"title":"Batman Begins","rating":"8.3"},{"title":"Avatar","rating":"7.9"}]
```

## `Array.prototype.filter()`

`filter` takes a callback function that applies the logic inside the callback on each element of the array. If an element returns true based on the criteria in the callback function, then it is included in the new array.

```javascript
var words = [:fontawesome-solid-link: 'spray', 'limit', 'elite', 'exuberant', 'destruction', 'present'];

const result = words.filter(word => word.length > 6);

console.log(result);
// expected output: Array [:fontawesome-solid-link: "exuberant", "destruction", "present"]
```

## `concat`

`concat` is called on one, then another array is provided as the argument to concat, which is added to the end of the first array. It returns a new array and does not mutate either of the original arrays.

```javascript
[:fontawesome-solid-link: 1, 2, 3].concat([:fontawesome-solid-link: 4, 5, 6]);
// Returns a new array [:fontawesome-solid-link: 1, 2, 3, 4, 5, 6]
```

## `Array.prototype.reduce()`

```javascript
const array1 = [:fontawesome-solid-link: 1, 2, 3, 4];
const reducer = (accumulator, currentValue) => accumulator + currentValue;

// 1 + 2 + 3 + 4
console.log(array1.reduce(reducer));
// expected output: 10

// 5 + 1 + 2 + 3 + 4
console.log(array1.reduce(reducer, 5));
// expected output: 15
```

```javascript
//example of filter, map, and reduce

function getRating(watchList) {

    let averageRatings = watchList.filter(x => x[:fontawesome-solid-link: "imdbRating"] > 8.0).map(x => (parseFloat(x[:fontawesome-solid-link: "imdbRating"])));
    console.log(averageRatings);
    let averageRating = averageRatings.reduce((a, c) => a + c) / averageRatings.length;

    return averageRating;
}
```

## `Array.prototype.every()`

The every method works with arrays to check if every element passes a particular test. It returns a Boolean value - true if all values meet the criteria, false if not.

```javascript
var numbers = [:fontawesome-solid-link: 1, 5, 8, 0, 10, 11];
numbers.every(function(currentValue) {
  return currentValue < 10;
});
// Returns false
```

## `Array.prototype.some()`

The some method works with arrays to check if any element passes a particular test. It returns a Boolean value - true if any of the values meet the criteria, false if not.

```javascript
var numbers = [:fontawesome-solid-link: 10, 50, 8, 220, 110, 11];
numbers.some(function(currentValue) {
  return currentValue < 10;
});
// Returns true
```

## Currying

```javascript
//Un-curried function
function unCurried(x, y) {
  return x + y;
}

//Curried function
function curried(x) {
  return function(y) {
    return x + y;
  }
}
//Alternative using ES6
const curried = x => y => x + y

curried(1)(2) // Returns 3
```

## Impartial Application

```javascript
//Impartial function
function impartial(x, y, z) {
  return x + y + z;
}
var partialFn = impartial.bind(this, 1, 2);
partialFn(10); // Returns 13
```
