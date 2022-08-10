# StringOps :
<p align="center">
  <img width="460" height="300" src = "https://imgs.search.brave.com/leIEr9JmWsLlFTxsOSaLy9RgZ3RFao9UGpqsnBErl18/rs:fit:613:225:1/g:ce/aHR0cHM6Ly90c2U0/Lm1tLmJpbmcubmV0/L3RoP2lkPU9JUC5h/MTVYTmhoS2xaa3F3/NjNiQklmSE93SGFG/dSZwaWQ9QXBp">
</p>
A parts of speech tagger that reads a string and returns all possible parts of speech of substrings from a user input (string).

## Contents :
* Requirements
* How to run the code over terminal
* Classes Used
* What happens during runtime?
* How does the API work
* Role of JSONObject class
* Future updates

## Requirements :
* JSONObject class in java : As of now the built in JSON class in java is depracated, but making use of the required [jar file](https://github.com/stleary/JSON-java). Download it by clicking [here](https://search.maven.org/remotecontent?filepath=org/json/json/20220320/json-20220320.jar).
* JDK-8 and above.
* 
## How to run the code over terminal : 
> Notice : 
It is to be noted that the jar file must and should be binded alongside compilation. Otherwise it wouldn't recognize org.json.JSONObject class.
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
* import java.util.Scanner
 
## What happens during runtime? :
> - We start of by taking the user's input as a string.<br>
> - The string obtained will be processed to remove unwanted characters.<br>

the process is as below :
```java
// String st
st = st.replaceAll("[,./'?!@#$%^&8()-+=`~_{}|<>0123456789]", " ");
```
Now the string after removing all unnecessary characters will be split into individual substrings as below :
```java
// str[] is the array holding substrings.
String str[] = st.split(" ");
```
> The substring str may contain unnecessary spaces as a member in array.<br> Q.) <i>What should we do as the API can't return anything for an empty string?.</i><br>Ans.<i> Simple dont consider it while sending it to the api for required data.</i>
<br>
Now we create an object of the class pos called obj, and call the member function <i>thesaurus</i>.

## How does the API work? :
> The API is a free api that was available at [rapid api](https://rapidapi.com/hub)<br> API NAME : [Synonym and word info](https://rapidapi.com/techytools/api/synonyms-word-info/)<br>
> As most web based API's work, this API uses a GET request by making use of HttpRequest,HttpClient classes of java.net .With this the client sends a GET request to the API and the JSON data is returned and a JSONObject is used to retrieve the data from the response.

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
