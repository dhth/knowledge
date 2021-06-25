
These time intervals are called timing events.

The two key methods to use with JavaScript are:

- `setTimeout(*function, milliseconds*`) → Executes a function, after waiting a specified number of milliseconds.
- `setInterval(*function, milliseconds*`) → Same as setTimeout(), but repeats the execution of the function continuously.

## `setTimeout`

`window.setTimeout(function, milliseconds);`

The `window.setTimeout()` method can be written without the window prefix.

The first parameter is a function to be executed.

The second parameter indicates the number of milliseconds before execution.

```html
<!DOCTYPE html>
<html>
<body>

<p>Click "Try it". Wait 3 seconds. The page will alert "Hello".</p>
<p>Click "Stop" to prevent the first function to execute.</p>
<p>(You must click "Stop" before the 3 seconds are up.)</p>

<button onclick="myVar = setTimeout(myFunction, 3000)">Try it</button>

<button onclick="clearTimeout(myVar)">Stop it</button>

<script>
function myFunction() {
  alert("Hello");
}
</script>
</body>
</html>
```

## `setInterval`

The `setInterval()` method repeats a given function at every given time-interval.

`window.setInterval(function, milliseconds);`

The `window.setInterval()` method can be written without the window prefix.

The first parameter is the function to be executed.

The second parameter indicates the length of the time-interval between each execution.

```html
<!DOCTYPE html>
<html>
<body>

<p>A script on this page starts this clock:</p>

<p id="demo"></p>

<button onclick="clearInterval(myVar)">Stop time</button>

<script>
var myVar = setInterval(myTimer ,1000);
function myTimer() {
  var d = new Date();
  document.getElementById("demo").innerHTML = d.toLocaleTimeString();
}
</script>

</body>
</html>
```
