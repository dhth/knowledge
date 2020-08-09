# Managing Packages with npm

## Intro

The Node Package Manager (npm) is a command-line tool used by developers to share and control modules (or packages) of JavaScript code written for use with Node.js.When starting a new project, npm generates a `package.json` file. This file lists the package dependencies for your project. Since npm packages are regularly updated, the `package.json` file allows you to set specific version numbers for each dependency. This ensures that updates to a package don't break your project.npm saves packages in a folder named `node_modules`. These packages can be installed in two ways:

1. globally in a root `node_modules` folder, accessible by all projects.
2. locally within a project's own `node_modules` folder, accessible only to that project.

## `package.json`

The `package.json` file is the center of any Node.js project or npm package. It stores information about your project, similar to how the <head> section of an HTML document describes the content of a webpage. It consists of a single JSON object where information is stored in key-value pairs. There are only two required fields; `"name"` and `"version"`, but it’s good practice to provide additional information about your project that could be useful to future users or maintainers.

```json
{
  "name": "fcc-learn-npm-package-json",
  "dependencies": {
    "express": "^4.14.0"
  },
  "main": "server.js",
  "scripts": {
    "start": "node server.js"
  },
  "engines": {
    "node": "8.11.2"
  },
  "repository": {
    "type": "git",
    "url": "https://idontknow/todo.git"
  },
  "author":"Dhruv Thakur"
}
```

## Semantic Versioning

`Versions` of the npm packages in the dependencies section of your package.json file follow what’s called Semantic Versioning (SemVer), an industry standard for software versioning aiming to make it easier to manage dependencies. Libraries, frameworks or other tools published on npm should use SemVer in order to clearly communicate what kind of changes projects can expect if they update.

Knowing SemVer can be useful when you develop software that uses external dependencies (which you almost always do). One day, your understanding of these numbers will save you from accidentally introducing breaking changes to your project without understanding why things that worked yesterday suddenly don’t work today. This is how Semantic Versioning works according to the official website:

```
"package": "MAJOR.MINOR.PATCH"
```

The MAJOR version should increment when you make incompatible API changes. The MINOR version should increment when you add functionality in a backwards-compatible manner. The PATCH version should increment when you make backwards-compatible bug fixes. 

This means that PATCHes are bug fixes and MINORs add new features but neither of them break what worked before. Finally, MAJORs add changes that won’t work with earlier versions.

## Use the Tilde-Character

In the last challenge, you told npm to only include a specific version of a package. That’s a useful way to freeze your dependencies if you need to make sure that different parts of your project stay compatible with each other. But in most use cases, you don’t want to miss bug fixes since they often include important security patches and (hopefully) don’t break things in doing so.

To allow an npm dependency to update to the latest PATCH version, you can prefix the dependency’s version with the tilde (`~`) character. Here's an example of how to allow updates to any 1.3.x version.

```
"package": "~1.3.8"
```

## Use the Caret-Character

Similar to how the tilde we learned about in the last challenge allows npm to install the latest PATCH for a dependency, the caret (`^`) allows npm to install future updates as well. The difference is that the caret will allow both MINOR updates and PATCHes.

Your current version of moment should be "~2.10.2" which allows npm to install to the latest 2.10.x version. If you were to use the caret (^) as a version prefix instead, npm would be allowed to update to any 2.x.x version.

```
"package": "^1.3.8"
```

This would allow updates to any 1.x.x version of the package.
