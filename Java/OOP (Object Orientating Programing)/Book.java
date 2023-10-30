public class Book {
    
    String name,author;

    double rate;

    public Book(){};

    public Book(String title){
        this.name = title;
    }

    public Book(String title, String author){
        this.name = title;
        this.author = author;
    }

    public Book(String title, String author, double rate){
        this.name = title;
        this.author = author;
        this.rate = rate;
    }

    @Override
    public String toString() {
        String out="";
        out+="title: "+this.name;
        out+="author: "+this.author;
        out+="rating: "+this.rate;
        return out;
    }


}
