# Regex

## Basic

```javascript
let extractStr = "Extract the word 'coding' from this string.";
let codingRegex = /coding/; 
let result = extractStr.match(codingRegex); 
```

## Cheat Sheet

```javascript
let myRegex = /regex/i;
// i -> ignores case
```

```javascript
let myRegex = /regex/g;
// g -> matches multiple
```

```javascript
let myRegex = /d.g/gi;
// . -> wildcard character -> matches anything, eg. dog, dig
```

```javascript
let myRegex = /b[:fontawesome-solid-link: aiu]/gi;
// [:fontawesome-solid-link: ] -> character set -> matches either -> bag, big, bug
```

```javascript
let myRegex = /[:fontawesome-solid-link: a-e]/gi;
// - → hyphen → matches characters from "a" to "e" inclusive. works for numbers too
```

```javascript
let myRegex = /[:fontawesome-solid-link: a-z0-9]/ig;
// characters and numbers combined in one set
```

```javascript
let myRegex = /[:fontawesome-solid-link: ^aeiou]/ig;
// negated character set -> matches anything but aeiou
//Note: carat used inside character set represents negation, outside, it is used to represent beginning of a pattern 
```

```javascript
let myRegex = /a+/ig;
// + -> match Characters that Occur One or More Times
// "abc" -> [:fontawesome-solid-link: "a"]
// "aabc" -> [:fontawesome-solid-link: "aa"]
// "bcd" -> [:fontawesome-solid-link: ]
```

```javascript
let goRegex = /go*/;
// * -> match Characters that Occur zero or More Times
// "goal" -> [:fontawesome-solid-link: "go"]
// "goooal" -> [:fontawesome-solid-link: "gooo"]
// "gut" -> [:fontawesome-solid-link: "g"]
// "wat" -> [:fontawesome-solid-link: ]
```

```javascript
let goRegex = /t[:fontawesome-solid-link: a-z]*i/;
// greedy match -> finds the longest possible part of a string that fits the regex pattern and returns it as a match -> used by default
// "titanic" -> [:fontawesome-solid-link: "titani"]

let goRegex = /t[:fontawesome-solid-link: a-z]*?i/;
// ? -> lazy match -> finds the smallest possible part of the string that satisfies the regex pattern -> used by default
// "titanic" -> [:fontawesome-solid-link: "titani"]
```

```javascript
//beginning of a pattern
let firstString = "Ricky is first and can be found.";
let firstRegex = /^Ricky/;
firstRegex.test(firstString);
// Returns true
let notFirst = "You can't find Ricky now.";
firstRegex.test(notFirst);
// Returns false
```

```javascript
//end of a pattern
let theEnding = "This is a never ending story";
let storyRegex = /story$/;
storyRegex.test(theEnding);
// Returns true
let noEnding = "Sometimes a story will have to end";
storyRegex.test(noEnding);
// Returns false
```

```javascript
// \w is shorthand for /[:fontawesome-solid-link: A-Za-z0-9_]+/
```

```javascript
// \W is shorthand for [:fontawesome-solid-link: ^A-Za-z0-9_]
// opposite of \w
```

```javascript
// \d is shorthand for [:fontawesome-solid-link: 0-9]
```

```javascript
// \D is shorthand for [:fontawesome-solid-link: ^0-9]
// opposite of \d
```

```javascript
/*
example
1) Usernames can only use alpha-numeric characters.

2) The only numbers in the username have to be at the end. There can be zero or more of them at the end.

3) Username letters can be lowercase and uppercase.

4) Usernames have to be at least two characters long. A two-character username can only use alphabet letters as characters.
*/

let userCheck = /^[:fontawesome-solid-link: a-z]([:fontawesome-solid-link: a-z]+\d*|\d\d)$/i;
```

```javascript
// \s -> whitespace
// \s also matches carriage return, tab, form feed, and new line characters.
let spaceRegex = /\s/g;
```

```javascript
let spaceRegex = /\S/g;
//opposite of \s
```

```javascript
//Specify Upper and Lower Number of Matches
let multipleA = /a{3,5}h/;
// "aaah" -> [:fontawesome-solid-link: "aaa"]
// "aah" -> [:fontawesome-solid-link: ]
```

```javascript
//specify only lower number of matches
let multipleA = /ha{3,}h/;
```

```javascript
//specify exact number of matches
let multipleHA = /ha{3}h/;
```

```javascript
//optional
let american = "color";
let british = "colour";
let rainbowRegex= /colou?r/;
rainbowRegex.test(american); // Returns true
rainbowRegex.test(british); // Returns true

// think of this symbol as saying the previous element is optional
```

```javascript
//capture groups
let repeatStr = "regex regex";
let repeatRegex = /(\w+)\s\1/;
repeatRegex.test(repeatStr); // Returns true
repeatStr.match(repeatRegex); // Returns [:fontawesome-solid-link: "regex regex", "regex"]

//Using the .match() method on a string will return an array with the string it matches, along with its capture group.
```

```javascript
//replacing
"Code Camp".replace(/(\w+)\s(\w+)/, '$2 $1');
// Returns "Camp Code"
```

```javascript
//example
//trim whitespace at beginning and end of string
let hello = "   Hello, World!  ";
let wsRegex = /(^\s+|\s+$)/g;
let matched = hello.match(wsRegex); // [:fontawesome-solid-link: "   ","  "]
let trimmed = hello.replace(wsRegex, "");
```
