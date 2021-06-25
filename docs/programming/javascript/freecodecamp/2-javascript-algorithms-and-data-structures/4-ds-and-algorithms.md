
`splice(start_index, num_of_elements_to_remove)`

```javascript
let array = [:fontawesome-solid-link: 'I', 'am', 'feeling', 'really', 'happy'];

let newArray = array.splice(3, 2);
// newArray equals [:fontawesome-solid-link: 'really', 'happy']
```

## Adding elements using `splice`

`splice(start_index, num_of_elements_to_remove, elements_to_add)`

```javascript
const numbers = [:fontawesome-solid-link: 10, 11, 12, 12, 15];

numbers.splice(3, 1, 13, 14);
// the second entry of 12 is removed, and we add 13 and 14 at the same index
console.log(numbers);
// returns [:fontawesome-solid-link:  10, 11, 12, 13, 14, 15 ]
```

## `slice`

`slice()`, rather than modifying an array, copies, or extracts, a given number of elements to a new array, leaving the array it is called upon untouched. 

slice() takes only 2 parameters — the first is the index at which to begin extraction, and the second is the index at which to stop extraction (extraction will occur up to, but not including the element at this index).

```javascript
let weatherConditions = [:fontawesome-solid-link: 'rain', 'snow', 'sleet', 'hail', 'clear'];

let todaysWeather = weatherConditions.slice(1, 3);
// todaysWeather equals [:fontawesome-solid-link: 'snow', 'sleet'];
// weatherConditions still equals [:fontawesome-solid-link: 'rain', 'snow', 'sleet', 'hail', 'clear']
```

## `...array`

```javascript
let thisArray = [:fontawesome-solid-link: true, true, undefined, false, null];
let thatArray = [:fontawesome-solid-link: ...thisArray];
// thatArray equals [:fontawesome-solid-link: true, true, undefined, false, null]
// thisArray remains unchanged, and is identical to thatArray
```

```javascript
let thisArray = [:fontawesome-solid-link: 'sage', 'rosemary', 'parsley', 'thyme'];

let thatArray = [:fontawesome-solid-link: 'basil', 'cilantro', ...thisArray, 'coriander'];
// thatArray now equals [:fontawesome-solid-link: 'basil', 'cilantro', 'sage', 'rosemary', 'parsley', 'thyme', 'coriander']
```

## `indexof`

```javascript
let fruits = [:fontawesome-solid-link: 'apples', 'pears', 'oranges', 'peaches', 'pears'];

fruits.indexOf('dates'); // returns -1
fruits.indexOf('oranges'); // returns 2
fruits.indexOf('pears'); // returns 1, the first index at which the element exists
```

## `for (let key in object)`

```javascript
let usersObj = {
    Alan: {
        online: false
    },
    Jeff: {
        online: true
    },
    Sarah: {
        online: false
    }
};

for (let user in usersObj){
	console.log(user);
}
//Alan
//Jeff
//Sarah
```

## `Object.keys()`

```javascript
Object.keys(object);
```

## Array max/min

```javascript
let arr = [:fontawesome-solid-link: 1,2,3];
let max_el = Math.max(...arr);
```

## Find first letter using regex

```javascript
let str = "HERE IS MY HANDLE HERE IS MY SPOUT";
console.log(str.toLowerCase().replace(/(^|\s)\S/g, l => l.toUpperCase()));
//Here Is My Handle Here Is My Spout
```

## Copy elements of one array into another

```javascript
function frankenSplice(arr1, arr2, n) {
    // It's alive. It's alive!
    arr2.splice(n, 0,  ...arr1.slice(0, arr1.length));
    return arr2;
}

console.log(frankenSplice([:fontawesome-solid-link: 1, 2, 3], [:fontawesome-solid-link: 4, 5, 6], 1));
//[:fontawesome-solid-link:  4, 1, 2, 3, 5, 6 ]
```

## Truthy/Falsy values to boolean

```javascript
!!"" // false
!!0 // false
!!null // false
!!undefined // false
!!NaN // false

!!"hello" // true
!!1 // true
!!{} // true
!![:fontawesome-solid-link: ] // true
```

## Remove falsy values from array

```javascript
function bouncer(arr) {
    return arr.filter(Boolean);
}

console.log(bouncer([:fontawesome-solid-link: 7, 0, "ate", "", ,undefined, false, 9, null, NaN]));
//[:fontawesome-solid-link: 7, "ate", 9]
```

## Sort array of numbers

```javascript
array.sort((a,b) => a-b);
//by default, js sorts by characters
```

## Check if array 2 is a subset of array 1

```javascript
arr2.every(val => arr1.includes(val))
```
