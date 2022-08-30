# StringOps :
<p align="center">
  <img width="460" height="300" src = "https://imgs.search.brave.com/leIEr9JmWsLlFTxsOSaLy9RgZ3RFao9UGpqsnBErl18/rs:fit:613:225:1/g:ce/aHR0cHM6Ly90c2U0/Lm1tLmJpbmcubmV0/L3RoP2lkPU9JUC5h/MTVYTmhoS2xaa3F3/NjNiQklmSE93SGFG/dSZwaWQ9QXBp"><br> <br>
  A parts of speech tagger that reads a string and returns all possible parts of speech of substrings from a user input (string).
</p>


## Contents :
* Requirements
* How to run the code over terminal
* Classes Used
* What happens during runtime?
* How do we handle repeated words?
* How does the API work
* Role of JSONObject class
* Future updates

## Requirements :
- JSONObject class in java : As of now the built in JSON class in java is depracated, but making use of the required [jar file](https://github.com/stleary/JSON-java).<br> You can download it by clicking [here](https://search.maven.org/remotecontent?filepath=org/json/json/20220320/json-20220320.jar)<br>
- JDK-8 and above.
 
## How to run the code over terminal : 
> Notice : 
Note that the jar file must and should be binded alongside compilation. Otherwise it wouldn't recognize org.json.JSONObject class.<br>

Compilation step :
```shell
javac -cp json-20220320.jar pos.java
```
Execution step :
```shell
java -cp :json-20220320.jar pos
```

## Classes Used : 
* java.net.URI
* org.json.JSONObject
* java.net.http.HttpClient
* java.net.http.HttpRequest
* java.net.http.HttpResponse
* java.util.Scanner
* java.util.LinkedHashSet
 
## What happens during runtime? :
> - We start by taking the user's input as a string.<br>
> - The string obtained will be processed to remove unwanted characters.<br>

the process is as below :
```java
// String st
st = st.replaceAll("[,./'?!@#$%^&*()-+=`~_{}|<>0123456789]", " ");
```
Now the string after removing all unnecessary characters will be split into individual substrings as below :
```java
// str[] is the array holding substrings.
String str[] = st.split(" ");
```
The substring str may contain unnecessary spaces as a member in array.<br> 
> Q. <i>What should we do as the API can't return anything for an empty string?.</i><br>A. <i> Simple dont consider it while sending it to the api for required data.</i>

## How do we handle repeated words?
* We use a simple mathematical concept, yet powerful enough to help us solve this case. The concept of Sets is made use of here.
* Luckily java has a class within java.util called [*LinkedHashSet*](https://www.geeksforgeeks.org/linkedhashset-in-java-with-examples/).
* LinkedHashSet implements the ideology we needed ,i.e, <q>A Set always contains unique elements.</q>

The implementation can be done as follows <br>
```java
// Object of LinkedHashSet. Also specifying that Set must contain strings only.
LinkedHashSet<String> set = new LinkedHashSet<String>(); 
for(String i : str){
  set.add(i); // adding all elements from str[] array and only unique elements will be added.
}
```

Now we call the member function <i>thesaurus</i> by passing each element of the object set as parameter.

## How does the API work? :
- The API is available at [rapid api](https://rapidapi.com/hub)<br>
- API NAME : [Synonym and word info](https://rapidapi.com/techytools/api/synonyms-word-info/)<br>
- As most web based API's work, this API uses a GET request by making use of HttpRequest,HttpClient classes of java.net .With this the client sends a GET request to the API and the JSON data is returned and a JSONObject is used to retrieve the data from the response.

## Role of JSONObject class :
* The JSON data retrieved as of now comprises of multiple JSON objects.
* The Object that contains the parts of speech is held at the Object named "data".
* The following block of code helps with the retrieving of required fields within "data".
```java
// response is the HttpRequest object that holds the returned JSON data
JSONObject Jobj = new JSONObject(response.body()).getJSONObject("data");
```

 
* the Object "data" contains five "pos" objects within itself.
* Now we access all the five "pos" as long as its value isnt null or empty.
* The following block of code will help understand how the above happens.
```java
for(int i=1;i<=5;i++){
    String str = (Jobj).getString("pos"+ i);
    if(str == "etc" && (st == "a" || st == "an")){
        str = "det"; // API for some reason doesn't recognize "a" and "an" as determiners.
    }
    if(str != "") // Eliminates empty fields
        System.out.print(str+" ");
}
```
## Future Updates :
Future updates to be carried out : <br>
* [ ] Spelling checks <br>
* [ ] Word meanings, synonyms, antonyms<br>

### Contributors
* [T ADITYA](https://github.com/Mikeyzgoat)
* [TANMAY V](https://github.com/thetanmayguy)
