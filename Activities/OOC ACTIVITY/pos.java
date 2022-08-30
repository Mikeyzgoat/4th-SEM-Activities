import java.net.URI;
import org.json.JSONObject;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.util.LinkedHashSet;
import java.util.Scanner;
public class pos {
	public static void thesaurus(String st){
		try{
			HttpRequest request = HttpRequest.newBuilder()
			.uri(URI.create("https://synonyms-word-info.p.rapidapi.com/v1/word?str="+st))
			.header("X-RapidAPI-Key","47b56b3dd5mshf5dbd0345c52e8cp1615fdjsncfbf112e88e4")
			.header("X-RapidAPI-Host", "synonyms-word-info.p.rapidapi.com")
			.method("GET", HttpRequest.BodyPublishers.noBody())
			.build();
			HttpClient client = HttpClient.newHttpClient();
	HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());
	JSONObject Jobj = new JSONObject(response.body()).getJSONObject("data");
        print(st+" : ");
        for(int i=1;i<=5;i++){
            String str = (Jobj).getString("pos"+ i);
            if(str != "")
                System.out.print(str+" ");
        }
        println("");
		}catch(Exception e){
			System.out.println(e);
		}
	}
    
    static void println(Object line){
        System.out.println(line);
    }
    
    static void print(Object line){
        System.out.print(line);
    }

    public static void dupes(String str[]){
        LinkedHashSet<String> set = new LinkedHashSet<String>();
        for(String i : str){set.add(i);}
        for(String s : set){
            if(s == "" || s == " "){
                continue;
            }
            else{
                thesaurus(s);
            }
            
        }
    }

    public static void main(String args[]){
        Scanner sc = new Scanner(System.in);
        print("Enter String : ");
        String st = sc.nextLine();
        st = st.replaceAll("[,./'?!@#$%^&*()-+=`~_{}|<>0123456789]", " ");
        String str[] = st.split(" ");

        dupes(str); // used to remove redundant strings
        
        sc.close();
    }
}
