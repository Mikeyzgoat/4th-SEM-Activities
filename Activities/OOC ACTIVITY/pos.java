import java.net.URI;
import org.json.JSONObject;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.util.Scanner;
public class pos {
	public void thesaurus(String st){
		try{
			HttpRequest request = HttpRequest.newBuilder()
			.uri(URI.create("https://synonyms-word-info.p.rapidapi.com/v1/word?str="+st))
			.header("X-RapidAPI-Key", "47b56b3dd5mshf5dbd0345c52e8cp1615fdjsncfbf112e88e4")
			.header("X-RapidAPI-Host", "synonyms-word-info.p.rapidapi.com")
			.method("GET", HttpRequest.BodyPublishers.noBody())
			.build();
			HttpClient client = HttpClient.newHttpClient();
	HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());
	JSONObject Jobj = new JSONObject(response.body()).getJSONObject("data");
        print(st+" : ");
        for(int i=1;i<=5;i++){
            String str = (Jobj).getString("pos"+ i);
            if(str == "etc" && (st == "a" || st == "an")){
                str = "det";
            }
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


    public static void main(String args[]){
        Scanner sc = new Scanner(System.in);
        pos obj = new pos();
        print("Enter String : ");
        String st = sc.nextLine();
        st = st.replaceAll("[,./'?!@#$%^&8()-+=`~_{}|<>0123456789]", " ");
        String str[] = st.split(" ");
        for(String i :str){
            if(i == " " || i == ""){
                continue;
            }
            else{
                obj.thesaurus(i);
            }
        }
        sc.close();
    }
}
