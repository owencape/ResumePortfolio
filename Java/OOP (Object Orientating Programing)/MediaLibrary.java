import java.util.ArrayList;
import java.util.Scanner;

public class MediaLibrary {

    private static ArrayList<Song> myPlaylist = new ArrayList<Song>();
    private static ArrayList<Book> myBookShelf = new ArrayList<Book>();
    
    public static void main(String[] args) {
        
        Song song1 = new Song("Just a Dream", "Nelly");
        Song song2 = new Song("Shower", "Becky G");
        Song song3 = new Song("Too Comfortable", "Future");
    

        myPlaylist.add(song1);myPlaylist.add(song2);myPlaylist.add(song3);

        printPlaylist(myPlaylist);

        song1.setName("Wheels on the bus");
        song1.setRating(1);
        myPlaylist.get(1).setRating(7);
        myPlaylist.get(2).setRating(10);

        printPlaylist(myPlaylist);

        addSong();

        printPlaylist(myPlaylist);

        printAveRating(myPlaylist);

        System.out.println(findASong());

        myBookShelf.add(new Book());
        myBookShelf.add(new Book("Rainbow Six"));
        myBookShelf.add(new Book("Jercy Packson","James Patterson"));

        printShelf(myBookShelf);
    }

    private static void printPlaylist(ArrayList<Song> arr){
        for(int i=0;i<arr.size();i++){
            System.out.println(arr.get(i));
        }
    }

    private static void printShelf(ArrayList<Book> arr){
        for(int i=0;i<arr.size();i++){
            System.out.println(arr.get(i));
        }

    }
    
        private static void addSong(){
        Scanner ui = new Scanner(System.in);
        System.out.println("What's the song title: ");
        String song = ui.nextLine();
        System.out.println("Who's the artist: ");
        String artist = ui.nextLine();
        System.out.println("What's the rating: ");
        double rating = ui.nextDouble();
        myPlaylist.add(new Song(song,artist,rating));

    }

    private static void printAveRating(ArrayList<Song> arr){
        double average = 0.0;
        double sum = 0.0;
        for(int i=0;i<arr.size();i++){
            sum+=arr.get(i).getRating();
        }
        average=sum/arr.size();
        System.out.println(average);

    }

    private static void findASong(){
        Scanner ui = new Scanner(System.in);
        System.out.println("Search: ");
        for(int i=0;i<myPlaylist.size();i++){
            if(myPlaylist.get(i).getName().equals(ui)){
                return myPlaylist.get();
            }
        }
    

    }


}
