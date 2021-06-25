/*
You will be provided with an initial array (the first argument in the destroyer function), followed by one or more arguments. Remove all elements from the initial array that are of the same value as these arguments.
*/
const destroyer = (arr, ...valsToRemove) => arr.filter(elem => !valsToRemove.includes(elem));

destroyer([:fontawesome-solid-link: 1, 2, 3, 1, 2, 3], 2, 3);
//[:fontawesome-solid-link: 1, 1]
```

## Spinal Tap Case

```javascript
str.replace(/\s/g,"-").replace(/_/g,"-").replace(/([:fontawesome-solid-link: a-z])([:fontawesome-solid-link: A-Z])/g, "$1-$2").toLowerCase();

/*
This Is Spinal Tap -> this-is-spinal-tap
thisIsSpinalTap -> this-is-spinal-tap
The_Andy_Griffith_Show -> the-andy-griffith-show
Teletubbies say Eh-oh -> teletubbies-say-eh-oh
AllThe-small Things -> all-the-small-things
*/
```

## Sorted Union

```javascript
const uniteUnique = (...arr) => arr.reduce((a, c) => a.concat(c.filter(x =>  !(x in a))));

uniteUnique([:fontawesome-solid-link: 1, 3, 2], [:fontawesome-solid-link: 5, 2, 1, 4], [:fontawesome-solid-link: 2, 1]);
//[:fontawesome-solid-link:  1, 3, 2, 5, 4 ]
```

## Replace with Regex based on key value pair

```javascript
return str.replace(/([:fontawesome-solid-link: &<>"'])/g, $1 => pairs[:fontawesome-solid-link: $1]);
```

## Binary to English

```javascript
function binaryAgent(str) {
    let els = str.split(" ");
    let trs = [:fontawesome-solid-link: ];
    for (let i=0;i<els.length;i++){
        trs.push(String.fromCharCode(parseInt(els[:fontawesome-solid-link: i], 2)))
    }
    return trs.join("");
}

console.log(binaryAgent("01000001 01110010 01100101 01101110 00100111 01110100 00100000 01100010 01101111 01101110 01100110 01101001 01110010 01100101 01110011 00100000 01100110 01110101 01101110 00100001 00111111"));
//Aren't bonfires fun!?
```
