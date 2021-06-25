- `shift` → removes first
- `unshift` → adds to first position
- `if (condition)` → condition needs a bracket

## Equalities and Inequalities

```javascript
//type conversion
1   ==  1   // true
1   ==  2   // false
1   == '1'  // true
"3" ==  3   // true

//strict equality
3 ===  3   // true
3 === '3'  // false

//inequality
3 !=  3   // false
3 != '3'  // false
4 !=  3   // true

//strict inequality
3 !==  3   // false
3 !== '3'  // true
4 !==  3   // true

//greater than
5   >  3   // true
7   > '3'  // true
2   >  3   // false
'1' >  9   // false
```

## Checking if property exists

```javascript
var myObj = {
  top: "hat",
  bottom: "pants"
};
myObj.hasOwnProperty("top");    // true
myObj.hasOwnProperty("middle"); // false
```

## Generate random numbers

```javascript
Math.floor(Math.random() * (max - min + 1)) + min
```
